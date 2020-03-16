# Antivirus

This project sets up a collaborative environment for data scientists to have readily accessible resources and dependencies to work with JHU CSSE's data for COVID-19 cases. 

The data is directly fetched raw from JHU's repository: https://github.com/CSSEGISandData/COVID-19.

## Collaboration with Git
To collaborate in this project, first clone the following URL: https://github.com/Gustrigos/Antivirus.git.

Add the following in terminal or cmd. 
```cmd
git clone https://github.com/Gustrigos/Antivirus.git.
```

## Environment Setup
This project works with Python 3.7 or later.

To start, create a virtual environment, activates it, and install all the dependencies needed for this project. 

```cmd
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
```

## Fetching Data 
fetch_data.py gets timeseries data for confirmed, death, and recovered cases directly from JHU CSSE's COVID-19 repository in raw csv format. It then stores each list into a pandas dataframe object. 
