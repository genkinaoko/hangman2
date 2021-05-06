import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def identity_function(x):
    return x

x = np.array([1.0, 0.5])
w = np.array([[0.1, 0.3, 0.5],[0.2, 0.4, 0.6]])
b = np.array([0.1, 0.2, 0.3])

print(x.shape)
print(w.shape)
print(b.shape)
A = np.dot(x, w) + b
print(A)
Z = sigmoid(A)
print(Z)

w1 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b1 = np.array([0.1, 0.2])

print(Z.shape)
print(w1.shape)
print(b1.shape)
A1 = np.dot(Z, w1) + b1
Z1 = sigmoid(A1)
print(Z1)

w2 = np.array([[0.1, 0.3], [0.2, 0.4]])
b2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, w2)  + b2
Y = identity_function(A2)
print(Y)
