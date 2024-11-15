# Funções auxiliares

import pickle
import os
from models import Ponto

def salvar_dados(ponto):
    if not os.path.exists("data"):
        os.makedirs("data")
    
    arquivo = f"data/{ponto.nome}_ponto.pkl"
    with open(arquivo, "wb") as f:
        pickle.dump(ponto, f)

def carregar_dados(nome):
    arquivo = f"data/{nome}_ponto.pkl"
    if os.path.exists(arquivo):
        with open(arquivo, "rb") as f:
            ponto = pickle.load(f)
        return ponto
    else:
        return Ponto(nome)
