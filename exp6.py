
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

guard_bands = [0.1, 0.2, 0.3, 0.5, 1.0]
interference = [1 / (g ** 2) for g in guard_bands]

print("Experiment 6: Adjacent-channel Interference")
print("-------------------------------------------")

for g, i in zip(guard_bands, interference):
    print(f"Guard band = {g:.1f} MHz, "
          f"Normalized interference = {i:.2f}")

plt.plot(guard_bands, interference, marker="o")
plt.title("Effect of Guard Band on Interference")
plt.xlabel("Guard Band (MHz)")
plt.ylabel("Normalized Interference")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("exp6_guard_band.png", dpi=200)

print("\nGraph saved as exp6_guard_band.png")
