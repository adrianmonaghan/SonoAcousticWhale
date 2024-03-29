import pcen
import torch
import torchaudio
import pandas as pd
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import pickle
from python_scripts.read_xwav_header import read_xwav_header
from pathlib import Path

def main():
    annot = pd.read_csv("data/pifsc_products_detections_annotations.csv")
    # annot.head()
    uncompressed_files = os.listdir("data/audio_data/uncompressed")

    data = {}
    file_path = Path('data/audio_data/uncompressed/Cross_A_01_050606_123845.d20.x.wav')
    data["file_name"] = "Cross_A_01_050606_123845.d20.x.wav"
    data["file_path"] = file_path
    data["header"] = read_xwav_header(file_path)

    waveform, sample_rate = torchaudio.load(file_path)
    waveform = waveform[0].unsqueeze(0)

