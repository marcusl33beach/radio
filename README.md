# radio

A simple command line utility that prompts the user to select a genre of music
and starts playing that genre using VLC media player.

This function displays a list of music genres to the user and allows them to
select one. Based on the selected genre, the function defines the URL of a
streaming radio station for that genre and starts playing the selected genre
using VLC media player in headless mode.

## Requirements
- Requires VLC to be installed
- Python modules required: os, subprocess, and pick
- Music source: https://icecast.org/

## Usage
- Run the script from the command line with `python3 radio.py`

## Output
- The selected genre of music is printed to the console.
- The bash command used to start playing the selected genre using VLC media player is printed to the console.
- The output of the bash command is printed to the console, indicating the success or failure of starting the selected genre.
