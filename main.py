

# User Input
from locale import normalize


pci = 37
deflcetion = 0.73
iri = 4.9
cvpd = 1912


# Constant values
w = {0.31, 0.273, 0.284, 0.133}

# Step 4 onwards
# Get fuzzy metrics from Give input & Graphs
normalized_fuzzy_set = 0 # will get from fuzzy metrics



# Step 5
v = w * normalized_fuzzy_set

# step 6
z = {0.33, 0.267, 0.2, 0.133, 0.07}  # Constant
FPCI = z * v

# Output  = a number only (fpci)