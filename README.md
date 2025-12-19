# RetentionAI Backend

## 📋 Vue d'ensemble

**RetentionAI** est une application backend intelligente conçue pour aider les directions des ressources humaines à anticiper les départs volontaires des employés et à proposer des plans de rétention personnalisés.

Le système combine un modèle de Machine Learning supervisé pour prédire le risque de départ (churn) et une IA générative pour créer des recommandations RH concrètes et personnalisées.

## 🎯 Objectifs

### Objectifs Business
- Identifier les profils à haut risque de démission
- Proposer des actions RH concrètes et personnalisées
- Réduire les décisions manuelles et subjectives
- Diminuer les coûts de turnover

### Objectifs Techniques
- Mettre en œuvre un pipeline ML supervisé
- Exposer le modèle via une API REST sécurisée
- Intégrer une IA générative externe (Gemini)
- Assurer la traçabilité complète des prédictions
- Garantir la sécurité par authentification JWT

## 🏗️ Architecture

```
retentionai-backend/
├── app/
│   ├── api/v1/
│   │   └── routes/
│   │       ├── auth.py              # Authentification JWT
│   │       ├── prediction.py        # Endpoint ML
│   │       └── retention.py         # Génération plans de rétention
│   ├── core/
│   │   ├── cors.py                  # Configuration CORS
│   │   └── __init__.py
│   ├── db/
│   │   └── models/
│   │       ├── base.py              # Base SQLAlchemy
│   │       ├── employee.py          # Modèle Employee
│   │       ├── prediction_history.py
│   │       └── user.py              # Modèle User
│   ├── schemas/
│   │   ├── employee.py              # Schémas Pydantic
│   │   ├── prediction.py
│   │   ├── retention.py
│   │   └── user.py
│   ├── services/
│   │   ├── auth_services.py         # Logique authentification
│   │   ├── employee_services.py
│   │   ├── history_prediction_services.py
│   │   ├── retention_services.py    # Intégration LLM
│   │   └── user_services.py
│   └── dependencies.py              # Dépendances FastAPI
├── data/
│   └── data.csv                     # Dataset RH
├── models/
│   └── logistic_regression_model.pkl # Modèle ML entraîné
├── notebooks/
│   ├── eda.ipynb                    # Analyse exploratoire
│   ├── preprocessing.ipynb          # Préparation des données
│   └── preprocessing_smote.ipynb    # Gestion déséquilibre
├── tests/
│   ├── test_gemini_mock.py          # Tests API LLM
│   └── test_model.py                # Tests modèle ML
├── utils/
│   └── main.py                      # Point d'entrée FastAPI
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🚀 Fonctionnalités

### 1. Machine Learning Supervisé

**Modèle de prédiction du churn employé**
- Analyse exploratoire des données (EDA)
- Preprocessing avancé (encodage, normalisation, SMOTE)
- Modèles comparés : Régression Logistique, Random Forest
- Optimisation par GridSearchCV
- Métriques : Matrice de confusion, Courbe ROC, F1-Score

### 2. API REST Sécurisée (FastAPI)

#### Authentification JWT

**POST `/register`**
```json
{
  "username": "hr_manager",
  "password": "securepassword"
}
```

**POST `/login`**
```json
{
  "username": "hr_manager",
  "password": "securepassword"
}
```
Retourne un token JWT pour accéder aux endpoints protégés.

#### Endpoints Métier

**POST `/predict`** (Protégé par JWT)
- Charge le modèle ML entraîné
- Prédit la probabilité de départ
- Enregistre la prédiction dans l'historique

```json
{
  "churn_probability": 0.78 ,
  "employe_id" : 1
}
```

**POST `/generate-retention-plan`** (Protégé par JWT)
- Génère un plan de rétention personnalisé si risque > 50%
- Utilise l'API Gemini/HuggingFace
- Retourne 3 actions concrètes

```json
{
  "retention_plan": [
    "Proposer 2 jours de télétravail par semaine",
    "Réévaluer la charge de déplacement professionnel",
    "Mettre en place un plan de formation personnalisé"
  ]
}
```

### 3. Base de Données PostgreSQL

**Table `users`**
- id, username, password_hash, created_at

**Table `predictions_history`**
- id, timestamp, user_id, employee_id, probability

**Table `employee`**
- id, age, Age , BusinessTravel , Department , Education ...

Traçabilité complète de toutes les prédictions réalisées.

### 4. Intégration IA Générative

Le système utilise l'API Gemini pour générer des plans de rétention personnalisés basés sur :
- Données démographiques (âge, ancienneté)
- Département et rôle
- Satisfaction et performance
- Équilibre vie pro/perso
- Probabilité de départ prédite

**Exemple de prompt dynamique :**
```
Agis comme un expert RH.

