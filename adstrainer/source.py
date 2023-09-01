#!/usr/bin/env python

"""
An ad-blocking conversion filter for the Liferea news aggregator.

Input (feed content) is read from standard input (stdin) and output (filtered
feed content) is written to standard output (stdout). The filter accepts a
single command-line argument which should consist of a comma-separated list of
keywords. Each hyperlink in the feed is matched against each keyword; if the
match is found to be positive, the hyperlink is filtered (removed).
"""

__name__ = 'adstrainer'
__version__ = '0.1'
__date__ = 'Thu, 17 Nov 2005'
__author__ = 'Aggelos Orfanakos <csst0266atcsdotuoidotgr>'

from sys import argv, stdin, stdout

import re

keywords = argv[1].split(',')

def filter(match):
    href = match.group(2)

    for keyword in keywords:
        if keyword in href:
            return ''

    return match.group()

content = stdin.read()

content = re.compile('(<|&lt;)a .*?href="?([^"]+)"?.*?(>|&gt;).+?(<|&lt;)/a(>|&gt;)', re.DOTALL).sub(filter, content)

stdout.write(content)