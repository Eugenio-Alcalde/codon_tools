#!/usr/bin/env python3
from codon_tools import SequenceAnalyzer

def test():
    from Bio.Seq import Seq
    from Bio.Alphabet import IUPAC

    sa = SequenceAnalyzer()
    seq = Seq('ATGGTGAGCAAGGGCGAGGAGCTGTTCACCGGGGTGGTGCCCATCCTGGTCGAGCTGGACGGCGACGTAAACGGCCACAAGTTCAGCGTGTCCGGCGAGGGCGAGGGCGATGCCACCTACGGCAAGCTGACCCTGAAGTTCATCTGCACCACCGGCAAGCTGCCCGTGCCCTGGCCCACCCTCGTGACCACCCTGACCTACGGCGTGCAGTGCTTCAGCCGCTACCCCGACCACATGAAGCAGCACGACTTCTTCAAGTCCGCCATGCCCGAAGGCTACGTCCAGGAGCGCACCATCTTCTTCAAGGACGACGGCAACTACAAGACCCGCGCCGAGGTGAAGTTCGAGGGCGACACCCTGGTGAACCGCATCGAGCTGAAGGGCATCGACTTCAAGGAGGACGGCAACATCCTGGGGCACAAGCTGGAGTACAACTACAACAGCCACAACGTCTATATCATGGCCGACAAGCAGAAGAACGGCATCAAGGTGAACTTCAAGATCCGCCACAACATCGAGGACGGCAGCGTGCAGCTCGCCGACCACTACCAGCAGAACACCCCCATCGGCGACGGCCCCGTGCTGCTGCCCGACAACCACTACCTGAGCACCCAGTCCGCCCTGAGCAAAGACCCCAACGAGAAGCGCGATCACATGGTCCTGCTGGAGTTCGTGACCGCCGCCGGGATCACTCTCGGCATGGACGAGCTGTACAAG', IUPAC.unambiguous_dna)

    print("Analyzed sequence: wt GFP")
    print(str(seq))

    m2stop_count = sa.count_muts_to_stop(seq)
    print("\nPossible single-point mutations to a stop codon:", m2stop_count)
    
    CpG_count, UpA_count = sa.count_CpG(seq)
    print("CpG count:", CpG_count, "\nUpA count:", UpA_count)
    
    opt_count, total_count, Fop = sa.calc_Fop(seq, verbosity = 0)
    print("Fraction of optimal codons:", Fop)
    print("(%i optimal sites, %i counted sites)" % (opt_count, total_count))

    print()    
    sa.calc_syn_codon_freqs(seq, verbosity = 2)
    



# when run as its own script, 
if __name__ == "__main__":
    test()
