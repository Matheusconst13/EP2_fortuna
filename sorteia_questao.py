import random

def valida_questao(questao):
    validacao = {}
    if 'titulo' not in questao:
        validacao['titulo'] = 'nao_encontrado'
    if 'nivel' not in questao:
        validacao['nivel'] = 'nao_encontrado'
    if 'opcoes' not in questao:
        validacao['opcoes'] = 'nao_encontrado'
    if 'correta' not in questao:
        validacao['correta'] = 'nao_encontrado'



    if len(questao) != 4:
        validacao['outro'] = 'numero_chaves_invalido'



    if 'titulo' in questao and (not questao['titulo'].strip()):
        validacao['titulo'] = 'vazio'



    if 'nivel' in questao and questao['nivel'] not in ['facil', 'medio', 'dificil']:
        validacao['nivel'] = 'valor_errado'



    if 'opcoes' in questao and len(questao['opcoes']) != 4:
        validacao['opcoes'] = 'tamanho_invalido'
    elif 'opcoes' in questao:


        opcoes_validas = {'A', 'B', 'C', 'D'}
        opcoes_presentes = set(questao['opcoes'].keys())
        if opcoes_validas != opcoes_presentes:
            validacao['opcoes'] = 'chave_invalida_ou_nao_encontrada'
        else:


            respostas_vazias = {letra for letra, resposta in questao['opcoes'].items() if not resposta.strip()}
            if respostas_vazias:
                validacao['opcoes'] = {letra: 'vazia' for letra in respostas_vazias}


    if 'correta' in questao and questao['correta'] not in {'A', 'B', 'C', 'D'}:
        validacao['correta'] = 'valor_errado'

    return validacao


def valida_questoes(questoes):
    problemas_questoes = []

    for questao in questoes:
        problemas = valida_questao(questao)
        problemas_questoes.append(problemas)

    return problemas_questoes

def sorteia_questao(questoes, nivel):
    
    if nivel in questoes:
        questoes_nivel = questoes[nivel]
        questao_sorteada = random.choice(questoes_nivel)
        return questao_sorteada
    