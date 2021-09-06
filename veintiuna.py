from random import choice
_valores = [str(v) for v in range(2, 11)] + ['A', 'J', 'Q', 'K']
_pintas = ['Corazones', 'Diamantes', 'Treboles', 'Picas']
_cartas = [(v, p) for v in _valores for p in _pintas]


class Repartidor:
  def __init__(self):
    self.mano = []

  def nueva_mano(self):
    self.mano = [choice(_cartas), choice(_cartas)]

  def tiene_as(self):
    for c in self.mano:
      if c[0] == 'A':
        return True
    return False

  def sumar_mano(self):
    valor = 0
    for c in sorted(self.mano):
      carta = self.valor_carta(c)
      if carta == 11 and (valor + carta) > 21:
        carta = 1
      valor += carta
    return valor

  def valor_carta(self, carta):
    if carta[0] in ['J', 'Q', 'K']:
      return 10
    elif carta[0] == 'A':
      return 11
    else:
      return int(carta[0])

  def decidir_jugada(self, mi_mano, mano_jug):
        jugada = 'planto'
        if mi_mano < 21 and mano_jug <= 21:
          if mano_jug > mi_mano:
            jugada = 'juego'
        
        return jugada