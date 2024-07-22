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


def exploit(query):
    """Attempts to exploit a potential SQL injection vulnerability.

    Args:
        query: The original SQL query string.

    Returns:
        None
    """
    modified_query = query + " WAITFOR DELAY '0:0:5'"
    start_time = time.time()
    simulate_query(modified_query)
    execution_time = time.time() - start_time

    if execution_time > 2:
        print("Vulnerability found!")
    else:
        print("No vulnerability found")


# Example usage
normal_query = "Hola"
exploit(normal_query)
