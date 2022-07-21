Arxiv Notify
============

C'mon, someone already did this before and for sure much better than this, but...

This is a very simple python script to gather any ArXiv RSS feed and save the papers that have specific keywords in the title or abstract. Keywords are get from a user generated file in the configuration folder. It runs through the RSS feed and saves a file on a user chosen location with the saved papers for each day (the ArXiv rss updates daily, just like the site).

##Dependencies:

Python 3+<br/>
feedparser<br/> 

##Setup:


When you run arxiv-notify.py the first time it will attempt to create two files in the /home/.config/arxiv_notify/ folder: 'tags' and 'feed'.

You can create them yourself if you want to be safe or if for some reason the code doesn't. 

The 'tags' file should have the keywords you want your papers to have on the titles, one for each line. Like this:

    globular 
    nuclei
    dark matter 
    halo

The 'feed' file lists the feeds that you want arxiv_notify to check for these keywords. Currently only ONE feed is available at a time, but in the future I want to add the option to search multiple feeds if needed. If the user don't create this file or leave it empty, the default feed is the whole astro.ph. However, you can select individual topics. For instance, if one wants to look into only the extragalactic papers, you would simply add this line to the 'feed' file:

    astro-ph.GA

Finally, you'll want to have an environment variable called 'ARXIV_NOTIFY_FOLDER' where arxiv_notify will save a text file with the papers it found, separated by day. For instance, in bash, you can add this line to .bashrc:

.. code-block :: bash 

     $ export ARXIV_NOTIFY_FOLDER='/path-to-save-folder'

Conveniently (for me), the saved file follows the standard of the vim-notes plugin (markdown).

##USAGE:

.. code-block:: python
        
    $ python arxiv-notify

##BUGS:

My goal is to have this script to run silently in the background and update daily. I'm still working on how I could this in the best way possible, so for now you'll have to run it manually everytime. 

##TODO:

    * Make it run silently and update daily
    * Add multiple feeds
