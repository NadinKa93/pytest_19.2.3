import pytest
from app.calculator import Calculator

class TestCalc: #название класса тестов
    def setup(self): #предварительный метод setup, в котором мы подключаем тестируемый объект Калькулятор
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): #простой тест на проверку правильности умножения
        assert self.calc.multiply(self, 2, 2) == 4

    def test_multiply_failed(self): # намеренное падение теста (failed test)
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self): #простой тест на проверку правильности деления
        assert self.calc.division(self, 6, 3) == 2

    def test_subtraction_calculate_correctly(self): #простой тест на проверку правильности вычитания
        assert self.calc.subtraction(self, 6, 2) == 4

    def test_adding_calculate_correctly(self): #простой тест на проверку правильности сложения
        assert self.calc.adding(self, 6, 1) == 7
