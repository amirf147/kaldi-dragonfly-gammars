# kaldi-dragonfly-grammars

## Current Status and Plans

I'm currently developing a custom grammar/rule set, starting from https://github.com/daanzu/kaldi-grammar-simple.git and incorporating the GUI from https://github.com/caspark/dragonfly-frons.git. 

As I progress, I plan to significantly modify these bases to create a personalized speech recognition system. I may also look at/incorporate projects such as https://github.com/dictation-toolbox/Caster.

I initially would like to have most of the functionality from https://github.com/amirf147/wsrmacros set up. 

> **Note:** Please note that this repository, in its current state, is not intended to be cloned and used. It currently serves as a place for me to document my progress. For example, I'm not using different branches; I just have a single main branch. I have two loaders here and there may be extra files. It might be a bit messy now, but I plan to clean it up later and make it more user-friendly. Currently, I'm still trying to put things together and get a working basis.


## Configuration (Optional)

The loader script uses a default model directory (`kaldi_model`). If you want to use a different model directory, you can create a `config.py` file in the same directory as this script with the following content:

```python
MODEL_DIRECTORY = 'your_model_directory'
```

Replace `'your_model_directory'` with the path to your model directory. The script will use this value instead of the default one.
