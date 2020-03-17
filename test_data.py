from fetch_data import df_confirmed, df_death, df_recovered
import matplotlib.pyplot as plt
import pandas as pd

def data_type(data):
	# get metadata (columns that describe the timeseries data)
	metadata = data.iloc[:,:4]

	# get date information and indexing data by country or region
	timeseries = data.set_index(data["Country/Region"]).drop(metadata.columns,axis=1)

	return metadata, timeseries

# Use case for Confirmed
metadata, timeseries = data_type(df_confirmed)

country = "US"

# data of a particular country
country_data = timeseries.loc[country].sum(axis=0)
country_data.index = pd.to_datetime(country_data.index)

today = country_data.index[-1].date()

# percentage change daily
print(country_data.pct_change(1))

# up to date data
print("data as of {}: ".format(today),country_data.iloc[-1])

plt.title("Confirmed cases in {country} as of {today}".format(country=country,today=today))
plt.xticks(rotation=45)
plt.ylabel("Confirmed Cases")
plt.xlabel("Date")
plt.plot(country_data)
plt.show()

