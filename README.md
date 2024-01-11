# Automação de Preenchimento de Tabela Web #

Este script Python utiliza a biblioteca PyAutoGUI para automatizar a interação com o navegador Google Chrome, preenchendo dados em um portal web. O objetivo é efetuar login, acessar um portal específico e preencher uma tabela com dados provenientes de um arquivo CSV.

# Pré-requisitos #
Certifique-se de ter as seguintes bibliotecas instaladas antes de executar o script:

_• pip install pandas
• pip install pyautogui_

# Utilização #
**1. Configuração do Ambiente**
• Abra um terminal e navegue até o diretório onde o script está localizado.

**2. Execução do Script**
• Execute o script utilizando um interpretador Python.
• _python nome_do_script.py_

**3. Aguarde a Execução**
O script abrirá o navegador Chrome, acessará um portal específico, preencherá campos de usuário e senha, e, em seguida, preencherá uma tabela com dados provenientes de um arquivo CSV.

**4. Observações**
• Certifique-se de ter o navegador Google Chrome instalado no sistema.
• O script pausará por alguns segundos entre os comandos para garantir a execução correta. Ajuste o tempo de pausa conforme necessário.
• O código assume que existe uma função preencher_tabela() no arquivo funcao.py. Certifique-se de que esse arquivo e a função estão corretamente implementados.

**5. Saída**
• O script imprime a tabela carregada a partir do arquivo CSV no terminal para fins de visualização.


Lembre-se de utilizar esse tipo de automação de forma ética e em conformidade com os termos de serviço do site que está sendo acessado.
