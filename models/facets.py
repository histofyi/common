from common.providers import s3Provider, awsKeyProvider
from .data import FacetClass

import logging

class Core(FacetClass):
    def __init__(self, aws_config=None):
        super().__init__(self.__class__.__name__, 'core', aws_config)


class PeptideNeighbours(FacetClass):
    def __init__(self, aws_config=None):
        super().__init__(self.__class__.__name__, 'peptide_neighbours', aws_config)

    
class PeptideAngles(FacetClass):
    def __init__(self, aws_config=None):
        super().__init__(self.__class__.__name__, 'peptide_angles', aws_config)


class AlleleMatch(FacetClass):
    def __init__(self, aws_config=None):
        super().__init__(self.__class__.__name__, 'allele_match', aws_config)
