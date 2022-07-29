import pytest
import pytest_ordering
@pytest.mark.run(order=7)
def test_a1(login):
    print("a1")

# B, A, C, E, D, F
@pytest.mark.run(order=2)
def test_run_order_methodA(setUp):
    print("Running method A")

@pytest.mark.run(order=1)
def test_run_order_methodB(setUp):
    print("Running method B")

@pytest.mark.run(order=3)
def test_run_order_methodC(setUp):
    print("Running method C")

@pytest.mark.run(order=5)
def test_run_order_methodD(setUp):
    print("Running method D")

@pytest.mark.run(order=4)
def test_run_order_methodE(setUp):
    print("Running method E")

@pytest.mark.run(order=6)
def test_run_order_methodF(setUp):
    print("Running method F")

