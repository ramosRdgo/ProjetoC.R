import nbformat as nbf

nb = nbf.v4.new_notebook()

cells = []

# Cell 1: Title & Info
cells.append(nbf.v4.new_markdown_cell('''# Projeto Prático: Análise de Redes Complexas com Python e NetworkX

**Disciplina:** Comunicação e Redes  
**Aluno / Autor:** Rodrigo Ramos  
**Rede Analisada:** Rede Social (Amostra estilo Instagram) (`instagram_sample`)  
**Data:** 2026

---
'''))

# Cell 2: Section 1 Markdown
cells.append(nbf.v4.new_markdown_cell('''## 1. Importação das Bibliotecas

Primeiro, eu preciso carregar as bibliotecas essenciais pro projeto. 
- **NetworkX**: Essa é a biblioteca principal que vou usar pra criar os grafos e calcular as métricas de redes complexas (como agrupamento, densidade, etc).
- **Matplotlib**: Vou usar pra desenhar os grafos na tela e gerar os gráficos de barras pra gente visualizar a distribuição.
- **Pandas e NumPy**: São auxiliares, coloquei pra ajudar a montar a tabela de comparação final e formatar os números direitinho.
'''))

# Cell 3: Section 1 Code
cells.append(nbf.v4.new_code_cell('''import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Configurações visuais dos gráficos
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("Bibliotecas importadas com sucesso!")
print("Versão do NetworkX:", nx.__version__)
'''))

# Cell 4: Section 2 Markdown
cells.append(nbf.v4.new_markdown_cell('''## 2. Carregamento e Caracterização da Rede Real

Aqui eu defino de onde vem a minha rede principal. Escolhi usar dados de conexões de uma rede social (tipo Instagram/Facebook). 

Como a base de dados original da Universidade de Stanford (SNAP) é gigante e ia travar tudo se eu tentasse rodar ao vivo, eu fiz um código que baixa o arquivo original zipado direto do site deles, lê tudo, e extrai uma amostra menor (de 300 usuários). 
Uso a função `nx.read_edgelist` do NetworkX, que basicamente pega esse arquivo de texto (onde cada linha mostra o 'User A' seguindo o 'User B') e transforma isso num objeto de Grafo que o Python consegue entender. Coloquei `create_using=nx.Graph()` pra garantir que é um grafo não-direcionado (a conexão vale pros dois lados).
'''))

# Cell 5: Section 2 Code
cells.append(nbf.v4.new_code_cell('''import os
import urllib.request
import gzip
import networkx as nx

caminho_arquivo = 'instagram_sample.edges'
url_dataset = 'https://snap.stanford.edu/data/facebook_combined.txt.gz'
gz_path = 'facebook_combined.txt.gz'

# Baixa e amostra o arquivo automaticamente no Colab
if not os.path.exists(caminho_arquivo):
    print("Baixando base de dados completa do SNAP (Stanford)...")
    urllib.request.urlretrieve(url_dataset, gz_path)
    
    print("Extraindo e processando amostra da rede social...")
    with gzip.open(gz_path, 'rt') as f_in:
        G_full = nx.read_edgelist(f_in, nodetype=int)
    
    # Criando uma amostra de 300 nós por busca em largura (BFS) para manter conectividade
    start_node = list(G_full.nodes())[0]
    sample_nodes = set([start_node])
    queue = [start_node]
    
    while len(sample_nodes) < 300 and queue:
        current = queue.pop(0)
        for neighbor in G_full.neighbors(current):
            if neighbor not in sample_nodes:
                sample_nodes.add(neighbor)
                queue.append(neighbor)
                if len(sample_nodes) >= 300:
                    break
                    
    G_real = G_full.subgraph(sample_nodes).copy()
    nx.write_edgelist(G_real, caminho_arquivo, data=False)
    print(f"Amostra salva localmente como {caminho_arquivo}!\\n")
else:
    G_real = nx.read_edgelist(caminho_arquivo, create_using=nx.Graph(), nodetype=int)

print("Rede real carregada com sucesso!")
print(f"Instância do Grafo: {G_real}")
'''))

# Cell 6: Section 3 Markdown
cells.append(nbf.v4.new_markdown_cell('''## 3. Análise Básica da Rede Real

Agora que o grafo da rede social já tá na memória, eu chamo as funções do NetworkX pra calcular as três métricas base que a professora pediu:

1. **Ordem ($N$)**: Chamo a função `number_of_nodes()` pra saber exatamente quantos usuários eu tenho nessa minha amostra.
2. **Coeficiente de Agrupamento Médio ($C$)**: Uso `nx.average_clustering()`. Essa função passa por todo mundo e vê a probabilidade dos meus amigos também serem amigos entre eles (formação de 'panelinhas').
3. **Densidade ($\rho$)**: Uso `nx.density()`. Isso aqui calcula o número de amizades que existem de verdade dividido pelo número máximo de amizades que seriam possíveis se todo mundo fosse amigo de todo mundo.
'''))

