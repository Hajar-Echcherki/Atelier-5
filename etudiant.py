class etudiant :
    def __init__(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne
 #list de type etudiant        
etudiant = [
{'nom' : 'abasi','prenom' : 'iman', 'age': 25,'cne': 90822223, 'moyenne': 14},
{'nom' : 'alam','prenom' : 'oumaima', 'age': 30,'cne': 67938923, 'moyenne': 16},
{'nom': 'laalam','prenom' : 'assia', 'age': 18,'cne': 2838933, 'moyenne': 9},
{'nom' : 'tyma','prenom' : 'siham', 'age': 40,'cne': 4342223, 'moyenne': 18},
]

#trie par age
etudiant.sort(key=lambda x: x.get('age'))
print(etudiant)
#trie par moyenne
etudiant.sort(key=lambda x: x.get('moyenne'))
print(etudiant)



