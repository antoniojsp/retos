import re

data = """
row_no,number
1,1.12.2
2,1.12.9
3,1.13.0
4,1.14.0
5,2.2.1
6,2.3.3
7,1.15.0
8,2.7.0
9,3.4.1
10,3.5.2
11,3.5.6
12,3.6.0
13,3.8.1
14,3.10.0
15,3.11.0
16,4.1.1
17,4.5.0
18,4.7.0
19,4.8.1
20,3.12.0
21,4.8.3
22,4.10.1
23,4.10.2
24,4.11.1
25,4.12.0
26,4.17.1
27,4.19.1
28,4.20.2
29,4.22.0
30,4.23.1
31,4.25.1
32,4.27.1
33,4.28.1
34,4.28.2
35,4.28.4
36,4.29.0
37,4.29.1
38,4.29.3
39,4.29.5
40,4.29.6
41,4.30.0
42,4.31.0
43,4.32.0
44,4.32.1
45,4.32.2
46,4.33.0
47,4.35.0
48,4.35.3
49,4.37.0
50,4.38.0
51,4.39.1
52,4.39.2
53,4.39.3
54,4.40.2
55,4.41.0
56,4.41.1
57,4.41.2
58,4.41.3
59,4.41.4
60,4.41.5
61,4.41.6
62,4.42.0
63,4.42.1
64,4.43.0
65,4.44.0
66,4.44.1
67,2.2.0-rc.3
68,2.1.0-beta.25
"""


def is_version_in_range(version_string):
    """Checks if a version string is within the range >= 5.0.0 and < 5.76.0.

    Args:
      version_string: The version string to check.

    Returns:
      True if the version is in range, False otherwise.
    """
    try:
        # Extract major, minor, patch from version string, ignoring pre-release parts
        parts = [int(part) for part in re.findall(r'(\d+)', version_string)]
        major, minor, patch = parts[:3]  # Handle versions with fewer parts

        return major == 5 and minor < 76
    except Exception:
        return False


matching_rows = []
for line in data.strip().split('\n')[1:]:  # Skip header row
    row_no, version = line.split(',')
    if is_version_in_range(version):
        matching_rows.append(int(row_no))

print("Matching row numbers:", matching_rows)
