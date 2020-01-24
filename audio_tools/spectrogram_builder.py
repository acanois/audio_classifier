import os
import numpy as np
import librosa
import librosa.display
import skimage.io
import matplotlib.pyplot as plt

def save_image(spectrogram, folder, out_name):
    output_path = os.path.join('data', 'images', folder)
    output_image = librosa.display.specshow(\
        librosa.power_to_db(spectrogram, ref=np.max),\
        sr=22050, hop_length=512,\
        bins_per_octave=12
    )
    plt.margins(0)
    plt.savefig(os.path.join(output_path, out_name), bbox_inches='tight', pad_inches=0.0)
    plt.close()

def create_spectrogram(filepath, folder):
    """ TODO: DOCS
    """
    file, samplerate = librosa.load(filepath, sr=22050)
    spectrogram = librosa.feature.melspectrogram(y=file, sr=22050, window='hann')

    return spectrogram