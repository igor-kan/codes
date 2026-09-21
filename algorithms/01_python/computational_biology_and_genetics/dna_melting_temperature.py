"""
Oligonucleotide DNA Melting Temperature Tm Estimation.
Reference: Campbell Biology (12th Ed.), Ch. 20 (DNA Tools and Biotechnology); Marmur-Doty formula.
"""
def marmur_doty_tm(dna_seq: str) -> float:
    """
    For sequences < 14 bp: Tm = (wA + xT)*2 + (yG + zC)*4.
    For sequences >= 14 bp: Tm = 64.9 + 41 * (yG + zC - 16.4) / (wA + xT + yG + zC).
    """
    dna = dna_seq.upper()
    n = len(dna)
    count_at = dna.count('A') + dna.count('T')
    count_gc = dna.count('G') + dna.count('C')
    
    if n < 14:
        return float(count_at * 2 + count_gc * 4)
    else:
        return float(64.9 + 41.0 * (count_gc - 16.4) / n)
