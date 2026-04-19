import customtkinter as ctk
from tkinter import ttk, messagebox
from models.salle import Salle
from services.services_salle import ServiceSalle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("680x650")
        self.resizable(False, False)

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.service_salle = ServiceSalle()

        self._construire_cadre_infos()
        self._construire_cadre_actions()
        self._construire_cadre_liste()

        self.lister_salles()

    def _construire_cadre_infos(self):

        self.cadreInfos = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfos.pack(pady=10, padx=20, fill="x")

        ctk.CTkLabel(
            self.cadreInfos,
            text="Informations de la salle",
            font=("Arial", 14, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=10)

        ctk.CTkLabel(
            self.cadreInfos,
            text="Code :",
            font=("Arial", 12)
        ).grid(row=1, column=0, padx=20, pady=8, sticky="e")

        self.entry_code = ctk.CTkEntry(
            self.cadreInfos,
            width=250,
            placeholder_text="Ex: A101"
        )
        self.entry_code.grid(row=1, column=1, padx=20, pady=8)

        ctk.CTkLabel(
            self.cadreInfos,
            text="Description :",
            font=("Arial", 12)
        ).grid(row=2, column=0, padx=20, pady=8, sticky="e")

        self.entry_description = ctk.CTkEntry(
            self.cadreInfos,
            width=250,
            placeholder_text="Ex: Salle informatique"
        )
        self.entry_description.grid(row=2, column=1, padx=20, pady=8)

        ctk.CTkLabel(
            self.cadreInfos,
            text="Catégorie :",
            font=("Arial", 12)
        ).grid(row=3, column=0, padx=20, pady=8, sticky="e")

        self.entry_categorie = ctk.CTkEntry(
            self.cadreInfos,
            width=250,
            placeholder_text="Ex: Laboratoire, Cours, Bureau"
        )
        self.entry_categorie.grid(row=3, column=1, padx=20, pady=8)

        ctk.CTkLabel(
            self.cadreInfos,
            text="Capacité :",
            font=("Arial", 12)
        ).grid(row=4, column=0, padx=20, pady=8, sticky="e")

        self.entry_capacite = ctk.CTkEntry(
            self.cadreInfos,
            width=250,
            placeholder_text="Ex: 30"
        )
        self.entry_capacite.grid(row=4, column=1, padx=20, pady=8)

    def _construire_cadre_actions(self):

        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=20)

        ctk.CTkButton(
            self.cadreActions,
            text="➕ Ajouter",
            width=130,
            fg_color="#28a745",
            hover_color="#1e7e34",
            command=self.ajouter_salle
        ).grid(row=0, column=0, padx=10, pady=10)

        ctk.CTkButton(
            self.cadreActions,
            text="✏️ Modifier",
            width=130,
            fg_color="#007bff",
            hover_color="#0056b3",
            command=self.modifier_salle
        ).grid(row=0, column=1, padx=10, pady=10)

        ctk.CTkButton(
            self.cadreActions,
            text="🗑️ Supprimer",
            width=130,
            fg_color="#dc3545",
            hover_color="#a71d2a",
            command=self.supprimer_salle
        ).grid(row=0, column=2, padx=10, pady=10)

        ctk.CTkButton(
            self.cadreActions,
            text="🔍 Rechercher",
            width=130,
            fg_color="#fd7e14",
            hover_color="#c96209",
            command=self.rechercher_salle
        ).grid(row=0, column=3, padx=10, pady=10)

    def _construire_cadre_liste(self):

        self.cadreList = ctk.CTkFrame(self, corner_radius=10)
        self.cadreList.pack(pady=10, padx=20, fill="both", expand=True)

        ctk.CTkLabel(
            self.cadreList,
            text="Liste des salles",
            font=("Arial", 14, "bold")
        ).pack(pady=8)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings",
            height=8
        )

        self.treeList.heading("code",        text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie",   text="Catégorie")
        self.treeList.heading("capacite",    text="Capacité")

        self.treeList.column("code",        width=60,  anchor="center")
        self.treeList.column("description", width=200, anchor="w")
        self.treeList.column("categorie",   width=130, anchor="center")
        self.treeList.column("capacite",    width=80,  anchor="center")

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

    def lister_salles(self):

        self.treeList.delete(*self.treeList.get_children())

        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert(
                "", "end",
                values=(s.code, s.description, s.categorie, s.capacite)
            )

    def ajouter_salle(self):

        salle = Salle(
            self.entry_code.get(),
            self.entry_description.get(),
            self.entry_categorie.get(),
            self.entry_capacite.get()
        )

        ok, msg = self.service_salle.ajouter_salle(salle)

        if ok:
            messagebox.showinfo("Succès", msg)
        else:
            messagebox.showerror("Erreur", msg)

        self.lister_salles()

    def modifier_salle(self):

        salle = Salle(
            self.entry_code.get(),
            self.entry_description.get(),
            self.entry_categorie.get(),
            self.entry_capacite.get()
        )

        ok, msg = self.service_salle.modifier_salle(salle)

        if ok:
            messagebox.showinfo("Succès", msg)
        else:
            messagebox.showerror("Erreur", msg)

        self.lister_salles()

    def supprimer_salle(self):

        code = self.entry_code.get()

        if not code:
            messagebox.showwarning(
                "Attention",
                "⚠️ Veuillez entrer le code de la salle à supprimer."
            )
            return

        confirmation = messagebox.askyesno(
            "Confirmation",
            f"Voulez-vous vraiment supprimer la salle {code} ?"
        )

        if confirmation:
            self.service_salle.supprimer_salle(code)
            messagebox.showinfo("Succès", f"✅ Salle {code} supprimée avec succès.")

            self.lister_salles()

    def rechercher_salle(self):

        # Récupérer le code saisi
        code = self.entry_code.get()

        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entry_code.delete(0, "end")
            self.entry_description.delete(0, "end")
            self.entry_categorie.delete(0, "end")
            self.entry_capacite.delete(0, "end")

            self.entry_code.insert(0, salle.code)
            self.entry_description.insert(0, salle.description)
            self.entry_categorie.insert(0, salle.categorie)
            self.entry_capacite.insert(0, salle.capacite)

        else:
            messagebox.showwarning(
                "Introuvable",
                f"❌ Aucune salle trouvée avec le code : {code}"
            )