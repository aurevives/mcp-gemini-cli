"""
MCP Gemini CLI - Votre second avis IA avec Gemini 2.5 Pro

Un serveur MCP qui encapsule Gemini CLI pour obtenir un second avis
avec le dernier modèle Google sur des problèmes complexes.
"""

__version__ = "1.0.0"
__author__ = "Aurelien Vives"
__email__ = "vives.aurelien993@gmail.com"

from .server import GeminiMCPServer

__all__ = ["GeminiMCPServer"]