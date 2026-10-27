
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = 1.0
cluster_sizes = [3, 4, 7, 12]
reuse_ratios = []

print("Experiment 3: Frequency Reuse Patterns")
print("--------------------------------------")
print("Cluster Size (N) | Reuse Ratio (D/R) | Reuse Distance (km)")

for N in cluster_sizes:
    ratio = math.sqrt(3 * N)
    distance = R * ratio
    reuse_ratios.append(ratio)
    print(f"{N:16} | {ratio:17.3f} | {distance:19.3f}")

plt.figure(figsize=(8, 5))
plt.bar([str(N) for N in cluster_sizes], reuse_ratios)
plt.title("Frequency Reuse for Different Cluster Sizes")
plt.xlabel("Cluster Size (N)")
plt.ylabel("Reuse Ratio (D/R)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("exp3_frequency_reuse.png", dpi=200)

print("\nGraph saved as exp3_frequency_reuse.png")
