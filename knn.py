import h5py
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Use h5py to load the MATLAB v7.3 file
with h5py.File('C:\\Users\\to_om\\OneDrive\\Documents\\My Side Projects\\Wireless_sensing_human_activity_recognition\\WiFi_CSI\\Room_3\\participant_2.mat', 'r') as file:
    # Load your data and labels - adjust 'X' and 'y' to the correct paths within your file
    # Note: HDF5 paths might resemble something like 'path/to/your/data'
    # This is just an example; you'll need to inspect the file structure to get the correct paths
    X = np.array(file['X'])
    y = np.array(file['y']).squeeze()  # Squeeze is used to convert y to 1D array if necessary

# Assuming your data (feature matrix) is stored in X and labels in y
# Now that data is loaded, the rest of your script can remain largely unchanged

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN model
knn_model = KNeighborsClassifier(n_neighbors=3)  # Example: 3 neighbors
knn_model.fit(X_train, y_train.ravel())  # Ensure y_train is the correct shape

# Predict on the test set
y_pred = knn_model.predict(X_test)

# Evaluate the model performance
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
