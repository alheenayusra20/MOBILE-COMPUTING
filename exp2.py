import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

R = 1.0
N = 7

area = (3 * math.sqrt(3) / 2) * R**2
D = R * math.sqrt(3 * N)

fig, ax = plt.subplots(figsize=(8, 7))

centres = [(0, 0)]

for i in range(6):
    angle = math.radians(60 * i)
    x = math.sqrt(3) * R * math.cos(angle)
    y = math.sqrt(3) * R * math.sin(angle)
    centres.append((x, y))

for i, (x, y) in enumerate(centres):
    cell = RegularPolygon(
        (x, y), 6, radius=R,
        orientation=math.radians(30),
        edgecolor="black",
        facecolor="lightblue",
        alpha=0.65
    )
    ax.add_patch(cell)
    ax.text(x, y, f"Cell {i+1}", ha="center", va="center")

ax.set_aspect("equal")
ax.set_title("Experiment 2: Hexagonal Cellular Layout")
ax.set_xlabel("Distance (km)")
ax.set_ylabel("Distance (km)")
ax.grid(True, linestyle="--", alpha=0.4)
ax.autoscale_view()
plt.tight_layout()
plt.savefig("exp2_hexagonal_layout.png", dpi=200)

print("Experiment 2: Hexagonal Cell Geometry")
print(f"Cell radius = {R:.2f} km")
print(f"Cell area = {area:.3f} square km")
print(f"Cluster size N = {N}")
print(f"Reuse ratio D/R = {math.sqrt(3*N):.3f}")
print(f"Reuse distance D = {D:.3f} km")
print("Graph saved as exp2_hexagonal_layout.png")
