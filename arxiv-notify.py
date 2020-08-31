import feedparser
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from datetime import date, datetime, timedelta
from threading import Timer
import os
from pathlib import Path
import sys

def setup():

    os.makedirs(home+'/.config/arxiv_notify/')
    Path(home+'/.config/arxiv_notify/tags').touch()
    Path(home+'/.config/arxiv_notify/feed').touch()

    print('SETUP:\n')
    print('Edit the files \'tag\' and \'feed\' in the '+home+'./config/arxiv_notify folder. If those files/folders are not there, create them.\n\n')
    print('Create the environmental variable ARXIV_NOTIFY_FOLDER where you will want to save the file with the papers found.\n')
    print('In bash you can add \n export ARXIV_NOTIFY_FOLDER=\'path-to-save-folder\' to .bashrc, for instance.')


def arxivnotify():

    papers = list()
    links = list()

    try:
        with open(home+'/.config/arxiv-notify/tags', 'r') as f:
            tags = [line.rstrip('\n') for line in f]
    except:
        print('tags file not found!')
        sys.exit()
    try:
        with open(home+'/.config/arxiv-notify/feed', 'r') as f:
            feed = [line.rstrip('\n') for line in f]
    except:
        feed = list('astro-ph')

    url = 'http://arxiv.org/rss/'+feed[0]
    data = feedparser.parse(url)

    for entry in data.entries:

        title = entry.title
        title = title[:len(title)-36]
        title = title[0:title.rfind('.')]    #removing the arxiv code stuff

        for tag in tags:
            if tag in title.split():
                papers.append(title)
                links.append(entry.link)

    pl = zip(papers, links)

    with open(anf+'arxiv_weekly_notes', 'a') as g:
        g.write('#'+str(date.today().strftime("%d/%m/%y"))+'\n\n')

    for p in pl:
        Notify.init('Arxiv Notification')
        Notify.Notification.new(summary=p[0], body='<a href=\"'+p[1]+'\">'+p[1]+'</a> \n').show()

        with open(anf+'arxiv_weekly_notes', 'a') as g:
            g.write(p[0]+'\n'+p[1]+' \n')



home = os.path.expanduser("~")

if not os.path.exists(home+'/.config/arxiv-notify/feed'):
    setup()
try:
    anf = os.getenv('ARXIV_NOTIFY_FOLDER')
except:
    print('ARXIV_NOTIFY_FOLDER environment variable not found!')
    sys.exit()


arxivnotify()
