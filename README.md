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
WhackEd4 is built with Python 3.9, wxPython 4.1.1 and PyAudio. The user interface is designed wxFormBuilder.
To build the setup executable you will need cx_Freeze and Inno Setup.
