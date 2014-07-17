from Db_data import Db_data

def test():
	data = Db_data()
	data.data_extractor('scndcmpl.csv')
	print data.ids
	print data.descs 
	print data.count


test()