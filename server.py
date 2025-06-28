#!/usr/bin/env python3
"""
MCP Gemini CLI Server - Get a second AI opinion with Gemini 2.5 Pro
"""

import sys
import os
from pathlib import Path
from typing import Dict, Any

# Standalone MCP server - works without external dependencies
from mcp.server.fastmcp import FastMCP
from gemini_client import GeminiClient


class BaseMCPServer:
    """Standalone base server for MCP."""
    
    def __init__(self, name: str):
        self.name = name
        self.mcp = FastMCP(name)
    
    def handle_error(self, error: Exception, context: str = "") -> Dict[str, str]:
        error_msg = f"{context}: {str(error)}" if context else str(error)
        return {"error": error_msg}
    
    def run(self, transport='stdio'):
        self.mcp.run(transport=transport)


class GeminiMCPServer(BaseMCPServer):
    """MCP server for Gemini CLI - Get a second AI opinion."""
    
    def __init__(self):
        super().__init__("gemini-cli")
        self.gemini_client = GeminiClient()
        self._initialize_api()
        self._register_tools()
    
    def _initialize_api(self):
        """Initialize and check Gemini CLI."""
        try:
            info = self.gemini_client.get_gemini_info()
            if info["available"]:
                print(f"✅ Gemini CLI initialized - Version: {info['version']}")
            else:
                print(f"⚠️  Warning: {info['error']}")
                print("   Make sure 'gemini' is installed and configured")
        except Exception as e:
            print(f"❌ Error initializing Gemini CLI: {str(e)}")
            raise
    
    def _register_tools(self):
        """Register MCP tools for Gemini CLI."""
        
        @self.mcp.tool()
        async def gemini_prompt(prompt: str, model: str = "gemini-2.5-pro") -> Dict[str, Any]:
            """Send prompt to Gemini 2.5 Pro for second opinion.
            
            Useful for:
            - Complex situations needing different perspective
            - Technical problems hard to solve
            - Validating approaches or solutions
            - Brainstorming and generating alternatives
            
            Args:
                prompt: Question or problem to submit to Gemini
                model: Gemini model to use (default: gemini-2.5-pro)
            
            Returns:
                dict: Gemini response with metadata
            """
            try:
                if not prompt.strip():
                    return self.handle_error(
                        Exception("Prompt cannot be empty"), 
                        "Prompt validation"
                    )
                
                print(f"🤖 Sending prompt to Gemini {model}...")
                
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
                        "model_info": "Gemini 2.5 Pro - Latest Google model",
                        "use_case": "Second AI opinion for complex problems"
                    }
                }
                
            except Exception as e:
                return self.handle_error(e, "Error executing Gemini prompt")
        
        @self.mcp.tool()
        async def gemini_analyze_codebase(
            question: str, 
            path: str = ".", 
            model: str = "gemini-2.5-pro"
        ) -> Dict[str, Any]:
            """Analyze codebase with Gemini 2.5 Pro (1M token context).
            
            Uses --all_files to include all project files and get
            global view of architecture and potential issues.
            
            Useful for:
            - Code audit and architectural review
            - Pattern and anti-pattern identification
            - Optimization and refactoring suggestions
            - Security analysis and best practices
            
            Args:
                question: Specific question about the codebase
                path: Directory to analyze (default: current directory)
                model: Gemini model to use (default: gemini-2.5-pro)
                
            Returns:
                dict: Detailed analysis with recommendations
            """
            try:
                if not question.strip():
                    return self.handle_error(
                        Exception("Question cannot be empty"), 
                        "Question validation"
                    )
                
                # Resolve path
                target_path = Path(path).resolve()
                
                print(f"📁 Analyzing codebase: {target_path}")
                print(f"🔍 Question: {question}")
                print(f"🤖 Model: {model} (1M tokens context)")
                
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
                        "use_case": "Complete codebase analysis",
                        "features": ["--all_files", "Global architecture", "Recommendations"]
                    }
                }
                
            except Exception as e:
                return self.handle_error(e, "Error analyzing codebase")
        
        @self.mcp.tool()
        async def gemini_status() -> Dict[str, Any]:
            """Check Gemini CLI status and configuration.
            
            Returns:
                dict: Information about Gemini CLI installation and configuration
            """
            try:
                info = self.gemini_client.get_gemini_info()
                
                return {
                    "success": True,
                    "gemini_cli": info,
                    "mcp_server": {
                        "name": self.name,
                        "tools_available": ["gemini_prompt", "gemini_analyze_codebase", "gemini_status"],
                        "description": "MCP Gemini CLI - Get a second AI opinion"
                    }
                }
                
            except Exception as e:
                return self.handle_error(e, "Error checking status")


# Global instance for export (required MCP pattern)
server = GeminiMCPServer()
mcp = server.mcp

def main():
    """Entry point for console script."""
    print("🚀 Starting MCP Gemini CLI Server...")
    print("📋 Available tools:")
    print("   • gemini_prompt - Second AI opinion with Gemini 2.5 Pro")
    print("   • gemini_analyze_codebase - Complete codebase analysis")
    print("   • gemini_status - Status and configuration")
    print()
    
    server.run()

if __name__ == "__main__":
    main()