from datetime import datetime

class Game(object):
    """ Game object which contains statistics to track movement in List
    """
    def __init__(self, name, entry_rank):
        self.name = name
        self.curr_rank = entry_rank
        self.top_rank = entry_rank
        self.bot_rank = entry_rank
        self.entry_date = datetime.now()
        self.exit_date = None
        self.climbs = 0
        self.falls = 0
        self.total_mov = 0
        self.achievements = []
        self.records = []

    def retire(self):
        print('Game: {}'.format(self.name))
