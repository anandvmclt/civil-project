

# User Input
from locale import normalize


pci = 66
deflcetion = 0.73
iri = 4.2
cvpd = 2560


# Constant values
w = {0.297, 0.247, 0.292, 0.163}

# Step 4 onwards
# Get fuzzy metrics from Give input & Graphs
normalized_fuzzy_set = 0 # will get from fuzzy metrics
# Step 5
v = w * normalized_fuzzy_set

# step 6
z = {0.33, 0.267, 0.2, 0.133, 0.07}  # Constant
FPCI = z * v

# Output  = a number only (fpci)