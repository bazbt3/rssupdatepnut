# rssupdatepnut
# v0.2.2 for Python 3.5

# Import RSS feed parser:
import feedparser

# Import date parser, parse:
import dateutil.parser

# Import JSON module:
import json

# Import os, used to check if files exist:
import os

# Import @33MHz and @thrrgilag's library for interacting with pnut.io:
import pnutpy

# Get RSS feed from Internet:
feed_title = 'http://bazbt3.10centuries.org/rss.xml'
d = feedparser.parse(feed_title)

# Extract the most recent feed post's title, link & published date:
p_title = d.entries[0].title
p_link = d.entries[0].link
p_publish = d.entries[0].published

p_latest = p_publish

# Create a list of title, link & published date:
p_list = []
p_list.append(p_title)
p_list.append(p_link)
p_list.append(p_publish)

# Save the latest post to a file, as JSON:
with open('rssupdatepnut_new.txt', 'w') as newfile:  
	json.dump(p_list, newfile)

# Does an 'rssupdatepnut_base.txt' file already exist, i.e. has this program run before? If no, create the file with its only contents as the most recent post date; if yes, read its contents:
if not os.path.exists('rssupdatepnut_base.txt'):
	basefile_w = open('rssupdatepnut_base.txt', 'w')
	basefile_w.write(p_publish)
	basefile_w.close()
if os.path.exists('rssupdatepnut_base.txt'):
	basefile_r = open('rssupdatepnut_base.txt', 'r') 
	p_last = basefile_r.read()
	basefile_r.close()

# Compare the post dates, if new > base, compile message & save latest over base:
p_last = dateutil.parser.parse(p_last)
p_latest = dateutil.parser.parse(p_latest)
pnut_message = ''
if p_latest > p_last:
	pnut_message = 'New blog post:\n' + p_title + '\n' + p_link + '\n' + p_publish
	basefile_w = open('rssupdatepnut_base.txt', 'w')
	basefile_w.write(p_publish)
	basefile_w.close()
	
# Setup pnut.io authorisation:
tokenfile = open("pnut_app_token.txt", "r")
token = tokenfile.read()
token = token.strip()
pnutpy.api.add_authorization_token(token)

# If a new blog post exists, create a public post using the text from pnut_message:
if pnut_message != '':
	posttext = pnut_message
	postcontent = pnutpy.api.create_post(data={'text': posttext})
