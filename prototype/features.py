
import csv
import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt


# Location of our first experiment's raw recordings.
DATA_DIR = Path.home() / "Documents/CSI-recordings/experiment-01"

# Use the exact same 52 CSI positions as collect.py.
HT_BINS = list(range(1, 27)) + list(range(38, 64))


def inspect_recording(file_path):
    valid = 0
    malformed = 0
    other_lines = 0

    # Store average magnitude for all valid CSI packets.
    mean_amplitudes = []

    # Store data from eligible HT packets only.
    ht_amplitudes = []
    ht_timestamps = []

    with open(
        file_path,
        "r",
        encoding="utf-8",
        errors="replace"
    ) as file:

        for line_number, line in enumerate(file, start=1):

            # Skip diagnostic lines such as PING_STATS.
            if not line.startswith("CSI_DATA,"):
                other_lines += 1
                continue

            try:
                # Parse the CSI_DATA line as CSV.
                fields = next(csv.reader([line]))

                # Match the 25-field format used by collect.py.
                if len(fields) != 25:
                    raise ValueError(
                        f"Expected 25 fields, got {len(fields)}"
                    )

                # Extract the CSI array.
                csi_values = json.loads(fields[24])

                # Validate CSI array size and contents.
                if (
                    int(fields[22]) != 128
                    or not isinstance(csi_values, list)
                    or len(csi_values) != 128
                    or any(type(v) is not int for v in csi_values)
                ):
                    raise ValueError("Expected 128 CSI integers")

                # Convert the CSI array into a NumPy array.
                csi_array = np.array(
                    csi_values,
                    dtype=float
                )

                # Separate the two components of each pair.
                first = csi_array[0::2]
                second = csi_array[1::2]

                # Calculate the magnitude of all 64 pairs.
                amplitudes = np.hypot(first, second)

                # Average magnitude across all 64 pairs.
                mean_amplitude = float(
                    np.mean(amplitudes)
                )

                mean_amplitudes.append(mean_amplitude)

                # Match the filtering rules in collect.py.
                #
                # fields[5]  == "1": HT packet
                # fields[7]  == "0": Required metadata condition
                # fields[23] == "0": Required metadata condition
                is_eligible_ht = (
                    fields[5] == "1"
                    and fields[7] == "0"
                    and fields[23] == "0"
                )

                if is_eligible_ht:

                    # Select the same 52 CSI pairs as collect.py.
                    selected_amplitudes = amplitudes[HT_BINS]

                    # Calculate mean magnitude of selected pairs.
                    ht_mean_amplitude = float(
                        np.mean(selected_amplitudes)
                    )

                    # Extract the device timestamp.
                    raw_timestamp = int(fields[18])

                    # Interpret it as unsigned 32-bit.
                    timestamp = raw_timestamp & 0xFFFFFFFF

                    # Store the HT measurement.
                    ht_amplitudes.append(ht_mean_amplitude)
                    ht_timestamps.append(timestamp)

                valid += 1

            except (
                csv.Error,
                json.JSONDecodeError,
                ValueError,
                TypeError,
                IndexError,
                StopIteration
            ) as error:

                malformed += 1

                print(
                    f"Invalid CSI line {line_number}: {error}"
                )

    # Print general recording statistics.
    print(f"\nRecording: {file_path.name}")
    print(f"Valid CSI records: {valid}")
    print(f"Malformed CSI records: {malformed}")
    print(f"Other diagnostic lines: {other_lines}")

    if mean_amplitudes:
        print(
            f"Average CSI amplitude: "
            f"{np.mean(mean_amplitudes):.2f}"
        )

        print(
            f"Minimum packet average: "
            f"{np.min(mean_amplitudes):.2f}"
        )

        print(
            f"Maximum packet average: "
            f"{np.max(mean_amplitudes):.2f}"
        )

    # Analyze eligible HT packets.
    if ht_amplitudes:

        print(f"Eligible HT packets: {len(ht_amplitudes)}")

        print(
            f"Average eligible HT magnitude: "
            f"{np.mean(ht_amplitudes):.2f}"
        )

        print(f"First HT timestamp: {ht_timestamps[0]}")
        print(f"Last HT timestamp: {ht_timestamps[-1]}")

        # Check for unexpected timestamp resets.
        if any(
            later < earlier
            for earlier, later in zip(
                ht_timestamps,
                ht_timestamps[1:]
            )
        ):
            raise ValueError(
                f"Non-monotonic timestamps in {file_path.name}"
            )

        # Convert assumed microseconds into elapsed seconds.
        # Each receiver has its own clock.
        elapsed_seconds = [
            (timestamp - ht_timestamps[0]) / 1_000_000
            for timestamp in ht_timestamps
        ]

        duration = elapsed_seconds[-1]

        print(
            f"Recording duration: {duration:.2f} seconds"
        )

        # Create graph of the eligible HT measurements.
        plt.figure(figsize=(12, 5))

        plt.plot(
            elapsed_seconds,
            ht_amplitudes,
            linewidth=0.8
        )

        plt.title(
            f"Eligible HT CSI Amplitude — {file_path.stem}"
        )

        plt.xlabel(
            "Elapsed Time (seconds, receiver-local)"
        )

        plt.ylabel(
            "Mean Raw CSI Magnitude (52 Selected Pairs)"
        )

        plt.grid(True, alpha=0.3)
        plt.tight_layout()

        # Save the graph outside the GitHub repository.
        output_path = (
            DATA_DIR / f"{file_path.stem}_ht_amplitude.png"
        )

        plt.savefig(output_path, dpi=150)
        plt.close()

        print(f"Graph saved: {output_path.name}")

    else:
        print("No eligible HT packets found.")


if __name__ == "__main__":

    for receiver in ["X01", "X02", "X03", "X04"]:

        recording = DATA_DIR / f"{receiver}.log"

        inspect_recording(recording)
