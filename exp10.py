import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

thresholds = [ -90, -85, -80, -75, -70 ]
handoff_events = [ 9, 7, 5, 3, 2 ]

print("Experiment 10: Handoff Thresholds")
print("---------------------------------")

for threshold, events in zip(thresholds, handoff_events):
    print(f"Threshold = {threshold} dBm, "
          f"Illustrative handoff events = {events}")

plt.plot(thresholds, handoff_events, marker="o")
plt.title("Handoff Threshold and Handoff Events")
plt.xlabel("Handoff Threshold (dBm)")
plt.ylabel("Illustrative Number of Handoff Events")
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("exp10_handoff.png", dpi=200)

print("\nGraph saved as exp10_handoff.png")
