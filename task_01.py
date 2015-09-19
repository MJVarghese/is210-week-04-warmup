#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """This creates a string that uses 2 arguments with a different variable.

    Args:
        wink (str):  Individual that is being winked to.
        numwink (int, optional): Total number of winks and nudges. Default: 2

    Returns:

        str: All arguments folded into a single sentence.

    Examples:

        >>>know_what_i_mean('Vince')
        'Know what I mean? VinceVince, nudge nudge'

        >>>know_what_i_mean('Lincoln', 3)
        'Know what I mean? LincolnLincolnLincoln, nudge nudge nudge'

    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