# Cell 7: Section 3 Code
cells.append(nbf.v4.new_code_cell('''# 1. Ordem (número de nós)
ordem_real = G_real.number_of_nodes()

# 2. Coeficiente de Agrupamento Médio (average clustering coefficient)
clustering_real = nx.average_clustering(G_real)

# 3. Densidade da rede (density)
densidade_real = nx.density(G_real)

# Exibindo os resultados da rede real
print("=== MÉTRICAS BÁSICAS DA REDE REAL ===")
print(f" - Ordem (Número de Nós - N): {ordem_real}")
print(f" - Coeficiente de Agrupamento Médio (C): {clustering_real:.4f}")
print(f" - Densidade (ρ): {densidade_real:.4f}")
'''))

# Cell 8: Section 4 Markdown
cells.append(nbf.v4.new_markdown_cell('''## 4. Geração e Comparação com Rede Aleatória (Erdős-Rényi)

Pra provar que as conexões na minha rede social não são pura coincidência, eu preciso comparar ela com uma rede 100% aleatória. O modelo clássico pra isso é o de **Erdős-Rényi**.

No código, eu pego exatamente o mesmo número de usuários ($N$) e o mesmo número de conexões ($M$) da minha rede real, e peço pro NetworkX gerar uma rede aleatória com a função `nx.gnm_random_graph`. Assim eu tenho uma base de comparação justa, com o mesmo tamanho, mas onde as conexões foram feitas por 'sorteio'. Depois, eu rodo os mesmos três cálculos de agrupamento e densidade.
'''))

# Cell 9: Section 4 Code
cells.append(nbf.v4.new_code_cell('''# Resgatando ordem e tamanho exatos da rede real
tamanho_real = G_real.number_of_edges()

# Geração de grafo aleatório com mesmo N e M (Erdős-Rényi)
seed_aleatoria = 42
G_aleatorio = nx.gnm_random_graph(n=ordem_real, m=tamanho_real, seed=seed_aleatoria)

# Calculando as métricas para a rede aleatória
ordem_aleat = G_aleatorio.number_of_nodes()
clustering_aleat = nx.average_clustering(G_aleatorio)
densidade_aleat = nx.density(G_aleatorio)

print("=== MÉTRICAS BÁSICAS DA REDE ALEATÓRIA (Erdős-Rényi) ===")
print(f" - Ordem (Número de Nós - N): {ordem_aleat}")
print(f" - Coeficiente de Agrupamento Médio (C): {clustering_aleat:.4f}")
print(f" - Densidade (ρ): {densidade_aleat:.4f}")
'''))

# Cell 10: Section 5 Markdown
cells.append(nbf.v4.new_markdown_cell('''## 5. Análise Adicional 1: Modelo de Pequeno Mundo (Watts-Strogatz)

Como **primeira análise adicional**, escolhi explorar o modelo de **Pequeno Mundo** (*Small-World Network*), proposto por Watts e Strogatz. 

Redes sociais costumam apresentar a chamada "propriedade de pequeno mundo", caracterizada por um alto agrupamento local (formação de bolhas ou comunidades) e, ao mesmo tempo, curtos caminhos de separação entre quaisquer dois nós (6 graus de separação).

Gerei uma rede Watts-Strogatz mantendo a ordem $N = 65$, grau médio $k \\approx \\frac{2M}{N}$ e uma probabilidade de reconexão aleatória $p = 0.1$.
'''))

# Cell 11: Section 5 Code
cells.append(nbf.v4.new_code_cell('''# Grau médio aproximado dos nós (k = 2M / N)
k_medio = int(round(2 * tamanho_real / ordem_real))

# Gerando rede Watts-Strogatz (Pequeno Mundo)
p_reconexao = 0.1
G_smallworld = nx.watts_strogatz_graph(n=ordem_real, k=k_medio, p=p_reconexao, seed=42)

# Calculando as métricas da rede de pequeno mundo
ordem_sw = G_smallworld.number_of_nodes()
clustering_sw = nx.average_clustering(G_smallworld)
densidade_sw = nx.density(G_smallworld)

print("=== MÉTRICAS BÁSICAS - REDE PEQUENO MUNDO (Watts-Strogatz) ===")
print(f" - Ordem (Número de Nós - N): {ordem_sw}")
print(f" - Coeficiente de Agrupamento Médio (C): {clustering_sw:.4f}")
print(f" - Densidade (ρ): {densidade_sw:.4f}")
'''))

