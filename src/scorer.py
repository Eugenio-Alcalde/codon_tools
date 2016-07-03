from .sequence_analyzer import SequenceAnalyzer
from .lookup_tables import opt_codons_E_coli

class StopAndCpGScorer:
    """Scores sequences based on the number of possible mutations to stop codons, number of CpGs, and number of UpAs. In the constructor, it is possible to set the relative weight of these three counts, including setting some of them to zero.
"""
    def __init__(self, m2stop_coef, CpG_coef, UpA_coef):
        self.sa = SequenceAnalyzer()
        self.m2stop_coef = m2stop_coef
        self.CpG_coef = CpG_coef
        self.UpA_coef = UpA_coef

    def calc_score_components(self, seq):
        m2stop_count = self.sa.count_muts_to_stop(seq)
        CpG_count, UpA_count = self.sa.count_CpG(seq)
        return m2stop_count, CpG_count, UpA_count

    def score(self, seq):
        m2stop_count, CpG_count, UpA_count = self.calc_score_components(seq)
        return self.m2stop_coef*m2stop_count + self.CpG_coef*CpG_count + self.UpA_coef*UpA_count


class FopScorer:
    """Scores sequences based on the fraction of optimal codons. By default, uses the E. coli optimal codons from Zhou et al. 2009. A different set of optimal codons can be specified in the constructor.
"""
    def __init__(self, opt_codons = opt_codons_E_coli):
        self.sa = SequenceAnalyzer()
        self.opt_codons = opt_codons

    def score(self, seq):
        opt_count, total_count, Fop = self.sa.calc_Fop(seq, self.opt_codons)
        return Fop