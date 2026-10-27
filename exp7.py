
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

area = 100
channel_per_cell = 20
radii = [1.0, 0.5]
cell_counts = []
capacities = []

print("Experiment 7: Cell Splitting")
print("----------------------------")

for R in radii:
    cell_area = (3 * math.sqrt(3) / 2) * R**2
    cells = math.ceil(area / cell_area)
    capacity = cells * channel_per_cell

    cell_counts.append(cells)
    capacities.append(capacity)

    print(f"Cell radius = {R:.1f} km")
    print(f"Approximate number of cells = {cells}")
    print(f"Total channel capacity = {capacity}")
    print()

plt.bar(["Before splitting", "After splitting"], capacities)
plt.title("Network Capacity Improvement by Cell Splitting")
plt.ylabel("Estimated Total Channels")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("exp7_cell_splitting.png", dpi=200)

print("Graph saved as exp7_cell_splitting.png")
