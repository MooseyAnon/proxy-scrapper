import requests
from datetime import datetime
from bs4 import BeautifulSoup

from csvsaver import SaveToCSV


def get_page(url):
	return requests.get(url, timeout=2)

def make_soup_obj(opened_link):
	data = opened_link.text.encode('utf-8')
	return BeautifulSoup(data, 'html.parser')

def find_table(soupObj, aclass):
	if not type(aclass) == str:
		aclass = str(aclass)
	return soupObj.find('table', {'class': aclass})

def parse_table(soupTable):
	"""parses the ip address table on www.ip-adress.com"""

	table_body = soupTable.find('tbody')
	rows = table_body.find_all('tr')
	data = []
	for row in rows:
		col = row.find_all('td')
		ns = [ele.text.strip() for ele in col]
		ns.append(datetime.now().time())
		ns.append(datetime.now().date())

		data.append(ns)

	SaveToCSV('proxies.csv', data)
	print 'succeffuly saved csv'




def main():

	PROXY_URL = 'https://www.ip-adress.com/proxy-list'
	IPA_TABLE_CLASS = 'htable proxylist'

	x = make_soup_obj(get_page(PROXY_URL))
	parse_table(find_table(x, IPA_TABLE_CLASS))

	# for example output look at proxies.csv


if __name__ == '__main__':
	main()



