import numpy as np

data = input()
data = data.split(' ')
temp = []
# 0-> on 1-> off
for mes in data:
    if mes == 'on':
        temp.append(0)
    else:
        temp.append(1)

V = np.array(temp)

a = np.array(((0.2, 0.8, 0), (0, 0.2, 0.8), (0, 0, 1)))
# Emission Probabilities
b = np.array(((0.1, 0.9), (0.1, 0.9), (0.6, 0.4)))
# Equal Probabilities for the initial distribution
initial_distribution = np.array((1/3, 1/3, 1/3))
alpha = np.zeros((V.shape[0], a.shape[0]))

for t in range(1, V.shape[0]):
    for i in range(a.shape[0]):
        alpha[0, :] += a[i] * initial_distribution[i]

alpha[0, :] *= b[:, V[0]]
alpha[0, :] /= np.sum(alpha[0, :])

for t in range(1, V.shape[0]):
    for i in range(a.shape[0]):
        alpha[t, :] += a[i] * alpha[t-1, i]
    alpha[t, :] *= b[:, V[t]]
    alpha[t, :] /= np.sum(alpha[t, :])

print(alpha[-1])
