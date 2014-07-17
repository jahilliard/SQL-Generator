import re

class Db_data:
	#initialize method for the Graph method
	def __init__(self):
		self.colnameid = "wc"
		self.colnamedesc = "wc"
		self.ids = []
		self.descs = []
		self.count = []
		self.ididx = "not correct"
		self.descidx = "not correct"
		self.countidx = "not correct"
	
	#reads and parses the csv document
	def data_extractor(self, cvs_file):
		with open(cvs_file) as f:
			line = f.readlines()
			for x in line:
				doc_content = x.split('\r')
			for x in doc_content:
				if x != doc_content[0]:
					min_data = x.split(',')
					if self.ididx != 'not correct':
						if min_data[self.ididx] == '?':
							self.ids.append('null')
						else:
							min_data[self.ididx] = int(min_data[self.ididx])
							self.ids.append(min_data[self.ididx])
					if self.descidx != 'not correct':
						if min_data[self.descidx] == '?':
							self.descs.append('null')
						else:
							min_data[self.descidx] = str(min_data[self.descidx])
							min_data[self.descidx] = min_data[self.descidx].strip()
							self.descs.append(min_data[self.descidx])
					if self.countidx != 'not correct':
						min_data[self.countidx] = int(min_data[self.countidx])
						self.count.append(min_data[self.countidx])
				else:
					min_data = x.split(',')
					for idx,val in enumerate(min_data):
						print val
						val = val.upper()
						if val.find('COUNT') != -1:
							self.countidx = idx
						if val.find('DESC') != -1:
							self.descidx = idx
						if val.find('ID') != -1:
							self.ididx = idx
					if self.ididx != 'not correct':
						self.colnameid = min_data[self.ididx]
					if self.descidx != 'not correct':
						self.colnamedesc = min_data[self.descidx]
