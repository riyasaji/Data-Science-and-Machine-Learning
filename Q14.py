import numpy as np
import matplotlib.pyplot as plt

data = np.array([[12, 35], [23,24], [55, 96], [93, 50], [20, 85], [72, 66],[89,56],[44,32],[89,90],[23,76]])
# Number of clusters (you can change this)
k = 3

# Initialize centroids randomly
centroids = data[np.random.choice(data.shape[0], k, replace=False)]

# Main K-means algorithm
num_iterations = 100
for iteration in range(num_iterations):
    # Calculate distances between data points and centroids
    distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)

    # Assign data points to the nearest centroid
    labels = np.argmin(distances, axis=1)
    print("Label: \n",labels)

    # Plot data points and current centroids
    plt.scatter(data[:, 0], data[:, 1], c=labels)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"Iteration {iteration}")
    plt.show()

    # Update centroids based on the mean of assigned data points
    new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(k)])

    # Check for convergence
    if np.array_equal(centroids, new_centroids):
        break

    centroids = new_centroids
# Print final cluster assignments and centroids
print("Distances: \n",distances)
print("Final Cluster Assignments:", labels)
print("Final Cluster Centroids:", centroids)
