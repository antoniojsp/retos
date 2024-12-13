from google.colab import runtime
import time
from IPython.display import clear_output

def countdown_timer(seconds=120):
  """Displays a red countdown timer in Google Colab.

  Args:
    seconds: The number of seconds to count down from. Defaults to 120 (2 minutes).
  """

  for remaining in range(seconds, -1, -1):
    minutes, secs = divmod(remaining, 60)
    time_str = '\033[91m{:02d}:{:02d}\033[0m'.format(minutes, secs) # Red color code
    clear_output(wait=True)  # Clear previous output
    print(f"Disconnecting in: {time_str}", end='\r')
    time.sleep(1)

  print("\nDisconnected!")
  runtime.unassign()  # Disconnect runtime


# Example usage (2 minute countdown):
countdown_timer()

# Example usage (5 minute countdown):
# countdown_timer(300)