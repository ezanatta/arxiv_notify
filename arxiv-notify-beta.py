import feedparser
import numpy as np
import re
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
from datetime import date, datetime, timedelta
from threading import Timer
from os.path import expanduser
import os

def tex_escape(text):
    """
        :param text: a plain text message
        :return: the message escaped to appear correctly in LaTeX
    """
    conv = {
        '&': '',
        '%': '',
        '$': '',
        '#': '',
        '_': '',
        '{': '',
        '}': '',
        '~': '',
        '^': '',
        '\\': '',
        '<': '',
        '>': '',
        ':': '',
    }
    regex = re.compile('|'.join(re.escape(str(key)) for key in sorted(conv.keys(), key = lambda item: - len(item))))
    return regex.sub(lambda match: conv[match.group()], text)


def arxivnotify():
    home = expanduser("~")
    anf = os.getenv('ARXIV_NOTIFY_FOLDER')

    papers = list()
    links = list()

    with open(home+'/.config/arxiv-notify/tags', 'r') as f:
        tags = [line.rstrip('\n') for line in f]

    url = 'http://arxiv.org/rss/astro-ph.GA'
    data = feedparser.parse(url)

    for entry in data.entries:

        title = entry.title
        title = tex_escape(title)
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


arxivnotify()
# x = datetime.today()
# y = x.replace(day=x.day, hour=15, minute=0, second=0, microsecond=0) + timedelta(days=1)
# delta_t = y-x

# secs = delta_t.total_seconds()

# t = Timer(secs, arxivnotify)
# t.start()
