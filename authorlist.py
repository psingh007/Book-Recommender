import pandas as pd
import random

def get_author_list(x):
	'''
	purpose: To take a column of author from the dataset and output a list with 
	all the authors in it

	:param x: input pd.series object 
	:type x: pd.core.series.Series

	return: list
	'''

	options_list = list(', '.join(x.array).split(','))
	#print(options_lst)

	return list(set(options_list))


if __name__ == '__main__':
	data = pd.read_csv("datav3.csv")
	a = data['author']
	list_author = get_author_list(a)
	top_10 = []
	for i in range(10):
		top_10.append(random.choice(list_author))
		assert top_10[i] != 'Anonymous' or top_10[i] != ''
	print(top_10)


	