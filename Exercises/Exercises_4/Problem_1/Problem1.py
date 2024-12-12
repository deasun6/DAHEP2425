import uproot 
import matplotlib.pyplot as plt
import numpy as np
import math
file = uproot.open(" /home/public/data/Lifetime/Lifetime.root")
print(file.keys()) 
tree = file["Tree"]
podaci = tree["t"].array()
print(podaci)

plt.hist(podaci)
plt.savefig("lifetimeDATA.png")