Arxiv Notify

C'mon, someone already did this before and for sure much better than this, but...

This is a very simple python script to gather any ArXiv RSS feed and save the papers that have specific keywords in the title. Those keywords are get from a user generated file in the configuration folder. 

When arxiv_notify is run, it runs through the RSS feed and shows notifications in the desktop for the papers it found within those constraints. Additionally, it saves a file on a user chose location with the saved papers for each day (the ArXiv rss updates daily, just like the site).

Dependencies:

Python 3+
feedparser
gi

Setup:

When you run arxiv-notify.py the first time it will attempt to create two files in the /home/.config/arxiv_notify/ folder: 'tags' and 'feed'.

You can create them yourself if you want to be safe or if for some reason the code doesn't. 

The 'tags' file should have the keywords you want your papers to have on the titles, one for each line. Like this:

globular
nuclei
dark matter
halo

The 'feed' file lists the feeds that you want arxiv_notify to check for these keywords. Currently only ONE feed is available at a time, but in future I want to add the option to search multiple feeds if needed. If the user don't create this file or leave it empty, the default feed is the whole astro.ph. However, you can select individual topics. For instance, if one wants to look into only the extragalactic papers, you would simply add this line to the 'feed' file:

astro.ph.GA

Finally, you'll want to have an environment variable called 'ARXIV_NOTIFY_FOLDER' where arxiv_notify will save a text file with the papers it found, separated by day. For instance, in bash, you can add this line to .bashrc:

export ARXIV_NOTIFY_FOLDER='/path-to-save-folder'

Conveniently (for me), the saved file follows the standard of the vim-notes plugin.


BUGS:

My goal is to have this script to run silently in the background and update daily. I'm still working on how I could this in the best way possible, so for now you'll have to run it manually everytime. And due to this, obvisouly if you run it more than one time in a single day it will created a repeated entry in the file saved in the ARXIV_NOTIFY_FOLDER. 

I only guarantee that it works for keywords with no spaces. Theoretically it should work for multiple words, like 'Globular cluster', but somehow it doesn't work sometimes. So in a case like this, for example, use "Globular" instead and it will work fine. 


