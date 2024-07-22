import time

def simulate_query(query):
  """Simulates the execution of a SQL query.

  If the query contains the string "WAITFOR DELAY", it simulates a successful
  time-based injection by pausing execution for 5 seconds. Otherwise, it prints
  "Query executed successfully" and returns immediately.

  Args:
    query: The SQL query string to simulate.

  Returns:
    None
  """
  if "WAITFOR DELAY" in query:
    time.sleep(5)
  else:
    print("Query executed successfully")

simulate_query("SELECT * FROM data;")


def exploit(query):
  """Attempts to exploit a potential SQL injection vulnerability.

  It modifies the input query to include a time-based delay using the
  "WAITFOR DELAY" command. It then calls `simulate_query` with the modified
  query. If `simulate_query` takes more than 2 seconds to execute, it prints
  "Vulnerability found!". Otherwise, it prints "No vulnerability found".

  Args:
    query: The SQL query string to exploit.

  Returns:
    None
  """
  modified_query = query
  start_time = time.time()
  simulate_query(modified_query)
  end_time = time.time()
  if end_time - start_time > 2:
    print("Vulnerability found!")
  else:
    print("No vulnerability found")

exploit("SELECT * FROM data;")
