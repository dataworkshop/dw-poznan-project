import os
import re
from jinja2 import FileSystemLoader, Environment


def prettify(code):
    """A super simple code prettifier"""
    pretty = []
    indent = 0
    for line in code.split('\n'):
        line = line.strip()
        # skip empty lines
        if len(line) == 0:
            continue
        # lower indentation on closing braces
        if line[-1] == '}' or line == '};' or line == 'protected:':
            indent -= 1
        pretty.append(('    ' * indent) + line)
        # increase indentation on opening braces
        if line[-1] == '{' or line == 'public:' or line == 'protected:':
            indent += 1
    pretty = '\n'.join(pretty)
    # leave empty line before {return, for, if}
    pretty = re.sub(r'([;])\n(\s*?)(for|return|if) ', lambda m: '%s\n\n%s%s ' % m.groups(), pretty)
    # leave empty line after closing braces
    pretty = re.sub(r'}\n', '}\n\n', pretty)
    # strip empty lines between closing braces (2 times)
    pretty = re.sub(r'\}\n\n(\s*?)\}', lambda m: '}\n%s}' % m.groups(), pretty)
    pretty = re.sub(r'\}\n\n(\s*?)\}', lambda m: '}\n%s}' % m.groups(), pretty)
    return pretty


def jinja(template_file, data):
    """Render Jinja template"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    loader = FileSystemLoader(dir_path + '/templates')
    template = Environment(loader=loader).get_template(template_file)
    data.update(**{
        'f': {
            'enumerate': enumerate,
            'round': lambda x: round(x, data.get('precision', 12) or 12),
            'zip': zip
        }
    })
    code = template.render(data)
    return prettify(code)


def port_trainset(X, y, classname='TrainSet'):
    return jinja('trainset.jinja', locals())


def port_testset(X, y, classname='TestSet'):
    return jinja('testset.jinja', locals())
