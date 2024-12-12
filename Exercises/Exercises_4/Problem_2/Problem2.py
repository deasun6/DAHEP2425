import uproot 
import matplotlib.pyplot as plt
import numpy as np
import math

plt.hist(podaci)
plt.savefig("lifetimeDATA.png")

def theoretical_pdf(t, tau):
    return ((1 / tau) * np.exp (-t/tau))

tau_values=[0.5, 1,  2, 3]
t_values=np.linspace(0, np.max(podaci),  500)

plt.figure(figsize=(10,6))
for tau in tau_values:
    plt.plot(t_values, theoretical_pdf(t_values,  tau))

plt.savefig("prob2.png")

t_int = 1
tau = 2

Probability = 1 -  np.exp(-t_int/tau)
print (Probability)