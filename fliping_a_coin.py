import matplotlib.pyplot as plt
import numpy as np

# mu, sigma = 0.10, 0.01  # mean and standard deviation
# s = np.random.rand(mu, sigma, 10000)
n = 5000
s = np.random.rand(n)
print(s)
mu, sigma, var = np.mean(s), np.std(s), np.var(s)
count, bins, ignored = plt.hist(s, n, density=True)
fun = []
for i in range(n - 1):
    fun.append(
        1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((s[i] - mu) ** 2) / (2 * sigma**2))
    )
# 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((s - mu) ** 2) / (2 * sigma**2))
plt.plot(
    bins,
    1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((bins - mu) ** 2) / (2 * sigma**2)),
    linewidth=2,
    color="r",
)
plt.show()
res = []
result = []
tail = 0
head = 0
last = 0
for i in range(n - 1):
    res.append(int(fun[i] > 1))
    if int(fun[i] < 1) == 1:
        tail += 1
    else:
        head += 1

    last = tail / (tail + head)

    result.append(last)
plt.plot(res)
plt.show()
plt.plot(result)
plt.show()
