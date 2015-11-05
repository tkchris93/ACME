import pandas as pd
import csv
import numpy as np
import random

def initialize(pclass_change=True):
	# get .csv file into data list
	my_file = open('titanic3.csv','r')
	reader = csv.reader(my_file)
	data = []
	for line in reader:
		data.append(line)

	# initialize pandas DataFrame
	df = pd.DataFrame(data[1:], index=range(len(data)-1), columns=data[0])

	# trim it down to just the important columns
	trimmed = df.loc[:,['pclass','survived','sex','age','sibsp','parch']]

	# replace values
	trimmed.loc[:,'sex'].replace('male','1', inplace=True)
	trimmed.loc[:,'sex'].replace('female','0', inplace=True)
	trimmed = trimmed.replace('', np.nan).dropna()

	# redo indexing
	trimmed.set_index([range(len(trimmed.loc[:,'pclass']))], inplace=True)

	# add first_class and second_class columns if prescribed
	if pclass_change:
		first_class = []
		second_class = []
		for i in xrange(0,len(trimmed.loc[:,'pclass'])):
			if trimmed.loc[i,'pclass'] == '1':
				first_class.append(1)
				second_class.append(0)
			elif trimmed.loc[i,'pclass'] == '2':
				first_class.append(0)
				second_class.append(1)
			elif trimmed.loc[i,'pclass'] == '3':
				first_class.append(0)
				second_class.append(0)
			else:
				print "problem"
		
		trimmed['first_class'] = pd.Series(first_class, index=trimmed.index)
		trimmed['second_class'] = pd.Series(second_class, index=trimmed.index)
		del trimmed['pclass']

	# sizes for training set and test set
	training_size = int(.6*len(trimmed.index))
	test_size = len(trimmed.index) - training_size

	# get sets of indices
	all_indices = set(range(len(trimmed.index)))
	training_indices = set(random.sample(all_indices,training_size))
	test_indices = all_indices - training_indices

	# splice using indices just calculated
	training = trimmed.loc[training_indices]
	test = trimmed.loc[test_indices]

	return training, test
