# kaldi-dragonfly-grammars
## Current Status and Plans (06 May 2024)

I'm currently developing a custom grammar/rule set, starting from https://github.com/daanzu/kaldi-grammar-simple.git and incorporating the GUI from https://github.com/caspark/dragonfly-frons.git. 

I am also thinking of just moving to exclusively use Caster. My customization for that will be at this repository: https://github.com/amirf147/caster-user-directory

I initially would like to have most of the functionality from https://github.com/amirf147/wsrmacros set up. 

## Window Switching
I use numbered win keys for window switching with the following
modifications to the taskbar in Windows 10:
- From windows settings app: Never combine taskbar buttons
- From windows settings app: Vertical taskbar on the right side
- From windows settings app: Small taskbar buttons
- Windhawk mod: "Disable grouping on the taskbar". This prevent the thumbnail preview pop up when you press a windows key plus a number
- Zero pinned items on the taskbar
- Taskbar size minimized using drag-to-resize

## attic

This directory contains code that i am still working on or maybe some leftover/failed experimentation. It is not meant to be run. It is more for just reference so I can remember what I did/tried.

## Configuration (Optional)

The loader script uses a default model directory (`kaldi_model`). If you want to use a different model directory, you can create a `config.py` file in the same directory as this script with the following content:

```python
MODEL_DIRECTORY = 'your_model_directory'
```

Replace `'your_model_directory'` with the path to your model directory. The script will use this value instead of the default one.
