#-*-coding:utf-8-*-
import numpy as np

class SampleImages():
    img = np.array([[ 8.5543060e-1, -2.6924706, -2.6418228, -2.6850739,
        -4.3925438, -5.0407677, -5.3005753, -5.7453804,
        -5.8561707, -5.5601006, -5.3261490, -5.1410065,
        -4.5818520],
       [-3.0735054, -3.7901077, -3.4134789, -3.3000298,
        -4.4461594, -5.0684700, -5.2847862, -5.5292130,
        -5.0336227, -1.6017990,  9.3610001e-1, -2.3256493,
        -3.9181061],
       [-4.1330681, -3.8515015, -8.1646347e-1, -8.9217377e-1,
        -1.3335342, -1.2172546, -2.7037621, -4.1382141,
        -3.2157097,  2.3868889e1,  5.9031010e1,  3.7333908e1,
         2.9150352],
       [-3.7557945, -4.4023552, -2.6779175,  2.4330521,
         1.9596630e1,  2.8124546e1,  9.1453476, -2.3631287e-1,
        -1.1780357,  8.9287781e1,  1.2990208e2,  4.8163338e1,
         1.0544186e1],
       [-1.1064110, -3.2025108, -4.1534920,  1.1203560e1,
         5.1554184e1,  4.1463577e1,  2.0989777e1,  3.7388954,
         2.8529358e-1,  3.2797913e1,  4.5255478e1,  2.1792320e1,
         7.5806313],
       [ 2.6179008, -2.5541153, -4.0398331,  1.2621078,
         2.0316647e1,  8.4888206e1,  1.2663353e2,  4.5039715e1,
         6.4030418,  6.5380898,  8.0477486,  7.3994331,
        -3.2645035e-1],
       [-1.9957390, -3.1956215, -1.5138664,  3.7298584e-1,
         2.1697487e1,  2.3932335e2,  2.1859827e2,  6.0338387e1,
         1.6322731e1,  2.1509933, -2.8086472, -3.4856110,
        -4.2747841],
       [-4.6783180, -1.6721725e-1,  9.7782021,  6.7177238,
         1.1235588e1,  8.6700378e1,  8.8574539e1,  3.5909302e1,
         1.3273281e1,  8.5235977e-1, -4.1762314, -5.4016571,
        -5.3319473],
       [-5.2759743, -1.1613426,  6.8409042,  2.5505638,
         4.3214531,  1.8136166e1,  2.1559727e1,  1.2120003e1,
         3.1703949e-1, -3.2974052, -5.2027702, -6.2712250,
        -5.8488922],
       [-4.7820740, -4.4724197, -3.0619736, -1.0619087,
         4.6185608,  8.2019844,  1.6174049,  1.0136795e-1,
         5.3901672e-3, -2.4079475, -5.0947685, -6.3966217,
        -6.1541367],
       [-4.2348442, -5.4827232, -5.2860909, -2.0456696e-1,
         4.3480976e1,  7.7862930e1,  3.0360786e1,  6.5378876,
         2.9734344, -1.8480148, -4.2827988, -5.2832336,
        -5.8148079],
       [-4.6846237, -5.8416519, -5.4832191,  1.1055450e1,
         1.2072739e2,  1.1762678e2,  3.1633408e1,  1.2005024e1,
         1.3760220e1,  1.2398556e1,  1.3810730, -2.0710144,
        -4.8352547],
       [-5.8347244, -6.3984108, -5.4164009,  7.5918579e-1,
         3.2535854e1,  3.9016018e1,  1.8140804e1,  2.1037762e1,
         9.5071274e1,  1.3168584e2,  3.7719284e1,  4.5783691,
        -3.2588120]], dtype=np.float32)

    aperture = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)

    aperture_bkg = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
      [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
      [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
      [0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)
