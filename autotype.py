from collections import deque
import time
import keyboard
import re
import sys

IS_COMMENT_START_WITH_HASH = True   # otherwise use //

# read content of file
def read_file(file_name):
    content = {}
    number = None
    command = None
    with open(file_name) as f:
        # while not end of file
        while True:
            line = f.readline()
            if not line:
                break
            
            if IS_COMMENT_START_WITH_HASH:
                regex = re.compile(r'^#\s+(\d+)\s+(\w+)$')
            else:
                regex = re.compile(r'^/{2}\s+(\d+)\s+(\w+)$')

            match = regex.match(line)

            if match:
                # get the number and the command
                number, command = match.groups()
                number = int(number)
                if command == 'start':
                    content[number] = []
                continue

            if command == 'start':
                line = line.strip()
                if len(line) > 0:
                    content[number].append(line)
            
    return content

def check_empty_content(content):
    if len(content) == 0:
        print('Nothing to play. Exiting')
        exit(0)

def play_content(content):
    check_empty_content(content)
    number, lines = content.pop(0)
    print('Plaing content: ', number)
    for line in lines:
        keyboard.write(line)
        keyboard.write('\n', delay=0.01)
        time.sleep(0.05)

def skip_to_next(content):
    check_empty_content(content)
    number, _ = content.pop(0)
    print('Skipping content: ', number)

def main():
    # read file name from command line
    if len(sys.argv) < 2:
        print('Usage: python3 autotype_text.py <file_name>')
        return
    
    content = read_file(sys.argv[1])
    # sort content by number
    content = sorted(content.items())
    print(content)
    print('Press ctrl+shift+1 to start and esc to exit')

    # create queue size of 3
    queue = deque(maxlen=3)

    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
            break
        queue.append(event)

        if len(queue) == 3:
            if queue[0].name == 'ctrl' and queue[1].name == 'shift' and queue[2].name == '1':
                time.sleep(0.3)
                play_content(content)
            if queue[0].name == 'ctrl' and queue[1].name == 'shift' and queue[2].name == '2':
                time.sleep(0.3)
                skip_to_next(content)

if __name__ == '__main__':
    main()
