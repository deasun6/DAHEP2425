import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# definiramo interval za cdf
x_values = np.linspace(-5, 5, 500)

# rcun za normal distribution (mean = 0, std_dev = 1)
cdf_values = norm.cdf(x_values, loc=0, scale=1)

# Step 3: Plot the CDF
plt.figure(figsize=(10, 6))
plt.plot(x_values, cdf_values, label="CDF of Gauss(μ = 0, σ = 1)", color="blue")
plt.title("Cumulative Distribution Function (CDF) of Standard Normal Distribution")
plt.xlabel("x")
plt.ylabel("CDF")
plt.grid(True)
plt.legend()
plt.savefig("standard_normal_cdf.png", format="png", dpi=300)
plt.show()



