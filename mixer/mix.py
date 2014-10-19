#!/usr/bin/env python

import sys
import select
import ctypes
from sdl2 import *
from sdl2.sdlmixer import *
import sdl2.ext as sdl2ext
import time

def play(chid, ch_wav, do_play):
    if Mix_Playing(chid) and not do_play:
        print "fadeout noise " + str(Mix_FadeOutChannel(chid, 2000))
    elif not Mix_Playing(chid) and do_play:
        print "fadein noise " + str(Mix_FadeInChannel(chid, ch_wav[chid], -1, 2000))
    print "error: " + SDL_GetError()

def main():
    """entry point"""
    SDL_Init(SDL_INIT_AUDIO)

    for i in range(Mix_GetNumMusicDecoders()):
        print "decoder {}: {}".format(i,Mix_GetMusicDecoder(i))

    print "mixinit " + str(Mix_Init(MIX_INIT_MP3))
    print "openaudio " + str(Mix_OpenAudio(44100,MIX_DEFAULT_FORMAT,2,1024))
    Mix_VolumeMusic(MIX_MAX_VOLUME)
    Mix_AllocateChannels(3)

    track_wav = [   Mix_LoadWAV('data/noise.wav'),
                    Mix_LoadWAV('data/440.wav'),
                    Mix_LoadWAV('data/220.wav'), ]
    track_counter = [ 0, 0, 0, ]

    running = True
    last_time = int(time.time())
    while running:
        tick = False
        now_time = int(time.time())

        if now_time > last_time:
            print "Tick"
            last_time = now_time

            track_counter = map( lambda x: max(0,x-1), track_counter )

            if select.select([sys.stdin,],[],[],0.0)[0]:
                c = sys.stdin.read(1)
                if c == 'q':
                    running = False
                    break
                elif c >= '0' and c <= '2':
                    print "refresh " + c
                    track_counter[int(c)] = 5;

            for i,x in enumerate(track_counter):
                play(i, track_wav, x>0)

    Mix_CloseAudio()
    Mix_FreeChunk(track_wav[0])
    Mix_FreeChunk(track_wav[1])
    Mix_FreeChunk(track_wav[2])
    Mix_Quit()

    #SDL_DestroyWindow(window)
    SDL_Quit()
    return 0


if __name__ == '__main__':
    main()
