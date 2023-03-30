'''Main function - Contains only main parts of the function
1. Initialize Centroids
2. Finding new labels for data points
3. Updating old label to new label 
4. Finally call a should_stop function to check if we should stop? 
NOTE: data-> [(x1,y1),(x2,y2),(x3,y3).....]

'''
import numpy as np
def main (data, k):
    centroids = initialize_centroids(k)

    while True:
        old_centroids = centroids
        labels = get_labels (data, centroids)
        centoids = update_centroid(data, labels, k)
        if should_stop(olds_centroids, new_centroids):
            break
    return labels

def initialize_centroids (data, k):
    x_min = y_min = float('inf')
    x_max, y_max = float('-inf')

    for point in data:
        x_min = min(point[0], x_min)
        y_min = min(point[1], y_min)
        x_max = max(point[0], x_max)
        y_max = max(point[1], y_max)

    centroids =  []
    for i in range (k):
        centroids.append([np.rand(x_min,x_max)],
                         [np.rand(y_min,y_max)])
    return centroids

