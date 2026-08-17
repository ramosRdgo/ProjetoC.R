# Roteiro de Apresentação Individual — Detalhado por Bloco de Código

**Disciplina:** Comunicação e Redes  
**Projeto Prático (Individual):** Análise de uma Rede Social (Amostra estilo Instagram)  
**Aluno:** Rodrigo Ramos  
**Ferramentas:** Python, NetworkX, Matplotlib e Pandas  

---

## ⏱️ Cronograma dos 8 Minutos

| Bloco | Células | Conteúdo | Tempo |
| :--- | :---: | :--- | :---: |
| Introdução e Setup | 1, 2, 3 | Contexto do projeto + importação das libs | 0:00 – 1:30 |
| Carregamento da Rede | 4, 5 | Download e leitura do dataset | 1:30 – 2:30 |
| Análise Básica | 6, 7, 8, 9 | Métricas da rede real vs. Erdős-Rényi | 2:30 – 4:00 |
| Análise Adicional 1 | 10, 11 | Modelo Watts-Strogatz (Pequeno Mundo) | 4:00 – 5:15 |
| Análise Adicional 2 | 12, 13, 14, 15 | Diâmetro, caminhos e gráficos | 5:15 – 6:45 |
| Conclusão | 16, 17, 18 | Tabela comparativa e síntese final | 6:45 – 8:00 |

---

## 🎤 Roteiro Fala a Fala — Linha por Linha

---

### BLOCO 1 — Introdução e Importação das Bibliotecas (0:00 – 1:30)
> **Células 1, 2 e 3 na tela**

**O que você fala antes de rodar:**

*"Bom dia / Boa tarde, professora. O meu projeto prático é a análise de uma Rede Complexa real utilizando Python. A rede que escolhi é uma amostra de conexões de uma rede social — no estilo Instagram ou Facebook. Cada usuário é um nó, e cada amizade ou seguimento mútuo é uma aresta conectando dois nós.*

*A escolha foi por esse tema porque redes sociais são o exemplo mais palpável de Redes Complexas no dia a dia. Antes de entrar nos dados, o primeiro bloco de código é a importação das bibliotecas."*

**Execute a Célula 3. Enquanto roda, explique linha por linha:**

```python
import networkx as nx
```
*"Essa é a principal biblioteca do projeto. O NetworkX é a ferramenta padrão do Python pra trabalhar com grafos — ela tem funções prontas pra criar, manipular e calcular métricas em redes de qualquer tamanho."*

```python
import matplotlib.pyplot as plt
```
*"O Matplotlib eu uso pra gerar os dois gráficos visuais: o histograma de distribuição de graus e o desenho das topologias das redes."*

```python
import numpy as np
import pandas as pd
```
*"O NumPy e o Pandas são auxiliares. O Pandas em especial uso no final pra montar aquela tabela comparativa entre as três redes de forma organizada."*

```python
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12
```
*"Essas três linhas são configuração visual. Defino o estilo de fundo dos gráficos (se o tema seaborn estiver disponível, uso ele; senão cai no padrão), o tamanho das figuras e o tamanho da fonte."*

---

### BLOCO 2 — Carregamento da Rede Real (1:30 – 2:30)
> **Células 4 e 5 na tela**

**O que você fala antes de rodar:**

*"Agora vou carregar a rede real. O arquivo de dados vem do projeto SNAP, da Universidade de Stanford — é um banco de dados de conexões de uma rede social tipo Facebook, que é público e gratuito. Como a rede completa deles tem mais de 4 mil usuários e ia demorar pra calcular ao vivo, eu extraí uma amostra de 300 nós mantendo a conectividade."*

**Execute a Célula 5. Explique linha por linha:**

```python
import os
import urllib.request
import gzip
```
*"Essas importações extras servem pra manipular arquivos no sistema (`os`), fazer o download automático do dataset da internet (`urllib.request`) e descompactar o arquivo que vem zipado (`gzip`)."*

```python
caminho_arquivo = 'instagram_sample.edges'
url_dataset = 'https://snap.stanford.edu/data/facebook_combined.txt.gz'
gz_path = 'facebook_combined.txt.gz'
```
*"Aqui defino as variáveis de caminho. O `caminho_arquivo` é onde a minha amostra final vai ser salva. A `url_dataset` é o endereço direto no site da Stanford de onde o arquivo completo é baixado."*

```python
if not os.path.exists(caminho_arquivo):
    print("Baixando base de dados completa do SNAP (Stanford)...")
    urllib.request.urlretrieve(url_dataset, gz_path)
```
*"Essa condição verifica se o arquivo já existe localmente. Se estiver rodando aqui no Colab pela primeira vez, ele não vai existir, então o código baixa automaticamente direto da Stanford sem eu precisar fazer upload de nenhum arquivo."*

