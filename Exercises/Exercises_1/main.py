from ClassDef import Boson, Higgs  # Import the Boson and Higgs classes

# Create an instance of Boson
boson = Boson(name="Photon", spin=1, momentum=10)
boson.PrintInfo()  # Print information of the Boson object

# Create an instance of Higgs with momentum 30
higgs_boson = Higgs(momentum=30)
higgs_boson.PrintInfo()  # Print information of the Higgs boson

# Calculate and print the energy of the Higgs boson
energy = higgs_boson.Energy()
print(f"Energy of Higgs: {energy}")
