##################################################################

# Name: Patrick Ernest
# NetId: pernes2
# UIN: 663182392
# Class: CS491 - Introduction to Data Science

##################################################################

# Question 2 : Reformatting Data - Super Bowl Champions - transform.py

##################################################################

import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen

##################################################################

# In this python code we use BeautifulSoup which is a web scraping
# tool, essentailly it is used to scrap data from web pages.

##################################################################
def run():
	res=urlopen("https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions")
	html=res.read()
	soup= BeautifulSoup(html,'html.parser')
	tab=soup.findAll("table",{"class":"wikitable sortable"})
	t=tab[1]
	with open('result.csv','w') as csvfile:
		fn=['game number','year','winning team','score','losing team','venue']
		w=csv.writer(csvfile,delimiter=',')
		w.writerow(fn)
		for row in t.find_all('tr')[1:51]:
			col=row.findAll("td")
			game_no=(col[0].find('a').get_text()).rstrip()
			year=((col[1].get_text())[-4:]).rstrip()
			wt=((col[2].get_text().split("!"))[0]).rstrip()
			score=((col[3].get_text().split("!"))[1]).rstrip()
			lt=((col[4].get_text().split("!"))[0]).rstrip()
			ven=((col[5].get_text().split("!"))[0]).rstrip()
			w.writerow((game_no,year,wt,score,lt,ven))
if __name__ == '__main__':
    run()
