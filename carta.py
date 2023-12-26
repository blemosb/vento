class Carta:
    pass

class CartaAlagamento(Carta):
    def __init__(self, nome):
        self.nome = nome

class CartaTesouro(Carta):
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome

class CartaEnchente(Carta):
    def __repr__(self):
        return "   CARTA ENCHENTE 💦"

class CartaHelicoptero(Carta):
    def __repr__(self):
        return " CARTA HELICOPTERO 🚁"

class CartaSacoAreia(Carta):
    def __repr__(self):
        return "CARTA SACO DE AREIA💰"

class CartaCoringa(Carta):
    def __repr__(self):
        return "   CARTA CORINGA🃏  "
