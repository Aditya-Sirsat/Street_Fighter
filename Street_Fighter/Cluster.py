from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


np.random.seed(0)
X = np.random.rand(100,2)
plt.scatter(X[:,0],X[:,1])
plt.show()


num_clusters = 3
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)

cluster_centers = kmeans.cluster_centers_
cluster_labels = kmeans.labels_

plt.scatter(X[:, 0], X[:, 1], c=cluster_labels, cmap='viridis', s=50, alpha=0.5)
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', s=200, marker='X')
plt.title('K-means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()