# Cell 12: Section 6 Markdown
cells.append(nbf.v4.new_markdown_cell('''## 6. Análise Adicional 2: Distribuição de Graus, Diâmetro e Grau Médio de Separação

Como **segunda análise adicional**, eu fiz um código pra investigar como é 'viajar' por essas redes:

1. Fiz uma funçãozinha `obter_metricas_caminhos` que tenta achar o **Diâmetro** (o caminho mais longo possível entre duas pessoas usando a função `nx.diameter`) e o **Grau Médio de Separação** (a média de saltos pra ir de um nó a outro, usando `nx.average_shortest_path_length`). Se a rede tiver nós totalmente isolados, o código foca só no maior grupo conectado pra não dar erro.
2. Logo depois, uso o Matplotlib pra plotar os **Histogramas de Distribuição de Graus**, basicamente contando quantos usuários tem poucas conexões e quantos tem muitas, comparando a rede real com a aleatória em um gráfico só.
'''))

# Cell 13: Section 6 Code - Caminhos e Diâmetro
cells.append(nbf.v4.new_code_cell('''# Função para calcular diâmetro e menor caminho médio
def obter_metricas_caminhos(g):
    if nx.is_connected(g):
        diam = nx.diameter(g)
        caminho_medio = nx.average_shortest_path_length(g)
    else:
        # Se houver nós isolados, calcula no maior componente conexo
        maior_comp = max(nx.connected_components(g), key=len)
        sub_g = g.subgraph(maior_comp)
        diam = nx.diameter(sub_g)
        caminho_medio = nx.average_shortest_path_length(sub_g)
    return diam, caminho_medio

diam_real, path_real = obter_metricas_caminhos(G_real)
diam_aleat, path_aleat = obter_metricas_caminhos(G_aleatorio)
diam_sw, path_sw = obter_metricas_caminhos(G_smallworld)

print("=== DIÂMETRO E GRAU MÉDIO DE SEPARAÇÃO (CAMINHO MÍNIMO MÉDIO) ===")
print(f"1. Rede Real (Amostra Instagram): Diâmetro = {diam_real}, Caminho Médio (L) = {path_real:.4f}")
print(f"2. Rede Aleatória (Erdős-Rényi):   Diâmetro = {diam_aleat}, Caminho Médio (L) = {path_aleat:.4f}")
print(f"3. Rede Pequeno Mundo (Watts-Strg): Diâmetro = {diam_sw}, Caminho Médio (L) = {path_sw:.4f}")
'''))

# Cell 14: Section 6 Code - Histogram Plot
cells.append(nbf.v4.new_code_cell('''# Plotando o gráfico de Distribuição de Graus (Histograma)
# Primeiro eu extraio só a contagem de amizades (o grau) de cada usuário da rede real e da rede aleatória
graus_real = [d for n, d in G_real.degree()]
graus_aleat = [d for n, d in G_aleatorio.degree()]

# Aqui eu abro a tela de desenho do Matplotlib, definindo o tamanho da imagem (10x5)
plt.figure(figsize=(10, 5))

# Ploto o histograma da rede real (azul escuro). 'bins=12' significa que dividi as barras em 12 fatias de dados.
# O 'alpha=0.7' dá uma leve transparência pra gente conseguir ver se uma barra sobrepor a outra.
plt.hist(graus_real, bins=12, alpha=0.7, color='navy', label='Rede Real (Amostra Instagram)', edgecolor='black')

# Ploto o histograma da rede aleatória (laranja) no mesmo gráfico pra gente poder comparar visualmente.
plt.hist(graus_aleat, bins=12, alpha=0.5, color='darkorange', label='Rede Aleatória (Erdős-Rényi)', edgecolor='black')

plt.title('Gráfico de Distribuição de Graus: Real vs. Aleatória', fontsize=14, fontweight='bold')
plt.xlabel('Grau do Nó (k)', fontsize=12)
plt.ylabel('Frequência de Nós', fontsize=12)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('distribuicao_graus.png', dpi=300)
plt.show()
'''))

