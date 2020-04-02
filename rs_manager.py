import pyrealsense2 as rs
import cv2
import numpy as np
from tqdm import tqdm
import random
import time


MAX_RESET_TIME = 10

def init_from_devidx(devidx):

	pipe = rs.pipeline()

	# config
	config = rs.config()
	config.enable_device(devidx)
	config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 6)
	config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 6)
	prof = pipe.start(config)

	# set high accuracy mode
	depth_sensor = prof.get_device().first_depth_sensor()
	preset_range = depth_sensor.get_option_range(rs.option.visual_preset)
	for i in range(int(preset_range.max)):
		visulpreset = depth_sensor.get_option_value_description(rs.option.visual_preset,i)
    	#print('%02d: %s'%(i,visulpreset))
		if visulpreset == "High Accuracy":
			depth_sensor.set_option(rs.option.visual_preset, i)
	return pipe, prof.get_device()




def my_get_frame(pipe,device):
	flag = 0
	while flag<MAX_RESET_TIME:
		try:
			f = pipe.wait_for_frames()			
			#flag = MAX_RESET_TIME
			break
		except RuntimeError, info:
			print ("RuntimeError:",info)
			# reset
			device.hardware_reset()
			flag+=1

	if flag == MAX_RESET_TIME :
		return None
	else:
		return f



# test
if __name__ == "__main__":

	pipe1,dev1 = init_from_devidx('822512061389')
	#pipe2,dev2 = init_from_devidx('821212060674')

	# align rgb and depth
	align = rs.align(rs.stream.color)

	for i in tqdm(range(500)):

		# get frame from camera1
		#f1 = pipe1.wait_for_frames()
		f1 =  my_get_frame(pipe1,dev1)
		#f1 = align.process(f1)
		img1 = np.asanyarray(f1.get_color_frame().get_data())
		dep1 = np.asanyarray(f1.get_depth_frame().get_data())
		visdep1 = (np.clip(dep1/5000.0*255,0,255)).astype('uint8')

		'''
		# get frame from camera2
		f2 =  my_get_frame(pipe2,dev2)
		f2 = align.process(f2)
		img2 = np.asanyarray(f2.get_color_frame().get_data())
		dep2 = np.asanyarray(f2.get_depth_frame().get_data())
		visdep2 = (np.clip(dep2/5000.0*255,0,255)).astype('uint8')
		'''

		# visualization
		cv2.imshow("c1",img1)
		cv2.imshow("d1",visdep1)
		#cv2.imshow("c2",img2)
		#cv2.imshow("d2",visdep2)

		cv2.waitKey(30)
	
