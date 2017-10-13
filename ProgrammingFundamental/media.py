# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:37:02 2017

@author: JINGR1
"""
import webbrowser
class Movie(object):
    '''This class provides a way to store movie related information'''
    VALID_RATINGS = ['G','PG','PG-13','R']
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)