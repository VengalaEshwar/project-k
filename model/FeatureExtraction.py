import numpy as np
import librosa
import pandas as pd
from scipy.stats import entropy
import os
def extract_features(audio_path):
    audio_path='d:\\coding\\temp\project-rtrp\\modelrecorded_audio.wav'
    print("entered the fe_1",audio_path)
    print(os.path.exists(audio_path))
    y, sr = librosa.load(audio_path, sr=None)
    features = {}
    print("entered the fe_1 loaded")
    # Fundamental Frequency (Fo), Minimum (Flo), and Maximum (Fhi)
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    pitches = pitches[magnitudes > np.median(magnitudes)]
    features['MDVP:Fo(Hz)'] = np.mean(pitches)
    features['MDVP:Fhi(Hz)'] = np.max(pitches)
    features['MDVP:Flo(Hz)'] = np.min(pitches)
    
    # Jitter calculations
    features['MDVP:Jitter(%)'] = np.std(pitches) / np.mean(pitches) * 100
    features['MDVP:Jitter(Abs)'] = np.std(pitches)
    features['MDVP:RAP'] = np.mean(np.abs(np.diff(pitches)))
    features['MDVP:PPQ'] = np.mean(np.abs(np.diff(pitches, n=5)))
    features['Jitter:DDP'] = features['MDVP:RAP'] * 3
    
    # Shimmer calculations
    S = np.abs(librosa.stft(y))
    features['MDVP:Shimmer'] = np.std(S) / np.mean(S)
    features['MDVP:Shimmer(dB)'] = 20 * np.log10(features['MDVP:Shimmer'])
    features['Shimmer:APQ3'] = np.mean(np.abs(np.diff(S, n=3)))
    features['Shimmer:APQ5'] = np.mean(np.abs(np.diff(S, n=5)))
    features['MDVP:APQ'] = np.mean(np.abs(np.diff(S, n=11)))
    features['Shimmer:DDA'] = features['Shimmer:APQ3'] * 3
    
    # NHR and HNR calculations
    harmonic, percussive = librosa.effects.hpss(y)
    features['NHR'] = np.mean(percussive) / np.mean(harmonic)
    features['HNR'] = np.mean(harmonic) / np.mean(percussive)
    
    # RPDE, DFA, Spread1, Spread2, D2, PPE
    features['RPDE'] = entropy(pitches)
    features['DFA'] = np.std(np.diff(pitches))
    features['spread1'] = np.max(pitches) - np.min(pitches)
    features['spread2'] = np.std(pitches)
    features['D2'] = np.var(pitches)
    features['PPE'] = entropy(pitches)
    try :
        print(features)
    except() :
        print("in the error of extraction")   
    return features
print(extract_features("recorded_audio.wav"))
# for item in temp :
#     print(item ,temp[item])
# try :
#     print(extract_features('recorded_audio.wav'))
# except :
#     print("in the error of extraction")    