import cv2
import pyautogui
import numpy as np
from skimage.transform import resize
import pickle
import time
import serial

model_filename = "model2.pkl"
model = pickle.load(open(model_filename, 'rb'))
x = 455
y = 164
width = 90
height = 80
arduino_port = 'COM3'
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)


def program():
    number = 1

    while number == 1:
        screenshot = pyautogui.screenshot()
        screenshot.save('screenshot.png')
        # img = cv2.imread('screenshot.png')
        # roi = img[y:y + height, x:x + width]
        # plt.imshow(roi)
        # plt.show()
        image_path = "screenshot.png"
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        roi = img[y:y + height, x:x + width]
        img = resize(roi, (90, 80))
        img = img.flatten()
        img = np.asarray([img])
        number = model.predict(img)
        number = int(number[0])
        number += 1
        print(number)
    ser.write(str(number).encode())
    time.sleep(5.5)
    ser.write(str(1).encode())


while True:
    program()

ser.close()
