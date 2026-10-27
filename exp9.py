import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import math

frequency_mhz = 900
distance_km = [0.1, 0.2, 0.5, 1, 2, 5]

print("Experiment 9: Path Loss Models")
print("------------------------------")
print("Frequency = 900 MHz")

free_space = []

for d in distance_km:
    fspl = 32.45 + 20 * math.log10(frequency_mhz) \
           + 20 * math.log10(d)
    free_space.append(fspl)
    print(f"Distance = {d} km, Free-space loss = {fspl:.2f} dB")

plt.plot(distance_km, free_space, marker="o")
plt.title("Free-Space Path Loss vs Distance")
plt.xlabel("Distance (km)")
plt.ylabel("Path Loss (dB)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("exp9_path_loss.png", dpi=200)

print("\nGraph saved as exp9_path_loss.png")
print("Note: This run calculates free-space path loss only.")
