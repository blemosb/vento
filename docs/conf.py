# Arquivo de configuração do Sphinx

# Importações necessárias
import os
import sys

# Adiciona o diretório raiz do seu projeto ao caminho de busca do Python
sys.path.insert(0, os.path.abspath('.'))

# Configurações do projeto
project = 'Ilha Proibida'
author = 'Grupo Vento'

# Outras configurações do Sphinx
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    # ... outras extensões necessárias para a documentação
]

# Configuração do tema da documentação (opcional)
html_theme = 'sphinx_rtd_theme'  # Exemplo usando o tema Read the Docs

# Mais configurações do Sphinx (se necessário)

# Configuração para gerar automaticamente a documentação a partir de docstrings (opcional)
autodoc_default_flags = [
    'members',
    'undoc-members',
    'private-members',
    'show-inheritance'
]
