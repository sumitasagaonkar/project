from oscar.apps.shipping import methods
from oscar.core import prices
from decimal import Decimal as D

'''class Standard(methods.Base):
    code = 'standard'
    name = 'Shipping eith high speedd'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('5.00'), incl_tax=D('5000.00'))

class Express(methods.Base):
    code = 'express'
    name = 'Shipping (Express)'

    def calculate(self, basket):
        return prices.Price(
            currency=basket.currency,
            excl_tax=D('4.00'), incl_tax=D('4.00'))


'''