"""
Wrapper client pour Gemini CLI
"""

import asyncio
import subprocess
import os
import logging
from typing import Dict, Any, Optional, List
from pathlib import Path


class GeminiClient:
    """Client wrapper pour interagir avec Gemini CLI."""
    
    def __init__(self):
        self.base_command = ["gemini"]
        self.logger = logging.getLogger(__name__)
    
    async def execute_prompt(
        self, 
        prompt: str, 
        model: str = "gemini-2.5-pro",
        stdin_data: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Exécute un prompt Gemini CLI en mode non-interactif.
        
        Args:
            prompt: Le prompt à envoyer à Gemini
            model: Modèle Gemini à utiliser
            stdin_data: Données à envoyer via stdin (optionnel)
            **kwargs: Options supplémentaires (debug, all_files, etc.)
            
        Returns:
            str: Réponse de Gemini CLI
            
        Raises:
            Exception: Si l'exécution échoue
        """
        try:
            # Construction de la commande
            cmd = self.base_command + ["-m", model, "-p", prompt]
            
            # Ajout des flags optionnels
            if kwargs.get("debug"):
                cmd.append("--debug")
            if kwargs.get("all_files"):
                cmd.append("--all_files")
            if kwargs.get("show_memory_usage"):
                cmd.append("--show_memory_usage")
            
            self.logger.info(f"Exécution commande Gemini: {' '.join(cmd[:4])}...")
            
            # Exécution de la commande
            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdin=subprocess.PIPE if stdin_data else None,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=kwargs.get("cwd", os.getcwd())
            )
            
            stdout, stderr = await process.communicate(
                input=stdin_data.encode() if stdin_data else None
            )
            
            if process.returncode != 0:
                error_msg = stderr.decode().strip()
                self.logger.error(f"Erreur Gemini CLI: {error_msg}")
                raise Exception(f"Gemini CLI a échoué: {error_msg}")
            
            result = stdout.decode().strip()
            self.logger.info(f"Réponse Gemini reçue ({len(result)} caractères)")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'exécution Gemini CLI: {str(e)}")
            raise
    
    async def analyze_codebase(
        self, 
        question: str, 
        path: str = ".",
        model: str = "gemini-2.5-pro"
    ) -> str:
        """
        Analyse un codebase complet avec Gemini CLI.
        
        Args:
            question: Question sur le codebase
            path: Chemin vers le répertoire à analyser
            model: Modèle Gemini à utiliser
            
        Returns:
            str: Analyse détaillée du codebase
        """
        try:
            # Vérification que le répertoire existe
            target_path = Path(path).resolve()
            if not target_path.exists():
                raise Exception(f"Le répertoire '{path}' n'existe pas")
            
            if not target_path.is_dir():
                raise Exception(f"'{path}' n'est pas un répertoire")
            
            self.logger.info(f"Analyse du codebase: {target_path}")
            
            # Construction du prompt pour l'analyse
            analysis_prompt = f"""Analyse ce codebase et réponds à cette question: {question}

Analyse l'architecture, les patterns utilisés, les technologies, 
et donne des recommandations spécifiques."""
            
            # Exécution avec --all_files pour inclure tout le codebase
            return await self.execute_prompt(
                prompt=analysis_prompt,
                model=model,
                all_files=True,
                cwd=str(target_path)
            )
            
        except Exception as e:
            self.logger.error(f"Erreur lors de l'analyse du codebase: {str(e)}")
            raise
    
    def check_gemini_available(self) -> bool:
        """
        Vérifie si Gemini CLI est disponible et configuré.
        
        Returns:
            bool: True si Gemini CLI est disponible
        """
        try:
            result = subprocess.run(
                ["gemini", "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            return False
    
    def get_gemini_info(self) -> Dict[str, Any]:
        """
        Récupère les informations sur l'installation Gemini CLI.
        
        Returns:
            dict: Informations sur Gemini CLI
        """
        info = {
            "available": False,
            "version": None,
            "error": None
        }
        
        try:
            if self.check_gemini_available():
                result = subprocess.run(
                    ["gemini", "--version"],
                    capture_output=True,
                    text=True,
                    timeout=10
                )
                info["available"] = True
                info["version"] = result.stdout.strip()
            else:
                info["error"] = "Gemini CLI n'est pas disponible ou configuré"
                
        except Exception as e:
            info["error"] = f"Erreur lors de la vérification: {str(e)}"
        
        return info