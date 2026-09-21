"""
Needleman-Wunsch Global Sequence Alignment.
Reference: Campbell Biology (12th Ed.), Ch. 21.
"""
import numpy as np

def needleman_wunsch(seq1: str, seq2: str, match: int = 1, mismatch: int = -1, gap: int = -1) -> int:
    """Computes optimal global alignment score."""
    n, m = len(seq1), len(seq2)
    dp = np.zeros((n + 1, m + 1), dtype=int)
    
    for i in range(n + 1):
        dp[i, 0] = i * gap
    for j in range(m + 1):
        dp[0, j] = j * gap
        
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            diag = dp[i-1, j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            up = dp[i-1, j] + gap
            left = dp[i, j-1] + gap
            dp[i, j] = max(diag, up, left)
            
    return int(dp[n, m])
