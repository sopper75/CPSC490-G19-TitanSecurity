"""Stub quality check. Used as the smoke test."""

import os

def main():
    print("Quality check stub: OK")
    if os.path.exists("sample_recording.txt"):
        print("Sample recording found.")
    else:
        print("Sample recording missing.")

if __name__ == "__main__":
    main()
