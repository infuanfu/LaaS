#!/usr/bin/env python

import sys
import select
import time

playing = [False, False, False,]

def Mix_Playing(x):
    return playing[x]

def Mix_FadeOutChannel(x,t):
    playing[x] = False
    return x

def Mix_FadeInChannel(x, wav, y, t):
    playing[x] = True
    return x

def play(chid, ch_wav, do_play):
    if Mix_Playing(chid) and not do_play:
        print "fadeout " + str(Mix_FadeOutChannel(chid, 2000))
    elif not Mix_Playing(chid) and do_play:
        print "fadein " + str(Mix_FadeInChannel(chid, ch_wav[chid], -1, 2000))

def main():
    """entry point"""
    track_wav = [0,1,2]
    track_counter = [ 0, 0, 0, ]

    running = True
    last_time = int(time.time())
    while running:
        tick = False
        now_time = int(time.time())

        if select.select([sys.stdin,],[],[],0.0)[0]:
            c = sys.stdin.read(1)
            if c == 'q':
                running = False
                break
            elif c >= '0' and c <= '2':
                print "refresh " + c
                track_counter[int(c)] = 5;

        if now_time > last_time:
            print "Tick"
            last_time = now_time

            track_counter = map( lambda x: max(0,x-1), track_counter )

            for i,x in enumerate(track_counter):
                play(i, track_wav, x>0)

    return 0


if __name__ == '__main__':
    main()
