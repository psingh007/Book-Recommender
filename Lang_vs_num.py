import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

def lan_vs_num(x):
	'''
	purpose: Takes a column of the languges plots a bar plot with languages and 
	number of books, excluding english and plot a pie chart with english and other languages.  

	:param x: input pd.series object 
	:type x: pd.core.series.Series

	return: None
	'''

	language_list = list(', '.join(x.array).split(','))
	language_list = list(set(language_list))

	counters  = []
	dic = {}
	for lan in language_list: 
		counters.append(', '.join(x.array).split(',').count(lan))

	
	Summ = 0
	for i in range(len(counters)-1):
		Summ  = Summ + counters[i]

	#remove eng from the list.
	for i in range(len(language_list)-1):
		if language_list[i] == ' eng':
			m = language_list.pop(i) #m = eng 
			n = counters.pop(i)  #n = # of eng books 
	
	Summ = Summ - n #subtract Summ of all books with number of eng books
	sizes = [n, Summ] #suzesfor pie chart
	labels = 'English', 'Other' #labels for pie chart

	colors = ['darkred', 'lightcoral']
	explode = (0, 0.1)
	# Plot
	plt.figure()
	plt.pie(sizes, explode = explode, labels=labels, colors=colors,
		autopct='%1.1f%%', shadow=False, startangle=140)
	plt.axis('equal')

	plt.figure()

	#graph the histogram without English
	y_pos = np.arange(len(language_list))
	print("y_pos= ", y_pos)
	plt.bar(y_pos, counters, align='center', alpha=0.5)
	plt.xticks(y_pos, language_list, rotation=90)
	plt.ylabel('this is counters')
	plt.title('Language vs number of books')
	plt.show()
	



if __name__ == '__main__':
	data = pd.read_csv("datav3.csv")
	a = data['language']
	lan_vs_num(a)

	'''
	plt.figure() # setup figure
	plt.plot(language_list,counters)
	plt.xlabel('this is language_list') # apply labels
	plt.ylabel('this is counters')
	plt.show() # show figure
	'''

	 









	
