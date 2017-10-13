# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 15:58:58 2017

@author: JINGR1
"""
import urllib
def read_text():
    quotes = open(r"E:\Mycode\python\ProgrammingFundamental\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_for_check):
    connection = urllib.request.urlopen("http://www.wdyl.com/profanity?q="+text_for_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document property.")
    
read_text()