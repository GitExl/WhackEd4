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

### Building on Windows

WhackEd4 is built with [Python 3.11](https://www.python.org/downloads/), using the wxPython 4 and Sounddevice
libraries. The user interface is designed with [wxFormBuilder](https://github.com/wxFormBuilder/wxFormBuilder/releases).
To build the setup executable you will need cx_Freeze and [Inno Setup](https://jrsoftware.org/isdl.php).
[7zip](https://www.7-zip.org/download.html) is required if you want to automatically create a standalone release Zip
archive.

wxPython, cx_Freeze and sounddevice can both be installed through Python's package manager "pip" by running
`pip install wxpython cx_freeze sounddevice` from a command line.

Running `build-release-package.cmd` will create a build with cx_Freeze, build an installer through Inno Setup and then
finally create a Zip file with the non-installer version.

### Building on macOS

For macOS, you need at least Python 3.13. Make sure to also `pip install platformdirs` and `py2app` besides
aforementioned `wxPython` and `sounddevice`. After that, run `python setup-mac.py py2app`. A `WhackEd4.app` bundle will
appear under `dist/`. Try to start it: if it fails on startup with an error, you can rerun it from Terminal to see
details, by executing directly `dist/WhackEd4.app/Contents/MacOS/WhackEd4`.

Caveats:
1. The app bundle is not signed or notarized, so if you try to redistribute it, it will still be usable, but only after
   users bypass the Gatekeeper security. You can sign it using Apple's tools if you have a developer ID. This app can
   still be started by directly running `python src/main.py` as long as you have the required modules (`wx`,
   `sounddevice` etc.) installed.
2. For some reason related to py2app and wxWidgets, the bundle is huge, over 90 MB.
