import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def inversion_method(num_samples, mu=0, sigma=1):
    """
    Generate random numbers using the inversion method for a Gaussian distribution.

    Parameters:
    - num_samples: The number of random numbers to generate.
    - mu: Mean of the normal distribution.
    - sigma: Standard deviation of the normal distribution.

    Returns:
    - samples: A list of generated random numbers.
    """
    # Step 1: Generate uniform random numbers between 0 and 1
    u = np.random.uniform(0, 1, num_samples)
    
    # Step 2: Use the inverse CDF (ppf function) to find x values corresponding to u
    samples = norm.ppf(u, loc=mu, scale=sigma)
    
    return samples

# Number of samples to generate
num_samples = 10000

# Generate random numbers using the inversion method
inversion_samples = inversion_method(num_samples, mu=0, sigma=1)

# Plot the histogram of generated samples and the target PDF using inversion method
x_values = np.linspace(-5, 5, 500)
pdf_values = norm.pdf(x_values, loc=0, scale=1)

plt.figure(figsize=(10, 6))
plt.hist(inversion_samples, bins=50, density=True, alpha=0.6, color='g', label="Generated Samples (Inversion)")
plt.plot(x_values, pdf_values, 'r-', label="Target PDF (Gaussian)")
plt.title("Random Number Generation Using Inversion Method")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.savefig("inversion_method_random_numbers.png", format="png", dpi=300)
plt.show()

# Efficiency comparison with Acceptance-Rejection Method
# Note: Inversion method is theoretically 100% efficient as it does not discard any numbers
print("Efficiency of the Inversion Method: 100%")

# Let's compare with the acceptance-rejection method
def acceptance_rejection(pdf, xmin, xmax, max_pdf, num_samples):
    samples = []
    total_attempts = 0

    while len(samples) < num_samples:
        x = np.random.uniform(xmin, xmax)
        u = np.random.uniform(0, max_pdf)
        total_attempts += 1

        if u < pdf(x):
            samples.append(x)
    
    return samples, total_attempts

# Define the Gaussian PDF
def gaussian_pdf(x, mu=0, sigma=1):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Parameters for the acceptance-rejection method
xmin, xmax = -5, 5
max_pdf = gaussian_pdf(0, 0, 1)

# Generate samples using acceptance-rejection method and count total attempts
ar_samples, total_attempts = acceptance_rejection(lambda x: gaussian_pdf(x, 0, 1), xmin, xmax, max_pdf, num_samples)
ar_efficiency = num_samples / total_attempts * 100

# Compare efficiencies
print(f"Total number of random numbers generated using acceptance-rejection: {total_attempts}")
print(f"Efficiency of the Acceptance-Rejection Method: {ar_efficiency:.2f}%")
