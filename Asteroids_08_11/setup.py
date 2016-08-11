"""Fichier d'installation de notre script salut.py."""

from cx_Freeze import setup, Executable

target = Executable(
    script="Asteroids.py",
    base="Win32GUI",
    compress=False,
    copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False,
    icon="icon.ico"
    )

setup(
    name = "Asteroids",
    version = "0.3",
    description = "An Asteroids game created by Dion Recai and Loïc Michel for the SPISE 2016",
    executables = [target],
)
