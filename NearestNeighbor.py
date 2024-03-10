class NearestNeighbor:
    def __init__(self, distance_function, n_neighbors=1):
        """
        Initialize the NearestNeighbor class.

        Parameters:
        - distance_function: A function to calculate the distance between two points.
        - n_neighbors: The number of nearest neighbors to consider.
        """
        self.distance_function = distance_function
        self.n_neighbors = n_neighbors
    
    def find_distance(self, point1, point2):
        """
        Calculate the distance between two points using the specified distance function.

        Parameters:
        - point1: First data point.
        - point2: Second data point.

        Returns:
        - Distance between the two points.
        """
        return self.distance_function(point1, point2)
    
    def find_nearest_neighbor(self, data_point, dataset, labels):
        """
        Find the nearest neighbor to a given data point in a dataset.

        Parameters:
        - data_point: The data point for which to find the nearest neighbor.
        - dataset: The dataset containing potential nearest neighbors.
        - labels: Labels corresponding to each data point in the dataset.

        Returns:
        - nearest_neighbor_labels: Labels of the nearest neighbors.
        """
        distances = [self.find_distance(data_point, point) for point in dataset]
        
        nearest_neighbor_indices = self.find_nearest_indices(distances)
        nearest_neighbor_labels = [labels[i] for i in nearest_neighbor_indices]

        return nearest_neighbor_labels
    
    def find_nearest_indices(self, distances):
        """
        Find indices of the nearest neighbors based on calculated distances.

        Parameters:
        - distances: List of distances from the data point to each point in the dataset.

        Returns:
        - nearest_neighbor_indices: Indices of the nearest neighbors.
        """
        indices = list(range(len(distances)))
        self.selection_sort(distances, indices)
        return indices[:self.n_neighbors]

    def selection_sort(self, distances, indices):
        """
        Perform selection sort on distances and keep track of corresponding indices.

        Parameters:
        - distances: List of distances to be sorted.
        - indices: List of indices to be sorted in parallel with distances.

        Returns:
        - None
        """
        n = len(distances)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if distances[j] < distances[min_idx]:
                    min_idx = j
            distances[i], distances[min_idx] = distances[min_idx], distances[i]
            indices[i], indices[min_idx] = indices[min_idx], indices[i]

# Define distance functions
import math

def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))

def manhattan_distance(point1, point2):
    return sum(abs(x - y) for x, y in zip(point1, point2))

def minkowski_distance(point1, point2, p):
    return sum(abs(x - y) ** p for x, y in zip(point1, point2)) ** (1 / p)

def chebyshev_distance(point1, point2):
    return max(abs(x - y) for x, y in zip(point1, point2))

def cosine_similarity(point1, point2):
    dot_product = sum(x * y for x, y in zip(point1, point2))
    magnitude1 = math.sqrt(sum(x ** 2 for x in point1))
    magnitude2 = math.sqrt(sum(y ** 2 for y in point2))
    return dot_product / (magnitude1 * magnitude2)

def hamming_distance(point1, point2):
    return sum(x != y for x, y in zip(point1, point2))

def jaccard_distance(set1, set2):
    intersection_size = len(set1.intersection(set2))
    union_size = len(set1.union(set2))
    return 1 - (intersection_size / union_size)

def correlation_distance(point1, point2):
    n = len(point1)
    mean1 = sum(point1) / n
    mean2 = sum(point2) / n
    covariance = sum((x - mean1) * (y - mean2) for x, y in zip(point1, point2)) / n
    std_dev1 = math.sqrt(sum((x - mean1) ** 2 for x in point1) / n)
    std_dev2 = math.sqrt(sum((y - mean2) ** 2 for y in point2) / n)
    return 1 - (covariance / (std_dev1 * std_dev2))
