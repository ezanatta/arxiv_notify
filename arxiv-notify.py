import feedparser
from datetime import date, datetime, timedelta
from threading import Timer
import os
from pathlib import Path
import sys
import argparse

def setup():

    os.makedirs(home+'/.config/arxiv_notify/')
    Path(home+'/.config/arxiv_notify/tags').touch()
    Path(home+'/.config/arxiv_notify/feed').touch()

    print('SETUP:\n')
    print('Edit the files \'tag\' and \'feed\' in the '+home+'./config/arxiv_notify folder. If those files/folders are not there, create them.\n\n')
    print('Create the environmental variable ARXIV_NOTIFY_FOLDER where you will want to save the file with the papers found.\n')
    print('In bash you can add \n export ARXIV_NOTIFY_FOLDER=\'path-to-save-folder\' to .bashrc, for instance.')


def arxivnotify(v):

    papers = list()
    links = list()
    summaries = list()
    found_tags = list()

    try:
        with open(conf_path+'tags', 'r') as f:
            tags = [line.rstrip('\n') for line in f]
    except:
        print('tags file not found!')
        sys.exit()
    try:
        with open(conf_path+'feed', 'r') as f:
            feed = [line.rstrip('\n') for line in f]
    except:
        feed = list('astro-ph')

    url = 'http://arxiv.org/rss/'+feed[0]
    data = feedparser.parse(url)


    if(v==1):
        print('Scraped papers for today:')
        for entry in data.entries:
            title = entry.title[0:entry.title.rfind('. ')]
            print("{0}".format(title))
    elif(v==2):
        print('Scraped papers for today:')
        for entry in data.entries:
            title = entry.title[0:entry.title.rfind('. ')]
            print("{0}".format(title))
        print('\nKeywords loaded for searching:')
        for tag in tags:
            print("{0}".format(tag))

    for entry in data.entries:

        for tag in tags:
            if (tag.lower() in entry.title.lower()) or ((tag.lower() in entry.summary.lower())):
                papers.append(entry.title[0:entry.title.rfind('. ')])    #removing the arxiv code stuff
                links.append(entry.link)
                summaries.append(entry.summary)
                found_tags.append(tag)


    with open(anf+'arxiv_weekly_notes') as g:
        if str(date.today().strftime("%d/%m/%y")) not in g.read():
            g.close()
            with open(anf+'arxiv_weekly_notes', 'a') as g:
                g.write('#'+str(date.today().strftime("%d/%m/%y"))+'\n\n')

    for p in zip(papers, links, found_tags):
        with open(anf+'arxiv_weekly_notes') as g:
            if str(p[1]) not in g.read():
                g.close()
                with open(anf+'arxiv_weekly_notes', 'a') as g:
                    g.write('*'+p[0]+'*\n'+p[1]+' \n_Keyword found:_ '+p[2]+'\n\n')

if __name__ == "__main__":

    home = os.path.expanduser("~")

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", default='/.config/arxiv-notify/', help="path to configuration folder (if not on the default location)", type=str, nargs='?')
    parser.add_argument("-v", default=0, help="verbose level; 0: quiet, 1: print today's papers, 2:print today's papers and tags being looked into them", type=int, nargs='?')
    args = parser.parse_args()

    conf_path = home+args.c
    verbosity = args.v


    if not os.path.exists(conf_path):
        setup()
    try:
        anf = os.getenv('ARXIV_NOTIFY_FOLDER')
    except:
        print('ARXIV_NOTIFY_FOLDER environment variable not found!')
        sys.exit()


    arxivnotify(verbosity)
