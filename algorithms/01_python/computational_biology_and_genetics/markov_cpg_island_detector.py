"""
CpG Island Detection via Observed-to-Expected Dinucleotide Frequency Ratio.
Reference: Campbell Biology (12th Ed.), Ch. 18 (Regulation of Gene Expression); Gardiner-Garden & Frommer (1987).
"""
def cpg_observed_to_expected_ratio(dna_seq: str) -> float:
    """
    Obs/Exp CpG = (Count(CG) * Length) / (Count(C) * Count(G)).
    A sequence with ratio > 0.6 and GC% > 50% is standardly classified as a CpG island.
    """
    dna = dna_seq.upper()
    n = len(dna)
    count_c = dna.count('C')
    count_g = dna.count('G')
    count_cg = dna.count('CG')
    
    if count_c == 0 or count_g == 0:
        return 0.0
    return float((count_cg * n) / (count_c * count_g))
