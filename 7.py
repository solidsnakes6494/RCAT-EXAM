import numpy as np

class KMeans:
    def __init__(self, n_clusters=2, max_iter=300):
        self.n_clusters = n_clusters
        self.max_iter = max_iter

    def fit(self, X):
        self.centroids = X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

        for _ in range(self.max_iter):
            labels = self._assign_labels(X)

            new_centroids = np.array([X[labels == k].mean(axis=0) for k in range(self.n_clusters)])

            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

    def _assign_labels(self, X):
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)

np.random.seed(42)
X = np.random.rand(100, 2)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

labels = kmeans._assign_labels(X)
print("Cluster labels:", labels)
"""
OUTPUT
Cluster labels: [1 0 2 1 0 1 0 2 1 2 2 2 1 1 2 2 1 0 2 0 1 1 1 1 2 0 0 0 2 2 2 0 1 1 1 0 1
 0 2 2 0 2 2 0 0 1 0 0 2 2 1 1 0 1 2 2 0 0 0 0 0 2 2 0 1 2 2 0 0 1 0 2 2 0
 2 0 1 0 0 1 1 0 1 2 1 2 2 2 0 0 2 0 1 0 2 1 0 2 0 0]
 """