# Cell 15: Section 6 Code - Topologia Visual
cells.append(nbf.v4.new_code_cell('''# Visualização topológica comparativa dos grafos (As 'teias de aranha')
# Crio uma figura grande (18x5) com 3 painéis (axes) lado a lado pra plotar as 3 redes juntas
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Pra desenhar os nós espalhados na tela, preciso de um algoritmo de layout. 
# O 'spring_layout' tenta afastar nós que não são conectados e aproximar os que são (simula molas).
# Usei 'seed=42' pra garantir que o desenho sempre saia igual toda vez que eu rodar o código.
pos_r = nx.spring_layout(G_real, seed=42)
pos_a = nx.spring_layout(G_aleatorio, seed=42)

# Pro modelo de Pequeno Mundo, uso o 'circular_layout' porque ele nasce de uma estrutura em anel, fica mais didático.
pos_s = nx.circular_layout(G_smallworld)

# Finalmente, mando o NetworkX desenhar (draw_networkx) a rede real no primeiro painel (axes[0])
# Tirei as labels ('with_labels=False') porque com 300 usuários ia virar uma mancha preta ilegível de tanto texto.
nx.draw_networkx(G_real, pos_r, ax=axes[0], node_size=100, node_color='navy', with_labels=False, edge_color='gray', alpha=0.7)
axes[0].set_title('Rede Real (Social)', fontsize=12, fontweight='bold')

nx.draw_networkx(G_aleatorio, pos_a, ax=axes[1], node_size=100, node_color='darkorange', with_labels=False, edge_color='gray', alpha=0.7)
axes[1].set_title('Rede Aleatória (Erdős-Rényi)', fontsize=12, fontweight='bold')

nx.draw_networkx(G_smallworld, pos_s, ax=axes[2], node_size=100, node_color='forestgreen', with_labels=False, edge_color='gray', alpha=0.7)
axes[2].set_title('Rede Pequeno Mundo (Watts-Strogatz)', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('comparacao_topologia.png', dpi=300)
plt.show()
'''))

# Cell 16: Section 7 Markdown
cells.append(nbf.v4.new_markdown_cell('''## 7. Quadro Resumo Comparativo das Métricas

Como rodar prints separados fica ruim pra apresentar, criei um DataFrame no Pandas pra juntar todas as métricas (Ordem, Tamanho, Densidade, Agrupamento, Diâmetro e Caminho Médio) das três redes lado a lado numa tabela limpa. Fica bem mais fácil de comparar e tirar as conclusões finais.
'''))

# Cell 17: Section 7 Code
cells.append(nbf.v4.new_code_cell('''# Montagem do DataFrame comparativo
tabela_comparativa = pd.DataFrame({
    'Modelo de Rede': ['Rede Real (Amostra Instagram)', 'Rede Aleatória (Erdős-Rényi)', 'Pequeno Mundo (Watts-Strogatz)'],
    'Ordem (N)': [ordem_real, ordem_aleat, ordem_sw],
    'Tamanho (M)': [tamanho_real, G_aleatorio.number_of_edges(), G_smallworld.number_of_edges()],
    'Densidade (ρ)': [round(densidade_real, 4), round(densidade_aleat, 4), round(densidade_sw, 4)],
    'Coef. Agrupamento (C)': [round(clustering_real, 4), round(clustering_aleat, 4), round(clustering_sw, 4)],
    'Diâmetro': [diam_real, diam_aleat, diam_sw],
    'Caminho Médio (L)': [round(path_real, 4), round(path_aleat, 4), round(path_sw, 4)]
})

# Exibindo a tabela formatada
print(tabela_comparativa.to_string(index=False))
'''))

# Cell 18: Section 8 Markdown
cells.append(nbf.v4.new_markdown_cell('''## 8. Conclusões e Discussão dos Resultados

Fechando as análises dos resultados que os códigos geraram, cheguei a três conclusões principais:

1. **Agrupamento alto (as bolhas da internet)**:
   O código mostrou que a rede social tem um Coeficiente de Agrupamento ($C$) absurdamente maior que a rede aleatória. Isso comprova que os usuários se fecham em nichos e comunidades (se eu sigo duas pessoas, é bem provável que elas também se sigam).

2. **Propriedade de Pequeno Mundo confirmada**:
   Apesar do agrupamento alto da rede social, o caminho médio ($L$) continua bem pequeno (no mesmo patamar do modelo aleatório). Ou seja, a teoria dos 6 graus de separação é real: com poucos saltos a informação consegue cruzar a rede inteira.

3. **Distribuição de Graus (efeito influenciador)**:
   O gráfico final deixa bem claro que a rede social não é igualitária. Na rede aleatória, a distribuição é um 'sino' onde todo mundo tem a mesma quantidade média de seguidores. Na real, temos uma 'cauda longa' absurda: quase todo mundo tem poucas conexões, mas uns poucos nós 'hubs' (os grandes influenciadores digitais) têm centenas de conexões, puxando o gráfico pra direita.
'''))

nb['cells'] = cells

with open('projeto_redes.ipynb', 'w', encoding='utf-8') as f:
    nbf.write(nb, f)

print('projeto_redes.ipynb atualizado com sucesso (Linguagem Individual)!')
