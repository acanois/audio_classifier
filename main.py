import os
import logging
import argparse

from audio_tools import spectrogram_builder as sb

def build_image_library(folder):
    data_path = os.path.join('data', 'audio')
    curr_path = os.path.join(data_path, folder)
    file_count = 0
    
    for file in os.listdir(curr_path):
        if file!= '.DS_Store':
            output_path = os.path.join(data_path, folder, file)
            logger.debug(f'{file_count} / {len(os.listdir(curr_path))}')
            logger.debug(f'processing {output_path}')
            spectrogram = sb.create_spectrogram(output_path, folder)
            sb.save_image(spectrogram, folder, file.replace('.wav', '.png'))
            file_count += 1


def init_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.addHandler(ch)

    return logger


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--fname', help='directory to scan', type=str, required=True)
    args = parser.parse_args()
    
    logger = init_logger()
    build_image_library(args.fname)
    