from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

print("\n===== TEST 1 : CONNEXION =====")
conn = dao.get_connection()
if conn and conn.is_connected():
    print("Connexion à MySQL réussie")
    conn.close()
else:
    print("Échec de connexion à MySQL")

print("\n===== TEST 2 : AJOUT =====")
s1 = Salle("A101", "Salle informatique", "Laboratoire", 30)
dao.insert_salle(s1)
print("Salle A101 ajoutée")

print("\n===== TEST 3 : RECHERCHE =====")
salle = dao.get_salle("A101")
if salle:
    print("Salle trouvée :")
    salle.afficher_infos()
else:
    print("Salle non trouvée")

print("\n===== TEST 4 : MODIFICATION =====")
s1.description = "Labo Python modifié"
s1.capacite = 35
dao.update_salle(s1)
print("Salle A101 modifiée")

salle_modifiee = dao.get_salle("A101")
if salle_modifiee:
    salle_modifiee.afficher_infos()

print("\n===== TEST 5 : TOUTES LES SALLES =====")
toutes = dao.get_salles()
print(f"Nombre de salles : {len(toutes)}")
for s in toutes:
    s.afficher_infos()

print("\n===== TEST 6 : SUPPRESSION =====")
dao.delete_salle("A101")
print("Salle A101 supprimée")

verification = dao.get_salle("A101")
if verification is None:
    print("Confirmation : la salle n'existe plus")
else:
    print("Erreur : la salle existe encore")
