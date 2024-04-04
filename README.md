# Notion Code Generator

Um gerador de código simples que, através de informações obtidas do Notion, gera código em python para simplificar a criação de automações.

## Requisitos

- Python 3.6 ou superior
- Poetry
- Notion API Token (crie um arquivo .env e adicione o token como NOTION_APITOKEN)

## Como usar

1. Clone o repositório
2. Instale as dependências e o script com:
```bash
poetry install
```
3. Execute o script com notioncodegen com os parâmetros necessários

## Parâmetros

- --database_id ou -v (Obrigatório): ID da base de dados do Notion
- --output ou -o (Opcional): Nome do arquivo de saída (default: output.py)


## Exemplos

```bash
notioncodegen --database_id 123456789 --output output.py
```
