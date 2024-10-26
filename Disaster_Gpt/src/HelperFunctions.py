"""Helper functions which assist in implementing toTwilio. """

# TODO: fill in natural disasters and what to do for each
def situation_message(naturalDisaster) -> str:
    """
    Function that outputs a list of precautions to take in an event of a specific natural disaster.
    :param naturalDisaster:
    :return:
    """
    if naturalDisaster == "hurricane":
        return "What to do in event of flood"
    elif naturalDisaster == "flood":
        return "WhWhat to do in event of flood"
    elif naturalDisaster == "blizzard":
        return ""
    elif naturalDisaster == "earthquake":
        return ""
    elif naturalDisaster == "landslide":
        return ""
