from get_news import get_news
import datetime as dt
from get_news import *

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

mex_sources = str(','.join(mexican_sources.values()))

topic = 'covid-19 and NS:RTRS'
source = 'RTRS'
start_date= dt.date(2020,1,22)
end_date = dt.date(2020,3,18)
n_articles = 100


covid_headlines = get_news(topic=topic,source=source,start_date=start_date,end_date=end_date,n_articles=n_articles)

# Sentiment, subjectivity, and polarity
from textblob import TextBlob


def sentiment_score(headlines):

	df = headlines
	df['Polarity'] = None
	df['Subjectivity'] = None
	df['Score'] = None

	# Getting the full article of the headlines rendered
	for idx, story_id in enumerate(df['storyId'].values):
		news_text = ek.get_news_story(story_id)
		sentA = TextBlob(news_text)

		# storing sentiment polarity and subjectivity
		df['Polarity'].iloc[idx] = sentA.sentiment.polarity
		df['Subjectivity'].iloc[idx] = sentA.sentiment.subjectivity

	    # labeling polarity based on a threshold
		positive_threshold = 0.05

		if sentA.sentiment.polarity >= positive_threshold:
			score = 'positive'
		elif -positive_threshold < sentA.sentiment.polarity < positive_threshold:
			score = 'neutral'
		else:
			score = 'negative'

		df['Score'].iloc[idx] = score

	return df

df = sentiment_score(headlines=covid_headlines)

# Exports output into a CSV file
#df.to_csv('news.csv')




