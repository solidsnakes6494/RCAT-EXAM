import numpy as np

def pca(X, k):
    X_std = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
    
    cov_matrix = np.cov(X_std, rowvar=False)
    
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    
    idx = eigenvalues.argsort()[::-1]
    eigenvectors = eigenvectors[:, idx]
    
    top_k_eigenvectors = eigenvectors[:, :k]
    
    projected_data = np.dot(X_std, top_k_eigenvectors)
    
    return projected_data

np.random.seed(0)
data = np.random.rand(100, 5)  

k = 2
projected_data = pca(data, k)

print("Original data shape:", data.shape)
print("Projected data shape:", projected_data.shape)
"""
OUTPUT
Original data shape: (100, 5)
Projected data shape: (100, 2)
"""
