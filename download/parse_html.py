#!/usr/bin/env python3    

from bs4 import BeautifulSoup

with open('gw_capitol_cases.html', 'r') as f:

    contents = f.read()

    soup = BeautifulSoup(contents, 'html.parser')
    for a in soup.find_all('a', href=True):
    	if "javascript:void(0)" in a['href']:
    		continue
    	print (a['href'])
