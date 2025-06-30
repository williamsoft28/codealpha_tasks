# codealpha_tasks
pour le 1 taks il faut lancer dabord le server avec python app.py et lancer le index.html puis tu renseigne ton long url 
 pour le 3 taks 

 # 🍽️ Restaurant Management System

Ce projet est un système de gestion de restaurant développé avec **Django** et **Django REST Framework**.  
Il permet de gérer les **commandes**, **réservations**, **tables**, **inventaire** et **menu** de manière automatisée via des APIs RESTful.

---

## ✅ Fonctionnalités Obligatoires Réalisées

### 1. 🎯 Backend avec Django
- Initialisation du projet Django (`restaurant`)
- Création de l'app principale (`restaurant_app`)
- Configuration de la base de données SQLite
- Migrations et lancement du serveur

---

### 2. 🧩 Modèles de Données (Database Models)
- `MenuItem` – Éléments du menu (nom, prix, description, en stock)
- `Table` – Tables disponibles (numéro, places, disponibilité)
- `Reservation` – Réservations de tables (client, date, table)
- `InventoryItem` – Stock (nom, quantité, seuil d’alerte)
- `Order` – Commandes par table
- `OrderItem` – Articles d'une commande (article + quantité)

---

### 3. 🔌 API REST créées pour :
- 📜 Voir les éléments du menu (`/api/menuitems/`)
- 🎫 Passer une commande (`/api/orders/`)
- 🍽 Réserver une table (`/api/reservations/`)
- 📦 Gérer l’inventaire (`/api/inventoryitems/`)

---

### 4. 🧠 Logique métier intégrée
- ✔ Vérifie si une table est disponible avant réservation
- ✔ Déduit automatiquement les stocks quand une commande est traitée
- ✔ Refuse les commandes si le stock est insuffisant
- ✔ Marque une commande comme "complétée"

---

## ▶️ Lancement du projet

```bash
# Installer les dépendances
pip install django djangorestframework

# Appliquer les migrations
python manage.py makemigrations
python manage.py migrate

# Lancer le serveur
python manage.py runserver

