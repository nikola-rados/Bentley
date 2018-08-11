from index.game import Game
import logging


log = logging.getLogger(__name__)

def test_game_instantiation():
    name = 'The Last of Us: Part 2'
    entry_rank = 2
    g = Game(name, entry_rank)
    assert g.name == name
    assert g.curr_rank == entry_rank
    assert g.top_rank == entry_rank
    assert g.bot_rank == entry_rank
