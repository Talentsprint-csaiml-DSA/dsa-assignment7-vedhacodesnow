def longest_common_subsequence(X, Y):
    # Get lengths of the strings
    m, n = len(X), len(Y)
    
    # Create a DP table where dp[i][j] stores the LCS length of X[:i] and Y[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the LCS is in dp[m][n]
    lcs_length = dp[m][n]
    
    # (Optional) Retrieve the LCS itself by backtracking
    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # Reverse the LCS since we constructed it backward
    lcs.reverse()
    
    return lcs_length  # Change this to `(lcs_length, ''.join(lcs))` to also return the LCS itself
