
import tensorflow as tf
from tensorflow import keras as keras
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras.optimizers import Adam

class ImageRecognitionModel:
    IMAGE_WIDTH = 256
    IMAGE_HEIGHT = 160
    def __init__(self):
        print('Work')

    def calc_IOU(self,y_true, y_pred, smooth=1):
        y_true_f = keras.layers.Flatten()(y_true)
        y_pred_f = keras.layers.Flatten()(y_pred)

        intersection = keras.backend.sum(y_true_f * y_pred_f)

        return (2 * (intersection + smooth) / (keras.backend.sum(y_true_f) + keras.backend.sum(y_pred_f) + smooth))

    def calc_IOU_loss(self, y_true, y_pred):
        return -self.calc_IOU(y_true, y_pred)

    def upsample_simple(self, filters, kernel_size, strides, padding):
        return layers.UpSampling2D(strides)

    def createModel(self, image_width = None, image_height = None, upsample = None):

        if image_width == None:
            input_img = self.IMAGE_WIDTH

        if image_height == None:
            image_height = self.IMAGE_HEIGHT

        if upsample == None:
            upsample = self.upsample_simple


        input_img = layers.Input((image_height, image_width, 3), name='RGB_Input')
        pp_in_layer = input_img

        c1 = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(pp_in_layer)  #
        c1 = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(c1)
        p1 = layers.MaxPooling2D((2, 2))(c1)

        c2 = layers.Conv2D(16, (3, 3), activation='relu', padding='same')(p1)
        c2 = layers.Conv2D(16, (3, 3), activation='relu', padding='same')(c2)
        p2 = layers.MaxPooling2D((2, 2))(c2)

        c3 = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(p2)
        c3 = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(c3)
        p3 = layers.MaxPooling2D((2, 2))(c3)

        c4 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(p3)
        c4 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(c4)
        p4 = layers.MaxPooling2D(pool_size=(2, 2))(c4)

        c5 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(p4)
        c5 = layers.Conv2D(128, (3, 3), activation='relu', padding='same')(c5)

        u6 = upsample(64, (2, 2), strides=(2, 2), padding='same')(c5)

        u6 = layers.concatenate([u6, c4])
        c6 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(u6)
        c6 = layers.Conv2D(64, (3, 3), activation='relu', padding='same')(c6)

        u7 = upsample(32, (2, 2), strides=(2, 2), padding='same')(c6)
        u7 = layers.concatenate([u7, c3])
        c7 = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(u7)
        c7 = layers.Conv2D(32, (3, 3), activation='relu', padding='same')(c7)

        u8 = upsample(16, (2, 2), strides=(2, 2), padding='same')(c7)
        u8 = layers.concatenate([u8, c2])
        c8 = layers.Conv2D(16, (3, 3), activation='relu', padding='same')(u8)
        c8 = layers.Conv2D(16, (3, 3), activation='relu', padding='same')(c8)

        u9 = upsample(8, (2, 2), strides=(2, 2), padding='same')(c8)
        u9 = layers.concatenate([u9, c1], axis=3)
        c9 = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(u9)
        c9 = layers.Conv2D(8, (3, 3), activation='relu', padding='same')(c9)

        d = layers.Conv2D(1, (1, 1), activation='sigmoid')(c9)
        seg_model = models.Model(inputs=[input_img], outputs=[d])

        seg_model.compile(optimizer=Adam(lr=1e-4),
                          loss=self.calc_IOU_loss, metrics=[self.calc_IOU])

        seg_model.summary()

        return seg_model


if __name__ == "__main__":
    model = ImageRecognitionModel()
    model1 = model.createModel()
    model1.load_weights(r'C:\\Users\\krzych\\Downloads\\model_v2.h5')

    def show_data(X, y, y_pred=None):
        if y_pred is None:
            y_pred = y
        print(y.shape)
        for x_i, y_i, y_pred_i in zip(X, y, y_pred):
            im = np.array(255 * x_i, dtype=np.uint8)
            im_mask = np.array(255 * y_i, dtype=np.uint8)
            im_pred = np.array(255 * y_pred_i, dtype=np.uint8)
            im_pred1 = np.array(255 * y_pred_i, dtype=np.uint8)
            print(f'imp_pred shape {im_pred.shape}')
            rgb_mask_pred = cv2.cvtColor(im_pred, cv2.COLOR_GRAY2RGB)
            rgb_mask_pred1 = cv2.cvtColor(im_pred, cv2.COLOR_GRAY2RGB)
            temp1 = rgb_mask_pred[:, :, 1:3]
            temp2 = rgb_mask_pred[:, :, 1:2]
            rgb_mask_pred[:, :, 1:3] = 0 * rgb_mask_pred[:, :, 1:3]
            rgb_mask_true = cv2.cvtColor(im_mask, cv2.COLOR_GRAY2RGB)
            rgb_mask_true[:, :, 0] = 0 * rgb_mask_true[:, :, 0]
            rgb_mask_true[:, :, 2] = 0 * rgb_mask_true[:, :, 2]

            print(im.shape, rgb_mask_pred.shape)

            img_pred = cv2.addWeighted(rgb_mask_pred, 0.5, im, 0.5, 0)
            img_true = cv2.addWeighted(rgb_mask_true, 0.5, im, 0.5, 0)

            loss = model.calc_IOU_loss(np.array([y_i]), np.array([y_pred_i]))
            plt.interactive(False)
            plt.figure(figsize=(20, 8))
            plt.subplot(1, 3, 1)
            plt.imshow(im)
            plt.title('Original image')
            plt.axis('off')
            plt.subplot(1, 3, 2)
            plt.imshow(img_pred)
            plt.title(f'Predicted masks {loss:0.4f}')
            plt.axis('off')
            plt.subplot(1, 3, 3)
            plt.imshow(img_true)
            plt.title('ground truth datasets')
            plt.axis('off')
            plt.tight_layout(pad=0)
            plt.show()

            return im


    import matplotlib.pyplot as plt
    import cv2
    import numpy as np


    immage2 = cv2.imread(r'C:\Users\krzych\Documents\AirSim\2020-10-02-20-32-05\images\img__0_1601663532026328700.png')
    im = np.asarray(immage2)/255


    print(f'Image shape {im.shape}')
    x = [[1, 2, 3]]
    y = np.array([4, 5, 6])


    arr = np.array([im])
    print(f'arr shape {arr.shape}')
    #print(arr[0])
    #np.append(arr, im)
    #print(f'arr shape {arr.shape}')


    y_pred = model1.predict(arr)
    print(f'y_pred  shape {y_pred.shape}')
    #plt.interactive(False)


    #print(f'arr2 shape {arr2.shape}')
    #np.append(arr2, y_pred)
    im = show_data(arr,y_pred)


