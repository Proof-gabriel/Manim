# --- Laboratório Manim ---

default:
    @just --list

rascunho ARQUIVO CENA:
    manim -pql {{ARQUIVO}} {{CENA}}

final ARQUIVO CENA:
    manim -pqh {{ARQUIVO}} {{CENA}}

limpar:
    rm -rf media/ partial_movie_files/ __pycache__/ ManimCE_*.log
    echo "Laboratório limpo."
