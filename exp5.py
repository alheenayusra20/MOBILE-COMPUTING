
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = 1.0
path_loss = 4
cluster_sizes = [7, 3]
sir_values = []

print("Experiment 5: Co-channel Interference and SIR")
print("--------------------------------------------")

for N in cluster_sizes:
    reuse_ratio = math.sqrt(3 * N)
    sir = (reuse_ratio ** path_loss) / 6
    sir_db = 10 * math.log10(sir)
    sir_values.append(sir_db)

    print(f"Cluster size N = {N}")
    print(f"Reuse ratio D/R = {reuse_ratio:.3f}")
    print(f"SIR = {sir:.3f}")
    print(f"SIR = {sir_db:.2f} dB")
    print()

plt.bar([str(N) for N in cluster_sizes], sir_values)
plt.title("Co-channel Interference: SIR Comparison")
plt.xlabel("Cluster Size (N)")
plt.ylabel("SIR (dB)")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("exp5_sir.png", dpi=200)
print("Graph saved as exp5_sir.png")
