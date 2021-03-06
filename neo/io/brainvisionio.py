# -*- coding: utf-8 -*-

from neo.io.basefromrawio import BaseFromRaw
from neo.rawio.brainvisionrawio import BrainVisionRawIO


class BrainVisionIO(BrainVisionRawIO, BaseFromRaw):
    _prefered_signal_group_mode = 'split-all'

    def __init__(self, filename):
        BrainVisionRawIO.__init__(self, filename=filename)
        BaseFromRaw.__init__(self, filename)