Voici les informations sur l'employé :
- Age : 35
- Département : Sales
- Role : Sales Executive
- Satisfaction : 3/5
- Performance : 4/5

Contexte : ce salarié a un risque élevé de départ (78%).

Tâche : propose 3 actions concrètes et personnalisées pour le retenir.
```

## 🛠️ Technologies Utilisées

- **Framework Backend** : FastAPI
- **Base de données** : PostgreSQL
- **ORM** : SQLAlchemy
- **Authentification** : JWT (python-jose, passlib)
- **Machine Learning** : scikit-learn, pandas, numpy 
- **IA Générative** : Google Gemini API
- **Tests** : Pytest
- **Conteneurisation** : Docker, Docker Compose
- **Visualisation** : Seaborn, Matplotlib (notebooks)

## 📦 Installation

### Prérequis
- Python 3.9+
- PostgreSQL 13+
- Docker & Docker Compose
- API Key Google Gemini

### Installation locale

1. **Cloner le repository**
```bash
git clone https://github.com/votre-org/retentionai-backend.git
cd retentionai-backend
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configuration des variables d'environnement**
```bash
cp .env.example .env
```

Modifier `.env` avec vos paramètres :
```env
DATABASE_URL=postgresql://user:password@localhost/retentionai
SECRET_KEY=your-secret-key-here
GEMINI_API_KEY=your-gemini-api-key
```

5. **Initialiser la base de données**
```bash
python -m app.db.database
```

6. **Lancer l'application**
```bash
uvicorn app.main:app --reload
```

L'API sera accessible sur `http://localhost:8000`

Documentation interactive : `http://localhost:8000/docs`

### Installation avec Docker

```bash
docker-compose up --build
```

## 🧪 Tests

### Exécuter tous les tests
```bash
pytest
```

### Tests spécifiques
```bash
# Test du modèle ML
pytest tests/test_model.py

# Test de l'intégration Gemini (avec mock)
pytest tests/test_gemini_mock.py
```

### Coverage
```bash
pytest --cov=app --cov-report=html
```

## 📊 Pipeline ML

### 1. Exploration des données (EDA)
- Distribution des variables
- Corrélations
- Détection des outliers
- Analyse de la cible (déséquilibre)

### 2. Preprocessing
- Suppression des colonnes inutiles (EmployeeNumber, Over18 ... )
- Encodage OneHot des variables catégorielles
- Normalisation/Standardisation des numériques
- Gestion du déséquilibre avec SMOTE

### 3. Entraînement
- Train/Test Split (80/20)
- Modèles comparés : Logistic Regression, Random Forest
- Validation croisée
- Optimisation des hyperparamètres (GridSearchCV)

### 4. Évaluation
- Matrice de confusion
- Courbe ROC et AUC
- Precision, Recall, F1-Score
- Classification Report

### 5. Sauvegarde
- Modèle sérialisé en `.pkl`
- Chargement dynamique dans l'API

## 🔐 Sécurité

- **Authentification JWT** : Tous les endpoints métier sont protégés
- **Hash des mots de passe** : bcrypt avec salt
- **CORS configuré** : Autorisation contrôlée des origines
- **Validation des données** : Pydantic schemas
- **SQL Injection** : Protection via ORM SQLAlchemy


## 📈 Monitoring & Logs

- Logging structuré des prédictions
- Traçabilité complète dans `predictions_history`
- Métriques d'utilisation du modèle



## 👥 Contribution

Les contributions sont les bienvenues ! Merci de suivre ces étapes :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT.


---

**Développé avec ❤️ pour optimiser la rétention des talents**