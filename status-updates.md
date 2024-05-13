
#### Status Update: 12 May 2024 
Preparing a potential transition to using Caster exclusively with the creation of this repository: https://github.com/amirf147/caster-user-directory. I am still daily driving with just dragonfly and this grammar set as of now.

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

