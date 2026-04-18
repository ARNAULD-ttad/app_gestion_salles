import json
import mysql.connector
from mysql.connector import Error
from models.salle import Salle


class DataSalle:

    def get_connection(self):
        try:
            with open("data/config.json", "r") as fichier:
                config = json.load(fichier)

            return mysql.connector.connect(
                host=config["host"],
                user=config["user"],
                password=config["password"],
                database=config["database"]
            )
        except Error as e:
            print("Erreur de connexion MySQL :", e)
            return None

    def insert_salle(self, salle):
        conn = self.get_connection()
        if conn is None:
            return

        try:
            curseur = conn.cursor()
            sql = """
                INSERT INTO salle (code, description, categorie, capacite)
                VALUES (%s, %s, %s, %s)
            """
            curseur.execute(sql, (
                salle.code,
                salle.description,
                salle.categorie,
                salle.capacite
            ))
            conn.commit()
        finally:
            conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        if conn is None:
            return

        try:
            curseur = conn.cursor()
            sql = """
                UPDATE salle 
                SET description=%s, categorie=%s, capacite=%s
                WHERE code=%s
            """
            curseur.execute(sql, (
                salle.description,
                salle.categorie,
                salle.capacite,
                salle.code
            ))
            conn.commit()
        finally:
            conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        if conn is None:
            return

        try:
            curseur = conn.cursor()
            sql = "DELETE FROM salle WHERE code=%s"
            curseur.execute(sql, (code,))
            conn.commit()
        finally:
            conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        if conn is None:
            return None

        try:
            curseur = conn.cursor(dictionary=True)
            sql = "SELECT * FROM salle WHERE code=%s"
            curseur.execute(sql, (code,))
            ligne = curseur.fetchone()

            if ligne:
                return Salle(
                    ligne["code"],
                    ligne["description"],
                    ligne["categorie"],
                    ligne["capacite"]
                )
            return None
        finally:
            conn.close()

    def get_salles(self):
        conn = self.get_connection()
        if conn is None:
            return []

        try:
            curseur = conn.cursor(dictionary=True)
            curseur.execute("SELECT * FROM salle")
            lignes = curseur.fetchall()

            return [
                Salle(
                    l["code"],
                    l["description"],
                    l["categorie"],
                    l["capacite"]
                )
                for l in lignes
            ]
        finally:
            conn.close()
