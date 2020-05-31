import numpy as np
# import cv2
# import pyscreenshot as ImageGrab
import sys
import time
# import pyautogui
from pynput.mouse import Button, Controller
from mss import mss


if __name__ == '__main__':
    # with mss() as sct:
    #     monitor = {"top": 400, "left": 320, "width": 370, "height": 1}
    #     # monitor = {"top": 0, "left": 0, "width": 1000, "height": 1}
    #     a = time.time()
    #     for i in range(100):
    #         img = sct.grab(monitor)
    #         # image = pyautogui.screenshot()
    #         # im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    # b = time.time()
    # print(b-a)
    np.set_printoptions(threshold=sys.maxsize)
    mouse = Controller()
    mins = 3
    while mins != -1:
        print(mins)
        # Sleep for a minute
        time.sleep(1)
        # Increment the minute total
        mins -= 1
    monitor = {"top": 400, "left": 320, "width": 370, "height": 1}
    # count = 0
    mouse.click(Button.left, 1)
    y = 500
    with mss() as sct:
        while True:
            img = sct.grab(monitor)
            img_array = np.array(img)
            val1 = img_array[0][0][0]
            val2 = img_array[0][240][0]
            val3 = img_array[0][480][0]
            val4 = img_array[0][-1][0]
            if val1==0:
                x = 320
                mouse.position = (x, y)
                time.sleep(0.01)
                mouse.click(Button.left, 1)
            if val2 == 0:
                x = 440
                mouse.position = (x, y)
                time.sleep(0.01)
                mouse.click(Button.left, 1)
            if val3 == 0:
                x = 560
                mouse.position = (x, y)
                time.sleep(0.01)
                mouse.click(Button.left, 1)
            if val4 == 0:
                x = 690
                mouse.position = (x, y)
                time.sleep(0.01)
                mouse.click(Button.left, 1)

            # count+=1


    # monitor = {"top": 200, "left": 270, "width": 475, "height": 690}
    # with mss() as sct:
    #     while True:
    #         # a = time.time()
    #         img = sct.grab(monitor)
    #         img_array = np.array(img)
    #         # img_array[:, 115, :] = 0
    #         # img_array[:, 115+230+4, :] = 0
    #         # img_array[:, 115+2*230, :] = 0
    #         # img_array[:, 115+3*230, :] = 0
    #         # print(img_array[:, 115, 0])
    #         # print(img_array[:, 115+230+4, 0])
    #         # print(img_array[:, 115+2*230, 0])
    #         # print(img_array[:, 115+3*230, :])
    #         # a = time.time()
    #         loc = (0, 0)
    #         val1 = np.where(img_array[:, 115, 0]==0)[0]
    #         val2 = np.where(img_array[:, 115+230+4, 0]==0)[0]
    #         val3 = np.where(img_array[:, 115+2*230, 0]==0)[0]
    #         val4 = np.where(img_array[:, 115+3*230, 0]==0)[0]
    #         if val1.shape[0]>0:
    #             yloc = val1[-1]/2
    #             loc = (x1+(115)/2, y1+yloc-5)
    #             mouse.position = loc
    #             time.sleep(0.01)
    #             mouse.click(Button.left, 1)
    #             # print(loc)
    #         if val2.shape[0]>0:
    #             yloc = val2[-1]/2
    #             loc = (x1+(115+230+4)/2, y1+yloc)
    #             mouse.position = loc
    #             time.sleep(0.01)
    #             mouse.click(Button.left, 1)
    #         #     print(loc)
    #         if val3.shape[0]>0:
    #             yloc = val3[-1]/2
    #             loc = (x1+(115+2*230)/2, y1+yloc)
    #             mouse.position = loc
    #             time.sleep(0.01)
    #             mouse.click(Button.left, 1)
    #             # print(loc)
    #         if val4.shape[0]>0:
    #             yloc = val4[-1]/2
    #             loc = (x1+(115+3*230)/2, y1+yloc)
    #             mouse.position = loc
    #             time.sleep(0.01)
    #             mouse.click(Button.left, 1)
            # b = time.time()
            # print(b-a)
    # image = cv2.cvtColor(img_array,
    #                      cv2.COLOR_RGB2BGR)
    # writing it to the disk using opencv
    # cv2.imwrite("image1.png", image)