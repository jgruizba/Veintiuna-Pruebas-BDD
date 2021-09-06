from veintiuna import *

repartidor = Repartidor()

# prueba para el inicio del juego con el repartidor
# resultado 2 cartas en la mano
def test_nueva_mano():
  repartidor.nueva_mano()
  assert len(repartidor.mano) == 2

def test_tiene_as_verdadero():
  repartidor.mano = [('A', 'Treboles'), ('J', 'Picas')]
  assert repartidor.tiene_as() == True

def test_tiene_as_falso():
  repartidor.mano = [('5', 'Treboles'), ('J', 'Picas')]
  assert repartidor.tiene_as() == False

def test_valor_carta_figura():
  carta = ('J', 'Picas')
  assert repartidor.valor_carta(carta) == 10

def test_valor_carta_numerica():
  carta = ('4', 'Picas')
  assert repartidor.valor_carta(carta) == 4

def test_valor_mano_veintiuna():
  repartidor.mano = [('A', 'Treboles'), ('J', 'Picas')]
  assert repartidor.sumar_mano() == 21

def test_jugada_valor_igual():
    valor_mano = 10
    valor_mano_jugador = 10
    assert repartidor.decidir_jugada(valor_mano, valor_mano_jugador) == 'planto'

def test_jugada_valor_menor():
    valor_mano = 10
    valor_mano_jugador = 21
    assert repartidor.decidir_jugada(valor_mano, valor_mano_jugador) == 'juego'

def test_jugada_valor_mayor():
    valor_mano = 20
    valor_mano_jugador = 16
    assert repartidor.decidir_jugada(valor_mano, valor_mano_jugador) == 'planto'

def test_jugada_veintiuna_planto():
    valor_mano = 21
    valor_mano_jugador = 19
    assert repartidor.decidir_jugada(valor_mano, valor_mano_jugador) == 'planto'

def test_jugada_veintiuna_juego():
    valor_mano = 19
    valor_mano_jugador = 21
    assert repartidor.decidir_jugada(valor_mano, valor_mano_jugador) == 'juego'

def test_jugador_por_encima():
    valor_mano = 8
    valor_mano_jugador = 22
    assert repartidor.decidir_jugada(valor_mano, valor_mano_jugador) == 'planto'

def test_repartidor_por_encima():
    valor_mano = 22
    valor_mano_jugador = 21
    assert repartidor.decidir_jugada(valor_mano, valor_mano_jugador) == 'planto'
