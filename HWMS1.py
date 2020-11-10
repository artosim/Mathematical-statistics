import numpy as np
import matplotlib.pyplot as plt
import math


def unif(x_, k):
    return ((k + 1) * x_) ** (1 / k)

def expo(x_, k):
    return (x_ / math.factorial(k)) ** (1 / k)


n = 1000
s = 100
param = 1


res_unif = []
for k in range(1, 100):
    deviations = []
    for _ in range(s):
        x_ = sum(np.power(np.random.uniform(0, 1, n), k)) / n
        deviations.append((unif(x_, k) - param) ** 2)
    res_unif.append(sum(deviations) / s)

res_expo = []
for k in range(1, 100):
    deviations = []
    for _ in range(s):
        x_ = sum(np.power(np.random.exponential(1, n), k)) / n
        deviations.append((expo(x_, k) - param) ** 2)
    res_expo.append(sum(deviations) / s)



plt.plot(range(1, 100), res_unif)
plt.title('Uniform')

# plt.plot(range(1, 100), res_expo)
# plt.title('Exponential')

plt.ylabel('RMSD')
plt.xlabel('k')
plt.show()
