import math
import random

import numpy as np

import constants

MIN_UNIT_VALUE = 100
POPULATION_SIZE = 100

STOCK_MAX_ITEMS = 5

STOCK_VOLATIBILITY_VALUE = 0
STOCK_PROVENTS_VALUE = 3
STOCK_APPRECIATION_VALUE = 0

STOCK_RATIO = 0.6

FII_MAX_ITEMS = 4
FII_VOLATIBILITY_VALUE = 3
FII_PROVENTS_VALUE = 3
FII_PVPA_VALUE = 3
FII_APPRECIATION_VALUE = 3

ELITE_RATIO = 0.5
MAX_STATES = 100


def simulate(total_investment):
    running = True

    population = create_population(total_investment, POPULATION_SIZE, MIN_UNIT_VALUE)

    state = 0

    while running and state < MAX_STATES:

        population = evolve_population(population)

        state += 1

    show_final_result(population[0])


def create_population(total_investment, population_size, min_unit_value):

    population = []

    for _ in range(population_size):
        # current_invested = 0
        current_population = []

        # find used investments
        used_code_stocks = set()

        while len(used_code_stocks) < STOCK_MAX_ITEMS:
            stock = random.choice(constants.STOCKS)

            if stock["code"] not in used_code_stocks:
                used_code_stocks.add(stock["code"])
                current_population.append(stock)

        # while current_invested < total_investment - min_unit_value:
        #     stock = get_random_stock(used_stocks)
        #     current_invested += stock["price"] * num_stocks
        #     current_population.append((stock, num_stocks))

        population.append(current_population)

    return population


def show_final_result(lista):
    print("Final result:")
    for _ in lista:
        print(_["code"])
    # quantidades_totais = {}

    # # Itera sobre a lista e acumula as quantidades
    # for investimento, quantidade in lista:
    #     nome = investimento["name"]
    #     if nome in quantidades_totais:
    #         quantidades_totais[nome]["quantidade"] += quantidade
    #     else:
    #         quantidades_totais[nome] = {
    #             "investimento": investimento,
    #             "quantidade": quantidade,
    #         }

    # # Converte o dicionário de volta para uma lista de tuplas
    # resultado = [
    #     (v["investimento"], v["quantidade"]) for v in quantidades_totais.values()
    # ]

    # for investimento, quantidade in resultado:
    #     print(
    #         investimento["name"], quantidade, "R$", investimento["price"] * quantidade
    #     )
    # print(resultado)


# def get_random_stock(used_stocks):
#     stock = ""
#     while stock == "":
#         s = random.choice(constants.STOCKS)
#         if s["code"] in used_stocks:
#             stock = s

#     # num_stocks = math.floor(100 / stock["price"])

#     return stock
#     # return stock, 1 if num_stocks < 1 else num_stocks


def evolve_population(population):

    # for _ in population:
    #     print(len(_))

    fitness_values = [calc_fitness(c) for c in population]

    # print(fitness_values)

    # Obtém a elite da população
    elite_index = np.argsort(fitness_values)[: int(len(population) * ELITE_RATIO)]
    elites = [population[i] for i in elite_index[::-1]]

    # first = elites[0][0]
    print("---")
    print(elites[0][0])

    new_population = []

    while len(new_population) < len(population) - len(elites):
        parent1, parent2 = random.choices(elites, k=2)

        child = [()] * len(parent1)

        for i in range(len(parent1)):
            # print(i)
            # print("parent1: ", len(parent1))
            # print("parent2: ", len(parent2))
            if random.random() < 0.5:
                child[i] = parent1[i]
            else:
                child[i] = parent2[i]

        new_population.append(child)

    return elites + new_population


def calc_fitness(investments):

    print("=============")

    total_value = 0
    for i in investments:
        if i["type"] == "stock":
            # volatility: less is better
            volatility = ((100 - i["volatility"]) / 100) * STOCK_VOLATIBILITY_VALUE
            # provents: more is better
            provents = (i["dy"] / 100) * STOCK_PROVENTS_VALUE
            # appreciation: more is better
            appreciation = (i["appreciation"] / 100) * STOCK_APPRECIATION_VALUE

            # print(i[0]["appreciation"])
            # print(volatility, provents, appreciation, " - ", i["code"])

            print(i["code"], (volatility + provents + appreciation))

            total_value += (
                volatility
                + provents
                + appreciation
                # volatility + provents + appreciation * ((i[0]["price"] * i[1]) / 10)
            )

    print("Total", total_value)
    print("=============")

    return total_value
