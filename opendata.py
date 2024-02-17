import h5py

# Replace this with your actual file path
file_path = 'C:\\Users\\to_om\\OneDrive\\Documents\\My Side Projects\\Wireless_sensing_human_activity_recognition\\WiFi_CSI\\Room_3\\participant_2.mat'

with h5py.File(file_path, 'r') as file:
    # Print all the main level contents
    print(list(file.keys()))
    # Assuming 'X' and 'y' are dataset names you're interested in
    # Note: Adjust these names based on what you find above
    X = file['X'][:]
    y = file['y'][:]

