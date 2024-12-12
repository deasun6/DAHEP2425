import numpy as np
import matplotlib.pyplot as plt

def acceptance_rejection(pdf, xmin, xmax, max_pdf, num_samples):
    """
    Generate random numbers according to a given PDF using the acceptance-rejection method.

    Parameters:
    - pdf: The target PDF function (should be normalized).
    - xmin, xmax: The range of x values to sample from.
    - max_pdf: The maximum value of the PDF in the range [xmin, xmax].
    - num_samples: The number of random numbers to generate.

    Returns:
    - samples: A list of generated random numbers.
    """
    samples = []
    
    while len(samples) < num_samples:
        # Step 1: Sample x uniformly from [xmin, xmax]
        x = np.random.uniform(xmin, xmax)
        
        # Step 2: Generate u uniformly from [0, max_pdf]
        u = np.random.uniform(0, max_pdf)
        
        # Step 3: Check if u < PDF(x)
        if u < pdf(x):
            samples.append(x)
    
    return samples

# Define a sample PDF (let's use a Gaussian as an example)
def gaussian_pdf(x, mu=0, sigma=1):
    """Gaussian PDF with mean mu and standard deviation sigma."""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Parameters for the Gaussian PDF
mu, sigma = 0, 1
xmin, xmax = -5, 5
max_pdf = gaussian_pdf(mu, mu, sigma)  # Max value of Gaussian PDF occurs at the mean

# Number of samples to generate
num_samples = 10000

# Generate random numbers using the acceptance-rejection method
samples = acceptance_rejection(lambda x: gaussian_pdf(x, mu, sigma), xmin, xmax, max_pdf, num_samples)

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
plt.savefig("acceptance_rejection_method.png", format="png", dpi=300)
plt.show()
