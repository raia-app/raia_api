#Raia API

1-Pra quem é o Raia? Para atletas amadores acompanharem sua evolução a partir de dados.
2-Qual problema essa pessoa tem hoje? Dificuldade de medir a própria evolução de maneira fácil.
3-O que ela consegue fazer com Raia? Consegue registrar seus dados diretamente, sem um smart watch, ou inserindo a partir dos arquivos
exportados do .fit

## Instalação

Requisitos: Python 3.15 ou mais novo e Git.

```
git clone https://github.com/raia-app/raia_api.git
cd raia_api
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --group dev
```

No Linux ou no macOS, troque a quarta linha por `source .venv/bin/activate`.

## Conferir o código

```
ruff check .
pytest
```