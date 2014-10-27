To run the audio part, you'll need SDL2 and SDL2_mixer.

# pre-requisites
  apt-get install build-essential libasound2-dev libmodplug-dev

# SDL2
  wget http://www.libsdl.org/release/SDL2-2.0.3.tar.gz
  tar xzvf SDL2-2.0.3.tar.gz
  cd SDL2-2.0.3
  ./configure && make && sudo make install

# SDL2_mixer
  wget http://www.libsdl.org/projects/SDL_mixer/release/SDL2_mixer-2.0.0.tar.gz
  tar xzvf SDL2_mixer-2.0.0.tar.gz
  cd SDL2_mixer-2.0.0
  ./configure && make && sudo make install

## Fix
On Debian you might have to edit `music_modplug.h` and `dynamic_modplug.h` and change `#include <modplug.h>` to `#include <libmodplug/modplug.h>` before building.
