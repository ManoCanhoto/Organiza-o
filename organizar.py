import os
import re
import shutil
from datetime import datetime

# 1. Configurações de Caminho
caminho_origem = ""
caminho_destino = os.path.join(caminho_origem, "ARQUIVOS_FORMATADOS")

# Cria a pasta de destino se ela não existir
if not os.path.exists(caminho_destino):
    os.makedirs(caminho_destino)
    print(f"✅ Pasta criada: {caminho_destino}")

def extrair_data_pdf(caminho_arquivo):
    if not FITZ_DISPONIVEL:
        return None
    try:
        doc = fitz.open(caminho_arquivo)
        texto = "".join([pagina.get_text() for pagina in doc])
        doc.close()
        # Busca padrão DD/MM/2026 ou DD-MM-2026
        datas = re.findall(r'(\d{2})[/-](\d{2})[/-](2026)', texto)
        if datas:
            return f"{datas[0][0]}-{datas[0][1]}-{datas[0][2]}"
    except:
        return None
    return None

def limpar_nome(nome_arquivo):
    # Remove a extensão e caracteres especiais
    nome_sem_ext = os.path.splitext(nome_arquivo)[0]
    apenas_letras = re.sub(r'[^a-zA-ZÀ-ÿ\s]', ' ', nome_sem_ext)
    
    # Lista de palavras que NÃO são nomes e devem ser ignoradas
    palavras_sujeira = [
        'atestado', 'medico', 'foto', 'documento', 'urgente', 
        'atest', 'pdf', 'jpg', 'png', 'imagem', 'whatsapp', 'final'
    ]
    
    # Filtra: mantém apenas palavras que não são "sujeira" e não são números
    partes = [p for p in apenas_letras.split() if p.lower() not in palavras_sujeira]
    
    if len(partes) >= 2:
        # Pega o primeiro e o segundo nome encontrado
        return f"{partes[0].capitalize()}_{partes[1].capitalize()}"
    elif len(partes) == 1:
        return partes[0].capitalize()
    
    return "Funcionario_Nao_Identificado"

# --- EXECUÇÃO ---
print("🚀 Iniciando processamento...")

for arquivo in os.listdir(caminho_origem):
    caminho_completo = os.path.join(caminho_origem, arquivo)
    
    # Pula pastas e arquivos temporários do Excel
    if os.path.isdir(caminho_completo) or arquivo.startswith('~$'):
        continue

    extensao = os.path.splitext(arquivo)[1].lower()
    
    # 1. Limpa o nome (Foca no funcionário)
    nome_base = limpar_nome(arquivo)
    
    # 2. Lógica de Data (Tenta PDF, se falhar usa data do sistema)
    data_final = None
    if extensao == ".pdf":
        data_final = extrair_data_pdf(caminho_completo)
    
    if not data_final:
        mtime = os.path.getmtime(caminho_completo)
        data_final = datetime.fromtimestamp(mtime).strftime('%d-%m-2026')

    # 3. Monta novo nome e move
    novo_nome = f"{nome_base}_{data_final}{extensao}"
    novo_caminho_completo = os.path.join(caminho_destino, novo_nome)

    try:
        shutil.move(caminho_completo, novo_caminho_completo)
        print(f"✔ Sucesso: {arquivo} -> {novo_nome}")
    except Exception as e:
        print(f"❌ Erro ao mover {arquivo}: {e}")    

print("\n✨ Tudo pronto ")