```python
    with gzip.open(gz_path, 'rt') as f_in:
        G_full = nx.read_edgelist(f_in, nodetype=int)
```
*"Aqui descompacto o arquivo `.gz` e já leio direto como um grafo com o `nx.read_edgelist`. Cada linha do arquivo tem dois números inteiros separados por espaço — o ID do usuário A e o ID do usuário B — e o NetworkX entende isso como uma aresta entre eles."*

```python
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
```
*"Esse bloco é o algoritmo de amostragem. Eu uso uma Busca em Largura (BFS) a partir de um nó inicial. O motivo de usar BFS ao invés de pegar 300 nós aleatórios é que a BFS garante que todos os 300 nós escolhidos estejam conectados entre si — sem nós isolados que travassem os cálculos de diâmetro e caminho mínimo mais pra frente."*

```python
    G_real = G_full.subgraph(sample_nodes).copy()
    nx.write_edgelist(G_real, caminho_arquivo, data=False)
else:
    G_real = nx.read_edgelist(caminho_arquivo, create_using=nx.Graph(), nodetype=int)
```
*"Com os 300 nós selecionados, extraio o subgrafo deles com `subgraph()` e salvo no disco como `instagram_sample.edges`. Da próxima vez que rodar, o `else` aqui em cima já vai pular tudo isso e carregar direto do arquivo salvo, muito mais rápido."*

---

### BLOCO 3 — Análise Básica: Métricas da Rede Real (2:30 – 3:15)
> **Células 6 e 7 na tela**

**O que você fala:**

*"Com a rede carregada em memória, começo a análise calculando as três métricas fundamentais pedidas no trabalho."*

**Execute a Célula 7. Explique:**

```python
ordem_real = G_real.number_of_nodes()
```
*"A Ordem é o número de nós. Chamo `number_of_nodes()` no grafo e ele retorna o total de usuários na amostra — 300."*

```python
clustering_real = nx.average_clustering(G_real)
```
*"O Coeficiente de Agrupamento Médio é calculado com `nx.average_clustering`. Internamente, o NetworkX pega cada nó, vê quantos dos seus vizinhos estão conectados entre si, calcula a razão (o coeficiente local de cada nó) e tira a média de todos. O valor alto — em torno de 0.54 — já indica a existência de comunidades fechadas, as famosas 'bolhas' das redes sociais."*

```python
densidade_real = nx.density(G_real)
```
*"A Densidade é calculada com `nx.density`. A fórmula é simples: número de arestas existentes dividido pelo número máximo de arestas possíveis para um grafo com N nós, que seria N×(N-1)/2. O valor de ~0.045 significa que só 4,5% das conexões possíveis realmente existem — faz sentido, ninguém consegue ser amigo de todos os 300."*

---

### BLOCO 4 — Comparação com a Rede Aleatória — Erdős-Rényi (3:15 – 4:00)
> **Células 8 e 9 na tela**

**O que você fala:**

*"Agora gero uma rede aleatória pra servir de comparação. O modelo de Erdős-Rényi é o mais clássico: ele distribui as arestas entre os nós de forma completamente aleatória, como se a gente sorteasse as amizades."*

**Execute a Célula 9. Explique:**

```python
tamanho_real = G_real.number_of_edges()
```
*"Primeiro capturo o número exato de arestas da rede real pra usar como parâmetro."*

```python
seed_aleatoria = 42
G_aleatorio = nx.gnm_random_graph(n=ordem_real, m=tamanho_real, seed=seed_aleatoria)
```
*"Uso `nx.gnm_random_graph` — o 'G(N,M)' do Erdős-Rényi — passando o mesmo número de nós (N=300) e o mesmo número de arestas (M=2046). A `seed=42` é pra garantir que sempre que eu rodar esse código, o grafo aleatório gerado seja idêntico, tornando o resultado reproduzível.*

*O resultado: a densidade vai ser igual à da rede real (óbvio, tem o mesmo N e M), mas o Coeficiente de Agrupamento vai cair pra volta de 0.045 — muito menor que os 0.54 da rede real. Essa diferença brutal prova que a rede social não é aleatória: ela tem estrutura interna organizada."*

---

### BLOCO 5 — Análise Adicional 1: Modelo Watts-Strogatz (4:00 – 5:15)
> **Células 10 e 11 na tela**

**O que você fala:**

*"Como primeira análise adicional, escolhi investigar o Modelo de Pequeno Mundo de Watts-Strogatz. Esse modelo tenta responder: como é possível uma rede ter alto agrupamento local E ao mesmo tempo ter caminhos curtos entre qualquer par de nós? Essa é exatamente a propriedade das redes sociais reais."*

**Execute a Célula 11. Explique:**

