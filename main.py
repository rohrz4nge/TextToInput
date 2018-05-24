from pynput.keyboard import Key, Controller
from time import sleep

keyboard = Controller()

"""
function writing a character to the stdin
possible parameters:
    character: the character to be printed, either a string with length 1, a member of Key or KeyCode"""
def write_char(character=None):
    if character:
        keyboard.press(character)
        keyboard.release(character)        

"""
function writing a string and a newline at the end to the stdin
possible parameters:
    text: a string of text
    typing_timeout: the timeout between each keystroke in seconds """
def write_string(text=None, typing_timeout=0.05):
    for ch in text:
        write_char(ch)
        sleep(typing_timeout)
    # writing the new line
    write_char(Key.enter)

"""
function writing multiple lines of text into the stdin, either from a supplied text or a file
possible arguments:
    text: a string of text
    path_to_file: the path to a text file, as string
    starting_pause: the timeout on initial start of the program in seconds
    pause_between_lines: the timeout between each written line in the input in seconds
    typing_timeout: the timeout between each keystroke in seconds """
def write_lines(text=None, path_to_file=None, starting_pause=5, pause_between_lines=2, typing_timeout=0.05):
    # splitting the text if text is given
    if text:
        text_lines = text.splitlines()
    # opening the text file if a path is given
    elif path_to_file:
        try:
            with open(path_to_file, encoding='utf-8') as f:
                text_lines = f.read().splitlines()
        except FileNotFoundError:
            raise FileNotFoundError('Wrong file or path')
    
    # if the required arguments are missing the error code is returned
    else:
        raise ValueError('The supplied parameters have to include either a string or the path to a textfile')
    
    sleep(starting_pause)
    # writing each line
    for line in text_lines:
        write_string(line, typing_timeout)
        sleep(pause_between_lines)

if __name__ == "__main__":
    write_lines(path_to_file='C:/file.txt')
