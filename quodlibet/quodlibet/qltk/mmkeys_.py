# -*- coding: utf-8 -*-
# Copyright 2004-2005 Joe Wreschnig, Michael Urman, Iñigo Serna
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation

class MmKeys(object):
    def __init__(self, player):
        try: import quodlibet._mmkeys as mmkeys
        except:
            try: import mmkeys
            except: return
        self.__keys = mmkeys.MmKeys()
        self.__keys.connect('mm_prev', self.__previous, player)
        self.__keys.connect('mm_next', self.__next, player)
        self.__keys.connect('mm_stop', self.__stop, player)
        self.__keys.connect('mm_playpause', self.__play_pause, player)

    def __previous(self, keys, key, player): player.previous()
    def __next(self, keys, key, player): player.next()
    def __stop(self, keys, key, player): player.stop()

    def __play_pause(self, keys, key, player):
        if player.song is None:
            player.reset()
        else: player.paused ^= True
