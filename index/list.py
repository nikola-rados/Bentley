class index(object):
    """ The actual structured list containing game objects

        List has to track the movement of items within the list.
    """

    def __init__(self):
        def _config_index(fname):
            """ Use config file to set up starting list
            """
            with open(fname, "r") as f:
                for line in f.readlines():
                    print(i)
