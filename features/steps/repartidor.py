from behave import *
from veintiuna import *

@given('un repartidor')
def step_imp(context):
  context.repartidor = Repartidor()

@when('el juego inicia')
def step_imp(context):
  context.repartidor.nueva_mano()

@then('el repartidor toma dos cartas')
def step_imp(context):
  assert len(context.repartidor.mano) == 2

@given('una {mano}')
def step_imp(context, mano):
  context.repartidor = Repartidor()
  context.repartidor.mano = [(x, 'Diamantes') for x in mano.split(',')]

@when('el repartidor sume las cartas')
def step_imp(context):
  context.valor_mano = context.repartidor.sumar_mano()

@then('el {valor:d} es correcto')
def step_imp(context, valor):
  assert context.valor_mano == valor

  # Escenario que determina la jugada del repartidor a partir de la jugada del jugador
@Given('los totales de las manos del {repartidor:d} y {jugador:d}')
def step_imp(context, jugador, repartidor):
    context.repartidor = Repartidor()
    context.valor_mano = repartidor
    context.valor_mano_jugador = jugador

@When('el repartidor determina la jugada')
def step_imp(context):
    context.jugada = context.repartidor.decidir_jugada(context.valor_mano, context.valor_mano_jugador)

@Then('la {jugada} es correcta')
def step_imp(context, jugada):
    assert context.jugada == jugada