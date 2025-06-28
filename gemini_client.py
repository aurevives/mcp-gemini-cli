"""
Wrapper client for Gemini CLI
"""

import asyncio
import subprocess
import os
import logging
from typing import Dict, Any, Optional, List
from pathlib import Path


class GeminiClient:
    """Client wrapper to interact with Gemini CLI."""
    
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
        Execute a Gemini CLI prompt in non-interactive mode.
        
        Args:
            prompt: The prompt to send to Gemini
            model: Gemini model to use
            stdin_data: Data to send via stdin (optional)
            **kwargs: Additional options (debug, all_files, etc.)
            
        Returns:
            str: Gemini CLI response
            
        Raises:
            Exception: If execution fails
        """
        try:
            # Build command
            cmd = self.base_command + ["-m", model, "-p", prompt]
            
            # Add optional flags
            if kwargs.get("debug"):
                cmd.append("--debug")
            if kwargs.get("all_files"):
                cmd.append("--all_files")
            if kwargs.get("show_memory_usage"):
                cmd.append("--show_memory_usage")
            
            self.logger.info(f"Executing Gemini command: {' '.join(cmd[:4])}...")
            
            # Execute command
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
                self.logger.error(f"Gemini CLI error: {error_msg}")
                raise Exception(f"Gemini CLI failed: {error_msg}")
            
            result = stdout.decode().strip()
            self.logger.info(f"Gemini response received ({len(result)} characters)")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error executing Gemini CLI: {str(e)}")
            raise
    
    async def analyze_codebase(
        self, 
        question: str, 
        path: str = ".",
        model: str = "gemini-2.5-pro"
    ) -> str:
        """
        Analyze a complete codebase with Gemini CLI.
        
        Args:
            question: Question about the codebase
            path: Path to the directory to analyze
            model: Gemini model to use
            
        Returns:
            str: Detailed codebase analysis
        """
        try:
            # Check that directory exists
            target_path = Path(path).resolve()
            if not target_path.exists():
                raise Exception(f"Directory '{path}' does not exist")
            
            if not target_path.is_dir():
                raise Exception(f"'{path}' is not a directory")
            
            self.logger.info(f"Analyzing codebase: {target_path}")
            
            # Build analysis prompt
            analysis_prompt = f"""Analyze this codebase and answer this question: {question}

Analyze the architecture, patterns used, technologies, 
and provide specific recommendations."""
            
            # Execute with --all_files to include entire codebase
            return await self.execute_prompt(
                prompt=analysis_prompt,
                model=model,
                all_files=True,
                cwd=str(target_path)
            )
            
        except Exception as e:
            self.logger.error(f"Error analyzing codebase: {str(e)}")
            raise
    
    def check_gemini_available(self) -> bool:
        """
        Check if Gemini CLI is available and configured.
        
        Returns:
            bool: True if Gemini CLI is available
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
        Get information about Gemini CLI installation.
        
        Returns:
            dict: Information about Gemini CLI
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
                info["error"] = "Gemini CLI is not available or configured"
                
        except Exception as e:
            info["error"] = f"Error during verification: {str(e)}"
        
        return info