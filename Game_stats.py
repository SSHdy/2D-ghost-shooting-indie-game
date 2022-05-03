class Gamestats():
    def __init__(self):
        self.speed_factor=5.0
        self.lives_cap=4
        self.lossthegame=False
        self.winthegame=False
        self.pausethegame=False
        self.reset()
    def reset(self):
        self.lives_left=self.lives_cap
# all the game status
        