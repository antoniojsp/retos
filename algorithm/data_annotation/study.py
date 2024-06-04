def is_interleave(a, b, c):
    """
    Checks if string 'c' is an interleaving of strings 'a' and 'b'.

    Args:
        a: The first string.
        b: The second string.
        c: The potential interleaved string.

    Returns:
        True if 'c' is an interleaving of 'a' and 'b', False otherwise.
    """

    len_a, len_b, len_c = len(a), len(b), len(c)
    if len_a + len_b != len_c:
        return False

    dp = [[False for _ in range(len_b + 1)] for _ in range(len_a + 1)]
    dp[0][0] = True

    for i in range(len_a + 1):
        for j in range(len_b + 1):
            if i > 0 and a[i - 1] == c[i + j - 1]:
                dp[i][j] = dp[i - 1][j]
            if j > 0 and b[j - 1] == c[i + j - 1]:
                dp[i][j] |= dp[i][j - 1]

    return dp[len_a][len_b]



