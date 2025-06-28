# MCP Gemini CLI 🚀

> **Votre second avis IA avec Gemini 2.5 Pro**

Un serveur MCP (Model Context Protocol) qui encapsule Google Gemini CLI pour obtenir un second avis intelligent sur des problèmes complexes directement dans Claude Code.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## ✨ Fonctionnalités

- 🧠 **Second avis IA** avec Gemini 2.5 Pro (dernier modèle Google)
- 📁 **Analyse complète de codebase** avec contexte 1M tokens
- 🔄 **Mémoire persistante** entre les conversations
- 🆓 **Gratuit** : 60 requêtes/minute, 1000/jour
- ⚡ **Intégration Claude Code** via MCP

## 🎯 Cas d'usage

### Quand utiliser ce MCP ?

- **Problèmes techniques complexes** nécessitant une perspective différente
- **Validation d'approches** architecturales ou de solutions
- **Brainstorming** et génération d'idées alternatives  
- **Audit de code** et review architectural complet
- **Situations bloquantes** où vous avez besoin d'un autre point de vue

## 🚀 Installation

### Prérequis

1. **Node.js 18+** pour Gemini CLI
2. **Python 3.8+** pour le serveur MCP
3. **Gemini CLI** installé et configuré

### 1. Installation de Gemini CLI

```bash
# Installation Gemini CLI (global)
npm install -g @google/gemini-cli

# Première configuration (authentification Google gratuite)
gemini
# ↳ Suivez les instructions pour vous connecter avec votre compte Google
```

### 2. Installation du MCP

```bash
# Cloner le repository
git clone https://github.com/aurevives/mcp-gemini-cli.git
cd mcp-gemini-cli

# Installer les dépendances Python
pip install -r requirements.txt
```

### 3. Configuration dans Claude Code

Ajoutez le serveur MCP à votre configuration Claude Code :

```bash
claude mcp add-json gemini-cli '{
  "command": "python3",
  "args": ["/chemin/vers/mcp-gemini-cli/server.py"],
  "env": {}
}'
```

Redémarrez Claude Code pour activer le MCP.

## 🛠️ Tools disponibles

### 1. `gemini_prompt`

Envoie un prompt à Gemini 2.5 Pro pour obtenir un second avis.

**Paramètres :**
- `prompt` (string) : La question ou problème à soumettre
- `model` (string, optionnel) : Modèle Gemini (défaut: `gemini-2.5-pro`)

**Exemple :**
```
Utilise gemini_prompt avec le prompt \"Comment optimiser cette fonction Python pour de gros volumes de données ?\"
```

### 2. `gemini_analyze_codebase`

Analyse complète d'un codebase avec le contexte 1M tokens de Gemini.

**Paramètres :**
- `question` (string) : Question spécifique sur le codebase
- `path` (string, optionnel) : Répertoire à analyser (défaut: répertoire courant)
- `model` (string, optionnel) : Modèle Gemini (défaut: `gemini-2.5-pro`)

**Exemple :**
```
Utilise gemini_analyze_codebase avec question \"Quels sont les points d'amélioration de l'architecture ?\" et path \".\"
```

### 3. `gemini_status`

Vérifie le statut et la configuration de Gemini CLI.

**Exemple :**
```
Utilise gemini_status pour vérifier la configuration
```

## 💡 Exemples d'usage

### Problème technique complexe

> **Vous :** \"J'ai un bug bizarre avec mes WebSockets qui se déconnectent aléatoirement\"
> 
> **Via MCP :** `gemini_prompt` → \"Analyse ce problème : WebSockets qui se déconnectent aléatoirement en production, mais pas en dev. Quelles sont les causes possibles et solutions ?\"

### Audit architectural 

> **Vous :** \"Je veux une review complète de mon API REST\"
>
> **Via MCP :** `gemini_analyze_codebase` → question: \"Fais un audit complet de cette API : architecture, sécurité, performance, et bonnes pratiques. Quelles améliorations recommandes-tu ?\"

### Brainstorming technique

> **Vous :** \"Comment implémenter un cache distribué efficace ?\"
>
> **Via MCP :** `gemini_prompt` → \"Quelles sont les différentes approches pour implémenter un cache distribué ? Compare Redis, Memcached, et solutions in-memory avec leurs avantages/inconvénients.\"

## 🔧 Configuration avancée

### Variables d'environnement

Aucune variable d'environnement requise. Le MCP utilise directement Gemini CLI qui doit être configuré au préalable.

### Customisation

Vous pouvez modifier le modèle par défaut en éditant `server.py` :

```python
# Ligne 67 - Changer le modèle par défaut
async def gemini_prompt(prompt: str, model: str = "gemini-2.5-flash") -> Dict[str, Any]:
```

## 🧪 Tests

```bash
# Test de base
python3 server.py

# Test d'un tool spécifique
python3 -c \"
from server import server
import asyncio

async def test():
    result = await server.mcp.call_tool('gemini_status', {})
    print(result)

asyncio.run(test())
\"
```

## 🤝 Contribution

1. Fork le repository
2. Créez une branche feature (`git checkout -b feature/nouvelle-fonctionnalite`)
3. Committez vos changements (`git commit -am 'Ajout nouvelle fonctionnalité'`)
4. Push sur la branche (`git push origin feature/nouvelle-fonctionnalite`)
5. Créez une Pull Request

## 📝 Licence

MIT License - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Auteur

**Aurelien Vives**
- GitHub: [@aurevives](https://github.com/aurevives)
- Email: vives.aurelien993@gmail.com

## 🙏 Remerciements

- [Google Gemini CLI](https://github.com/google-gemini/gemini-cli) pour l'excellent CLI
- [Model Context Protocol](https://modelcontextprotocol.io/) pour le standard MCP
- [Anthropic Claude Code](https://claude.ai/code) pour l'intégration

---

⭐ **Si ce MCP vous aide, n'hésitez pas à donner une étoile au repository !** ⭐