from collections import deque
import time
import keyboard
import re
import sys
import os
import threading

from audio_player import play_wav
from config.autotype_config import *

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
autoplay = False 

# read content of file
def read_file(file_name):
    content = {}
    number = None
    command = None
    with open(file_name, encoding='utf-8') as f:
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

def play_block_line(line):

    # if line contains comment
    if '# shift+tab' in line:
        keyboard.press_and_release(SHIFT_TAB_HOTKEY)
        time.sleep(0.1)
        return

    for s in line:
        keyboard.write(s, delay=0.06)
        
    keyboard.write('\n', delay=0.01)
    time.sleep(0.1)

def play_line_in_thread(number):
     file_path =  os.path.join(BASE_DIR, AUDIO_DIR_NAME, f'block_{number}.wav')
     print(file_path)
     if os.path.exists(file_path):
        print('Plaing file: ', file_path)
        play_wav(file_path)

def play_content_block(number, block, voice=False):
    global autoplay

    th = threading.Thread(target=lambda: play_line_in_thread(number))
    th_started = False

    runblock = False

    is_synth_text = False
    while block:
        line = block.pop(0)
        if line.startswith('"""!'):
            th.start()
            th_started = True
            is_synth_text = True
        elif line.endswith('"""') and is_synth_text:
            is_synth_text = False
            continue

        if is_synth_text:
            if '?' in line:
                print('Stop block. Press ctrl+8 to continue!')
                autoplay = False

            if '$' in line:
                 print('^F5 pressed to run block')
                 runblock = True

            continue

        play_block_line(line)
        if runblock:
            keyboard.press_and_release(RUN_HOTKEY)
            runblock = False
    # Wait for thread to finish
    
    if th_started:
        th.join()

def skip_to_next_block(content):
    check_empty_content(content)
    number, _ = content.pop(0)
    print('Skipping content: ', number)

def main():
    global autoplay

    # read file name from command line
    if len(sys.argv) < 2:
        print('Usage: python3 autotype_text.py <file_name>')
        return
    
    content = read_file(sys.argv[1])
    # sort content by number
    content = sorted(content.items())
    # print(content)
    print('Press ctrl+5 to start and esc to exit')

    # create queue size of 3
    queue = deque(maxlen=3)
    block = None

    while True:
        if not block:
            check_empty_content(content)
            number, block = content.pop(0)
            print('Plaing block: ', number)

        if not autoplay:
            # Wait for the next event.
            event = keyboard.read_event()
            # print(event)
            if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
                break

            queue.append(event)

            if len(queue) == 3:
                if queue[0].name == 'ctrl' and queue[2].name == '6':
                    time.sleep(0.3)
                    play_content_block(number, block)
                if queue[0].name == 'ctrl' and queue[2].name == '5':
                    time.sleep(0.3)
                    line = block.pop(0)
                    print(f'lines left: {len(block)}')
                    play_block_line(line)
                if queue[0].name == 'ctrl' and queue[2].name == '7':
                    time.sleep(0.3)
                    skip_to_next_block(content)

                if queue[0].name == 'ctrl' and queue[2].name == '8':
                    print("Start autoplay with voice")
                    autoplay = True
        else:
            time.sleep(0.3)
            play_content_block(number, block, voice=True)
            keyboard.write('\n', delay=0.01)

if __name__ == '__main__':
    main()
