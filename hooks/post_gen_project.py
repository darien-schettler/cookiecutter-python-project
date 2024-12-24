#!/usr/bin/env python
import os
import subprocess

def init_git():
    """Initialize git repository."""
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)

def setup_poetry():
    """Initialize poetry and install dependencies."""
    subprocess.run(["poetry", "install"], check=True)
    subprocess.run(["poetry", "run", "pre-commit", "install"], check=True)

def main():
    init_git()
    setup_poetry()
    
    print("\n🎉 Project successfully created!")
    print("\nNext steps:")
    print("1. Create a virtual environment: poetry shell")
    print("2. Install dependencies: poetry install")
    print("3. Initialize pre-commit: pre-commit install")
    print("4. Start coding! 🚀")

if __name__ == "__main__":
    main()
