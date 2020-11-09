import airsim
import time
import numpy as np
import matplotlib.pyplot as plt
import cv2

class CarController:
    def __init__(self):
        self.client = airsim.CarClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.car_controls = airsim.CarControls()

    def carControl(self, throttle: float, steering: float, brake: int):
        car_state = self.client.getCarState()
        print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))
        self.car_controls.throttle = throttle
        self.car_controls.steering = steering
        self.client.setCarControls(self.car_controls)
        time.sleep(5)
        self.car_controls.brake = brake

        self.client.setCarControls(self.car_controls)
        time.sleep(5)
        # get camera images from the car
        responses = self.client.simGetImages([
            #airsim.ImageRequest("0", airsim.ImageType.DepthVis)  # depth visualization image
            #,airsim.ImageRequest("1", airsim.ImageType.DepthPerspective, True)  # depth in perspective projection
            #airsim.ImageRequest("1", airsim.ImageType.Scene)  # scene vision image in png format
            airsim.ImageRequest("1", airsim.ImageType.Scene, False,False)
        ])  # scene vision image in uncompressed RGB array
        print('Retrieved images: %d', len(responses))

        for response in responses:
            img1d = np.fromstring(response.image_data_uint8, dtype=np.uint8)  # get numpy array
            img_rgb = img1d.reshape(response.height, response.width,3)  # reshape array to 3 channel image array H X W

            return img_rgb



if __name__ == '__main__':

    car = CarController()
    car.carControl(0.2, 0.2,0)
    car.carControl(0, 0,0)
