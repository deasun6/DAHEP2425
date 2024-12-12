import numpy as np
import matplotlib.pyplot as plt

# Measured data
forces = np.array([1, 2, 3, 4, 5])  # Forces in Newtons
accelerations = np.array([9.8, 21.2, 34.5, 39.9, 48.5])  # Accelerations in m/s²
uncertainties = np.array([1.0, 1.9, 3.1, 3.9, 5.1])  # Uncertainties in m/s²

# Define the Chi-squared function
def chi_squared(m):
    predicted_accelerations = forces / m
    chi2 = np.sum(((accelerations - predicted_accelerations) / uncertainties) ** 2)
    return chi2

# Generate values of m to evaluate chi-squared over a range
m_values = np.linspace(0.1, 10, 1000)  # Mass values to evaluate
chi2_values = np.array([chi_squared(m) for m in m_values])

# Find the minimum chi-squared value and the corresponding m estimate
min_chi2_index = np.argmin(chi2_values)
m_hat = m_values[min_chi2_index]
min_chi2 = chi2_values[min_chi2_index]

# Determine the uncertainty range for m (within chi^2_min + 1)
uncertainty_range = m_values[np.abs(chi2_values - min_chi2) <= 1]
sigma_m_hat = (uncertainty_range[-1] - uncertainty_range[0]) / 2

# Print the estimated values
print(f"Estimated mass (m̂): {m_hat:.2f} kg")
print(f"Uncertainty in mass (σₘ̂): {sigma_m_hat:.2f} kg")

# Plot the Chi-squared function
plt.figure(figsize=(10, 6))
plt.plot(m_values, chi2_values, label=r'$\chi^2(m)$ function')
plt.axvline(m_hat, color='r', linestyle='--', label=r'$\hat{m}$')
plt.fill_between(m_values, min_chi2, min_chi2 + 1, color='red', alpha=0.3, label=r'$1\sigma$ range')
plt.xlabel('Mass (m)')
plt.ylabel(r'$\chi^2(m)$')
plt.title(r'$\chi^2$ Function for Mass Estimation')
plt.legend()
plt.grid(True)
plt.savefig("chi2_function_plot.png", format="png", dpi=300)
plt.savefig("chi2_plot.png")
