import os
import logging
import audio_analyzer

def build_image_library():
    data_path = os.path.join('data', 'audio')

    for folder in os.listdir(data_path):
        if folder != '.DS_Store':
            curr_path = os.path.join(data_path, folder)
            for file in os.listdir(curr_path):
                if file != '.DS_Store':
                    output_path = os.path.join(data_path, folder, file)
                    logger.debug(f"processing {output_path}")
                    audio_analyzer.create_spectrogram(output_path, folder, file.replace('.wav', '.png'))

def init_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger.addHandler(ch)

    return logger


if __name__ == "__main__":
    logger = init_logger()
    build_image_library()
    