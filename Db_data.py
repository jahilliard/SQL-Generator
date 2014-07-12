class Db_data:
	#initialize method for the Graph method
	def __init__(self):
		self.colnameid = "wc"
		self.colnamedesc = "wc"
		self.ids = []
		self.descs = []
		self.counts = []
	
	#reads and parses the csv document
	def data_extractor(self, cvs_file):
		with open(cvs_file) as f:
			line = f.readlines()
			for x in line:
				doc_content = x.split('\r')
			for x in doc_content:
				if x != doc_content[0]:
					min_data = x.split(',')
					if min_data[1] == '?':
						self.ids.append('null')
					else:
						min_data[1] = int(min_data[1])
						self.ids.append(min_data[1])
					if min_data[2] == '?':
						self.descs.append('null')
					else:
						min_data[2] = str(min_data[2])
						min_data[2] = min_data[2].strip()
						self.descs.append(min_data[2])
					min_data[3] = int(min_data[3])
					self.counts.append(min_data[3])
				else:
					min_data = x.split(',')
					self.colnameid = min_data[1]
					self.colnamedesc = min_data[2]

	# def correct_name_calc:
	# 	for x in self.ids:
	# 		if x != self.ids[0]:
	# 			get 