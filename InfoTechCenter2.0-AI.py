import time
import sys

def boot_up_sequence(duration, interval):
    """
    Simulates a boot-up sequence with a loading animation.

    Parameters:
        duration (float): The total duration of the boot-up sequence in seconds.
        interval (float): The interval between each animation frame in seconds.
    """
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(1)  # Wait for 1 second before starting the boot-up sequence

    frames = 20  # Total number of frames for the loading animation
    ellipsis = 0  # Initial number of ellipses in the animation

    # Calculate the total number of iterations based on duration and interval
    total_iterations = int(duration / interval)

    # Loop through each iteration
    for i in range(total_iterations):
        # Calculate the progress percentage
        percent_complete = (i + 1) / total_iterations * 100
        # Construct the boot-up message with ellipses and progress percentage
        message = f"Infotech Center System Booting{'.' * ellipsis} ({percent_complete:.1f}% complete)"
        # Write the message to stdout, overwriting the previous message using '\r'
        sys.stdout.write("\r" + message)
        sys.stdout.flush()  # Flush the stdout buffer to ensure immediate display
        time.sleep(interval)  # Pause for the specified interval
        ellipsis = (ellipsis + 1) % (frames + 1)  # Update the number of ellipses for animation

    # Print the final boot-up completion message
    print("\n\nOperating System Booted Up - Retina Scanned - Access Granted!")

if __name__ == "__main__":
    boot_up_duration = 5  # Duration of the boot-up sequence in seconds
    animation_interval = 0.25  # Interval between each animation frame in seconds
    boot_up_sequence(boot_up_duration, animation_interval)
