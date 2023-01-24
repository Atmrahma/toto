#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import gc 
"""This module provides an interface to the optional garbage collector"""
class Animal: 
    def __init__(self, name, species, paws, diet, mother) -> None:
        self.name = name
        self.species = species
        self.paws = paws
        self.diet = diet
        self.mother = mother
        self.children = []
        self.parents = [mother]
        self.ans = get_mother(mother)

    def get_grand_childen(self):
        """get a child of child of animal"""
        children1 = self.children # list of children
        children2 = ""
        for child in children1[:-1]:
            # for each child from all children
            for _ in gc.get_objects():
                # search in garbage collector
                if isinstance(_, Animal):
                    # if _ repsent an instance of animal class
                    if child in _.name:
                        # search for a child in all names variables
                        children2=children2+", ".join(_.children)
                        # join to the children of children the child
        return f"Children of the G1 are: {children1}, children of G2 are: {children2}"

    def add_child(self, name):
        """add a child to an animal"""
        child = Animal(name, self.species, self.paws, self.diet, self.name)
        self.children.append(name)
        

    def remove_child(self, name):
        """remove a child to an animal"""
        child = Animal(name, self.species, self.paws, self.diet, self.name)
        self.children.remove(name)

    def get_children(self):
        """get children of an animal"""
        nb_children = len(self.children) # get a number of children
        if nb_children > 1:
            # in case of animal has more than one child
            return f" has {len(self.children)} children : {self.children}"
        elif nb_children == 1:
            return f" has only one child : {self.children}"
        else:
            return f" has no children"

    def __str__(self) -> str:
        """what we want to print when we run this script"""
        return f" The {self.species} {self.name} son of {self.mother}" + self.get_children()

def get_mother(child):
    """get a mother of an animal"""
    for element in gc.get_objects():
        if isinstance(element, Animal):
            # check if element is an instance of Animal class
            if child in element.children:
                # search for child in the childrens list 
                return element.name
            # we only need the name of child
            elif child in element.name:
                # we get a mother of the child
                return element.mother

class Cow(Animal):
    """Cow inherits from animal class"""
    def __init__(self, name, species, paws, diet, mother)-> None:
        # the cow class inherits all arg from Animal class
        super().__init__(name, species, paws, diet, mother)
if __name__ == "__main__":
    animal1 = Animal("Grey", "persan", 4, "carnivore", "Coco")
    animal2 = Animal("Sugar", "siamois", 4, "carnivore", "Loulou")
    
    animal1.add_child("King") # add a child "King" to an animal1
    animal1.add_child("Ice")
    animal1.add_child("Cute")
    
    #animal1.remove_child("Cute")
    
    chaton1 = Animal("Ice", "Persan", 4, "carnivore", "Grey")
    chaton1.add_child("Rafi")
    
    print(animal1.children) # list of children
    print(animal1.get_grand_childen()) # children of children of animal
    print(get_mother("King")) # mother of child "X"
    print(animal1)
    
    vache= Cow("jiji", "Charolaise", 4, "Herbivore", "Doll")
    vache.add_child("Caramel")
    print(vache.children) # get a children of the cow "jiji" 