import cv2

import numpy as np
import time

class ImageDetector:


	@staticmethod
	def start_detect():

		image_cascade = cv2.CascadeClassifier()

	@staticmethod
	def start_video_cam():
		WATCH_CASCADE = cv2.CascadeClassifier("cascade.xml")
		cap = cv2.VideoCapture(0)

		while True:
			ret, img = cap.read()
			gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			integral_model = WATCH_CASCADE.detectMultiScale(gray, 30, 30)

			for (x, y, w, h) in integral_model:
				cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

			cv2.imshow('img', img)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break

		cap.release()
		cv2.destroyAllWindows()