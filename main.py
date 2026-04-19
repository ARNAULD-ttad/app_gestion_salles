from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

print("\n===== TEST 1 : AJOUT VALIDE =====")
s1 = Salle("B202", "Classe générale", "Cours", 40)
ok, msg = service.ajouter_salle(s1)
print(msg)

print("\n===== TEST 2 : AJOUT INVALIDE (capacité = 0) =====")
s_invalide = Salle("X999", "Test", "Test", 0)
ok, msg = service.ajouter_salle(s_invalide)
print(msg)

print("\n===== TEST 3 : AJOUT INVALIDE (champ vide) =====")
s_vide = Salle("", "Test", "Test", 20)
ok, msg = service.ajouter_salle(s_vide)
print(msg)

print("\n===== TEST 4 : LISTE DES SALLES =====")
salles = service.recuperer_salles()
print(f"✅ Nombre de salles : {len(salles)}")
for s in salles:
    s.afficher_infos()

print("\n===== TEST 5 : MODIFICATION =====")
s1.description = "Classe modifiée"
s1.capacite = 45
ok, msg = service.modifier_salle(s1)
print("\n===== TEST 6 : RECHERCHE =====")
salle = service.rechercher_salle("B202")
if salle:
    print("✅ Salle trouvée :")
    salle.afficher_infos()

print("\n===== TEST 7 : SUPPRESSION =====")
service.supprimer_salle("B202")
print("✅ Salle B202 supprimée")
verification = service.rechercher_salle("B202")
if verification is None:
    print("✅ Confirmation : salle supprimée avec succès")