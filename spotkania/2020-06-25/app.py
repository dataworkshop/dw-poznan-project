import numpy as np
import pandas as pd
import os
import tensorflow as tf

print("Tensorflow versioin ", tf.__version__)


def get_path():
    _URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
    path_to_zip = tf.keras.utils.get_file('cats_and_dogs.zip',
             origin=_URL, extract=True)
    PATH = os.path.join(os.path.dirname(path_to_zip),
             'cats_and_dogs_filtered')
    train_dir = os.path.join(PATH,'train')
    val_dir = os.path.join(PATH,'validation')
    return train_dir, val_dir

from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_data_gen():
    return ImageDataGenerator(
        rescale=1./255,
        rotation_range=45,

        width_shift_range=.15,
        height_shift_range=.15,
        horizontal_flip=True,
        vertical_flip=False,
        zoom_range=0.5
    )

def get_train_val(datagen,batch_size=64):
    train_dir, val_dir = get_path();
    return (
        datagen.flow_from_directory(train_dir, class_mode='binary', batch_size=batch_size),
        datagen.flow_from_directory(val_dir, class_mode='binary', batch_size=batch_size),
         
    )

train_it, val_id = get_train_val(get_data_gen())

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D,Flatten, Dropout, MaxPooling2D



my_model = tf.keras.models.load_model("my_model.h5")
print(my_model.summary())


import streamlit  as st

st.title('Image Augmentation')
st.markdown("### Subtitle")


st.sidebar.title("Featurs")

page = st.sidebar.selectbox("Choose a page", ["Image upload", "Augmentation"])

"""
# Another app
"""

if page == "Image upload":
    from PIL import Image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg","png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img = img.resize((256,256))
        st.image(img, caption="Upload image", use_column_width=True)

        img = tf.keras.preprocessing.image.img_to_array(img)
        img = img.reshape((1,256,256,3))
        st.write(my_model.predict(img))


# st.markdown("")

if page == "Augmentation":
    horizontal_flip = st.sidebar.checkbox("Horizontal Fliip")
    vertical_flip = st.sidebar.checkbox("Vertical Fliip")

    rotation_range = st.sidebar.slider("Rotation range", 0.0,360.0,0.0)
    width_shift_range = st.sidebar.slider("Width shift range", -1.0,1.0,0.0, step=0.05)
    height_shift_range = st.sidebar.slider("Height shift range", -1.0,1.0,0.0, step=0.05)
    
    zoom_range = st.sidebar.slider("Zoom range", 0.0,5.0,0.0, step=0.05)
    


    datagen =  ImageDataGenerator(
        rescale=1./255,
        rotation_range=rotation_range,

        width_shift_range=width_shift_range,
        height_shift_range=height_shift_range,
        horizontal_flip=horizontal_flip,
        vertical_flip=vertical_flip,
        zoom_range=zoom_range
    )
    train_it, val_it = get_train_val(datagen)
    x,y = val_it.next()

    st.image(
        x, caption = [
            f'(real: {y}, pred: {y_pred})' for y,y_pred in zip(y,my_model.predict(x))
        ]
    )


st.title("Kod z pliku");

st.code(open("./app.py").read(),language="python");


st.title("Kod w postaci tekstu")


"""
```python
import numpy as np
import pandas as pd
import os
import tensorflow as tf

print("Tensorflow versioin ", tf.__version__)


def get_path():
    _URL = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
    path_to_zip = tf.keras.utils.get_file('cats_and_dogs.zip',
             origin=_URL, extract=True)
    PATH = os.path.join(os.path.dirname(path_to_zip),
             'cats_and_dogs_filtered')
    train_dir = os.path.join(PATH,'train')
    val_dir = os.path.join(PATH,'validation')
    return train_dir, val_dir

from tensorflow.keras.preprocessing.image import ImageDataGenerator

def get_data_gen():
    return ImageDataGenerator(
        rescale=1./255,
        rotation_range=45,

        width_shift_range=.15,
        height_shift_range=.15,
        horizontal_flip=True,
        vertical_flip=False,
        zoom_range=0.5
    )

def get_train_val(datagen,batch_size=64):
    train_dir, val_dir = get_path();
    return (
        datagen.flow_from_directory(train_dir, class_mode='binary', batch_size=batch_size),
        datagen.flow_from_directory(val_dir, class_mode='binary', batch_size=batch_size),
         
    )

train_it, val_id = get_train_val(get_data_gen())

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D,Flatten, Dropout, MaxPooling2D



my_model = tf.keras.models.load_model("my_model.h5")
print(my_model.summary())


import streamlit  as st

st.title('Image Augmentation')
st.markdown("### Subtitle")


st.sidebar.title("Featurs")

page = st.sidebar.selectbox("Choose a page", ["Image upload", "Augmentation"])

"""
# Another app
"""

if page == "Image upload":
    from PIL import Image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg","png"])

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img = img.resize((256,256))
        st.image(img, caption="Upload image", use_column_width=True)

        img = tf.keras.preprocessing.image.img_to_array(img)
        img = img.reshape((1,256,256,3))
        st.write(my_model.predict(img))


if page == "Augmentation":
    horizontal_flip = st.sidebar.checkbox("Horizontal Fliip")
    vertical_flip = st.sidebar.checkbox("Vertical Fliip")

    rotation_range = st.sidebar.slider("Rotation range", 0.0,360.0,0.0)
    width_shift_range = st.sidebar.slider("Width shift range", -1.0,1.0,0.0, step=0.05)
    height_shift_range = st.sidebar.slider("Height shift range", -1.0,1.0,0.0, step=0.05)
    
    zoom_range = st.sidebar.slider("Zoom range", 0.0,5.0,0.0, step=0.05)
    


    datagen =  ImageDataGenerator(
        rescale=1./255,
        rotation_range=rotation_range,

        width_shift_range=width_shift_range,
        height_shift_range=height_shift_range,
        horizontal_flip=horizontal_flip,
        vertical_flip=vertical_flip,
        zoom_range=zoom_range
    )
    train_it, val_it = get_train_val(datagen)
    x,y = val_it.next()

    st.image(
        x, caption = [
            f'(real: {y}, pred: {y_pred})' for y,y_pred in zip(y,my_model.predict(x))
        ]
    )

```

"""