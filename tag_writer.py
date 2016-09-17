# coding=utf-8

import eyed3
import glob, os
import re
from os.path import basename

def write_tags(*args, **kwargs):
	try:	
		audiofile = eyed3.load(kwargs.get('file'))
		audiofile.tag.artist = unicode(kwargs.get('artist').decode('utf-8'))
		audiofile.tag.title = unicode(kwargs.get('title').decode('utf-8'))
		
		audiofile.tag.save()	
	except eyed3.id3.tag.TagException as e:
		print "Tag Error({0})".format(e)
	except AttributeError as a:
		print "Attribute Error({0})".format(a)

def main():
	#os.chdir("tracks")
	for file in glob.glob("*.mp3"):
		try:
			m = re.search('^.*(?= -)',basename(file))
			artist = m.group(0)
			m1 = re.search('(?<=- ).*((Mix|Remix|Edition|Dub|Jam)(\)|ix-www.groovytunes.org))',basename(file))		
			try:	
				temp_title = m1.group(0)
				#print("TEMP TITLE: %s" % temp_title)
				temp_title_ = temp_title.replace('[ClapCrate.com]','')	
				title = temp_title_.replace('-www.groovytunes.org','')			
				#print("TITLE: %s" % 	title)	
				#title = temp_title		
				t_dict = {
					'file': file,
					'artist': artist,
					'title': title,
				}		
				write_tags(**t_dict)
			except:
				m1 = re.search('(?<=- ).*(?=\.mp3)',basename(file))	
				try:
					temp_title = m1.group(0)
					#print("TEMP TITLE: %s" % temp_title)
					temp_title_ = temp_title.replace('[ClapCrate.com]','')	
					title = temp_title_.replace('-www.groovytunes.org','')	
					#print("TITLE: %s" % 	title)		
					t_dict = {
						'file': file,
						'artist': artist,
						'title': title,
					}		
					write_tags(**t_dict)
				except:
					print "Attribute Error({0})".format(a)				
		except AttributeError as a:
			print "Attribute Error({0})".format(a)



if __name__ == "__main__":
	main()