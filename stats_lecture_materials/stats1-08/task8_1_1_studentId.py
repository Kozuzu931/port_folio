#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# %% Modules and Libraries
import random

# %% author
__author__ = "Kousuke Tsuchiya"
__studentId__ = "s1f101700158"

# %% DNA class
class DNA(object):
    """
        Represents a DNA sequence (A, T, G, C) 
    """
    def __init__(self, dna):
        super(DNA, self).__init__()
        # define instance variables
        self.org_dna = dna                 # hold the users' DNA sequence
        self.mutated_dna = dna             # hold mutated DNA sequence
        self.org_fre = self.__frequency()  # frequencies of A,C,G,T in original sequence
        self.final_fre = self.__frequency()  # frequencies of A,C,G,T in mutated sequence
        self.mutation_success = 0            # record successful single mutations
        self.length = len(dna)              # the length of DNA sequence
        
    def __str__(self):
        return self.mutated_dna
    
    def __frequency(self): 
        # dictionary comprehension:
        # calculate frequencies of A, C, G, T in the mutated sequence
        # Hint: use an object method provided by class "str" 
        fre = {
            base: 
                self.mutated_dna.count(base)/float(len(self.mutated_dna)) 
            for base in 'ATGC'
        }
        return fre

    def get_base_frequencies(self):
        return self.__frequency()
    
    def mutate(self, pos, mut2base):
        # 1. create a temporary list of the string
        tmp = list(self.mutated_dna)
        # 2. whether the given base at the "pos" position is same as 
        #    the mutated base. If yes, increase one count.
        if tmp[pos] != mut2base:
            self.mutation_success += 1
            # replacement with the given base at "pos" position
            tmp[pos] = mut2base
            # convert the list of string, tmp, to a string
            self.mutated_dna = ''.join(tmp)
            # recalculate the frequences of standard DNA bases
            self.final_fre = self.__frequency()
        

    def get_length(self):
        return self.length
    
    def format_freq(self):
        # List comprehension to generate a string
        return ', '.join(
                [
                    '{}: {:.2f}'.format(base, self.final_fre[base])
                    for base in self.final_fre
                ])

# %% Main 
dna = DNA('ACGGAGATTTCGGTATGCAT')
num_mutations = 10000
print('Starting DNA: {}'.format(dna))
print('{}'.format(dna.format_freq()))
for i in range(num_mutations):
    # get the length of DNA sequence
    l = dna.get_length()
    # A function in module "random" is used to randomly generate 
    # an integer as the position 
    rnd_site = random.randint(0, l-1)
    # A function in module "random" is used to randomly choice one base 
    # from A, T, G, C.
    rnd_base = random.choice(list('ATGC'))
    # Call the object method defined in object dna to simulate 
    # random mutations
    dna.mutate(rnd_site, rnd_base)

print('DNA after {} mutations: {}'.format(num_mutations, dna))
print('{}'.format(dna.format_freq()))
print('{} ({:.2f} %) mutations performed'.format(
        dna.mutation_success, dna.mutation_success/num_mutations*100))