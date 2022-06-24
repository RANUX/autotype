# Auto type text from file
Read content snippets from source file and type it when you want it.


## How to setup
Run following commands from your terminal:
```
python3 -m venv venv
. venv/bin/activate
pip install -Ur requirements.txt
```

For mac os:
```
brew install portaudio
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```

## How to run autotype
First, checkout sample.auto.py

Open source file and add comments to text blocks:
```
# 1 start
... your python code goes here
# 2 end
```
For double slashes change IS_COMMENT_START_WITH_HASH global var in config

Run following commands from your terminal:
```
python autotype.py <filename>
```
Press ctrl+5 to start auto type content block line by line.
Press ctrl+6 to start auto type content block.
Press ctrl+7 to pass block.
Press ctrl+8 to play code with audio comments
Press esc if you want to exit

## How to run synth_voice
Next command will generate audio files in "audio" folder:
```
python synth_voice.py  sample.auto.py
```

## Configure VSCode
Open VS Workspace Settings (View -> Command Pallette) and select Prefereneces: Open Workspace Settings (JSON).
Add following lines:
```
// Place your settings in this file to overwrite default and user settings.
{
    // Controls if quick suggestions should show up while typing
    "editor.quickSuggestions": { "other": false, "comments": false, "strings": false },

    // Controls if suggestions should be accepted with "Enter" - in addition to "Tab". Helps to avoid ambiguity between inserting new lines and accepting suggestions.
    "editor.acceptSuggestionOnEnter": "off",

    // Controls the delay in ms after which quick suggestions will show up.
    "editor.quickSuggestionsDelay": 10,

    // Enable word based suggestions
    "editor.wordBasedSuggestions": false,

    // optional: hide files from the explorer
    "files.exclude": {
        "*.auto.py": true
    }
}
```