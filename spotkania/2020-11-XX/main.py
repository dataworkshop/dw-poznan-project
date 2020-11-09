from CarController import CarController
from  ImageRecognitionModel import ImageRecognitionModel
import matplotlib.pyplot as plt
import cv2
import numpy as np

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


model = ImageRecognitionModel()
model1 = model.createModel()
model1.load_weights(r'C:\\Users\\krzych\\Downloads\\model_v2.h5')
car = CarController()
image = car.carControl(0.2, 0.2,0)
im = np.asarray(image)/255
arr = np.array([im])
y_pred = model1.predict(arr)
im = show_data(arr, y_pred)
