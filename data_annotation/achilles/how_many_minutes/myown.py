


def minutes_between_time(start_time, end_time):
  """Calculates the number of minutes between two times in the same day.

  Args:
      start_time: A string representing the start time in 24-hour format (e.g., "14:09").
      end_time: A string representing the end time in 24-hour format (e.g., "14:27").

  Returns:
      The number of minutes between the start and end times.
  """

  start_hour, start_minute = map(int, start_time.split(":"))
  end_hour, end_minute = map(int, end_time.split(":"))

  return (end_hour - start_hour) * 60 + (end_minute - start_minute)

# Example usage
start_time = "2:09"
end_time = "2:27"
minutes_diff = minutes_between_time(start_time, end_time)

print(minutes_diff)