# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:03:59 2017

@author: JINGR1
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1506179240635&di=fbd6d7cd368f4bfca4501a660607ce54&imgtype=0&src=http%3A%2F%2Fs13.sinaimg.cn%2Fmiddle%2F9b82a8c54c12b54e68e0c%26960",
                        "http://www.iqiyi.com/v_19rrjb2t5k.html")
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1506179882888&di=0c0c1d64dfb52395e93b983405b59b73&imgtype=0&src=http%3A%2F%2Fwww.xuekewang.com%2Fuploads%2Fallimg%2F100930%2F150350C14-0.jpg",
                     "http://www.iqiyi.com/w_19rtepe9ll.html")

#print(avatar.storyline)

#avatar.show_trailer()

tomb_raider = media.Movie("Tomb Raider",
                          "lara is the only daughter of a noble family who has dedicated herself to the adventures of the world in search of ancient superpowers.",
                          "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1506776009&di=0fc3da57b491668982d33e5c687cdb38&imgtype=jpg&er=1&src=http%3A%2F%2Fimg2.mtime.cn%2Fup%2F1255%2F2751255%2FB967CE60-0465-4B4C-9EC5-75CBE82A08EF_500.jpg",
                          "http://video.mtime.com/67718/?mid=108482")
movies = [toy_story, avatar, tomb_raider]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
