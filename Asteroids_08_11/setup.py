"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "Asteroids",
    version = "0.2",
    description = "An Asteroids game created by Dion Recai and Loïc Michel for the SPISE 2016",
    executables = [Executable("Asteroids.py")],
)
