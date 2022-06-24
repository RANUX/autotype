from autotype import read_file
import sys
import torch
import os

from config.synth_voice_config import *

device = torch.device(TORCH_DEVICE)

model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                     model=SILERO_MODEL,
                                     language=LANGUAGE,
                                     speaker=MODEL_ID)
model.to(device)  # gpu or cpu

def synth_content_block(number, block):
    comment_lines = []
    is_synth_text = False
    while block:
        line = block.pop(0)
        if line.startswith('"""!'):
            is_synth_text = True
        elif line.endswith('"""') and is_synth_text:
            comment_lines.append(line.replace('"""', ''))
            is_synth_text = False

        if is_synth_text:
            comment_lines.append(line.replace('"""!', ''))

    # create dir if not exists
    if not os.path.exists(AUDIO_DIR_NAME):
        os.makedirs(AUDIO_DIR_NAME)

    if not comment_lines:
        print('Nothing to process')
        return

    audio_paths = model.save_wav(text=' '.join(comment_lines),
                            speaker=SPEAKER,
                            sample_rate=SAMPLE_RATE,
                            audio_path=os.path.join(AUDIO_DIR_NAME, f'block_{number}.wav'))
    print('Save audio to: ', audio_paths)

def main():
    # read file name from command line
    if len(sys.argv) < 2:
        print('Usage: python3 synth_voice.py <file_name>')
        return

    content = read_file(sys.argv[1])
    # sort content by number
    content = sorted(content.items())

    while content:
        number, block = content.pop(0)
        print('Synthes block N: ', number)
        synth_content_block(number, block)
        

if __name__ == '__main__':
    """Usage: python3 synth_voice.py <file_name>"""
    main()