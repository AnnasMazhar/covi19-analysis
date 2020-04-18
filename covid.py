import pandas as pd


def get_data(fileName):
	data = pd.read_csv(fileName).drop(['UID','iso2','iso3','code3','FIPS','Admin2','Lat','Long_'], axis=1)
	return data

print(get_data('time_series_covid19_confirmed_US.csv'))