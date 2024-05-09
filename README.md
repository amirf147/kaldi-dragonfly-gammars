# kaldi-dragonfly-grammars

#### Status Update: 09 May 2024 (10:25)
It seems that it was just a python version issue. I just got Caster working with python version 3.10.5. 

#### Status Update: 09 May 2024 (09:35)
I'm attempting to get Caster working. 
Current error when trying to install via the batch file:
```
  Will build using: "C:\Users\amirf\AppData\Local\Programs\Python\Python39\python.exe"
  3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)]
  Python's architecture is 64bit
  cfg.VERSION: 4.1.0
  
  Running command: build
  Running command: build_wx
  Command '"C:\Users\amirf\AppData\Local\Programs\Python\Python39\python.exe" -c "import setuptools, distutils.msvc9compiler as msvc; mc = msvc.MSVCCompiler(); mc.initialize(); print(mc.cc)"' failed with exit code 1.
  Traceback (most recent call last):
  
    File "<string>", line 1, in <module>
  
    File "C:\Users\amirf\AppData\Local\Programs\Python\Python39\lib\site-packages\setuptools\_distutils\msvc9compiler.py", line 400, in initialize
  
      vc_env = query_vcvarsall(VERSION, plat_spec)
  
    File "C:\Users\amirf\AppData\Local\Programs\Python\Python39\lib\site-packages\setuptools\_distutils\msvc9compiler.py", line 280, in query_vcvarsall
  
      raise DistutilsPlatformError("Unable to find vcvarsall.bat")
  
  distutils.errors.DistutilsPlatformError: Unable to find vcvarsall.bat
```
I do have the appropriate visual studio build tools installed.. I did try a bunch of other things too which I might document later. This is just a quick update.


## Current Status and Plans (06 May 2024)

I'm currently developing a custom grammar/rule set, starting from https://github.com/daanzu/kaldi-grammar-simple.git and incorporating the GUI from https://github.com/caspark/dragonfly-frons.git. 

As I progress, I plan to significantly modify these bases to create a personalized speech recognition system. I may also look at/incorporate projects such as https://github.com/dictation-toolbox/Caster.

I initially would like to have most of the functionality from https://github.com/amirf147/wsrmacros set up. 

> **Note:** Please note that this repository, in its current state, is not intended to be cloned and used. It currently serves as a place for me to document my progress. It might be a bit messy now, but I plan to clean it up later and make it more user-friendly. Currently, I'm still trying to put things together and get a working basis.

## attic

This directory contains code that i am still working on or maybe some leftover/failed experimentation. It is not meant to be run. It is more for just reference so I can remember what I did/tried.

## Configuration (Optional)

The loader script uses a default model directory (`kaldi_model`). If you want to use a different model directory, you can create a `config.py` file in the same directory as this script with the following content:

```python
MODEL_DIRECTORY = 'your_model_directory'
```

Replace `'your_model_directory'` with the path to your model directory. The script will use this value instead of the default one.
