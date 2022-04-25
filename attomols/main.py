"""
ATtoMols's main module.
"""


def can_atoms_single_bond(at0, at1):
    """
    Check whether two atoms can single bond, return True or False.
    """
    if 1 in at0.single and 1 in at1.single:
        return True
    return False






