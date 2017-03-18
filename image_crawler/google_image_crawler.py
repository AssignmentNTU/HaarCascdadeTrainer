from icrawler.builtin.google import GoogleImageCrawler


class GoogleImageCrawlerClass:

	@staticmethod
	def start_crawl_image(directory_file, number_image, keyword):

		google_crawler = GoogleImageCrawler(storage={'backend': 'FileSystem', 'root_dir': directory_file})
		google_crawler.crawl(
					keyword=keyword, offset=0, max_num=number_image,)
