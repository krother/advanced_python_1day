"""
Type hint examples
(Python 3.10+)

1. implementiere die Funktion
"""
from typing import Any, Literal

Fruit = Literal["apple", "pear", "cantaloupe"]
FruitBasket = set[Fruit]
Basket = set[Any]

FruitPrices = dict[Fruit, float]

PRICES: FruitPrices = {
    "apple": 1.23,
    "pear": 4.56,
    "cantaloupe": 7.89,
    "watermelon": 12.34,
}

def calc_total_price(basket: Basket, prices: FruitPrices) -> float:
    ...


basket = {"Apfel", "Cantaloupe"}
print(calc_total_price(...))
