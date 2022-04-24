# Auto type text from file
Read content snippets from source file and type it when you want it.

## How to setup
Run following commands from your terminal:
```
python3 -m venv venv
. venv/bin/activate
pip install -Ur requirements.txt
```
## How to run
Open source file and add comments to text blocks:
```
# 1 start
... your python code goes here
# 2 end
```
For double slashes change IS_COMMENT_START_WITH_HASH global var

Run following commands from your terminal:
```
python autotype.py <filename>
```
Press ctrl+shift+1 to start auto typing.
Press esc if you want to exit

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