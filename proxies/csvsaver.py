import csv
import os 



class SaveToCSV:
	def __init__(self, afile, s_input):
		self.f_name = afile 
		self.someinput = s_input
		self.save(self.f_name, self.someinput)

	def _create_csv(self, afile, someinput):
		try:
			with open(afile, 'wb') as af:
				f = csv.writer(af,delimiter = ',',
                        quoting=csv.QUOTE_MINIMAL)
				f.writerows(someinput)
		except IOError as e:
			return e, 'had a problem creating {0}'.format(afile)

	def _append_csv(self, afile):
		try:
			with open(afile, 'a') as af:
				f = csv.writer(af)
				f.writerows(someinput)
		except IOError as e:
			return e, 'had a problem opening and appending to {0}'.format(afile)

	def _check_file(self, afile):
		return os.path.exists(afile)

	def save(self, afile, someinput):
		if self._check_file(afile):
			self._append_csv(afile, someinput)
		else:
			self._create_csv(afile, someinput)



class ReadFromCSV:

	"""deals with reading from proxies file. allows for either all proxy document contents
	or just a list of ips/ports."""

	def __init__(self, path, just_proxies=False):
		self.path2 = path
		self.content = []
		self.proxie_rows = []
		self.prox = just_proxies
		self.open_csv(self.path2, self.prox)

	def _check_path(self, path):
		if os.path.exists(path): 
			return 0
		else:
			return -1

	def _read(self, path, just_proxies=False):
		try:
			with open(path, 'rb') as rf:
				reader = csv.reader(rf)
				if just_proxies:
					self.proxie_rows = [row[0] for row in reader]
				self.content = [row for row in reader]
				# return self.content
		except IOError as e:
			print e, 'could not open file'

	def open_csv(self, path, just_proxies=False):
		if not self._check_path(path) == 0:
			print 'File does not exist'
		return self._read(path, self.prox)

	def _read_just_proxies(self, path, just_proxies=False):
		return self._read(path, self.prox)
		










