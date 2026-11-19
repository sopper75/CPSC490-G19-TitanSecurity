
import csv
import math
from datetime import datetime
from pathlib import Path

import matplotlib.pyplot as plt


DATA_DIR = Path.home() / "Documents/CSI-recordings/experiment-01"
CSV_PATH = DATA_DIR / "live_events.csv"

BOARDS = ["X01", "X02", "X03", "X04"]

# Store measurements separately for each receiver.
times = {board: [] for board in BOARDS}
scores = {board: [] for board in BOARDS}
events = []

# Read the original monitoring CSV.
with CSV_PATH.open(newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))

# Use the monitoring application's first timestamp as time zero.
start = datetime.fromisoformat(
    rows[0]["display_receipt_time"]
)

for row in rows:
    timestamp = datetime.fromisoformat(
        row["display_receipt_time"]
    )

    elapsed = (timestamp - start).total_seconds()

    # Save event markers.
    event = row["event"].strip()

    if event:
        events.append((elapsed, event))

    # Save receiver variation measurements.
    board = row["board"].strip()
    value = row["variation_percent"].strip()

    if board not in BOARDS or not value:
        continue

    try:
        score = float(value)
    except ValueError:
        continue

    if not math.isfinite(score):
        continue

    times[board].append(elapsed)
    scores[board].append(score)


# Create four plots sharing the same time axis.
fig, axes = plt.subplots(
    4,
    1,
    figsize=(13, 11),
    sharex=True
)

for ax, board in zip(axes, BOARDS):

    # Plot the variation measurements.
    ax.plot(
        times[board],
        scores[board],
        linewidth=1.2
    )

    # Mark experiment events with dashed vertical lines.
    for event_time, event_name in events:
        ax.axvline(
            event_time,
            color="gray",
            linestyle="--",
            alpha=0.55
        )

    ax.set_title(f"{board} — CSI Variation")
    ax.set_ylabel("Variation (%)")
    ax.grid(True, alpha=0.25)


# Put event numbers above the first graph.
for number, (event_time, event_name) in enumerate(events, 1):
    axes[0].text(
        event_time,
        1.02,
        str(number),
        transform=axes[0].get_xaxis_transform(),
        ha="center",
        fontsize=10
    )

axes[-1].set_xlabel("Monitoring Elapsed Time (seconds)")

fig.suptitle(
    "November 13 Experiment — CSI Variation by Receiver",
    fontsize=15
)

plt.tight_layout(rect=(0, 0, 1, 0.96))

output_path = DATA_DIR / "experiment_variation_timeline.png"

plt.savefig(output_path, dpi=150)
plt.close()

print(f"Graph saved: {output_path}")
print("\nEvent marker legend:")

for number, (event_time, event_name) in enumerate(events, 1):
    print(f"{number}. {event_time:.2f}s — {event_name}")
