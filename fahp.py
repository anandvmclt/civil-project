# Importing Graphs
import json
import numpy as np
from itertools import chain
from graphs import xp, yp1, yp2, yp3, yp4, yp5, xd, yd1, yd2, yd3, yd4, yd5, xi, yi1, yi2, yi3, yi4, yi5, xc, yc1, yc2, yc3, yc4, yc5


# --------------------------* Starting Calculations*---------------------------------

# General Function for Normalize a raw Matrics ( Accept list as input)
def normalize_matrics(raw):
    try:
        sum_of_raw = sum(raw)
        normalized_raw = []
        for obj in raw:
            if obj > 0:
                val = obj/sum_of_raw
            else:
                val = 0
            normalized_raw.append(round(val,3))
        return normalized_raw
    except Exception as ex:
        print(ex)
        return None
        


def fahp_project(input_data):
    wz = []
    final_const = []
    try:
        file = open('data.json', 'r')
        data = json.load(file)
        wz = data['wz']
        final_const = data['final_const']
    except Exception as ex:
        print("Exp:", ex)
    # Get corresponding values from Graph for each items
    pci_row_matrics = []
    deflection_row_matrics = []
    iri_row_matrics = []
    cvpd_row_matrics = []

    try:
        pci_row_matrics.append(round(np.interp(input_data[0], xp, yp1), 3))
        pci_row_matrics.append(round(np.interp(input_data[0], xp, yp2), 3))
        pci_row_matrics.append(round(np.interp(input_data[0], xp, yp3), 3))
        pci_row_matrics.append(round(np.interp(input_data[0], xp, yp4), 3))
        pci_row_matrics.append(round(np.interp(input_data[0], xp, yp5), 3))
    except Exception as ex:
        print(ex)

    try:
        deflection_row_matrics.append(round(np.interp(input_data[1], xd, yd1), 3))
        deflection_row_matrics.append(round(np.interp(input_data[1], xd, yd2), 3))
        deflection_row_matrics.append(round(np.interp(input_data[1], xd, yd3), 3))
        deflection_row_matrics.append(round(np.interp(input_data[1], xd, yd4), 3))
        deflection_row_matrics.append(round(np.interp(input_data[1], xd, yd5), 3))
    except Exception as ex:
        print(ex)


    try:
        iri_row_matrics.append(round(np.interp(input_data[2], xi, yi1), 3))
        iri_row_matrics.append(round(np.interp(input_data[2], xi, yi2), 3))
        iri_row_matrics.append(round(np.interp(input_data[2], xi, yi3), 3))
        iri_row_matrics.append(round(np.interp(input_data[2], xi, yi4), 3))
        iri_row_matrics.append(round(np.interp(input_data[2], xi, yi5), 3))
    except Exception as ex:
        print(ex)


    try:
        cvpd_row_matrics.append(round(np.interp(input_data[3], xc, yc1), 3))
        cvpd_row_matrics.append(round(np.interp(input_data[3], xc, yc2), 3))
        cvpd_row_matrics.append(round(np.interp(input_data[3], xc, yc3), 3))
        cvpd_row_matrics.append(round(np.interp(input_data[3], xc, yc4), 3))
        cvpd_row_matrics.append(round(np.interp(input_data[3], xc, yc5), 3))
    except Exception as ex:
        print(ex)


    # Step 2 : normailize step 1 values
    pci_norm = normalize_matrics(pci_row_matrics)
    deflection_norm = normalize_matrics(deflection_row_matrics)
    iri_norm = normalize_matrics(iri_row_matrics)
    cvpd_norm = normalize_matrics(cvpd_row_matrics)
    sum_of_normalized_raws = [pci_norm , deflection_norm, iri_norm, cvpd_norm]



    # Step 3 : Constant values
    nm = sum_of_normalized_raws

    # step 4 : Multiplying Normalized matrics into a Constant Raw
    M1 = np.array([wz])
    M2 = np.array(nm)
    vx = M1.dot(M2)  

    # step 5 : Multiplying above anser with into a Constant Raw matric
    final_const_raw = np.array([final_const])
    vx_transformed = vx.T
    FPCI = final_const_raw.dot(vx_transformed)
    return FPCI[0][0]


# opz = fahp_project([37, 0.73, 4.9, 1912])
# print(opz)