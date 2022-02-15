import matplotlib.pyplot as plt
import numpy as np
import math

def check_bounded(c, threshold, max_steps):
    z_n = 0
    for n in range(max_steps):
        z_n = np.exp(z_n) + c
    return abs(z_n) < threshold

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


c = complex_matrix(-1, 3, -2, 2, pixel_density=512)
plt.imshow(check_bounded(c, threshold=3, max_steps=20), cmap="Spectral")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()