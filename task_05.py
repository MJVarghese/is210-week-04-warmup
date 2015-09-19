#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that has a default"""


def defaults(my_required, my_optional=True):
    """This compares the truthfullness of 2 arguments.

    Args:
        my_required (bool):
        my_optional (bool, optional): Default is True

    Returns:
        Whether boolean are identical.

        Examples:
        >>> defaults(True)
        True
        >>> defaults(True, False)
        False
        >>> defaults(False, False)
        True

    """
    return my_optional is my_required
