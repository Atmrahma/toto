from Animal2 import *

class Model():
    """A class to stock information about the animal class files"""
    def __init__(self, filename):
        self.filename = filename
        self.file=open(self.filename, "r+",encoding="utf-8")
        self.dico_animaux = {}
        self.animal_list = []

    def read_file(self):
        """used to read the file"""
        for line in self.file:
            line = line.strip() #remove the \n
            tab = line.split(",") #split with separate by ,
            ani_mal = Animal(tab[0],tab[1],tab[2],tab[3],tab[4])
            self.dico_animaux[ani_mal.name] = ani_mal
            self.animal_list.append(ani_mal.name)
            #print(self.dico_animaux)

    def save(self, dict_animal):
        """used to add an animal to the file"""
        self.file = open(self.filename, "r+", encoding="utf-8")
        self.read_file() #use the methode read_file()
        self.file.write("\n"+dict_animal["species"] + "," + dict_animal["age"]
                        + "," + dict_animal["diet"] + "," + dict_animal["foot"]
                        + "," + dict_animal["name"])
        self.file.close() #we have to close every opened file

    def remove_animal(self, unwanted_animal):
        """used to delete an animal from the file"""
        del self.dico_animaux[unwanted_animal]

        self.file.seek(0)#envoyer le cursseur au début de fichier
        file_handler = self.file.readlines() #read all the file line by line
        self.file.seek(0)
        self.file.truncate()
        for line in file_handler:
            separated_line= line.strip("\n").split(",")
            if separated_line[-1] != unwanted_animal:
                self.file.write(line)
        self.file.close()

    def edit_animal(self, dict_animal):
        """used to modify the animal"""
        self.remove_animal(dict_animal["name"]) # delete the current animal
        self.file= open(self.filename, "r+")
        self.file.seek(0)
        self.read_file()
        self.file.write("\n"+ dict_animal["species"] + "," + dict_animal["age"]
                                + "," + dict_animal["diet"] + "," + dict_animal["foot"]
                                + "," + dict_animal["name"])
        self.save(dict_animal)
        self.file.close()

    def close(self):
        """to close the opened file"""
        self.file.close()

    def get_attributes(self)-> []:
        """get attributes of the Animal class"""
        attr = []
        first_key = next(iter(self.dico_animaux)) # get first key of the dict
        for key in self.dico_animaux[first_key].__dict__:
            attr.append(key)
        return attr

    def elements(self, animal):
        """used to give separated information about the animal selected"""
        self.file.seek(0)
        for line in self.file:
            if animal in line:
                line = line.strip("\n").split(",")
                return line

if __name__ == "__main__":

    path= "a.txt"
    model = Model(path)
    model.read_file()
    print(model.dico_animaux["Sonia"])
    print("12345678")
    model.close()