import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 120)


def get_data(fileName):
	data = pd.read_csv(fileName).drop(['UID','iso2','iso3','code3','FIPS','Admin2','Lat','Long_'], axis=1)
	data['Province_State'].fillna('<all>', inplace=True)
	return data

confirmed_us = get_data('time_series_covid19_confirmed_US.csv')
deaths_us = get_data('time_series_covid19_deaths_US.csv')


def by_state(dataset, state):
	states = dataset['Province_State'].unique()
	states.sort()
	dates = list(dataset.columns[3:].unique())
	statewise_report = pd.DataFrame(columns=dates, index = states)
	# import pdb; pdb.set_trace()
	for st in states:
		state = dataset[dataset['Province_State'].str.contains(st)]
		print(type(state))
		# for dt in dates:

	return statewise_report

by_state(confirmed_us, "Alabama")
