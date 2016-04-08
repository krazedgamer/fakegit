#!/usr/bin/env python
#
# Copyright (c) 2016 Wilson Ding
# 
#

import datetime
import math
import itertools
import urllib2
import json

def commit(content, commitdate):
    template = ("""echo {0} >> fakegit\n"""
    """GIT_AUTHOR_DATE={1} GIT_COMMITTER_DATE={2} """
    """git commit -a -m "fakegit" > /dev/null\n""")
    return template.format(content, commitdate.isoformat(), 
            commitdate.isoformat())

def fake_it(username, repo):
    template = ('#!/bin/bash\n'
        'REPO={0}\n'
        'git init $REPO\n'
        'cd $REPO\n'
        'touch README.md\n'
        'git add README.md\n'
        'touch fakegit\n'
        'git add fakegit\n'
        '{1}\n'
        'git remote add origin git@github.com:{2}/$REPO.git\n'
        'git pull\n'
        'git push -u origin master\n')
    strings = []

    date_list = [datetime.datetime(2016, 5, 7, 12, 00, 00, 000000) - datetime.timedelta(days=x) for x in range(0, 31)]

    for date in date_list:
        strings.append(commit("Notice Me Senpai Prakhar", date))
    return template.format(repo, "".join(strings), username)

def save(output, filename):
    """Saves the list to a given filename"""
    f = open(filename, "w")
    f.write(output)
    f.close()

def main():
    print ("Get a free Freetail Hackers Shirt!")
    print ("Use this script to get a month of commits from April 7,2016 to May 7,2016...")
    print ("Notice Me Prakhar Senpai. Pls no hate. Use at your own discretion...")
    print ("")
    print ("")
    print ('Enter your github username:')
    username = raw_input(">")

    print ('Enter name of the repo to be used by fakegit:')
    repo = raw_input(">")

    output = fake_it(username, repo)

    save(output, 'fakegit.sh')
    print ('fakegit.sh saved.')

if __name__ == '__main__':
    main()