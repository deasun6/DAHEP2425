import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# prvo definiram vrijednosti za tri distrbucije
params = [
    {"mu": 200, "sigma": 2, "label": "Gauss(μ = 200, σ = 2)"},
    {"mu": 210, "sigma": 3, "label": "Gauss(μ = 210, σ = 3)"},
    {"mu": 190, "sigma": 4, "label": "Gauss(μ = 190, σ = 4)"}
]

# Create a range of x values to plot the Gaussian curves
x_values = np.linspace(180, 220, 500)

plt.figure(figsize=(10, 6))

# Loop through each set of parameters and plot the Gaussian curve
for param in params:
    mu = param["mu"]
    sigma = param["sigma"]
    y_values = norm.pdf(x_values, mu, sigma)  # Get the PDF values for the current Gaussian
    plt.plot(x_values, y_values, label=param["label"])

# Add titles and labels
plt.title("Gaussian Distributions for Different (μ, σ) Values")
plt.xlabel("Mass (GeV)")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)

# Save the plot as a PNG file
plt.savefig("gaussian_distributions.png", format="png", dpi=300)

# Show the plot
plt.show()

# Step 2: Calculate probability to produce the new particle with a mass of 205 GeV or more
mu, sigma = 200, 2
prob_above_205 = norm.sf(205, mu, sigma)  # sf (Survival Function) is equivalent to 1 - CDF
print(f"Probability of producing a particle with mass ≥ 205 GeV: {prob_above_205:.4f}")

# Step 3: Calculate probability of producing a particle with mass between 199 and 201 GeV
prob_between_199_and_201 = norm.cdf(201, mu, sigma) - norm.cdf(199, mu, sigma)
print(f"Probability of producing a particle with mass between 199 and 201 GeV: {prob_between_199_and_201:.4f}")

# Step 4: Calculate probability of independently producing two new particles with masses above 203 GeV
prob_above_203 = norm.sf(203, mu, sigma)
prob_two_particles_above_203 = prob_above_203 ** 2  # Independent events: multiply individual probabilities
print(f"Probability of independently producing two particles with mass > 203 GeV: {prob_two_particles_above_203:.4f}")
