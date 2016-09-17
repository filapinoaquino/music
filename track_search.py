# coding=utf-8

from py_bing_search import PyBingWebSearch
import re
import sys
import webbrowser


def main():
	api_key = ""
	artist = raw_input("Artist: ") 
	song = raw_input("Song: ")	
	pirate = "(zippyshare | dancedj.club | mypromosound.com | clapcrate.com | fordj.uk | epdj.org | www.djlist.org | deepdj.org | www.djlist.org | hulkshare | sickworldmusic | zippygo | themusic.lt | housezone.lt | www.radiofly.ws | exclusivesource4dj | techdeephouse.com | www.groovytunes.org | MusiKA.biz | drunkenbeat.net | music-for-djs)"	
	#pirate = "zippyshare"
	search_term = artist + " AND " + song + " AND " + pirate

	#print("You are searching for: %s" % search_term)
	print('')
	bing_web = PyBingWebSearch(api_key, search_term)
	first_twenty_result = bing_web.search(limit=100, format='json') #1-20

	count = 1
	for result in first_twenty_result:
		m = re.search('(\.zippyshare\.com|hulkshare\.com\\\S*|tusfiles\.com|filescdn\.com)',result.url)
		try:
			url = m.group(0)
			#print url	
			print("Result Tally: %s" % str(count))
			print("Title: %s" % result.title)
			print("Description: %s" % result.description)
			print("URL: %s" % result.url)
			print('')
			chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
			webbrowser.get(chrome_path).open(result.url)
			count = count + 1								
		except:
			continue
if __name__ == "__main__":
	main()