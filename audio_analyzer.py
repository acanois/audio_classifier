import os
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

def create_spectrogram(filepath, folder, out_name):
    """ TODO: DOCS
    """
    file, samplerate = librosa.load(filepath, sr=None)
    spectrogram = librosa.feature.melspectrogram(y=file, sr=samplerate)
    librosa.display.specshow(librosa.power_to_db(spectrogram, ref=np.max), hop_length=128)
    
    output_path = os.path.join('data', 'images', folder, out_name)
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0)