from pynput.keyboard import Key, Controller
from time import sleep


keyboard = Controller()


def write_char(character=None):
    """Write a character on the keyboard
    
    Keyword arguments:
    character -- the character to be printed, either a string with length 1, a member of Key or KeyCode
    """
    
    if character:
        keyboard.press(character)
        keyboard.release(character)        


def write_string(text=None, typing_timeout=0.05):
    """Write a string and a newline at the end on the keyboard
    
    Keyword arguments:
    text -- a string of text
    typing_timeout -- the timeout between each keystroke in seconds
    """
    
    for ch in text:
        write_char(ch)
        sleep(typing_timeout)
    # writing the new line
    write_char(Key.enter)


def write_lines(text=None, starting_pause=5, pause_between_lines=2, typing_timeout=0.05):
    """Write multiple lines of text on the keyboard
    
    Keyword arguments:
    text -- a list of strings of text, each representing a line
    starting_pause -- the timeout on initial start of the program in seconds
    pause_between_lines -- the timeout between each written line in the input in seconds
    typing_timeout -- the timeout between each keystroke in seconds
    """
    
    sleep(starting_pause)
    # writing each line
    for line in text:
        write_string(line, typing_timeout)
        sleep(pause_between_lines)
        
def write_text(text=None, path=None, starting_pause=5, pause_between_lines=2, typing_timeout=0.05):
    """ Write multiple lines of text on the keyboard, either from a supplied text or a file
    
    Keyword arguments:
    text -- a string of text
    path -- the path to a text file, as string
    starting_pause -- the timeout on initial start of the program in seconds
    pause_between_lines -- the timeout between each written line in the input in seconds
    typing_timeout -- the timeout between each keystroke in seconds
    """
    # splitting the text if text is given
    if text:
        text_lines = text.splitlines()
    # opening the text file
    elif path:
        text_lines = read_file(path)
        # if the reading operation wasn't successful the function is stopped
        if text_lines is None:
            return None
    # if the required arguments are missing the error code is returned
    else:
        raise ValueError('The supplied parameters have to include either a string or the path to a textfile')
    # writing the lines of text
    write_lines(text_lines, starting_pause, pause_between_lines, typing_timeout)


def read_file(path):
    """Read a list of text lines, as string, from the given file path
    
    Keyword Arguments:
    path -- the path to a text file, as string
    """
    
    try:
        with open(path, encoding='utf-8') as f:
            text_lines = f.read().splitlines()
    except FileNotFoundError:
        raise
    return text_lines
    

if __name__ == "__main__":
    write_text(text='Lorem ipsum dolor sit amet\nconsetetur sadipscing elitr')
