import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def acceptance_rejection_with_count(pdf, xmin, xmax, max_pdf, num_samples):
    """
    Generate random numbers according to a given PDF using the acceptance-rejection method.
    Count the total number of attempts made.

    Parameters:
    - pdf: The target PDF function (should be normalized).
    - xmin, xmax: The range of x values to sample from.
    - max_pdf: The maximum value of the PDF in the range [xmin, xmax].
    - num_samples: The number of random numbers to generate.

    Returns:
    - samples: A list of generated random numbers.
    - total_attempts: The total number of attempts made.
    """
    samples = []
    total_attempts = 0

    while len(samples) < num_samples:
        # Step 1: Sample x uniformly from [xmin, xmax]
        x = np.random.uniform(xmin, xmax)
        
        # Step 2: Generate u uniformly from [0, max_pdf]
        u = np.random.uniform(0, max_pdf)
        
        # Step 3: Increment the total number of attempts
        total_attempts += 1

        # Step 4: Check if u < PDF(x)
        if u < pdf(x):
            samples.append(x)
    
    return samples, total_attempts

# Define the Gaussian PDF with mean = 0 and standard deviation = 1
def gaussian_pdf(x, mu=0, sigma=1):
    """Gaussian PDF with mean mu and standard deviation sigma."""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Parameters for the Gaussian PDF
mu, sigma = 0, 1
xmin, xmax = -5, 5
max_pdf = gaussian_pdf(mu, mu, sigma)  # Max value of Gaussian PDF occurs at the mean

# Number of samples to generate
num_samples = 10000

# Generate random numbers using the acceptance-rejection method and count the total attempts
samples, total_attempts = acceptance_rejection_with_count(lambda x: gaussian_pdf(x, mu, sigma), xmin, xmax, max_pdf, num_samples)

# Calculate the efficiency of the acceptance-rejection method
efficiency = num_samples / total_attempts

# Print the total number of attempts and the efficiency
print(f"Total number of random numbers generated to get {num_samples} accepted samples: {total_attempts}")
print(f"Efficiency of the acceptance-rejection method: {efficiency * 100:.2f}%")

# Plot the histogram of generated samples and the target PDF
x_values = np.linspace(xmin, xmax, 500)
pdf_values = gaussian_pdf(x_values, mu, sigma)

plt.figure(figsize=(10, 6))
plt.hist(samples, bins=50, density=True, alpha=0.6, color='b', label="Generated Samples")
plt.plot(x_values, pdf_values, 'r-', label="Target PDF (Gaussian)")
plt.title("Random Number Generation Using Acceptance-Rejection Method")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.savefig("accepted_random_numbers_histogram.png", format="png", dpi=300)
plt.show()
