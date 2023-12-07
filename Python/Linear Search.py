def linear_search(search: list, target):
    """
    return index of target being seatced for
    """
    for idx, val in enumerate(search):
        if val == target:
            return idx,

    return None
