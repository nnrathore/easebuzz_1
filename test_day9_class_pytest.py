import pytest
import allure

@pytest.fixture()
def login():
    print("this is fixer")

def test_payment(login):
    print("\nthis code is for payment")

def test_Add_beni():
    print("\nthis is for add benificiory")

pytest


allure-pytest



