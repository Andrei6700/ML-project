import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

# Imagine 1: Puncte liniar separabile
np.random.seed(42)
x1 = np.random.uniform(0, 5, (100, 2))
x2 = np.random.uniform(5, 10, (100, 2))

plt.figure(figsize=(5, 5))
plt.scatter(x1[:, 0], x1[:, 1], color='red')
plt.scatter(x2[:, 0], x2[:, 1], color='blue')
plt.axis('off')  # Elimină etichetele și axele
plt.savefig('data1.png', bbox_inches='tight', pad_inches=0)
plt.close()  # Închide figura pentru a elibera memoria

# Imagine 2: Puncte non-liniar separabile (cercuri concentrice)
X, y = make_circles(n_samples=200, factor=0.5, noise=0.05)

plt.figure(figsize=(5, 5))
plt.scatter(X[y == 0, 0], X[y == 0, 1], color='green')
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='orange')
plt.axis('off')  # Elimină etichetele și axele
plt.savefig('data2.png', bbox_inches='tight', pad_inches=0)
plt.close()  # Închide figura pentru a elibera memoria
