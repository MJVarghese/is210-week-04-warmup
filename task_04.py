#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Is there enough good and litterboxes for the kittens?"""


def too_many_kittens(kittens, litterboxes, catfood):
    """Checs if there are enough food & boxes for the kittens.

    Args:
        kittens (int): The number of kittens.
        litterboxes (int): The availability of litterboxes.
        catfood (bool): True = enough food. False = there isn't enough.

    Returns:
        Boolean. True or False, stating if there are too many kittens.

    Examples:

        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False

    """
    return not (litterboxes >= kittens and catfood)
