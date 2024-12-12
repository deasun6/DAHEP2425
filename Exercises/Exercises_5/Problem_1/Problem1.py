import matplotlib.pyplot as plt
import numpy as np
import uproot
from scipy.optimize import minimize

# Podaci sile (F) i izmjerenog ubrzanja (a) sa nesigurnostima (sigma)
forces = np.array([1, 2, 3, 4, 5])  # N
accelerations = np.array([9.8, 21.2, 34.5, 39.9, 48.5])  # m/s²
uncertainties = np.array([1.0, 1.9, 3.1, 3.9, 5.1])  # nesigurnosti u a

# Definiramo negativnu log-likelihood funkciju
def neg_log_likelihood(m):
    # Teorijsko ubrzanje prema trenutnoj procjeni mase m
    predicted_accelerations = forces / m
    
    # Log-likelihood funkcija za normalnu distribuciju: zbir kvadrata odstupanja ponderiranih nesigurnostima
    likelihood = -0.5 * np.sum(((accelerations - predicted_accelerations) / uncertainties) ** 2)
    
    # Vraćamo negativnu vrijednost jer scipy.optimize.minimize minimizira funkciju
    return -likelihood

# Procjena mase koja maksimizira vjerodostojnost
initial_guess = 1.0  # Početna procjena za masu
result = minimize(neg_log_likelihood, initial_guess)
mass_estimate = result.x[0]

# Ispis procijenjene mase
print(f"Procijenjena masa putem maksimalne vjerodostojnosti: {mass_estimate:.2f} kg")

# Vizualizacija rezultata
plt.errorbar(forces, accelerations, yerr=uncertainties, fmt='o', label='Izmjereni podaci s nesigurnostima')
plt.plot(forces, forces / mass_estimate, 'r-', label=f'Najbolja procjena modela (masa = {mass_estimate:.2f} kg)')
plt.xlabel('Sila (N)')
plt.ylabel('Ubrzanje (m/s²)')
plt.title('Sila vs. Ubrzanje sa MLE Podesenim Modelom')
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("aFm_plot.png")