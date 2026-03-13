import os
import re
import fitz  # PyMuPDF
from datetime import datetime

# 1. Seu caminho de rede
caminho_pasta = r #Endereço do aquivo 

def extrair_data_pdf(caminho_arquivo):
    """Tenta ler a data de emissão dentro do texto do PDF."""
    try:
        doc = fitz.open(caminho_arquivo)
        texto = ""
        for pagina in doc:
            texto += pagina.get_text()
        doc.close()
        
        # Procura padrões de data (Ex: 10/03/2026 ou 10-03-2026)
        datas = re.findall(r'(\d{2})[/-](\d{2})[/-](2026)', texto)
        if datas:
            dia, mes, ano = datas[0]
            return f"{dia}-{mes}-{ano}"
    except Exception as e:
        print(f"Erro ao ler PDF {caminho_arquivo}: {e}")
    return None

def limpar_nome(nome_arquivo):
    """Extrai apenas Nome e Sobrenome do nome atual do arquivo."""
    nome_sem_ext = os.path.splitext(nome_arquivo)[0]
    # Pega apenas letras e espaços, remove números e símbolos
    apenas_letras = re.sub(r'[^a-zA-ZÀ-ÿ\s]', ' ', nome_sem_ext)
    partes = apenas_letras.split()
    
    if len(partes) >= 2:
        return f"{partes[0].capitalize()}_{partes[1].capitalize()}"
    elif len(partes) == 1:
        return partes[0].capitalize()
    return "Arquivo_Sem_Nome"

# --- EXECUÇÃO PRINCIPAL ---
print("Iniciando organização...")

for arquivo in os.listdir(caminho_pasta):
    caminho_completo = os.path.join(caminho_pasta, arquivo)
    
    if os.path.isfile(caminho_completo):
        extensao = os.path.splitext(arquivo)[1].lower()
        nome_base = limpar_nome(arquivo)
        data_final = None

        # Lógica para PDF: Tenta ler por dentro
        if extensao == ".pdf":
            data_final = extrair_data_pdf(caminho_completo)
        
        # Lógica para outros arquivos (ou se o PDF falhou na leitura interna)
        if not data_final:
            mtime = os.path.getmtime(caminho_completo)
            data_final = datetime.fromtimestamp(mtime).strftime('%d-%m-2026')

        # Monta o novo nome seguindo o padrão: Nome_Sobrenome_DD-MM-2026
        novo_nome = f"{nome_base}_{data_final}{extensao}"
        novo_caminho = os.path.join(caminho_pasta, novo_nome)

        # Evita erro se o nome já for igual
        if arquivo != novo_nome:
            print(f"Renomeando: {arquivo} -> {novo_nome}")
            try:
                os.rename(caminho_completo, novo_caminho)
            except Exception as e:
                print(f"Não foi possível renomear {arquivo}: {e}")

print("\nConcluído!")