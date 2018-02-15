# Import RSS feed parser:
import feedparser

# Import JSON module:
import json

# Import os, used to check if files exist:
import os

# Get RSS feed from Internet:
feed_title = 'http://bazbt3.10centuries.org/rss.xml'
d = feedparser.parse(feed_title)

# Extract 10 feed posts' titles, links & published-on data:
number = 9
p_list = []
p_details = []
while number >= 0:	
	p_title = d.entries[number].title
	# Keep most recent title for later comparison:
	if number == 0:
		p_latest = p_title
	p_link = d.entries[number].link
	p_publish = d.entries[number].published

	# Create a nested list of posts
	p_details.append(p_title)
	p_details.append(p_link)
	p_details.append(p_publish)
	
	p_list.append(p_details)
	
	number -= 1
	p_details = []

# Print the list of posts:
post = 9
while post >= 0:
	item = 0
	while item < 3:
	 print(p_list[post][item])
	 item += 1
	post -= 1

# Save the latest posts list to a file, as JSON:
#rssupdatepnut_base.txt
with open('rssupdatepnut_new.txt', 'w') as outfile:  
	json.dump(p_list, outfile)

# Does an 'rssupdatepnut_base.txt' file already exist? If yes, compare its most recent post with the mew data. If not, create it with the most recent post title:
# p_latest
if os.path.exists('rssupdatepnut_base.txt'):
	print('it exists')
elif not os.path.exists('rssupdatepnut_base.txt'):
	with open('rssupdatepnut_base.txt', 'w') as outfile:  
		json.dump(p_latest, outfile)
