# encoding : utf8
"""controller for the graphic interface"""
from view2 import Application
from model2 import Model

class Controller:
    '''
    Defining the controller class and its methods.
    '''
    def __init__(self):
        '''
        Controller class constructor.
        '''
        self.model = Model("a.txt")
        self.model.read_file()
        self.view = Application(self)
        self.view.view_window()


    def display(self, value):
        """ used to display an animal """
        self.view.display_label(self.model.dico_animaux[value])
    def add_animal(self, dict_animal):
        """used to add an animal to the dictionary """
        self.model.save(dict_animal)
    def delete_animal(self, unwanted_animal):
        """used to delete an animal from the dictionary"""
        self.model.remove_animal(unwanted_animal)
    def modify_animal(self, dict_animal):
        """used to edit or modify an animal in the dict"""
        self.model.edit_animal(dict_animal)
    def get_model_entries(self):
        """ used to get all entries from the model"""
        return self.model.get_attributes()
    def get_animal_list(self):
        """used to get a list of all animals"""
        return self.model.animal_list
    def elements(self, animal):
        """used to get all the animals
        elements from the model"""
        return self.model.elements(animal)
    def quit_window(self):
        """used to quit the window"""
        print("close app")
        self.model.close()
        self.view.destroy()
if __name__ == "__main__":
    C = Controller()
