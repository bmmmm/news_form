import geonamescache
import feedparser
from newspaper import Article

gc = geonamescache.GeonamesCache()

#static variables
offline = True
all_cities_low = gc.get_cities()
googlemaps='https://www.google.com/maps/search/?api=1&query='
#static links
offline_path = r'C:\Users\bma\Documents\programming\news_form\data\rss-en-all.xml'
link_dw_all = 'https://rss.dw.com/atom/rss-en-all'
link_open_europe_all = 'https://openeurope.org.uk/feed/?post_type=today&tags=article-50'


def search_city( city_list):
	for city_article in city_list:
		for city_all in all_cities_low.values():
			if city_article == city_all['name'].lower():
				print(city_list)
				print('City found >> ',city_article, city_all['countrycode']) 
				print(city_all['latitude'],city_all['longitude'])
				print(googlemaps+str(city_all['latitude'])+','+str(city_all['longitude']))

	

if offline:
	d = feedparser.parse(offline_path)
else:
	d = feedparser.parse(link_dw_all)
for news_post in d.entries:
	# link response splited
	formated_link = news_post.link.split('?',1)[0]
	#https://www.dw.com/de/was-lesen-100-gute-bücher/a-45926702?maca=de-rss-de-all-1119-xml-atom
	#print(news_post.title,'\n',formated_link,'\n')
	article = Article(formated_link, language='en')
	article.download()
	article.parse()
	article.nlp()
	print('')
	#print(formated_link)
	#print(article.keywords)
	search_city(article.keywords)
	#print(article.summary)
	print('')


#print(gc.get_cities_by_name('Heilbronn') )



