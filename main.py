import pandas as pd
import pyautogui
import time
import funcao # importando arquivo que contém a função "preencher_tabela()"

# delay para os comandos globais
pyautogui.PAUSE = 0.5 

# Abrindo o chrome no windows
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# Acessando o portal
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(2)

# Selecionando o campo de usuário
pyautogui.press('tab') 

# Digitando usuário e senha
pyautogui.write('test2@gmail.com')
pyautogui.press('tab')
pyautogui.write('test123')
pyautogui.press('tab')

# Logando
pyautogui.press('enter')
time.sleep(2)

# Importando tabela produtos e lendo
tabela = pd.read_csv('produtos.csv')
print(tabela) # Print somente para conhecimento e visualização da tabela no terminal. Não influencia no código

funcao.preencher_tabela(tabela) 

