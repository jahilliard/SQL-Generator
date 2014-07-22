from Db_data import Db_data
from collections import defaultdict

def main():
	csv_docs = []
	data = Db_data()
	data.data_extractor('scndcmpl.csv')
	print "case"
	D = defaultdict(list)
	for i,item in enumerate(data.ids):
	    D[item].append(i)
	D = {k:v for k,v in D.items() if len(v)>0}
	for key, val in D.iteritems():
		if key == 'null':
			print "\twhen " + data.colnameid + " is null then null"
		else:
			compare = []
			names = []
			for x in val:
				compare.append(data.count[x])
				names.append(data.descs[x])
			idx = compare.index(max(compare))
			print "\twhen " + data.colnameid + " = " + str(key) + " then '" + names[idx] + "'"
	print "end"

def repeat_map():
	csv_docs = []
	data = Db_data()
	data.data_extractor('resmap.csv')
	print data.ids
	print data.descs 
	print data.count
	print data.map
				

					


repeat_map()