#!/usr/bin/env python

import sys
import ctypes
from sdl2 import *
from sdl2.sdlmixer import *

def main():
    """entry point"""
    SDL_Init(SDL_INIT_VIDEO|SDL_INIT_AUDIO)
    window = SDL_CreateWindow(b"Hello World",
                              SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              592, 460, SDL_WINDOW_SHOWN)
    #windowsurface = SDL_GetWindowSurface(window)

    #image = SDL_LoadBMP(b"exampleimage.bmp")
    #SDL_BlitSurface(image, None, windowsurface, None)

    SDL_UpdateWindowSurface(window)
    #SDL_FreeSurface(image)

    for i in range(Mix_GetNumMusicDecoders()):
        print "decoder {}: {}".format(i,Mix_GetMusicDecoder(i))

    print "mixinit " + str(Mix_Init(MIX_INIT_MP3))
    print "openaudio " + str(Mix_OpenAudio(44100,MIX_DEFAULT_FORMAT,2,1024))
    Mix_VolumeMusic(MIX_MAX_VOLUME)
    Mix_AllocateChannels(3)

    noise = Mix_LoadWAV('data/noise.wav')
    t440 = Mix_LoadWAV('data/440.wav')
    t220 = Mix_LoadWAV('data/220.wav')

    running = True
    event = SDL_Event()
    while running:
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                running = False
                break
            elif event.type == SDL_KEYDOWN:
                if event.key.keysym.sym == SDLK_a:
                    if Mix_Playing(0):
                        print "fadeout noise " + str(Mix_FadeOutChannel(0, 2000))
                    else:
                        print "fadein noise " + str(Mix_FadeInChannel(0, noise, -1, 2000))
                    print "error: " + SDL_GetError()
                elif event.key.keysym.sym == SDLK_s:
                    if Mix_Playing(1):
                        print "fadeout 440 " + str(Mix_FadeOutChannel(1, 2000))
                    else:
                        print "fadein 440 " + str(Mix_FadeInChannel(1, t440, -1, 2000))
                    print "error: " + SDL_GetError()
                elif event.key.keysym.sym == SDLK_d:
                    if Mix_Playing(2):
                        print "fadeout 220 " + str(Mix_FadeOutChannel(2, 2000))
                    else:
                        print "fadein 220 " + str(Mix_FadeInChannel(2, t220, -1, 2000))
                    print "error: " + SDL_GetError()

    Mix_CloseAudio()
    Mix_FreeChunk(noise)
    Mix_FreeChunk(t440)
    Mix_FreeChunk(t220)
    Mix_Quit()

    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0


if __name__ == '__main__':
    main()
