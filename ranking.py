# ranking.py
import json
import os

ARQUIVO_RANKING = 'ranking.json'

def carregar_ranking():
    if os.path.exists(ARQUIVO_RANKING):
        try:
            with open(ARQUIVO_RANKING, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def salvar_pontuacao(nome, pontos, tempo):
    if not nome.strip():
        nome = "Anônimo"
        
    ranking = carregar_ranking()
    novo_registro = {"nome": nome, "pontos": pontos, "tempo": tempo}
    ranking.append(novo_registro)
    
    # Critérios de ordenação:
    # 1. Pontos em ordem decrescente (-x['pontos']) -> Mais pontos fica primeiro
    # 2. Tempo em ordem crescente (x['tempo']) -> Menos tempo fica primeiro (em caso de empate nos pontos)
    # A ordenação do Python é estável, preservando a ordem de chegada se os pontos e tempo forem idênticos.
    ranking.sort(key=lambda x: (-x['pontos'], x['tempo']))
    
    # Mantém apenas os 5 melhores
    ranking = ranking[:5]
    
    with open(ARQUIVO_RANKING, 'w', encoding='utf-8') as f:
        json.dump(ranking, f, ensure_ascii=False, indent=4)