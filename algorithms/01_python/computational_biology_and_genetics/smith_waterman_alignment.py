"""
Smith-Waterman Dynamic Programming Local Sequence Alignment.
Reference: Campbell Biology (12th Ed.), Ch. 21 (Genomes and Their Evolution).
"""
import numpy as np

def smith_waterman(seq1: str, seq2: str, match: int = 2, mismatch: int = -1, gap: int = -1) -> int:
    """Computes the maximum local alignment score between two sequences."""
    n, m = len(seq1), len(seq2)
    H = np.zeros((n + 1, m + 1), dtype=int)
    max_score = 0
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score_diag = H[i-1, j-1] + (match if seq1[i-1] == seq2[j-1] else mismatch)
            score_up = H[i-1, j] + gap
            score_left = H[i, j-1] + gap
            H[i, j] = max(0, score_diag, score_up, score_left)
            if H[i, j] > max_score:
                max_score = H[i, j]
                
    return int(max_score)
