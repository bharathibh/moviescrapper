import requests
from bs4 import BeautifulSoup

class Scrapper(object):
	"""Init the URL to the class"""
	def __init__(self, url=None):
		super(Scrapper, self).__init__()
		self.url = url

	def get_class(self, klass):
		self.page = requests.get(self.url)
		self.soup = BeautifulSoup("".join(line.strip() for line in self.page.text.split('\n')), "html.parser")
		return self.soup.find_all(class_=klass)
	
	def get_tag(self, resultset, attrs):
		for html in resultset:
			print html

if __name__ == '__main__':
	scrpr = Scrapper(url='https://www.spicinemas.in/bengaluru/show-times')
	print scrpr.get_class('movie__show show show-time ')
	print scrpr.get_tag(scrpr.get_class('movie__show show show-time '),{'class':'filter-value movie__name'})

