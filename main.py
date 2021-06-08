from bs4 import BeautifulSoup
from textblob import TextBlob
import requests
import nltk
import pandas as pd
#nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer
import time

start=time.time()
sia=SentimentIntensityAnalyzer()


urls=['https://oilprice.com/Latest-Energy-News/World-News/US-Claws-Back-Millions-From-Pipeline-Ransomware-Attackers.html','https://oilprice.com/Latest-Energy-News/World-News/North-Sea-Oil-Floating-Off-Europe-Could-Signal-Weak-Asian-Demand.html','https://oilprice.com/Latest-Energy-News/World-News/OPEC-Head-Global-Oil-Inventories-Will-Continue-To-Draw-Down.html','https://oilprice.com/Latest-Energy-News/World-News/Scientists-Find-Cheap-And-Easy-Way-To-Extract-Lithium-From-Seawater.html','https://oilprice.com/Latest-Energy-News/World-News/EU-Approves-21B-Green-Transition-Fund.html','https://oilprice.com/Latest-Energy-News/World-News/Renewables-Was-Sole-US-Energy-Source-With-Rising-Consumption-In-2020.html','https://oilprice.com/Latest-Energy-News/World-News/Russia-Claims-Its-Compliance-With-OPEC-Cuts-Was-Almost-100-In-May.html','https://oilprice.com/Latest-Energy-News/World-News/Peak-Oil-Demand-May-Be-Ten-Years-Away.html','https://oilprice.com/Latest-Energy-News/World-News/Uganda-Picks-Four-Firms-For-New-Oil-Exploration-Round.html','https://oilprice.com/Latest-Energy-News/World-News/US-Natural-Gas-Storage-Capacity-Hardly-Increased-Since-Start-Of-Shale-Boom.html','https://oilprice.com/Latest-Energy-News/World-News/Russia-Bets-On-Waste-To-Energy-Plants.html','https://oilprice.com/Latest-Energy-News/World-News/Canadian-EV-Maker-Unveils-Worlds-First-Crypto-Mining-Car.html','https://oilprice.com/Latest-Energy-News/World-News/Brazils-Worst-Drought-In-91-Years-Is-Good-News-For-LNG.html','https://oilprice.com/Latest-Energy-News/World-News/Extreme-Drought-Puts-Californias-Power-Supply-At-Risk.html','https://oilprice.com/Latest-Energy-News/World-News/More-Than-2-Billion-Tons-Of-Coal-Mining-Capacity-Is-About-To-Come-Online.html','https://oilprice.com/Latest-Energy-News/World-News/Larger-Than-Expected-Crude-Draw-Fuels-Oil-Price-Rally.html']
def get_news_articles(url):
	'''
	takes in a url and returns the content of the news article.

	'''
	# bs4 setup
	req=requests.get(url)
	soup=BeautifulSoup(req.text,'lxml')
	# the news content is inside the 'wysiwyg clear' class.
	para_content=soup.find('div',class_='wysiwyg clear')
	# getting all the text which is in 'p' tags inside the div class.
	para_text=para_content.find_all('p')

	res=[]
	# conveting each element to text
	output=[ele.text for ele in para_text]
	output1=[]
	# replacing the line break or '\n' with empty strings 
	#-and storing it in output1
	for i in output:
		i=i.replace('\n','')
		output1.append(i)

	# the last 2 elements contain the name of the person who wrote the article and more info,etc , dropping them
	for i in range(len(output1)):
		res.append(output1[i-2])
	# thee first 2 elements contain the name and some unneccessary info, dropping them.
	res.pop(0)
	res.pop(0)
	# since the final prouduct is a list of strings, merging them to form a paragraph.
	final=''
	final=final.join(res)
	# returning the string
	return final


def get_polarity_score_textblob(para):
	'''
	takes in an article(string) and computes the polarity score
	'''
	analysis=TextBlob(para).sentiment
	score=analysis.polarity
	return score

def get_polarity_score_nltk_vader(para):
	'''
	takes in an article(string) and computes the polarity score, nltk.
	'''
	score=sia.polarity_scores(para)
	return score

def make_df(news,nltk,textblob):
	'''
	Stores all the data in a dataframe, can be converted to csv/excel etc
	'''
	data={'News Article':news,'NLTK Score':nltk,'TextBlob Score':textblob}
	df=pd.DataFrame(data)
	return df

def main():
	
	# getting all the articles in a list
	news_list=[]
	for i in urls:
		para=get_news_articles(i)
		news_list.append(para)
	
	# getting the nltk and textblob polarity scores for each article
	#- and storing it in a list
	nltk_scores=[]
	textblob_scores=[]
	for news in news_list:
		score_nltk=get_polarity_score_nltk_vader(news)
		nltk_scores.append(score_nltk)

		score_textblob=get_polarity_score_textblob(news)
		textblob_scores.append(score_textblob)

	# storing everything in a dataframe
	df=make_df(news_list,nltk_scores,textblob_scores)

	return df.head()



print(main())
print('Time Taken:',time.time()-start)