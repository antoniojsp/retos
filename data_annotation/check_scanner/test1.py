

import requests
from bs4 import BeautifulSoup
import urllib.parse

def scan_website(url: str) -> dict:
  """
  Scans a given URL for OWASP Top 10 vulnerabilities.

  Args:
    url: The URL of the website to scan.

  Returns:
    A dictionary containing the scan results with vulnerability names as keys
    and boolean values indicating whether the vulnerability was detected (True)
    or not (False).
  """
  results = {
      "Injection": False,
      "Broken Authentication": False,
      "Sensitive Data Exposure": False,
      "XML External Entities (XXE)": False,
      "Broken Access Control": False,
      "Security Misconfiguration": False,
      "Cross-Site Scripting (XSS)": False,
      "Insecure Deserialization": False,
      "Using Components with Known Vulnerabilities": False,
      "Insufficient Logging & Monitoring": False,
  }

  try:
    # --- 1. Injection ---
    # Basic check for SQL injection vulnerability
    payload = "' OR '1'='1"
    test_url = url + urllib.parse.quote(payload)
    response = requests.get(test_url)
    if "error in your SQL syntax" in response.text.lower():
      results["Injection"] = True

    # --- 2. Broken Authentication ---
    # Check for default credentials
    # This requires knowledge of the application and cannot be reliably
    # determined with a simple scan. Manual testing is recommended.

    # --- 3. Sensitive Data Exposure ---
    # Check for sensitive data in the response (e.g., passwords, credit card numbers)
    # This requires defining patterns for sensitive data and is highly
    # application-specific. Manual review is recommended.

    # --- 4. XML External Entities (XXE) ---
    # Requires sending a malicious XML payload and observing the response.
    # This is out of scope for a basic scanner and requires specialized tools.

    # --- 5. Broken Access Control ---
    # Requires testing access to restricted resources with different user roles.
    # This is out of scope for a basic scanner and requires knowledge of the
    # application's access control mechanisms.

    # --- 6. Security Misconfiguration ---
    # Check for common misconfigurations like directory listing, verbose error messages, etc.
    response = requests.get(url)
    if "Index of" in response.text:
      results["Security Misconfiguration"] = True
    if "stack trace" in response.text.lower():
      results["Security Misconfiguration"] = True

    # --- 7. Cross-Site Scripting (XSS) ---
    # Basic check for reflected XSS
    payload = "<script>alert('XSS')</script>"
    test_url = url + urllib.parse.quote(payload)
    response = requests.get(test_url)
    if payload in response.text:
      results["Cross-Site Scripting (XSS)"] = True

    # --- 8. Insecure Deserialization ---
    # Requires sending a malicious serialized object and observing the response.
    # This is out of scope for a basic scanner and requires specialized tools.

    # --- 9. Using Components with Known Vulnerabilities ---
    # This requires analyzing the website's source code and identifying
    # used libraries and their versions. Out of scope for this basic scanner.

    # --- 10. Insufficient Logging & Monitoring ---
    # This cannot be reliably determined with a simple scan. Manual review of
    # the application's logging and monitoring mechanisms is required.

  except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
  except Exception as e:
    print(f"An error occurred: {e}")

  return results

# Example usage
if __name__ == "__main__":
  ur = "http://sca.antoniocodes.net/"
  url_to_scan = ur
  scan_results = scan_website(url_to_scan)
  print(scan_results)
  print("\nScan Results:")
  for vulnerability, detected in scan_results.items():
    print(f"{vulnerability}: {detected}")