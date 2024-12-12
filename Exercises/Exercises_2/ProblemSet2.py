#KOPIJA ZA DRUGE VJEZBE IZ NEKIFILE
import uproot 
import matplotlib.pyplot as plt
import numpy as np
file = uproot.open("/home/public/data/ggH125/ZZ4lAnalysis.root")
print(file.keys())
# Navigate to the ZZTree TDirectoryFile
zz_tree = file["ZZTree"]

# List contents inside the ZZTree directory
print(zz_tree.keys())
# Access the TTree "candTree" inside ZZTree
cand_tree = zz_tree["candTree"]

# List branches in the candTree,  ugasit  cu o vu n aredbu
#print(cand_tree.keys())

# Print information about the branches in the candTree 
#IDUCA LINIJA PREDUGA JER ISPISuJE SVE BRANCHES PA SAM JE STAVILA U KOMENTAR
#print(cand_tree.show())

# Access a specific branch and read the data
branch_data = cand_tree["LepPt"].array()  # Replace 'branch_name' with the actual branch name you want to read
print("LepPt:")
print(branch_data)
print("_______________________________________________________________________________")
# Ispis svih grana 
# Pretvori podatke u Pythonovu listu i ispiši
#print(branch_data.tolist())
branch_data = cand_tree["LepEta"].array()  # Replace 'branch_name' with the actual branch name you want to read
print("LepEta:")
print(branch_data)
print("_______________________________________________________________________________")
branch_data = cand_tree["LepPhi"].array()  # Replace 'branch_name' with the actual branch name you want to read
print("LepPhi:")
print(branch_data)
print("_______________________________________________________________________________")
print("_______________________________________________________________________________")
# Read the branches into awkward arrays
lep_pt = cand_tree["LepPt"].array()
lep_eta = cand_tree["LepEta"].array()
lep_phi = cand_tree["LepPhi"].array()

# Display some information about the data
print("LepPt:", lep_pt[:5])   # Print the first 5 events to get a sense of the data
print("LepEta:", lep_eta[:5])
print("LepPhi:", lep_phi[:5])
print("_______________________________________________________________________________")
# Now, let's organize the leptons into Z1 and Z2
# Assuming each event has 4 leptons (if not, filtering might be needed)

# Separate leptons from Z1 and Z2 based on the given rule
# Z1 consists of the first two leptons and Z2 consists of the third and fourth leptons

# Extract the first two leptons for Z1
Z1_lep_pt = lep_pt[:, :2]   # The first two leptons
Z1_lep_eta = lep_eta[:, :2]
Z1_lep_phi = lep_phi[:, :2]

# Extract the third and fourth leptons for Z2
Z2_lep_pt = lep_pt[:, 2:4]  # The third and fourth leptons
Z2_lep_eta = lep_eta[:, 2:4]
Z2_lep_phi = lep_phi[:, 2:4]
print("_______________________________________________________________________________")
# Display the first few entries to confirm the grouping
print("Prva dva leptona")
print("\nZ1 Leptons:")
print("Pt:", Z1_lep_pt[:5])
print("Eta:", Z1_lep_eta[:5])
print("Phi:", Z1_lep_phi[:5])
print("_______________________________________________________________________________")
print("Druga dva leptona")
print("\nZ2 Leptons:")
print("Pt:", Z2_lep_pt[:5])
print("Eta:", Z2_lep_eta[:5])
print("Phi:", Z2_lep_phi[:5])

#IZNAD PRINTA SAMO PAR PODATAKA DA SE DOBIJE OSJECAJ KKO TO IZGLEDA

# Izračunaj px, py, pz
lep_px = lep_pt * np.cos(lep_phi)
lep_py = lep_pt * np.sin(lep_phi)
lep_pz = lep_pt * np.sinh(lep_eta)

# Izračunaj energiju (pretpostavka: masa leptona = 0, E ≈ |p|)
lep_energy = np.sqrt(lep_px**2 + lep_py**2 + lep_pz**2)

# Funkcija za izračun invarijantne mase dvaju leptona
def invariant_mass(energy1, energy2, px1, px2, py1, py2, pz1, pz2):
    return np.sqrt((energy1 + energy2)**2 - (px1 + px2)**2 - (py1 + py2)**2 - (pz1 + pz2)**2)

# Izračunaj invarijantnu masu za prvi Z bozon (Z1)
Z1_mass = invariant_mass(
    lep_energy[:, 0], lep_energy[:, 1],
    lep_px[:, 0], lep_px[:, 1],
    lep_py[:, 0], lep_py[:, 1],
    lep_pz[:, 0], lep_pz[:, 1]
)

# Izračunaj invarijantnu masu za Higgsov bozon koristeći sva četiri leptona
Higgs_mass = invariant_mass(
    lep_energy[:, 0] + lep_energy[:, 1], lep_energy[:, 2] + lep_energy[:, 3],
    lep_px[:, 0] + lep_px[:, 1], lep_px[:, 2] + lep_px[:, 3],
    lep_py[:, 0] + lep_py[:, 1], lep_py[:, 2] + lep_py[:, 3],
    lep_pz[:, 0] + lep_pz[:, 1], lep_pz[:, 2] + lep_pz[:, 3]
)
# Nacrtaj histograme za mase
plt.figure(figsize=(10, 6))

plt.hist(Z1_mass, bins=50, color='blue', alpha=0.5, label="Invariant Mass of Z1")
plt.hist(Higgs_mass, bins=50, color='red', alpha=0.5, label="Invariant Mass of Higgs")

plt.title("Invariant Mass Histograms of Z1 and Higgs Boson")
plt.xlabel("Mass (GeV/c^2)")
plt.ylabel("Events")
plt.legend(loc="upper right")
plt.savefig("higgs_z1_histogram.png")