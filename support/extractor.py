import librosa
import numpy as np
import pandas as pd

def extract_features_3_sec(file_path, file_name):
    '''
    returns a dataframe containing 57 features
    '''
    y, sr = librosa.load(file_path, sr=None)

    segment_length = 66149 # 3 seconds

    num_segments = len(y) // segment_length

    feature_list = []

    for i in range(num_segments):
        start_sample = i * segment_length
        end_sample = start_sample + segment_length

        segment = y[start_sample:end_sample]

        chroma_stft = librosa.feature.chroma_stft(y=segment, sr=sr)
        rms = librosa.feature.rms(y=segment)
        spectral_centroid = librosa.feature.spectral_centroid(y=segment, sr=sr)
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=segment, sr=sr)
        rolloff = librosa.feature.spectral_rolloff(y=segment, sr=sr)
        zero_crossing_rate = librosa.feature.zero_crossing_rate(segment)
        harmony = librosa.effects.harmonic(segment)
        perceptr = librosa.effects.percussive(segment)
        tempo, _ = librosa.beat.beat_track(y=segment, sr=sr)
        mfcc = librosa.feature.mfcc(y=segment, sr=sr, n_mfcc=20)

        features = {
            'filename': f'{file_name}.{i}.wav',
            'length': len(segment),
            'chroma_stft_mean': np.mean(chroma_stft),
            'chroma_stft_var': np.var(chroma_stft),
            'rms_mean': np.mean(rms),
            'rms_var': np.var(rms),
            'spectral_centroid_mean': np.mean(spectral_centroid),
            'spectral_centroid_var': np.var(spectral_centroid),
            'spectral_bandwidth_mean': np.mean(spectral_bandwidth),
            'spectral_bandwidth_var': np.var(spectral_bandwidth),
            'rolloff_mean': np.mean(rolloff),
            'rolloff_var': np.var(rolloff),
            'zero_crossing_rate_mean': np.mean(zero_crossing_rate),
            'zero_crossing_rate_var': np.var(zero_crossing_rate),
            'harmony_mean': np.mean(harmony),
            'harmony_var': np.var(harmony),
            'perceptr_mean': np.mean(perceptr),
            'perceptr_var': np.var(perceptr),
            'tempo': tempo
        }

        for j in range(1, 21):
            features[f'mfcc{j}_mean'] = np.mean(mfcc[j-1])
            features[f'mfcc{j}_var'] = np.var(mfcc[j-1])

        feature_list.append(features)

    df = pd.DataFrame(feature_list)

    return df