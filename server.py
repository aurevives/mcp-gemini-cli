#!/usr/bin/env python3
"""
MCP Gemini CLI Server - Votre second avis IA avec Gemini 2.5 Pro

Serveur MCP qui encapsule Gemini CLI pour obtenir un second avis
avec le dernier modèle Google sur des problèmes complexes.
"""

import sys
import os
from pathlib import Path
from typing import Dict, Any

# Ajouter le répertoire MCP parent au PATH pour BaseMCPServer
parent_mcp_dir = Path(__file__).parent.parent / "MCP"
sys.path.insert(0, str(parent_mcp_dir))

try:
    from shared.base_server import BaseMCPServer
except ImportError:
    # Fallback si BaseMCPServer n'est pas disponible
    print("Warning: BaseMCPServer not found, using basic MCP setup")
    from mcp.server.fastmcp import FastMCP
    
    class BaseMCPServer:
        def __init__(self, name: str):
            self.name = name
            self.mcp = FastMCP(name)
        
        def handle_error(self, error: Exception, context: str = "") -> Dict[str, str]:
            error_msg = f"{context}: {str(error)}" if context else str(error)
            return {"error": error_msg}
        
        def run(self, transport='stdio'):
            self.mcp.run(transport=transport)

from gemini_client import GeminiClient


class GeminiMCPServer(BaseMCPServer):
    """Serveur MCP pour Gemini CLI - Votre second avis IA."""
    
    def __init__(self):
        super().__init__("gemini-cli")
        self.gemini_client = GeminiClient()
        self._initialize_api()
        self._register_tools()
    
    def _initialize_api(self):
        """Initialise et vérifie Gemini CLI."""
        try:
            info = self.gemini_client.get_gemini_info()
            if info["available"]:
                print(f"✅ Gemini CLI initialisé - Version: {info['version']}")
            else:
                print(f"⚠️  Avertissement: {info['error']}")
                print("   Assurez-vous que 'gemini' est installé et configuré")
        except Exception as e:
            print(f"❌ Erreur initialisation Gemini CLI: {str(e)}")
            raise
    
    def _register_tools(self):
        """Enregistre les tools MCP pour Gemini CLI."""
        
        @self.mcp.tool()
        async def gemini_prompt(prompt: str, model: str = "gemini-2.5-pro") -> Dict[str, Any]:
            """Envoie un prompt à Gemini 2.5 Pro pour obtenir un second avis.
            
            Particulièrement utile pour :
            - Situations complexes nécessitant une perspective différente
            - Problèmes techniques difficiles à résoudre  
            - Validation d'approches ou de solutions
            - Brainstorming et génération d'idées alternatives
            
            Args:
                prompt: La question ou problème à soumettre à Gemini
                model: Modèle Gemini à utiliser (défaut: gemini-2.5-pro)
            
            Returns:
                dict: Réponse de Gemini avec métadonnées
            """
            try:
                if not prompt.strip():
                    return self.handle_error(
                        Exception("Le prompt ne peut pas être vide"), 
                        "Validation prompt"
                    )
                
                print(f"🤖 Envoi du prompt à Gemini {model}...")
                
                response = await self.gemini_client.execute_prompt(
                    prompt=prompt,
                    model=model
                )
                
                return {
                    "success": True,
                    "model": model,
                    "prompt": prompt,
                    "response": response,
                    "metadata": {
                        "tool": "gemini_prompt",
                        "model_info": "Gemini 2.5 Pro - Dernier modèle Google",
                        "use_case": "Second avis IA pour problèmes complexes"
                    }
                }
                
            except Exception as e:
                return self.handle_error(e, "Erreur lors de l'exécution du prompt Gemini")
        
        @self.mcp.tool()
        async def gemini_analyze_codebase(
            question: str, 
            path: str = ".", 
            model: str = "gemini-2.5-pro"
        ) -> Dict[str, Any]:
            """Analyse complète d'un codebase avec Gemini 2.5 Pro (contexte 1M tokens).
            
            Utilise --all_files pour inclure tous les fichiers du projet et obtenir
            une vision globale de l'architecture et des problèmes potentiels.
            
            Particulièrement utile pour :
            - Audit de code et review architectural
            - Identification de patterns et anti-patterns
            - Suggestions d'optimisation et refactoring
            - Analyse de sécurité et bonnes pratiques
            
            Args:
                question: Question spécifique sur le codebase
                path: Répertoire à analyser (défaut: répertoire courant)
                model: Modèle Gemini à utiliser (défaut: gemini-2.5-pro)
                
            Returns:
                dict: Analyse détaillée avec recommandations
            """
            try:
                if not question.strip():
                    return self.handle_error(
                        Exception("La question ne peut pas être vide"), 
                        "Validation question"
                    )
                
                # Résolution du chemin
                target_path = Path(path).resolve()
                
                print(f"📁 Analyse du codebase: {target_path}")
                print(f"🔍 Question: {question}")
                print(f"🤖 Modèle: {model} (contexte 1M tokens)")
                
                analysis = await self.gemini_client.analyze_codebase(
                    question=question,
                    path=str(target_path),
                    model=model
                )
                
                return {
                    "success": True,
                    "model": model,
                    "question": question,
                    "path": str(target_path),
                    "analysis": analysis,
                    "metadata": {
                        "tool": "gemini_analyze_codebase",
                        "model_info": "Gemini 2.5 Pro - 1M tokens context",
                        "use_case": "Analyse complète de codebase",
                        "features": ["--all_files", "Architecture globale", "Recommandations"]
                    }
                }
                
            except Exception as e:
                return self.handle_error(e, "Erreur lors de l'analyse du codebase")
        
        @self.mcp.tool()
        async def gemini_status() -> Dict[str, Any]:
            """Vérifie le statut et la configuration de Gemini CLI.
            
            Returns:
                dict: Informations sur l'installation et la configuration Gemini CLI
            """
            try:
                info = self.gemini_client.get_gemini_info()
                
                return {
                    "success": True,
                    "gemini_cli": info,
                    "mcp_server": {
                        "name": self.name,
                        "tools_available": ["gemini_prompt", "gemini_analyze_codebase", "gemini_status"],
                        "description": "MCP Gemini CLI - Votre second avis IA"
                    }
                }
                
            except Exception as e:
                return self.handle_error(e, "Erreur lors de la vérification du statut")


# Instance globale pour l'export (pattern requis MCP)
server = GeminiMCPServer()
mcp = server.mcp

if __name__ == "__main__":
    print("🚀 Démarrage MCP Gemini CLI Server...")
    print("📋 Tools disponibles:")
    print("   • gemini_prompt - Second avis IA avec Gemini 2.5 Pro")
    print("   • gemini_analyze_codebase - Analyse complète de codebase")
    print("   • gemini_status - Statut et configuration")
    print()
    
    server.run()