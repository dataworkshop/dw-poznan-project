from sklearn.svm import SVC, LinearSVC, OneClassSVM
from sklearn.decomposition import PCA
try:
    from skbayes.rvm_ard_models import RVC
except ImportError:
    from micromlgen.patches import RVC

from micromlgen import platforms
from micromlgen.utils import jinja


def port_rvm(clf, classname, **kwargs):
    """Port a RVM classifier"""
    assert classname is None or len(classname) > 0, 'Invalid class name'
    template_data = {
        **kwargs,
        'kernel': {
            'type': clf.kernel,
            'gamma': clf.gamma,
            'coef0': clf.coef0,
            'degree': clf.degree
        },
        'sizes': {
            'features': len(clf.relevant_vectors_[0]),
        },
        'arrays': {
            'vectors': clf.relevant_vectors_,
            'coefs': clf.coef_,
            'actives': clf.active_,
            'intercepts': clf.intercept_,
            'mean': clf._x_mean,
            'std': clf._x_std
        },
        'classname': classname if classname is not None else 'RVM',
    }
    return jinja('rvm/rvm.jinja', template_data)


def port_svm(clf, classname=None, **kwargs):
    """Port a SVC / LinearSVC classifier"""
    assert isinstance(clf.gamma, float), 'You probably didn\'t set an explicit value for gamma: 0.001 is a good default'
    assert classname is None or len(classname) > 0, 'Invalid class name'
    if classname is None:
        classname = 'OneClassSVM' if isinstance(clf, OneClassSVM) else 'SVM'
    support_v = clf.support_vectors_
    n_classes = len(clf.n_support_)
    template_data = {
        **kwargs,
        'kernel': {
            'type': clf.kernel,
            'gamma': clf.gamma,
            'coef0': clf.coef0,
            'degree': clf.degree
        },
        'sizes': {
            'features': len(support_v[0]),
            'vectors': len(support_v),
            'classes': n_classes,
            'decisions': n_classes * (n_classes - 1) // 2,
            'supports': clf.n_support_
        },
        'arrays': {
            'supports': support_v,
            'intercepts': clf.intercept_,
            'coefs': clf.dual_coef_
        },
        'classname': classname
    }
    return jinja('svm/svm.jinja', template_data)


def port_pca(pca, classname=None, **kwargs):
    """Port a PCA"""
    template_data = {
        'arrays': {
            'components': pca.components_,
            'mean': pca.mean_
        },
        'classname': classname if classname is not None else 'PCA'
    }
    return jinja('pca/pca.jinja', template_data)


def port(
        clf,
        classname=None,
        classmap=None,
        platform=platforms.ARDUINO,
        precision=None):
    assert platform in platforms.ALL, 'Unknown platform %s. Use one of %s' % (platform, ', '.join(platforms.ALL))
    if isinstance(clf, (SVC, LinearSVC, OneClassSVM)):
        return port_svm(**locals())
    elif isinstance(clf, RVC):
        return port_rvm(**locals())
    elif isinstance(clf, PCA):
        return port_pca(pca=clf, **locals())
    raise TypeError('clf MUST be one of SVC, LinearSVC, OneClassSVC, RVC, PCA')