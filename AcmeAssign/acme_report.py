#!/usr/bin/env python
from random import randint, sample, uniform
from acme import Product
import random as rand

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
Products = []


def generate_products(num_products=30):
    for num_products in range(num_products):
        prod = rand.choice(ADJECTIVES) + rand.choice(NOUNS)
        Products.append(prod)
    return Products

def inventory_report(Products):
    pass


if __name__ == '__main__':
    inventory_report(generate_products())