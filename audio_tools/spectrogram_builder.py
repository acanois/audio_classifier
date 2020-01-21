import os
import numpy as np
import librosa
import skimage.io

def create_spectrogram(filepath, folder, out_name):
    """ TODO: DOCS
    """
    file, samplerate = librosa.load(filepath, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=file, sr=samplerate)
    output_path = os.path.join('data', 'images', folder, out_name)
    skimage.io.imsave(os.path.join(output_path, out_name), spectrogram)