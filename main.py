import sys
import os

from image_crawler.google_image_crawler import GoogleImageCrawlerClass
from detector.image_detector import ImageDetector
"""
How haar cascade works, It trains the negative image
, to detect particular handwritten we just use several image and
duplicate it
"""


def start_google_crawl(name_dir, number, keyword):
	GoogleImageCrawlerClass.start_crawl_image(directory_file=name_dir, number_image=number, keyword=keyword)


def generate_txt_file_for_neg_image(name_dir):

	for image_path in os.listdir(name_dir):
		file_path = "neg5/"+image_path+"\n"
		with open("bg.txt", 'a') as f:
			f.write(file_path)


def combine_all_lst_file():
	with open("info.lst", "a") as f:
		ls = os.listdir("info")
		for dir in ls:
			if "info" in dir:
				with open("info/"+dir) as g:
					f.writelines(g.readlines())


if __name__ == "__main__":
	# combine_all_lst_file()
	# name_dir = sys.argv[1]
	# number_image = int(sys.argv[2])
	# keyword = sys.argv[3]
	#
	# print("keyword: %s, name_dir=%s, number_image=%d" % (keyword, name_dir, number_image))
	#
	# start_google_crawl(name_dir=name_dir, number=number_image, keyword=keyword)
	# generate_txt_file_for_neg_image(name_dir)
	ImageDetector.start_video_cam()