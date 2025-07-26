Application d'authentification Django - Documentation et instructions de mise en route

---

PAGE D'AUTHENTIFICATION
-----------------------
Ce projet inclut une page d'authentification personnalisée (login) utilisant le système d'authentification de Django et un modèle utilisateur personnalisé. La page de connexion est stylisée avec Tailwind CSS et utilise les palettes de couleurs définies dans la configuration Tailwind.

La page de connexion est accessible à la racine de l'URL ("/").

TESTS
-----
Des tests pour la page d'authentification sont inclus dans authapp/tests.py. Ces tests couvrent :
- L'affichage de la page de connexion pour les utilisateurs anonymes
- Connexion valide (avec redirection vers le tableau de bord)
- Connexion invalide (le formulaire est réaffiché, l'utilisateur n'est pas connecté)
- Redirection pour les utilisateurs déjà authentifiés

INSTRUCTIONS DE MISE EN ROUTE
-----------------------------
1. Clonez le dépôt et placez-vous dans le dossier du projet.

2. Créez votre fichier d'environnement :
   Copiez .env.example en .env et renseignez les variables d'environnement nécessaires.

3. Construisez et démarrez les conteneurs :
   docker compose up --build

4. Dans un autre terminal, lancez le watcher Tailwind (pour le développement) :
   docker compose run --rm tailwind

5. Pour l'initialisation de Django et les migrations, exécutez les commandes suivantes dans le conteneur djangoapp :
   docker compose run --rm djangoapp python manage.py makemigrations
   docker compose run --rm djangoapp python manage.py migrate
   docker compose run --rm djangoapp python manage.py createsuperuser

6. Pour lancer les tests :
   docker compose run --rm djangoapp python manage.py test authapp

REMARQUES
---------
- Toutes les commandes de Django doivent être exécutées dans le conteneur djangoapp avec docker compose run --rm djangoapp ...
- Le serveur de développement démarre automatiquement avec docker compose up, mais Tailwind CSS doit être lancé séparément avec docker compose run --rm tailwind pour la mise à jour dynamique des styles.
- Le fichier .env est requis pour les variables d'environnement (base de données, envirronement, etc.).