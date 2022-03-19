from src.Character import character


class Game:
    player = character("default character", "default desc", 100)

    def setPlayer(self, player):
        self.player = player

    def getPlayer(self):
        return self.player