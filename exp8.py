import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sectors = ["Omnidirectional", "120-degree", "60-degree"]
interferers = [6, 2, 1]

print("Experiment 8: Sectored Cell and Interference")
print("--------------------------------------------")

for sector, count in zip(sectors, interferers):
    print(f"{sector}: Assumed interferers = {count}")

plt.bar(sectors, interferers)
plt.title("Effect of Cell Sectoring on Interference")
plt.xlabel("Antenna Configuration")
plt.ylabel("Assumed Number of Interferers")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("exp8_sectoring.png", dpi=200)

print("\nGraph saved as exp8_sectoring.png")
