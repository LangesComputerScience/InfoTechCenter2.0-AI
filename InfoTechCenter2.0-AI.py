import time
import sys

def boot_up_sequence(duration, interval):
    """Simulates a boot-up sequence with a loading animation."""
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(1)

    frames = 20
    ellipsis = 0

    total_iterations = int(duration / interval)
    for i in range(total_iterations):
        percent_complete = (i + 1) / total_iterations * 100
        message = f"Infotech Center System Booting{'.' * ellipsis} ({percent_complete:.1f}% complete)"
        sys.stdout.write("\r" + message)
        sys.stdout.flush()
        time.sleep(interval)
        ellipsis = (ellipsis + 1) % (frames + 1)

    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    boot_up_duration = 5  # Duration of the boot-up sequence in seconds
    animation_interval = 0.25  # Interval between each animation frame in seconds
    boot_up_sequence(boot_up_duration, animation_interval)
