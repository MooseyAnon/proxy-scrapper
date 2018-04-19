from csvsaver import ReadFromCSV

def get_proxies_only(path):
	x = ReadFromCSV(path, just_proxies=True).proxie_rows
	return x

def get_full_proxy_info(path):
	x = ReadFromCSV(path).content
	return x

def split_host_port(proxy):
	return proxy.split(':')




