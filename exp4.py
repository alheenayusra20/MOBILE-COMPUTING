
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = 1.0
cluster_sizes = [7, 3]

print("Experiment 4: Co-channel Reuse Ratio")
print("------------------------------------")

for N in cluster_sizes:
    ratio = math.sqrt(3 * N)
    D = R * ratio
    print(f"Cluster size N = {N}")
    print(f"Cell radius R = {R} km")
    print(f"Reuse ratio D/R = {ratio:.3f}")
    print(f"Reuse distance D = {D:.3f} km")
    print()

ratios = [math.sqrt(3 * N) for N in cluster_sizes]

plt.figure(figsize=(7, 5))
plt.bar([str(N) for N in cluster_sizes], ratios)
plt.title("Co-channel Reuse Ratio")
plt.xlabel("Cluster Size (N)")
plt.ylabel("Reuse Ratio (D/R)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("exp4_reuse_ratio.png", dpi=200)

print("Graph saved as exp4_reuse_ratio.png")
