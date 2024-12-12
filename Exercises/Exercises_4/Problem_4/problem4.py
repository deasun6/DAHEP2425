import matplotlib.pyplot as plt
import numpy as np
import uproot

file = uproot.open(" /home/public/data/Lifetime/Lifetime.root")
print(file.keys()) 
tree = file["Tree"]
podaci = tree["t"].array()


def theoretical_pdf(t, tau):
  return (1/tau)*np.exp(-t/tau)

def log_likelihood(tau, data):
    return np.sum(np.log(theoretical_pdf(data, tau)))

tau_values = np.linspace(0.1, 10, 100)  
log_likelihood_values = []


for tau in tau_values:
    log_likelihood_values.append(log_likelihood(tau, podaci))

negative_2_log_likelihood = -2 * np.array(log_likelihood_values)

plt.figure(figsize=(10, 6))
plt.plot(tau_values, negative_2_log_likelihood, label="-2 ln(L)")
plt.xlabel("τ (mean lifetime)")
plt.ylabel("-2 ln(L)")
plt.title("Log-Likelihood Function")
plt.axhline(y=np.min(negative_2_log_likelihood), color='r', linestyle='--', label='Min -2 ln(L)')
plt.legend()
plt.grid()
plt.savefig("log_likelihood_plot.png")
plt.show()

# Izračunavanje očekivane vrijednosti τ i nesigurnosti
# Očekivana vrijednost tau je ona za koju je -2 ln(L) minimalna
tau_hat = tau_values[np.argmin(negative_2_log_likelihood)]

# Izračunavanje nesigurnosti na temelju razlike
uncertainty = np.sqrt(1 / np.min(negative_2_log_likelihood))

print(f"Očekivana vrijednost τ: {tau_hat:.2f} ± {uncertainty:.2f}")
