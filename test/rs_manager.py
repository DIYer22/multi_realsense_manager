import pyrealsense2 as rs
import cv2
import numpy as np
from tqdm import tqdm
import random
import time
from boxx import *


MAX_RESET_TIME = 10


def init_from_devidx(devidx):
    for tryi in range(5):
        try:
            with timeit():
                if 1:
                    pass

                    # config

                    config = rs.config()
                    config.enable_device(devidx)
                    config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 6)
                    config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 6)
                    pipe = rs.pipeline()
                with timeit():
                    prof = pipe.start(config)
                    # time.sleep(5)
                device = prof.get_device()
                # set high accuracy mode
                depth_sensor = device.first_depth_sensor()
                preset_range = depth_sensor.get_option_range(rs.option.visual_preset)
                for i in range(int(preset_range.max)):
                    visulpreset = depth_sensor.get_option_value_description(
                        rs.option.visual_preset, i
                    )
                    # print('%02d: %s'%(i,visulpreset))
                    if visulpreset == "High Accuracy":
                        with timeit("High Accuracy"):
                            # i == 3
                            depth_sensor.set_option(rs.option.visual_preset, i)
            raise RuntimeError("raise")
            return "aa"
            return pipe, prof.get_device()
        except RuntimeError as e:
            print(tryi)
            print(e)
            device.hardware_reset()
            time.sleep(1.0)
    raise Exception()


def my_get_frame(pipe, device):
    flag = 0
    while flag < MAX_RESET_TIME:
        try:
            f = pipe.wait_for_frames()
            # flag = MAX_RESET_TIME
            break
        except RuntimeError as info:
            print("RuntimeError:", info)
            # reset
            device.hardware_reset()
            flag += 1

    if flag == MAX_RESET_TIME:
        return None
    else:
        return f


# test
if __name__ == "__main__":
    context = rs.context()
    connect_device = []
    for d in context.devices:
        if d.get_info(rs.camera_info.name).lower() != "platform camera":
            connect_device.append(d.get_info(rs.camera_info.serial_number))
    pipe1, dev1 = init_from_devidx(connect_device[0])
if 0:
    # align rgb and depth
    align = rs.align(rs.stream.color)

    for i in tqdm(range(500)):

        # get frame from camera1
        # f1 = pipe1.wait_for_frames()
        f1 = my_get_frame(pipe1, dev1)
        # f1 = align.process(f1)
        img1 = np.asanyarray(f1.get_color_frame().get_data())
        dep1 = np.asanyarray(f1.get_depth_frame().get_data())
        visdep1 = (np.clip(dep1 / 5000.0 * 255, 0, 255)).astype("uint8")

        """
        # get frame from camera2
        f2 =  my_get_frame(pipe2,dev2)
        f2 = align.process(f2)
        img2 = np.asanyarray(f2.get_color_frame().get_data())
        dep2 = np.asanyarray(f2.get_depth_frame().get_data())
        visdep2 = (np.clip(dep2/5000.0*255,0,255)).astype('uint8')
        """

        # visualization
        cv2.imshow("c1", img1)
        # cv2.imshow("d1",visdep1)
        # cv2.imshow("c2",img2)
        # cv2.imshow("d2",visdep2)

        cv2.waitKey(30)
