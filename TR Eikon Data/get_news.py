# Thomson Reuters Eikon API Implementation to track news
import os
from dotenv import load_dotenv
load_dotenv()

import eikon as ek
ek.set_app_key(os.getenv('EIKON_API_KEY'))
import pandas as pd

def get_news(topic,source,start_date,end_date,n_articles):

	'''
	To search a company, Append 'R:' in front of RIC (ticker followed by a dot and Echange ID (eg: TSLA.O))
	
	The following is a list of news sources and their respective code from Mexico. 

	mexican_sources = {
		'Mexico Ledger': 'MEXLED',
		'El Financiero': 'ELMEX',
		'El Economista': 'ELECOP',
		'La Jornada': 'LAMEX',
		'Mega News': 'MEGNEW',
		'Milenio': 'MILMEX',
		'El Nacional': 'ELNACI',
		'Expansion': 'EXPSPB',
		'Excelsior': 'EXCMEX',
		'Mural': 'MURMEX',
		'El Norte': 'ELNORT',
		'Estrategia': 'ESTMEX',
		'La I': 'LAIMEX',
		'Al Chile': 'ALCHIL',
		'Publimetro': 'PUBMEX',
		'Comunicae': 'COMMEX',
		'Diario de Yucatan': 'DIADEY',
		'Contexto Durango': 'CONDED', 
	}

	'''

	# formats query based on function inputs
	#search = '{topic} and NS:{source}'.format(topic=topic,source=source)
	search = topic

	# getting headlines 
	headlines = ek.get_news_headlines(query=search,date_from=start_date,date_to=end_date, count=n_articles)

	return headlines
       
