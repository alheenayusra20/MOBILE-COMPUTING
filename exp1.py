import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

R = 1
centers = [(0, 0)]

for angle in range(0, 360, 60):
    x = np.sqrt(3) * R * np.cos(np.radians(angle))
    y = np.sqrt(3) * R * np.sin(np.radians(angle))
    centers.append((x, y))

fig, ax = plt.subplots(figsize=(8, 7))

for i, (cx, cy) in enumerate(centers):
    angles = np.radians(np.arange(30, 390, 60))
    x = cx + R * np.cos(angles)
    y = cy + R * np.sin(angles)

    ax.plot(x, y, "b-")
    ax.plot(cx, cy, "r^")

    ax.text(cx, cy + 0.2, f"BS{i+1}",
            ha="center", fontsize=9)
    ax.text(cx, cy - 0.2, f"Cell {i+1}",
            ha="center", fontsize=8)

ax.set_title("Experiment 1: Basic Cellular Network Structure")
ax.set_xlabel("X Position")
ax.set_ylabel("Y Position")
ax.set_aspect("equal")
ax.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("exp1_cellular_network.png", dpi=200)

print("Experiment 1: Basic Cellular Network")
print("------------------------------------")
print("Total cells = 7")
print("Total base stations = 7")
print("Each cell is served by one base station.")
print("Graph saved as exp1_cellular_network.png")