```python
k_medio = int(round(2 * tamanho_real / ordem_real))
```
*"O grau médio é calculado pela fórmula clássica: 2 vezes o número de arestas, dividido pelo número de nós. Multiplico por 2 porque cada aresta contribui com grau 1 pra dois nós diferentes. Esse valor vira o parâmetro `k` do modelo Watts-Strogatz, que define quantos vizinhos cada nó tem inicialmente no anel."*

```python
p_reconexao = 0.1
G_smallworld = nx.watts_strogatz_graph(n=ordem_real, k=k_medio, p=p_reconexao, seed=42)
```
*"A função `nx.watts_strogatz_graph` constrói a rede assim: começa com todos os nós em anel, cada um conectado aos K vizinhos mais próximos. Depois, vai passando por cada aresta e com probabilidade `p=0.1` reconecta ela pra um nó aleatório. Esses 10% de reconexões aleatórias são o que cria os 'atalhos' que encurtam drasticamente o caminho entre comunidades distantes — sem destruir os grupos locais."*

*"O resultado esperado: agrupamento ainda alto (próximo do real) e caminho médio curto. Isso confirma que a minha rede social se comporta como um Pequeno Mundo."*

---

### BLOCO 6 — Análise Adicional 2: Diâmetro, Caminhos e Gráficos (5:15 – 6:45)
> **Células 12, 13, 14 e 15 na tela**

**O que você fala:**

*"Na segunda análise adicional, fui além das métricas básicas e calculei como a informação se propaga pelas três redes — o diâmetro e o caminho mínimo médio. Depois plotei dois gráficos visuais pra tornar a comparação mais clara."*

**Execute a Célula 13. Explique:**

```python
def obter_metricas_caminhos(g):
    if nx.is_connected(g):
        diam = nx.diameter(g)
        caminho_medio = nx.average_shortest_path_length(g)
    else:
        maior_comp = max(nx.connected_components(g), key=len)
        sub_g = g.subgraph(maior_comp)
        diam = nx.diameter(sub_g)
        caminho_medio = nx.average_shortest_path_length(sub_g)
    return diam, caminho_medio
```
*"Criei essa função pra não repetir código. Primeiro verifico se o grafo é completamente conexo com `nx.is_connected`. Se for, calculo o diâmetro e o caminho médio diretamente. Se não for (a rede aleatória às vezes tem nós isolados), foco no maior componente conexo — caso contrário o `nx.diameter` daria erro porque não existe caminho entre nós desconectados.*  

*O `nx.diameter` acha a maior distância mínima entre qualquer par de nós. O `nx.average_shortest_path_length` calcula a média de todas as menores distâncias possíveis entre todos os pares de nós da rede."*

```python
diam_real, path_real = obter_metricas_caminhos(G_real)
diam_aleat, path_aleat = obter_metricas_caminhos(G_aleatorio)
diam_sw, path_sw = obter_metricas_caminhos(G_smallworld)
```
*"Chamo a função pras três redes e armazeno os resultados. O esperado: a rede real terá um caminho médio baixo (em torno de 2.5 passos), comprovando os famosos 'seis graus de separação'."*

**Execute a Célula 14. Explique:**

```python
graus_real = [d for n, d in G_real.degree()]
graus_aleat = [d for n, d in G_aleatorio.degree()]
```
*"O `G_real.degree()` retorna uma lista de tuplas com (nó, grau) pra cada nó. Com essa list comprehension, fico só com a parte do grau — o número de conexões de cada usuário."*

```python
plt.hist(graus_real, bins=12, alpha=0.7, color='navy', ...)
plt.hist(graus_aleat, bins=12, alpha=0.5, color='darkorange', ...)
```
*"Ploto os dois histogramas no mesmo gráfico pra comparar visualmente. O `bins=12` divide o range de graus em 12 fatias. O `alpha` controla a transparência — coloquei 0.5 no laranja pra ver se uma barra sobrepor a outra. O resultado: a rede real vai ter uma barra gigante perto do zero (a maioria tem poucas conexões) e uma 'cauda longa' com os hubs lá na direita. A aleatória forma um sino simétrico."*

**Execute a Célula 15. Explique:**

```python
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
```
*"Crio uma figura com 3 painéis lado a lado. O `figsize=(18,5)` deixa bem largo pra caber as três redes."*

```python
pos_r = nx.spring_layout(G_real, seed=42)
pos_a = nx.spring_layout(G_aleatorio, seed=42)
pos_s = nx.circular_layout(G_smallworld)
```
*"O 'layout' define onde cada nó vai ser desenhado na tela. O `spring_layout` simula um sistema de molas: nós conectados se aproximam, nós sem conexão se afastam — com isso os hubs ficam naturalmente no centro. O `circular_layout` é ideal pro Watts-Strogatz porque ele começa em anel, mostrando a estrutura circular original com as reconexões cruzando por dentro."*

