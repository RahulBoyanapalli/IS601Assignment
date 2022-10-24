import pytest
import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests  is in the same folder as the IcecreamMachine stuff
from IcecreamMachine import IceCreamMachine
#this is an example test showing  to cascade fixtures to build up state
#test file
@pytest.fixture
def machine():
    icm = IceCreamMachine()
    return icm
@pytest.fixture
def first_order(machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine
@pytest.fixture
def second_order(first_order, machine):
    machine.handle_container("cup")
    machine.handle_flavor("vanilla")
    machine.handle_flavor("next")
    machine.handle_toppings("done")
    machine.handle_pay(10000,"10000")
    return machine

def test_production_line(second_order):
    assert second_order is not None
#na