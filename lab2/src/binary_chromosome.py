import random as rand
class BinaryChromosome:
    def __init__(self , length):
        self.length = length
        self.genes = self.generate_genes(length)

    def generate_genes(self, length):
        return ''.join([str(rand.randint(0, 1)) for _ in range(length)])

    def copy(self, new_genes):
        new_chromosome =  BinaryChromosome(self.length)
        new_chromosome.genes = new_genes
        return new_chromosome
    