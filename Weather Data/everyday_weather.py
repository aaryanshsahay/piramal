from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
import re


#url for both links , kosamba and jambusar weather conditions
urls=['https://www.worldweatheronline.com/kosamba-weather-history/gujarat/in.aspx','https://www.worldweatheronline.com/jambusar-weather-history/gujarat/in.aspx']
#for measuring time
start=time.time()

#this function gets the value and stores it in a nested list.
def get_data_from_url(url):
	data=[]

	req=requests.get(url)
	soup=BeautifulSoup(req.text,'lxml')

	divs=soup.find_all('div',class_='row text-center')
	
	a=divs[0].text
	#since the site doesnt use html tables , manually editing each value and then updating the list
	a=a.split('TimeWeatherTempFeelsWindGustRainHumidityCloudPressureVis')
	a=a[1].split('mbExcellent')
	#total 8 observations -> 00:00,00:03,00:06,00:09,00:12,00:15,00:18,00:21
	for i in range(8):
		a1=a[i].split(' ')
		#the temperature has degree celcius so replacing it with an empty string
		a1[2]=a1[2].replace('°c','')
		a1[3]=a1[3].replace('°c','')
		#some elements contain unneccesary info like 'km/h' or 'from' , removing them.
		a1.pop(4)
		a1.pop(4)
		a1.pop(7)
		#here separating numeric value from integer like 'NW72' to just '72' 
		temp=re.findall(r'\d+',a1[4])
		a2=list(map(int,temp))
		a1[4]=str(a2[0])
		a1[5]=a1[5].split('km/h')[1]
		#some elements are separated incorrectly , joining them to get the correct data.
		s=''
		a1[5]=s.join(a1[i] for i in [5,6])
		##some elements are separated incorrectly , editing them to get the correct data.
		a3=a1[5].split('mm')[0]
		a4=a1[5].split('mm')[1]
		#updating list with the updated values
		a1[5]=a3
		a1[6]=a4
		#separating % values (humidity and cloud and pressure) and storing them individually in the list
		a5=a1[6].split('%')[0]
		a6=a1[6].split('%')[1]
		a7=a1[6].split('%')[2]
		#updating the values in the list
		a1[6]=a5
		a1.append(a6)
		a1.append(a7)
		#adding the final clean list to the main list which will contain all the lists
		data.append(a1)
	return data

#this function takes the nested list and creates a dataframe
def make_df_from_data(data):
	df=pd.DataFrame(data,columns=['Time','Temp','Feels','Wind','Gust','Rain(mm)','Humidity(%)','Cloud(%)','Pressure(mb)'])
	return df

## to get kosamba data
kosamba_data=get_data_from_url(urls[0])

## to get jambusar data
jambusar_data=get_data_from_url(urls[1])
## converting it into a dataframe , one can store this as a csv/excel later
kosamba_df=make_df_from_data(kosamba_data)
jambusar_df=make_df_from_data(jambusar_data)

#demo output : shows all the collected data for the current date.
print('Kosamba')
print(kosamba_df)
print('+'*100)
print('Jambusar')
print(jambusar_df)

print('Time Taken:',time.time()-start())