import genetic_solver as gen
from problem import Problem
import random as rand
import numpy.random as npr

def main():
    change_mutation_and_Crossover()

def change_mutation_and_Crossover():
    mutations = [0.05, 0.1, 0.15, 0.2, 0.25]
    cross_overs = [0.1, 0.15, 0.2, 0.25, 0.3]

    for mutation in mutations:
        for cross_over in cross_overs:
            problem = Problem(200)
            mappers = gen.GeneticAlgorithmMappers(
                mutation_func,
                cross_over_func,
                succession_divider
            )
            params = gen.GeneticAlgorithmHyperParameters(mutation, cross_over, 100, 100, 10)
            print(mutation, cross_over, winning_solution_value(problem, mappers, params))

def winning_solution_value(problem, mappers, params):
    solver = gen.GeneticSolver(params)
    solutions = [solver.solve(problem, mappers) for _ in range(25)]
    return round(sum([solutions]) / 25, 2)

def cross_over_func(genes_pair, probability):
    if rand.random() < probability:
        cross_over_point = rand.randint(0, len(genes_pair[0]))
        return ["".join(genes_pair[i][:cross_over_point] + genes_pair[1 - i][cross_over_point:]) for i in range(2)]
    return genes_pair

def mutation_func(genes, probability):
    if rand.random() < probability:
        gene_index = rand.randint(0, len(genes) - 1)
        mutable_genes = list(genes)
        mutable_genes[gene_index] = str(1 - int(mutable_genes[gene_index]))
        return "".join(mutable_genes)
    return genes

def succession_divider(population, fitness_values, winners_size):
    mn = min(fitness_values)
    adjusted_fitness = [fitness + abs(mn)*1.001 for fitness in fitness_values]

    mx = sum(adjusted_fitness)

    selection_probs = [fitness/mx for fitness in adjusted_fitness]
    winners_ids = npr.choice(len(population), winners_size, p=selection_probs, replace=False)
    loosers, winners = [], []
    for id in range(len(population)): (loosers, winners)[id in winners_ids].append(id)
    return [population[id] for id in loosers], [population[id] for id in winners]

main()