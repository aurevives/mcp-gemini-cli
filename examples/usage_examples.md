# 📚 Exemples d'usage MCP Gemini CLI

Ce fichier contient des exemples concrets d'utilisation du MCP Gemini CLI dans Claude Code.

## 🎯 Scénarios d'usage typiques

### 1. Déblocage sur un problème technique

**Situation :** Vous êtes bloqué sur un bug complexe

**Dans Claude Code :**
```
J'ai un problème avec mon API qui retourne des timeouts aléatoirement. 
Peux-tu utiliser gemini_prompt pour avoir un second avis sur les causes possibles ?

Prompt: "API timeouts aléatoires en production: les requêtes prennent 30s+ parfois, 
mais généralement <1s. Base de données PostgreSQL, serveur Node.js, reverse proxy Nginx. 
Quelles sont les causes les plus probables et comment les investiguer ?"
```

### 2. Review d'architecture

**Situation :** Vous voulez un audit externe de votre code

**Dans Claude Code :**
```
Peux-tu analyser l'architecture de mon projet avec gemini_analyze_codebase ?

Question: "Fais un audit complet de cette application web : architecture, patterns, 
sécurité, performance. Quels sont les points d'amélioration prioritaires ?"
Path: "."
```

### 3. Choix technologique

**Situation :** Hésitation entre plusieurs solutions techniques

**Dans Claude Code :**
```
J'hésite entre plusieurs solutions pour gérer les sessions utilisateur. 
Utilise gemini_prompt avec ce prompt :

"Pour une app web Node.js avec 10k+ utilisateurs simultanés, quelle est la meilleure 
approche pour les sessions : JWT, Redis sessions, ou database sessions ? 
Compare les avantages/inconvénients de chaque solution."
```

### 4. Optimisation de performance

**Situation :** Application lente, besoin d'optimisation

**Dans Claude Code :**
```
Mon app React est lente. Peux-tu demander à Gemini d'analyser le codebase ?

Utilise gemini_analyze_codebase avec :
Question: "Cette app React a des problèmes de performance. Identifie les 
bottlenecks potentiels et propose des optimisations concrètes."
Path: "./src"
```

### 5. Refactoring complexe

**Situation :** Besoin de refactorer du legacy code

**Dans Claude Code :**
```
Je dois refactorer ce vieux module. Demande l'avis de Gemini :

gemini_prompt: "Ce module legacy (5000+ lignes, pattern monolithique) doit être 
refactorisé. Quelle stratégie adopter : refactor progressif, réécriture complète, 
ou approche étape par étape ? Donne un plan concret."
```

## 🔄 Workflow recommandé

### Étape 1: Analyse initiale
```
Utilise gemini_status pour vérifier que tout fonctionne
```

### Étape 2: Exploration du problème
```
gemini_prompt avec une description claire de votre problème
```

### Étape 3: Analyse contextuelle
```
gemini_analyze_codebase pour une analyse complète si nécessaire
```

### Étape 4: Synthèse
Combinez les insights de Gemini avec votre expertise Claude pour une solution optimale.

## 🎨 Prompts efficaces

### Pour gemini_prompt

**✅ Bon prompt :**
```
"Application e-commerce avec 50k+ produits. Les recherches sont lentes (>5s). 
Base données MySQL, index sur nom/catégorie. Frontend React avec pagination. 
Quelles optimisations prioriser : ElasticSearch, cache Redis, ou optimisation SQL ?"
```

**❌ Prompt vague :**
```
"Mon site est lent, comment l'optimiser ?"
```

### Pour gemini_analyze_codebase

**✅ Bonne question :**
```
"Cette API REST suit-elle les bonnes pratiques ? Vérifie la sécurité, 
la structure des endpoints, la gestion d'erreurs, et les patterns utilisés."
```

**❌ Question trop large :**
```
"Dis-moi tout sur ce code"
```

## 🛠️ Tips et astuces

### 1. Contexte riche
Toujours donner le maximum de contexte pertinent à Gemini (technos, contraintes, objectifs).

### 2. Questions spécifiques  
Plutôt que "comment améliorer ?", demandez "quelles sont les 3 optimisations prioritaires ?".

### 3. Validation croisée
Utilisez Gemini pour valider les solutions proposées par Claude et vice-versa.

### 4. Problèmes complexes
Pour les gros problèmes, décomposez en plusieurs questions ciblées.

### 5. Suivi des recommandations
Documentez les conseils de Gemini et trackez leur implémentation.

## 🚀 Cas d'usage avancés

### Pair programming virtuel
```
gemini_prompt: "Je code une feature de notification push. Tu peux me challenger 
sur mon approche ? Voici le plan : [votre plan]. Quels edge cases je rate ?"
```

### Code review automatique
```
gemini_analyze_codebase: "Fais une code review de ce module en te concentrant sur : 
sécurité, maintenabilité, tests manquants, et potentiels bugs."
```

### Exploration de nouvelles technos
```
gemini_prompt: "Je veux migrer de REST vers GraphQL pour cette API. 
Analyse les bénéfices/risques spécifiques à mon cas d'usage."
```

---

💡 **N'hésitez pas à expérimenter avec différents types de prompts pour découvrir ce qui fonctionne le mieux pour vos besoins !**