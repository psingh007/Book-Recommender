import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

def top_ten_books(fname):
	'''
	purpose: Takes a column of the languges plots a bar plot with languages and 
	number of books, excluding english and plot a pie chart with english and other languages.  

	:param x: input pd.series object 
	:type x: pd.core.series.Series

	return: None
	'''


	import csv
	#from goodreads import client
	#gc = client.GoodreadsClient('pvr3ns4Le0DCqEpAG2jlQ', '4BM2D4d8ZvFcJNqRQ3OjQq1Qh3OrvMAvHiI0lTOUFE')
	with open(fname,'r',encoding="utf-8") as f:
		reader = csv.reader(f)
		fieldnames = next(reader)
		# print(fieldnames)
		csv_reader = csv.DictReader(f,fieldnames=fieldnames)
		cntAuthor={}
		d1 = []
		for row in csv_reader:
			d={}
			for k,v in row.items():
				d[k]=v
			d1.append(d)
		#print(d1)

		Dic1 = {}
		for entry in d1:
			key = entry['title']
			Dic1[key] = entry['rating']

		Dic2 = {}
		for entry in d1:
			key = entry['title']
			Dic2[key] = entry['ratings_count']

		Dic3 = {}
		for entry in d1:
			key = entry['title']
			Dic3[key] = entry['text_reviews_count']
	
	# plot ratings vs book name

	#NEED TO GET TOP 10 
	plt.figure()
	plt.bar(range(len(Dic1)),list(Dic1.values()), align='center')
	plt.xticks(range(len(Dic1)), list(Dic1.keys()),rotation=90)
	plt.ylabel('ratings')
	plt.title('Book Name vs. ratings')



	# plot ratings_count vs book name

	#NEED TO GET TOP 10
	plt.figure()
	plt.bar(range(len(Dic2)),list(Dic2.values()), align='center')
	plt.xticks(range(len(Dic2)), list(Dic2.keys()),rotation=90)
	plt.ylabel('ratings')
	plt.title('Book Name vs. ratings')

	# plot text_reviews_count vs book name
	#NEED TO GET TOP 10
	plt.figure()
	plt.bar(range(len(Dic3)),list(Dic3.values()), align='center')
	plt.xticks(range(len(Dic3)), list(Dic3.keys()),rotation=90)
	plt.ylabel('ratings')
	plt.title('Book Name vs. ratings')
	plt.show()	

	#graph the histogram without English
	'''
	y_pos = np.arange(len(language_list))
	print("y_pos= ", y_pos)
	plt.bar(y_pos, counters, align='center', alpha=0.5)
	plt.xticks(y_pos, language_list, rotation=90)
	plt.ylabel('this is counters')
	plt.title('Language vs number of books')
	plt.show()
	'''
	



if __name__ == '__main__':
	#data = pd.read_csv("datav3.csv")
	fname = "datav3.csv"
	top_ten_books(fname)


'''

	assert isinstance(x, pd.core.frame.DataFrame) #check if the input is a dataframe. 

	title = x['title']
	title = list(set(list(', '.join(title.array).split(','))))

	rating = x['rating']
	print(type(rating))
	print(type(rating[0]))
	rating = list(set(list(', '.join(rating.array).split(','))))

	ratings_count = x['ratings_count']
	ratings_count = list(set(list(', '.join(ratings_count.array).split(','))))

	text_reviews_count = x['text_reviews_count']
	text_reviews_count = list(set(list(', '.join(text_reviews_count.array).split(','))))



	counters  = []
	dic = {}
	for lan in language_list: 
		counters.append(', '.join(x.array).split(',').count(lan))

	plt.figure()
'''



