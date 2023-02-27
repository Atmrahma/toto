# encoding : utf8
"""The view of the graphic interface """
from tkinter import *
from tkinter import messagebox

class Application(Tk):
    """Class for the Tkinter view """
    def __init__(self, controller):
        """Constructor for the Tkinter view"""
        Tk.__init__(self)
        self.geometry("500x700")
        self.minsize(200,300)
        self.title("TP5_inlo")
        self.config(bg= "#D4D4D4", bd=3)
        self.controller = controller
        self.attributes = self.controller.get_model_entries()
        self.animal_list = self.controller.get_animal_list()
        self.creer_widgets()


    def creer_widgets(self):
        """used to create the different widgets of the graphical interface"""
        #Labels
        self.label = Label(self, text="J'adore Python !")
        self.label1 = Label(self, text="")
        self.search_label= Label(self, text="Rechercher")

        #Buttons
        self.display_bouton = Button(self, text="Afficher",bg= "#9B9BCD", command= self.display_something)
        self.add_bouton = Button(self, text="Ajouter",bg= "#9B9BCD", command= self.add_animal_)
        self.delete_bouton = Button(self, text="Supprimer", bg= "#9B9BCD", command= self.delete_animal)
        self.edit_bouton= Button(self, text="Modifier", bg= "#9B9BCD", command= self.elements)
        self.quit_bouton = Button(self, text="Quitter", bg="#9B9BCD", command=self.quit_window)

        #Entries
        self.search = Entry(self)
        self.entries = {}
        self.entries_label = {}
        # associate for each Entry a Label
        for att in self.attributes:
            self.entries[att] = Entry(self)
            self.entries_label[att] = Label(self, text=att)
        #Listbox
        self.listbox= Listbox(self)# animals list box
        position = 0
        for animal1 in self.animal_list:
            position += 1
            self.listbox.insert(position, animal1)

        # the pack is used to display the widgets
        self.label.pack()
        self.label1.pack()
        self.search_label.pack()
        self.search.pack()
        self.listbox.pack()
        self.display_bouton.pack()
        self.delete_bouton.pack()
        # display each entry of the attributes
        for att in self.attributes:
            self.entries_label[att].pack()
            self.entries[att].pack()
        self.add_bouton.pack()
        self.edit_bouton.pack()
        self.quit_bouton.pack()
    def quit_window(self):
        """used to close the window"""
        self.controller.quit_window()

    def display_something(self):
        """Used to display the animal by search"""
        #current_selection = self.listebox.get(self.listebox.curselection())
        #self.controller.display(self.get(current_selection))
        #return self.model.about_animal(current_selection)
        self.controller.display(self.search.get()) # display what the user insert in the search entry
    def display_label(self, value):
        """used to display an animal from the label"""
        self.label1['text'] = value

    def add_animal_(self):
        """
        used to add an animal and delete a previous text
        """
        dict_animal = {} # dictionary contains the animals and their elements
        for key in self.entries:
            dict_animal[key] = self.entries[key].get() # get the key from the entry
        # delete the enries text(key) from the begining to the end
        self.controller.add_animal(dict_animal) # add animal to the dictionary
        self.listbox.insert(END, dict_animal["name"]) # insert at the end of the listbox the animals name

    def delete_animal(self):
        """used to delete an animal from
        the list and from the dictinary"""
        #current_selection = self.listbox.get(ACTIVE)
        #ACTIVE return the currently selected item of the listbox
        #current_selection = self.listbox.get(ACTIVE)
        current_selection = self.listbox.get(self.listbox.curselection())  # get the animals selected
        self.controller.delete_animal(current_selection) # delete the animals selected from the file

        for i in range(self.listbox.size()): # browse the listbox
            if self.listbox.get(i) == current_selection:
                self.listbox.delete(i) # remove the selected one
                messagebox.showinfo(title="Suppression", message="L'animal a été bien supprimé")
    def elements(self):
        """"""
        for key in self.entries:
            self.entries[key].delete(0, END) # delete the content from 0 to the end
        current_selection = self.listbox.get(ACTIVE)
        elem = self.controller.elements(current_selection)
        for att in range(0, len(self.attributes)):
            #inserts the animal's attributes
            self.entries[self.attributes[att]].insert(0,elem[att])


    def view_window(self):
        self.title("Ma Première App :-)")
        self.mainloop()

if __name__ == "__main__":
    app = Application()
    app.view_window()
