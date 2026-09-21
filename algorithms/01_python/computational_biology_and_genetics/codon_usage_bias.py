"""
Relative Synonymous Codon Usage (RSCU) Calculation.
Reference: Campbell Biology (12th Ed.), Ch. 17 (From Gene to Protein); Sharp & Li (1987).
"""
from collections import Counter
from typing import Dict

def compute_rscu(cds_sequence: str, codon_family_map: Dict[str, str]) -> Dict[str, float]:
    """
    RSCU_i = (X_i * n) / sum_j^n X_j where n is the number of synonymous codons.
    """
    codons = [cds_sequence[i:i+3].upper() for i in range(0, len(cds_sequence)-2, 3)]
    counts = Counter(codons)
    rscu = {}
    
    # Invert family map: aa -> list of codons
    aa_to_codons = {}
    for cod, aa in codon_family_map.items():
        aa_to_codons.setdefault(aa, []).append(cod)
        
    for aa, family in aa_to_codons.items():
        total = sum(counts.get(c, 0) for c in family)
        n = len(family)
        for c in family:
            if total > 0:
                rscu[c] = (counts.get(c, 0) * n) / total
            else:
                rscu[c] = 1.0
    return rscu
