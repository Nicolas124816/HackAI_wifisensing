import os
import numpy as np
from scipy.io import loadmat #loadmat for .mat files

def process_mat_file(file_path):
    # Load the .mat file
    mat = loadmat('participant_1.mat')
    data = mat['DATA']  # Adjust 'DATA' based on how it's named in your .mat files
    
    # Assuming the structure is as described: 336248x92 with complex numbers in columns 2-91
    # Extract features and labels
    time_duration_seconds = data[:, 0]  # First column
    activities = data[:, -1]  # Last column for activities
    csi_data = data[:, 1:-1]  # CSI data columns
    
    # Process complex numbers into amplitude and phase
    amplitude = np.abs(csi_data)
    phase = np.angle(csi_data)
    
    # Optionally, reshape or manipulate your features here as needed
    # For simplicity, we're concatenating amplitude and phase
    features = np.concatenate((amplitude, phase), axis=1)
    
    return features, activities



ft, act = process_mat_file('participant_1.mat')

print(len(ft))
print(len(act))