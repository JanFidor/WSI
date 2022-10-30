from random import shuffle
import numpy as np
import random
from binary_chromosome import BinaryChromosome

class GeneticAlgorithmMappers():
    def __init__(self, mutation_function, cross_over_function, succession_divider) -> None:
        self.mutation_function = mutation_function
        self.cross_over_function = cross_over_function
        self.succession_divider = succession_divider

class GeneticAlgorithmHyperParameters():
    def __init__(self, mutation_rate, cross_over_rate, population_size, epochs_count, succession_size) -> None:
        self.mutation_rate = mutation_rate
        self.cross_over_rate = cross_over_rate
        self.population_size = population_size
        self.epochs_count = epochs_count
        self.succession_size = succession_size


class GeneticSolver():
    def __init__(self, hyper_parameters) -> None:
        self.hyper_parameters = hyper_parameters
    
    def solve(self, problem, mappers: GeneticAlgorithmMappers):
        population_size = self.hyper_parameters.population_size
        population = [BinaryChromosome(problem.input_size) for _ in range(population_size)]

        epochs_count = self.hyper_parameters.epochs_count
        for _ in range(epochs_count):
            population = self.new_population(population, problem.evaluate, mappers)
        
        winners_with_score = [(winner, problem.evaluate(winner.genes)) for winner in population]
        return max(winners_with_score, key=lambda x: x[1])[0]


    def new_population(self, population, fitness_function, mappers: GeneticAlgorithmMappers):
        winners_size = self.hyper_parameters.succession_size
        fitness_values = [fitness_function(chr.genes) for chr in population]

        loosers, winners = mappers.succession_divider(population, fitness_values, winners_size)
        cross_over_loosers = self.cross_over_population(loosers, mappers)
        new_chromosomes = self.mutated_population(cross_over_loosers, mappers)
        return new_chromosomes + winners

    def cross_over_population(self, population, mappers: GeneticAlgorithmMappers):
        random.shuffle(population)
        random_pairs =  [population[i*2:i*2 + 2] for i in range(len(population) // 2)]
        cross_over_pairs = [self.cross_over_pair(pair, mappers) for pair in random_pairs]
        a =  [item for sublist in cross_over_pairs for item in sublist]
        return a

    def cross_over_pair(self, pair, mappers: GeneticAlgorithmMappers):
        assert(len(pair) == 2)
        genes = [chr.genes for chr in pair]
        probability = self.hyper_parameters.cross_over_rate
        new_genes = mappers.cross_over_function(genes, probability)
        return [chr.copy(new_genom) for chr, new_genom in zip(pair, new_genes)]

    def mutated_population(self, population, mappers: GeneticAlgorithmMappers):
        probability = self.hyper_parameters.mutation_rate
        new_genes = [mappers.mutation_function(chromosome.genes, probability) for chromosome in population]
        return [chr.copy(genes) for chr, genes in zip(population, new_genes)]

