"""
Data captured from:

Thomas M. Smolen, David B. Manley, and Bruce E.  Poling, "Vapor-Liquid Equilibrium Data for the NH3-H20 
System and Its Description with a Modified Cubic Equation of State", J. Chem. Eng. Data, 1991

by Ian Bell

According to researchers at NIST TRC, the y_H2O values should be ignored because they were not directly measured, 
rather they were backed out from the equation of state, making this PTX data rather than PTXY
"""

Smolen_data = {
293.15:{
    'z_H2O': [9.51700E-01, 9.51700E-01, 9.47800E-01, 9.47800E-01, 9.28300E-01, 9.02800E-01, 8.95600E-01, 8.50600E-01, 8.50600E-01, 8.50000E-01, 8.50000E-01, 8.39600E-01, 8.39600E-01, 8.00100E-01, 8.00100E-01, 7.97600E-01, 7.97500E-01, 7.97500E-01, 7.45500E-01, 7.45500E-01, 6.99000E-01, 6.98000E-01, 6.98000E-01, 6.01400E-01, 6.01400E-01, 5.92700E-01, 5.92700E-01, 5.91600E-01, 5.91600E-01, 4.98500E-01, 4.98500E-01, 4.97300E-01, 4.97300E-01, 2.99200E-01, 2.99200E-01, 2.97200E-01, 2.97200E-01, 2.07400E-01, 2.07400E-01, 2.07400E-01, 2.07400E-01, 1.07100E-01, 1.07100E-01, 9.96000E-02, 9.96000E-02, 9.90000E-02, 9.90000E-02, 5.82000E-02, 5.82000E-02, 4.99000E-02, 4.64000E-02, 4.64000E-02, 4.61000E-02, 4.61000E-02, 4.51000E-02, 3.95000E-02, 3.95000E-02],
    'x_H2O': [9.51800E-01, 9.51800E-01, 9.47900E-01, 9.47900E-01, 9.28400E-01, 9.03000E-01, 8.95800E-01, 8.50800E-01, 8.50800E-01, 8.50300E-01, 8.50300E-01, 8.39900E-01, 8.39900E-01, 8.00400E-01, 8.00400E-01, 7.97900E-01, 7.97900E-01, 7.97900E-01, 7.45600E-01, 7.45600E-01, 6.99200E-01, 6.98100E-01, 6.98100E-01, 6.01900E-01, 6.01900E-01, 5.93300E-01, 5.93300E-01, 5.92200E-01, 5.92200E-01, 4.99500E-01, 4.99500E-01, 4.98500E-01, 4.98500E-01, 3.01600E-01, 3.01600E-01, 2.99900E-01, 2.99900E-01, 2.08800E-01, 2.08800E-01, 2.08900E-01, 2.08900E-01, 1.08300E-01, 1.08300E-01, 1.00600E-01, 1.00600E-01, 1.00000E-01, 1.00000E-01, 5.88000E-02, 5.88000E-02, 5.06000E-02, 4.66000E-02, 4.66000E-02, 4.66000E-02, 4.66000E-02, 4.57000E-02, 3.98000E-02, 3.98000E-02],
    'y_H2O': [3.51000E-01, 3.51000E-01, 3.29000E-01, 3.29000E-01, 2.46000E-01, 1.74000E-01, 1.59000E-01, 9.41000E-02, 9.41000E-02, 9.36000E-02, 9.36000E-02, 8.34000E-02, 8.34000E-02, 5.48000E-02, 5.48000E-02, 5.34000E-02, 5.34000E-02, 5.34000E-02, 3.13000E-02, 3.13000E-02, 1.98000E-02, 1.96000E-02, 1.96000E-02, 7.83000E-03, 7.83000E-03, 7.22000E-03, 7.22000E-03, 7.15000E-03, 7.15000E-03, 3.09000E-03, 3.09000E-03, 3.06000E-03, 3.06000E-03, 6.24000E-04, 6.24000E-04, 6.17000E-04, 6.17000E-04, 3.23000E-04, 3.23000E-04, 3.24000E-04, 3.24000E-04, 1.55000E-04, 1.55000E-04, 1.45000E-04, 1.45000E-04, 1.44000E-04, 1.44000E-04, 9.16000E-05, 9.16000E-05, 8.06000E-05, 7.53000E-05, 7.53000E-05, 7.54000E-05, 7.54000E-05, 7.41000E-05, 6.59000E-05, 6.59000E-05],
    'p_psia': [9.20000E-01, 9.22000E-01, 9.52000E-01, 9.68000E-01, 1.23600E+00, 1.68600E+00, 1.81300E+00, 2.75400E+00, 2.81400E+00, 2.79600E+00, 2.82400E+00, 3.06400E+00, 3.11600E+00, 4.25700E+00, 4.27600E+00, 4.42000E+00, 4.41800E+00, 4.55100E+00, 6.80500E+00, 6.80600E+00, 9.67400E+00, 9.85500E+00, 9.83800E+00, 1.93940E+01, 1.93960E+01, 2.05930E+01, 2.05910E+01, 2.04430E+01, 2.04320E+01, 3.61700E+01, 3.60820E+01, 3.63950E+01, 3.62610E+01, 7.75100E+01, 7.75120E+01, 7.78290E+01, 7.79790E+01, 9.61580E+01, 9.61500E+01, 9.60280E+01, 9.60380E+01, 1.09317E+02, 1.09292E+02, 1.10416E+02, 1.10391E+02, 1.10508E+02, 1.10414E+02, 1.15970E+02, 1.16009E+02, 1.17458E+02, 1.17508E+02, 1.17434E+02, 1.17572E+02, 1.17578E+02, 1.18085E+02, 1.18417E+02, 1.18225E+02]
},
323.15:{
    'z_H2O': [0.9517, 0.9517, 0.9478, 0.9478, 0.9283, 0.9028, 0.9028, 0.8956, 0.8956, 0.8506, 0.8506, 0.8500, 0.8500, 0.8396, 0.8396, 0.8001, 0.8001, 0.7976, 0.7975, 0.7975, 0.7455, 0.7455, 0.6990, 0.6980, 0.6980, 0.6014, 0.6014, 0.5927, 0.5927, 0.5916, 0.5916, 0.4985, 0.4985, 0.4973, 0.4973, 0.2992, 0.2992, 0.2972, 0.2972, 0.2074, 0.2074, 0.2074, 0.2074, 0.1071, 0.0996, 0.0990, 0.0582, 0.0499, 0.0464, 0.0464, 0.0461, 0.0451, 0.0395, 0.0395],
    'x_H2O': [0.9517, 0.9519, 0.9481, 0.9481, 0.9287, 0.9033, 0.9033, 0.8962, 0.8962, 0.8513, 0.8513, 0.8509, 0.8509, 0.8404, 0.8404, 0.8010, 0.8010, 0.7986, 0.7987, 0.7987, 0.7457, 0.7457, 0.6994, 0.6983, 0.6983, 0.6028, 0.6028, 0.5943, 0.5943, 0.5932, 0.5932, 0.5009, 0.5009, 0.5001, 0.5001, 0.3046, 0.3046, 0.3033, 0.3033, 0.2107, 0.2107, 0.2104, 0.2104, 0.1099, 0.1017, 0.1013, 0.0596, 0.0513, 0.0468, 0.0468, 0.0473, 0.0464, 0.0400, 0.0400],
    'y_H2O': [0.441, 0.441, 0.419, 0.419, 0.325, 0.241, 0.241, 0.222, 0.222, 0.139, 0.139, 0.139, 0.139, 0.125, 0.125, 0.0864, 0.0864, 0.0845, 0.0846, 0.0846, 0.0529, 0.0529, 0.0359, 0.0356, 0.0356, 0.0168, 0.0168, 0.0158, 0.0158, 0.0157, 0.0157, 0.00814, 0.00814, 0.00810, 0.00810, 0.00249, 0.00249, 0.00247, 0.00247, 0.00150, 0.00150, 0.00150, 0.00150, 0.000803, 0.000752, 0.000749, 0.000479, 0.000422, 0.000390, 0.000390, 0.000393, 0.000386, 0.000340, 0.000340],
    'p_psia': [3.881, 3.885, 4.051, 4.044, 5.020, 6.486, 6.506, 6.951, 6.979, 10.192, 10.199, 10.247, 10.275, 11.199, 11.231, 15.004, 15.029, 15.449, 15.432, 15.515, 22.532, 22.532, 30.772, 31.102, 31.037, 56.173, 56.125, 59.079, 59.008, 58.713, 58.657, 94.808, 94.776, 95.384, 95.486, 183.693, 183.723, 184.491, 184.575, 225.414, 225.205, 225.433, 225.416, 256.696, 259.310, 259.487, 272.975, 277.271, 277.004, 276.572, 277.403, 278.262, 279.695, 278.715]
},
353.15:{
    'z_H2O': [0.9517, 0.9517, 0.9478, 0.9478, 0.9283, 0.9028, 0.9028, 0.8956, 0.8956, 0.8506, 0.8506, 0.8506, 0.8500, 0.8500, 0.8500, 0.8396, 0.8396, 0.8396, 0.8001, 0.8001, 0.7976, 0.7975, 0.7975, 0.6990, 0.7455, 0.7455, 0.6980, 0.6980, 0.6014, 0.6014, 0.5927, 0.5927, 0.5916, 0.5916, 0.4985, 0.4985, 0.4973, 0.4973, 0.2992, 0.2972, 0.2074, 0.2074],
    'x_H2O': [0.9522, 0.9522, 0.9485, 0.9485, 0.9292, 0.9039, 0.9039, 0.8970, 0.8970, 0.8522, 0.8522, 0.8522, 0.8520, 0.8520, 0.8520, 0.8415, 0.8415, 0.8415, 0.8022, 0.8022, 0.8000, 0.8002, 0.8002, 0.6998, 0.7458, 0.7458, 0.6985, 0.6985, 0.6042, 0.6042, 0.5959, 0.5959, 0.5948, 0.5948, 0.5033, 0.5033, 0.5028, 0.5028, 0.3096, 0.3089, 0.2131, 0.2136],
    'y_H2O': [0.522, 0.522, 0.500, 0.500, 0.404, 0.312, 0.312, 0.292, 0.292, 0.195, 0.195, 0.195, 0.194, 0.194, 0.194, 0.178, 0.178, 0.178, 0.129, 0.129, 0.127, 0.127, 0.127, 0.0610, 0.0844, 0.0844, 0.0605, 0.0605, 0.0329, 0.0329, 0.0313, 0.0313, 0.0311, 0.0311, 0.0184, 0.0184, 0.0184, 0.0184, 0.00742, 0.00740, 0.00499, 0.00500],
    'p_psia': [12.652, 12.647, 13.139, 13.141, 15.845, 19.777, 19.756, 21.016, 20.993, 29.360, 29.577, 29.372, 29.559, 29.665, 29.656, 31.875, 32.055, 32.053, 41.491, 41.481, 42.431, 42.340, 42.312, 78.385, 59.508, 59.516, 78.766, 78.798, 131.112, 131.314, 136.750, 136.723, 135.965, 136.132, 204.820, 204.580, 206.243, 205.804, 367.860, 369.466, 448.911, 449.592]
},
383.15:{
    'z_H2O': [0.9517, 0.9517, 0.9478, 0.9478, 0.9283, 0.9283, 0.9028, 0.9028, 0.8956, 0.8956, 0.8506, 0.8506, 0.8506, 0.8500, 0.8500, 0.8500, 0.8396, 0.8396, 0.8396, 0.8001, 0.8001, 0.7976, 0.7976, 0.7975, 0.7975, 0.7455, 0.6980, 0.6980, 0.4985, 0.4973, 0.6014, 0.5927, 0.5916],
    'x_H2O': [0.9528, 0.9528, 0.9492, 0.9492, 0.9301, 0.9301, 0.9050, 0.9050, 0.8984, 0.8984, 0.8538, 0.8538, 0.8538, 0.8540, 0.8540, 0.8540, 0.8434, 0.8434, 0.8434, 0.8043, 0.8043, 0.8022, 0.8022, 0.8027, 0.8027, 0.7461, 0.6990, 0.6990, 0.5069, 0.5070, 0.6064, 0.5985, 0.5974],
    'y_H2O': [0.589, 0.589, 0.569, 0.569, 0.475, 0.475, 0.382, 0.382, 0.362, 0.362, 0.256, 0.256, 0.256, 0.256, 0.256, 0.256, 0.237, 0.237, 0.237, 0.180, 0.180, 0.178, 0.178, 0.179, 0.179, 0.124, 0.0939, 0.0939, 0.0354, 0.0354, 0.0568, 0.0546, 0.0543],
    'p_psia': [33.859, 33.807, 35.003, 35.008, 40.977, 41.135, 49.727, 49.640, 52.489, 52.257, 70.333, 70.169, 70.457, 70.578, 71.072, 70.507, 75.415, 75.995, 75.862, 95.405, 95.242, 97.031, 96.976, 96.656, 96.617, 132.339, 168.502, 168.371, 383.037, 384.921, 260.233, 269.881, 269.052]
},
413.15:{
    'z_H2O': [0.9517, 0.9478, 0.9283, 0.9028, 0.8956, 0.8506, 0.8500, 0.8396, 0.8001, 0.7976, 0.7975, 0.6980],
    'x_H2O': [0.9536, 0.9503, 0.9314, 0.9066, 0.9004, 0.8560, 0.8567, 0.8460, 0.8070, 0.8053, 0.8061, 0.6995],
    'y_H2O': [0.655, 0.638, 0.549, 0.457, 0.437, 0.325, 0.326, 0.305, 0.241, 0.238, 0.239, 0.133],
    'p_psia': [77.610, 79.696, 91.330, 107.787, 112.246, 145.576, 146.115, 154.521, 189.506, 193.174, 192.251, 316.668],
}
}

import quantities as pq, json
data = []
for T in [293.15, 323.15, 353.15, 383.15, 413.15]:
    x_H2O = Smolen_data[T]['x_H2O']
    y_H2O = Smolen_data[T]['y_H2O']
    p_Pa = pq.Quantity(Smolen_data[T]['p_psia'],pq.psi).rescale(pq.Pa)
    for i in range(len(p_Pa)):
        pt = {'p (Pa)': float(p_Pa[i]),
              'T (K)': T,
              'x (molar)': [1-x_H2O[i], x_H2O[i]],
              'y (molar)': [1-y_H2O[i], y_H2O[i]],
              'rho\' (guess,mol/m3)': -1,
              'rho\'\' (guess,mol/m3)': -1,
              'type': "PTXY"
              }
        data.append(pt)

with open('PTXY-Smolen.json','w') as fp:
    JSON_data = {'about': {'names': ['Ammonia','Water']},
                'data': data
                }
    fp.write(json.dumps(JSON_data,indent=2))