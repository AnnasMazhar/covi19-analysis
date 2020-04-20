import pandas as pd

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 140)

base_url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/"

def get_data(fileName):
	data = pd.read_csv(base_url+fileName).drop(['UID','iso2','iso3','code3','FIPS','Country_Region','Admin2','Lat','Long_'], axis=1)
	data['Province_State'].fillna('<all>', inplace=True)
	return data

confirmed_us = get_data('time_series_covid19_confirmed_US.csv')
deaths_us = get_data('time_series_covid19_deaths_US.csv')


def by_state(dataset, state):
	states = dataset['Province_State'].unique()
	states.sort()
	st = dataset[dataset['Province_State'] == state]#.str.contains(st)]
	return st

# print(by_state(confirmed_us, "New York"))

def by_day(dataset, state, columnName):
	# import pdb; pdb.set_trace()
	dates = dataset.columns[3:]
	v_name = "Day"
	i = 1
	columns = []
	for x in range(len(dates)):
		columns.append(v_name+str(i))
		i+=1
	df_byDay = pd.DataFrame(column=columnName, index=dates)


	return df_byDay

print(by_day(confirmed_us,by_state(confirmed_us, "Newyork"), "ToTal Confirmed"))

def get_county(column):
	return column.split(',')[0]

def by_county(dataset, county):
	cty = dataset[dataset['Combined_Key'].str.match(county)]
	return cty
	
by_county(confirmed_us,"Wyoming")
