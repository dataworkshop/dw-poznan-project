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

print(get_path())
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


def get_model(image_shape):
    IMG_WIDTH = image_shape[0]
    IMG_HEIGHT = image_shape[1]

    model = Sequential([
        Conv2D(16,3,activation='relu', input_shape=(IMG_WIDTH,IMG_HEIGHT,3)),
        MaxPooling2D(),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(512, activation='relu'),
        Dense(1, activation='sigmoid', name='activation')
    ])

    print(model.summary())
    model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

    return model

model = get_model(train_it.image_shape)

model.fit(train_it, epochs=2, validation_data=val_id)

model.save('my_model.h5')
x,y = train_it.next();
print([
  (y_pred[0],y)    for y_pred, y in zip(model.predict(x),y)
])