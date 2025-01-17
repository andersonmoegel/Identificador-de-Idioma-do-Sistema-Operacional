# Identificador do Sistema Operacional e seu Idioma

Este código é uma ferramenta desenvolvida para uso empresarial em plataformas que executam scripts. Ele captura informações sobre o sistema operacional, incluindo a versão do Windows e o idioma do sistema, e registra essas informações em um arquivo de log.

## Funcionalidades

- **Remoção de Caracteres Especiais**: O código normaliza o idioma do sistema para remover caracteres especiais, garantindo que os dados sejam salvos de forma limpa.
- **Registro de Informações**: Salva a versão do Windows e o idioma do sistema em um arquivo de texto no diretório `C:\Windows\Temp\Idioma.txt`.
- **Tratamento de Erros**: Inclui tratamento de exceções para lidar com possíveis erros ao salvar o arquivo.

## Uso

Para utilizar o código, basta executá-lo em um ambiente Python. As informações serão automaticamente salvas no caminho especificado.

### Reativando a funcionalidade de mostrar o nome do sistema operacional

A funcionalidade que exibe o nome do sistema operacional está disponível, mas foi ocultada para atender a requisitos específicos. Para reativá-la, você pode descomentar a linha correspondente no código:

```python
# Adicione esta linha para mostrar o nome do sistema operacional
# print(f"Nome do Sistema Operacional: {platform.system()}")
```

## Requisitos

- Python 3.x
- Bibliotecas padrão: `locale`, `os`, `platform`, `unicodedata`

## Execução

1. Certifique-se de que o Python esteja instalado em sua máquina.
2. Copie o código para um arquivo Python (por exemplo, `salvar_idioma.py`).
3. Execute o script usando o terminal ou prompt de comando:

   ```bash
   python idioma.py
   ```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou relatar problemas.

## Licença

Este projeto é de uso livre e não possui restrições de licença.
