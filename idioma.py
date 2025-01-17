import locale
import os
import platform
import unicodedata

# Função para remover caracteres especiais
def remover_caracteres_especiais(texto):
    return ''.join((c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn'))

# Obtém a versão do Windows
versao_windows = platform.version()

# Obtém o idioma do sistema
idioma_sistema = locale.getdefaultlocale()[0]

# Normaliza o idioma para remover caracteres especiais
idioma_sistema = remover_caracteres_especiais(idioma_sistema)

# Caminho para salvar o log diretamente em C:\Windows\Temp
caminho_log = os.path.join('C:\\', 'Windows', 'Temp', 'Idioma.txt')

# Abre o arquivo em modo de escrita
try:
    with open(caminho_log, 'w', encoding='utf-8') as file:
        # Escreve a versão do Windows e o idioma
        file.write(f"{idioma_sistema}\n")

    print(f"Informações salvas em: {caminho_log}")

except FileNotFoundError as e:
    print(f"Erro ao salvar o arquivo: {e}")
