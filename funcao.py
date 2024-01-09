# Importando as bibliotecas necessárias
import pandas as pd
import pyautogui
import time

# Definindo a função 'preencher_tabela' que aceita um DataFrame 'tabela' como entrada
def preencher_tabela(tabela):
    
    # Iterando sobre as linhas do DataFrame 'tabela'
    for linha in tabela.index:
    
        # Pressionando a tecla 'tab' para selecionar o primeiro campo de preenchimento
        pyautogui.press('tab')
    
        # Configurando delay de (0.1 segundos) para preenchimento mais rapido
        pyautogui.PAUSE = 0.1
    
        # Iterando sobre as colunas especificadas
        colunas = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo"]
        for coluna in colunas:
    
            # Obtendo o valor da célula correspondente na linha e coluna e convertendo para string
            codigo = str(tabela.loc[linha, coluna])
    
            # Digitando o valor no campo atual e pressionando 'tab'
            pyautogui.write(codigo)
            pyautogui.press('tab')
    
        # Tratando o preenchimento do campo "obs"
        obs = tabela.loc[linha, "obs"]
        if not pd.isna(obs):  # Verificando se o valor não é um NaN (nulo)
            pyautogui.write(obs)
    
        # Pressionando 'tab' e 'enter' para enviar
        pyautogui.press('tab')
        pyautogui.press('enter')
    
        # Aguardando 1 segundo antes de prosseguir para a próxima iteração
        time.sleep(1)
    
        # Loop para retornar ao campo inicial e continuar preenchendo (pressiona 'shift'+'tab' 8 vezes)
        for _ in range(8):
            pyautogui.hotkey('shift', 'tab')
