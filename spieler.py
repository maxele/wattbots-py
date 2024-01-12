class Spieler():
    gespielte_karten = []
    karten = []
    punkte = [0, 0]
    stiche = [0, 0]

    def __init__(self, index):
        self.index = index

    def __str__(self):
        return f"Spieler-{self.index} {self.karten} (DefaultSpieler)"

    def __repr__(self):
        return self.__str__()

    def add_gespielte_karten(self, l):
        for k in l:
            self.gespielte_karten.append(k)

    def reset_gespielte_karten(self):
        self.gespielte_karten = []

    def update(self, punkte, stiche):
        self.punkte = punkte
        self.stiche = stiche

    def set_karten(self, k):
        self.karten = k

    def set_logik(self, logik):
        self.logik = logik

    def unsogn(self, trumpf):
        return self.karten[-1]

    def ausspielen(self, runde):
        return self.karten.pop()

    def hebn(self):
        return False

    def schianore(self):
        return False

    def schlogtausch(self):
        return False
