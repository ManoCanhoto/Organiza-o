# 📂 Automação de Renomeação de Atestados com Python

Este projeto foi desenvolvido para automatizar a organização de arquivos de atestados médicos recebidos por e-mail, que normalmente chegam em formatos diferentes e com nomes despadronizados.

O script percorre automaticamente uma pasta contendo **PDFs e imagens**, identifica a **data presente no documento** e renomeia os arquivos seguindo um padrão organizado.

## 🚀 Objetivo

Facilitar a organização de documentos e reduzir o tempo gasto com tarefas manuais de renomeação de arquivos.

Antes da automação:
SAMUEL LINS SANHO 090326.jpeg
SANDRA BEZERRA.jfif
SARA TAIS DE LIMA BASTOS.jpg

Depois da automação:
Samuel_Lins_11-03-2026.jpeg
Sandra_Bezerra_13-03-2026.jfif
Sara_Tais_11-03-2026.jpg


## ⚙️ Tecnologias utilizadas

- Python
- Regex (Expressões Regulares)
- Manipulação de arquivos
- Biblioteca **PyMuPDF** para leitura de PDFs

## 📌 Funcionalidades

✔️ Acessa automaticamente uma pasta de arquivos  
✔️ Lê o conteúdo de arquivos **PDF**  
✔️ Identifica padrões de data dentro do documento  
✔️ Padroniza o nome dos arquivos  
✔️ Renomeia automaticamente os arquivos

▶️ Como usar

Clone o repositório

git clone https://github.com/seuusuario/seu-repositorio.git

Instale as dependências

pip install pymupdf

Configure o caminho da pasta no script

caminho_pasta = r"CAMINHO_DA_SUA_PASTA"

Execute o script

python organizar.py

