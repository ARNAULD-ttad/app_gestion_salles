class Salle:

    def __init__(self, code, description, categorie, capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite

    def afficher_infos(self):
        print("==================================")
        print(f"Code        : {self.code}")
        print(f"Description : {self.description}")
        print(f"Catégorie   : {self.categorie}")
        print(f"Capacité    : {self.capacite}")
        print("==================================")