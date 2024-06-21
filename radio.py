from pick import pick
import os
import subprocess

##############################################################################
# Requiers VLC to be installed
# python module requiered os, subprocess and pick
# Music source https://icecast.org/
#
# Uese: python3 radio.py
##############################################################################

def main():
    """
    Prompts the user to select a genre of music and starts playing that genre using VLC media player.

    This function displays a list of music genres to the user and allows them to select one. Based on the selected genre, the function defines the URL of a streaming radio station for that genre and starts playing the selected genre using VLC media player in headless mode.

    Parameters:
    None

    Returns:
    None

    Prints:
    - Option selected: The genre of music selected by the user.
    - Bash command: The bash command used to start playing the selected genre using VLC media player.
    - Output: The output of the bash command, which indicates the success or failure of starting the selected genre.

    Raises:
    None
    """

    title = "What's your jam?: "
    options = ["Country", "Rock", "Blues", "Jazz"]

    option, index = pick(options, title, indicator="=>", default_index=1)

    print("Option selected:", option)

    match option:
        case 'Rock':
            choice = "http://ais-edge147-dal03.cdnstream.com/1697_64"
        case 'Country':
            choice = "http://ais-edge94-nyc04.cdnstream.com/1976_128.mp3"
        case 'Blues':
            choice = "http://ais-edge148-pit01.cdnstream.com/1992_128.mp3"
        case 'Jazz':
            choice = "http://streams.radiomast.io/700d62fe-dcc8-4171-a430-0f0393320b3d"
        case _:
            print("Something's wrong with the internet")
            return

    # Define the bash command so we can jam
    bash_command = f"vlc {choice} --no-video --intf dummy"

    # Run the bash command using subprocess so we can keep jamming
    process = subprocess.Popen(bash_command, shell=True, stdout=subprocess.PIPE)
    output, error = process.communicate()

    # Print the bash command so we can see how we are jamming
    print("Bash command:", bash_command)

    # Print the output  of bash so we can see how we are jamming.
    print("Output:", output.decode())

if __name__ == "__main__":
    main()
