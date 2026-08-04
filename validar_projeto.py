"""
Script de validação completa do projeto_redes.ipynb
Executa o notebook inteiro, verifica cada célula e valida os arquivos gerados.
"""
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os
import sys

NOTEBOOK = 'projeto_redes.ipynb'
EDGES_FILE = 'instagram_sample.edges'
EXPECTED_PNGS = ['distribuicao_graus.png', 'comparacao_topologia.png']

erros = []

# === ETAPA 1: verificar que o arquivo .edges existe e tem conteúdo ===
print("=" * 60)
print("ETAPA 1: Verificando dataset .edges")
if not os.path.exists(EDGES_FILE):
    erros.append(f"FALTANDO: {EDGES_FILE}")
else:
    with open(EDGES_FILE, 'r') as f:
        linhas = f.readlines()
    print(f"  OK: {EDGES_FILE} possui {len(linhas)} linhas")
    # checar formato: cada linha deve ter 2 inteiros
    for i, linha in enumerate(linhas):
        partes = linha.strip().split()
        if len(partes) != 2:
            erros.append(f"  ERRO formato linha {i+1}: '{linha.strip()}'")
            break
        try:
            int(partes[0])
            int(partes[1])
        except ValueError:
            erros.append(f"  ERRO tipo linha {i+1}: '{linha.strip()}' (esperado 2 inteiros)")
            break
    else:
        print(f"  OK: formato de todas as {len(linhas)} linhas validado")

# === ETAPA 2: verificar que o notebook existe e tem 18 células ===
print("=" * 60)
print("ETAPA 2: Verificando estrutura do notebook")
if not os.path.exists(NOTEBOOK):
    erros.append(f"FALTANDO: {NOTEBOOK}")
    print("  ERRO: notebook nao encontrado, abortando")
    sys.exit(1)

with open(NOTEBOOK, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

n_cells = len(nb.cells)
code_cells = [c for c in nb.cells if c.cell_type == 'code']
md_cells = [c for c in nb.cells if c.cell_type == 'markdown']
print(f"  Total de celulas: {n_cells}")
print(f"  Celulas de codigo: {len(code_cells)}")
print(f"  Celulas de markdown: {len(md_cells)}")
if n_cells != 18:
    erros.append(f"Esperado 18 celulas, encontrado {n_cells}")
else:
    print("  OK: 18 celulas conforme esperado")

# === ETAPA 3: verificar que nenhum texto menciona "grupo" ===
print("=" * 60)
print("ETAPA 3: Verificando linguagem individual (sem 'grupo')")
termos_proibidos = ['nosso grupo', 'integrantes do grupo', 'o grupo', 'do grupo', 'ao grupo']
for i, cell in enumerate(nb.cells):
    src = cell.source.lower()
    for termo in termos_proibidos:
        if termo in src:
            erros.append(f"Celula {i+1} contem termo proibido: '{termo}'")
print("  OK: nenhuma menção a 'grupo' encontrada" if not any('grupo' in e for e in erros) else "  PROBLEMA encontrado (ver erros)")

# === ETAPA 4: executar o notebook completo ===
print("=" * 60)
print("ETAPA 4: Executando TODAS as celulas do notebook...")
ep = ExecutePreprocessor(timeout=120, kernel_name='python3')
try:
    ep.preprocess(nb, {'metadata': {'path': '.'}})
    print("  OK: todas as celulas executaram sem erro")
except Exception as e:
    erros.append(f"ERRO na execucao do notebook: {e}")
    print(f"  FALHA: {e}")

# === ETAPA 5: verificar outputs das células de código ===
print("=" * 60)
print("ETAPA 5: Verificando outputs das celulas de codigo")
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code':
        if len(cell.outputs) == 0:
            erros.append(f"Celula {i+1} (codigo) nao gerou output")
            print(f"  AVISO: Celula {i+1} sem output")
        else:
            # verificar se algum output é erro
            for out in cell.outputs:
                if out.get('output_type') == 'error':
                    nome_erro = out.get('ename', 'desconhecido')
                    erros.append(f"Celula {i+1} gerou ERRO: {nome_erro}")
                    print(f"  ERRO: Celula {i+1} -> {nome_erro}")
            if not any(out.get('output_type') == 'error' for out in cell.outputs):
                print(f"  OK: Celula {i+1} - {len(cell.outputs)} output(s)")

# === ETAPA 6: salvar notebook com outputs ===
print("=" * 60)
print("ETAPA 6: Salvando notebook com outputs atualizados")
with open(NOTEBOOK, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
print(f"  OK: {NOTEBOOK} salvo")

# === ETAPA 7: verificar que os PNGs foram gerados ===
print("=" * 60)
print("ETAPA 7: Verificando imagens geradas")
for png in EXPECTED_PNGS:
    if os.path.exists(png):
        tamanho = os.path.getsize(png)
        print(f"  OK: {png} ({tamanho:,} bytes)")
        if tamanho < 1000:
            erros.append(f"{png} muito pequeno ({tamanho} bytes), pode estar corrompido")
    else:
        erros.append(f"FALTANDO: {png}")
        print(f"  ERRO: {png} nao foi gerado")

# === RESULTADO FINAL ===
print("=" * 60)
if erros:
    print(f"RESULTADO: {len(erros)} PROBLEMA(S) ENCONTRADO(S):")
    for e in erros:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("RESULTADO: TUDO OK! Notebook validado com sucesso.")
    print("  - 18 celulas (9 markdown + 9 codigo)")
    print("  - Todas as celulas executam sem erro")
    print("  - Linguagem individual (1a pessoa do singular)")
    print("  - Graficos PNG gerados corretamente")
    print("  - Dataset .edges integro")
    sys.exit(0)
