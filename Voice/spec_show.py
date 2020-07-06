import numpy as np
import matplotlib.pyplot as plt
import librosa
import os 


def plot_fbank(filepath, time_start=0.0, duration=None):
    y, sample_rate = librosa.load(wav_path, sr=None)

    # clip one segment
    if duration is not None:
        start = int(sample_rate * time_start)
        end = start + int(sample_rate * duration)
        y = y[start:end]

    # fft setting
    n_fft = 512
    win_length = 25  # ms
    hop_length = 10  # ms
    win_length = sample_rate * win_length // 1000  # ms to value number
    hop_length = sample_rate * hop_length // 1000  # ms to value number

    S = np.abs(librosa.core.stft(y, n_fft=n_fft, win_length=win_length, hop_length=hop_length))

    # The official api can't assign the mel bins number, so I assign it myself
    n_mels = 40
    fmin = 0.0
    fmax = None
    # Build a Mel filter
    mel_basis = librosa.filters.mel(sample_rate, n_fft, n_mels = n_mels, fmin=fmin, fmax=fmax)
    # Linear scale to mel scale
    mel_fbank = np.dot(mel_basis, S)

    S = librosa.core.power_to_db(mel_fbank)

    plt.axis('off')
    plt.imshow(S,origin='lower')

    # save_path = 'fbank_show/' + filepath.split('/')[-1].split('.')[0] + '.png'
    # plt.savefig(save_path, dpi=200,bbox_inches = 'tight', pad_inches = 0)
    plt.show()

if __name__ == "__main__":
    wav_path = 'tmp_data/id10032-yZDyZR1JlFo-0000001.wav'
    plot_fbank(wav_path)
    
    
    