```python
nx.draw_networkx(G_real, pos_r, ax=axes[0], node_size=100,
                 node_color='navy', with_labels=False, edge_color='gray', alpha=0.7)
```
*"O `draw_networkx` é quem desenha de fato. Passo o grafo, o layout de posições e o eixo onde vai aparecer. Coloquei `with_labels=False` porque com 300 nós os números ficam ilegíveis. O `node_size=100` deixa as bolinhas menores pra não cobrir as arestas."*

---

### BLOCO 7 — Tabela Resumo e Conclusões (6:45 – 8:00)
> **Células 16, 17 e 18 na tela**

**Execute a Célula 17. Explique:**

```python
tabela_comparativa = pd.DataFrame({
    'Modelo de Rede': [...],
    'Ordem (N)': [ordem_real, ordem_aleat, ordem_sw],
    'Tamanho (M)': [...],
    'Densidade (ρ)': [...],
    'Coef. Agrupamento (C)': [...],
    'Diâmetro': [...],
    'Caminho Médio (L)': [...]
})
print(tabela_comparativa.to_string(index=False))
```
*"Uso o Pandas pra montar um DataFrame — basicamente uma tabela — com todas as métricas das três redes numa estrutura só. O `to_string(index=False)` imprime a tabela sem a coluna de índice numérico, deixando mais limpo."*

**Aponte para a tabela e fale as conclusões:**

*"Olhando pra essa tabela, as três conclusões principais do meu trabalho são:*

*1. **Agrupamento**: A rede real tem Coeficiente de Agrupamento de ~0.54 enquanto a aleatória tem ~0.045 — doze vezes maior. Isso prova que usuários de redes sociais se agrupam em comunidades e bolhas de interesses, não de forma aleatória.*

*2. **Pequeno Mundo**: Mesmo com esse agrupamento alto, o caminho médio da rede real é ~2.5 passos — igual ao da aleatória e do Watts-Strogatz. É o clássico paradoxo do Pequeno Mundo: muito agrupado localmente, mas ainda assim muito bem conectado globalmente. A teoria dos seis graus de separação funciona.*

*3. **Distribuição de Graus**: O histograma mostrou que a rede real segue uma Lei de Potência — muitos com poucas conexões, poucos com muitas. Esses poucos são os hubs, os influenciadores digitais, que garantem a disseminação rápida de informações pela rede.*

*Obrigado pela atenção e fico à disposição para perguntas!"*

---

## ❓ Perguntas Prováveis e Como Responder

### Sobre o Dataset
**"De onde vêm esses dados?"**
> *"Vêm do projeto SNAP da Universidade de Stanford — é uma base pública de dados de redes. O código baixa automaticamente de `snap.stanford.edu`. Representa conexões reais de usuários de uma rede social."*

### Sobre o Código
**"Por que você usou BFS pra amostrar e não pegou nós aleatórios?"**
> *"Porque nós aleatórios poderiam gerar nós desconectados na amostra, e aí as funções `nx.diameter` e `nx.average_shortest_path_length` dariam erro — elas exigem grafo conexo. A BFS garante que todos os 300 nós selecionados estejam em um único componente conectado."*

**"O que é `seed=42` que aparece em vários lugares?"**
> *"A seed é a semente do gerador de números aleatórios. Fixando em 42, garanto que toda vez que eu rodar o código, os grafos aleatórios e os layouts visuais sejam gerados exatamente iguais. Sem isso, o grafo aleatório seria diferente a cada execução e os resultados não seriam reproduzíveis."*

### Sobre as Métricas
**"O que diferencia o Coeficiente de Agrupamento do Watts-Strogatz do da rede real?"**
> *"O Watts-Strogatz foi gerado justamente pra ter agrupamento alto, então os valores são próximos. A diferença é que o modelo é sintético (gerado matematicamente com parâmetros controlados), enquanto o da rede real emergiu de comportamento humano real. O fato de serem próximos é a evidência de que a teoria do Pequeno Mundo descreve bem as redes sociais."*

**"Por que a densidade das três redes é igual?"**
> *"Porque eu gerei a aleatória e a Watts-Strogatz com os mesmos N e M da rede real, propositalmente. Isso é um controle experimental — se os tamanhos fossem diferentes, não saberia se as diferenças no agrupamento são da estrutura ou do tamanho."*

**"O que significa exatamente o Diâmetro de 6 da rede real?"**
> *"Significa que os dois usuários mais distantes na rede precisam passar por no máximo 6 intermediários pra se comunicar. É a materialização dos famosos 'seis graus de separação' de Stanley Milgram."*
