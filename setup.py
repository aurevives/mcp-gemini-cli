#!/usr/bin/env python3
"""
Setup script for MCP Gemini CLI Server
"""

from setuptools import setup, find_packages

setup(
    name="mcp-gemini-cli",
    version="1.0.0",
    description="MCP server for Gemini CLI - Get a second AI opinion with Gemini 2.5 Pro",
    author="aurevives",
    url="https://github.com/aurevives/mcp-gemini-cli",
    py_modules=["server", "gemini_client"],
    install_requires=[
        "mcp>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mcp-gemini-cli=server:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)