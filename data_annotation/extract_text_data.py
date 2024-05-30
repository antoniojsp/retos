import re
from datetime import datetime
import matplotlib.pyplot as plt

# Log strings to represent the events
log_data = [
    "2024-04-27 08:15:23,123 INFO  [auth] User 'john_doe' successfully logged in from IP '192.168.1.10'",
    "2024-04-27 08:19:15,789 INFO  [auth] User 'jane_smith' successfully logged in from IP '192.168.1.11'",
    "2024-04-27 08:25:00,456 INFO  [auth] User 'john_doe' logged out",
    # Add other log lines as needed
]

# Patterns to match login and logout events
login_pattern = re.compile(r'(?P<timestamp>[\d-]+ [\d:,]+) INFO  \[auth\] User \'(?P<user>\w+)\' successfully logged in')
logout_pattern = re.compile(r'(?P<timestamp>[\d-]+ [\d:,]+) INFO  \[auth\] User \'(?P<user>\w+)\' logged out')

events = []

# Extract events
for line in log_data:
    login_match = login_pattern.match(line)
    logout_match = logout_pattern.match(line)
    if login_match:
        events.append((login_match.group('timestamp'), login_match.group('user'), 'login'))
    elif logout_match:
        events.append((logout_match.group('timestamp'), logout_match.group('user'), 'logout'))

# Convert timestamp to datetime object and sort events by time
events = [(datetime.strptime(ts, '%Y-%m-%d %H:%M:%S,%f'), user, action) for ts, user, action in events]
events.sort(key=lambda event: event[0])

print(events)

from collections import defaultdict

# Dictionary to keep track of active sessions
active_users = defaultdict(lambda: 0)
concurrent_users = []

for timestamp, user, action in events:
    if action == 'login':
        active_users[user] += 1
    elif action == 'logout':
        active_users[user] -= 1
        # Remove user if count falls to zero (logout completed)
        if active_users[user] == 0:
            del active_users[user]
    concurrent_users.append((timestamp, len(active_users)))

# Extract the time series data
times, user_counts = zip(*concurrent_users)

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(times, user_counts, marker='o', linestyle='-')
plt.title("Concurrent Database Users Over Time")
plt.xlabel("Time")
plt.ylabel("Number of Concurrent Users")
plt.grid(True)
plt.show()


private static boolean detectCycle(ListNode head) {
	    ListNode slow = head, fast = head;
	    while (fast != null && fast.next != null) {
	        slow = slow.next;
	        fast = fast.next.next;
	        if (slow == fast) {
	            return true;
	        }
	    }
	    return false;
	}