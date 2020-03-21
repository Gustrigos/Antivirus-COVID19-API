from fetch_data import df_confirmed, df_death, df_recovered
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

def data_type(data):
	# get metadata (columns that describe the timeseries data)
	metadata = data.iloc[:,:4]

	# get date information and indexing data by country or region
	timeseries = data.set_index(data["Country/Region"]).drop(metadata.columns,axis=1)

	return metadata, timeseries

def country_stats(country):

	# data of a particular country
	try:
		country_data = timeseries.loc[country]
		country_data.index = pd.to_datetime(country_data.index)
	except:
		country_data = timeseries.loc[country].sum(axis=0)
		country_data.index = pd.to_datetime(country_data.index)

	# percentage change daily
	daily_growth = country_data.pct_change(1)

	return country_data, daily_growth


def plot_country(country,start_date,end_date):

	country_data, daily_growth = country_stats(country)

	# latest day data
	print("data as of {}: ".format(today),country_data.iloc[-1])

	plt.title("Confirmed cases in {country} as of {today}".format(country=country,today=today))
	plt.xticks(rotation=45)
	plt.ylabel("Confirmed Cases")
	plt.xlabel("Date")
	plt.plot(country_data.loc[start_date:end_date])
	
def plot_countries(country_list,start_date,end_date):

	cumulative_df = pd.DataFrame()
	growth_df = pd.DataFrame()

	for i in country_list:
		country_data, daily_growth = country_stats(i)
		cumulative_df[i] = country_data
		growth_df[i] = daily_growth

	cumulative_df.loc[start_date:end_date].plot()
	plt.title("Cumulative confirmed cases in the world as of {today}".format(today=today))
	plt.xticks(rotation=45)
	plt.ylabel("Confirmed Cases")
	plt.xlabel("Date")
	plt.legend()

	return cumulative_df, growth_df

#### Inputs ####   

# Use case for Confirmed
metadata, timeseries = data_type(df_confirmed)

country = "US"
critical_country_list = ['US', 'Mexico', 'Italy','France','Iran']
latam_country_list = ['Mexico','Colombia','Peru','Ecuador','Argentina','Uruguay','Chile'] 

country_list = latam_country_list

today = timeseries.T.index[-1]

start_date = dt.date(2020,3,1)
end_date = today

cumulative_df, growth_df = plot_countries(country_list,start_date=start_date,end_date=end_date)


plt.show()


