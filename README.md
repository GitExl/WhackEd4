WhackEd4
========

Description
-----------
As a replacement for the DOS-based Dehacked, WhackEd4 allows you to load and edit Doom Dehacked files.
It also expands on the features of the original Dehacked:

- A configurable workspace with separate editor windows.
- Sprite previews from a loaded IWAD and PWADs.
- Full support for Boom's extensions such as codepointer and thing flag mnemonics.
- State animation preview with sound playback (where possible).
- Editing multiple states at the same time.
- Filtering the displayed list of states by thing states, weapon states or unused states.
- Does not require a Doom executable, but reads engine data from table files.
- State highlighting based on sprite index.
- Separate undo actions for every editor window.
- Copy and pasting things and states.
- Support for DeHackEd features of Doom 1.9, The Ultimate Doom 1.9, Boom, Marine's Best Friend, Doom Retro and ZDaemon.

Dependencies
------------
WhackEd4 is built with [Python 3.9](https://www.python.org/downloads/), using the wxPython 4.1.1 and PyAudio libraries. The user interface is designed with [wxFormBuilder](https://github.com/wxFormBuilder/wxFormBuilder/releases).
To build the setup executable you will need cx_Freeze and [Inno Setup](https://jrsoftware.org/isdl.php). [7zip](https://www.7-zip.org/download.html) is required if you want to automatically create a standalone release Zip archive.

wxPython and cx_Freeze can both be installed through Python's package manager "pip", by running `pip install wxpython cx_freeze` from a command line. PyAudio can be installed through pip as well, but under Windows I've had more success by installing the appropriate binary version from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio. The Wheel (`.whl`) files can be fed directly into pip to install them, for example: `pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl`

Running `build-release-package.cmd` will create a build with cx_Freeze, build an installer through Inno Setup and then finally create a Zip file with the non-installer version.
