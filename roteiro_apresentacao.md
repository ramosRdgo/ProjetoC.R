# Roteiro de Apresentação Individual (Tempo Máximo: 8 Minutos)

**Disciplina:** Comunicação e Redes  
**Projeto Prático (Individual):** Análise da Rede Cortical de Felino (`bn-cat-mixed-species_brain_1`)  
**Aluno:** Rodrigo Ramos  
**Ferramentas:** Python, NetworkX, Matplotlib e Pandas  

---

## ⏱️ Divisão do Tempo (Cronograma dos 8 Minutos)

| Bloco | Seção do Notebook | Conteúdo Principal | Tempo Estimado |
| :--- | :--- | :--- | :---: |
| **1. Introdução** | Seções 1 e 2 | Apresentação do tema e do dataset da rede real | **1 min** (0:00 - 1:00) |
| **2. Análise Básica** | Seções 3 e 4 | Métricas da Rede Real vs. Rede Aleatória (Erdős-Rényi) | **1.5 min** (1:00 - 2:30) |
| **3. Análise Adicional 1** | Seção 5 | Modelo de Pequeno Mundo (Watts-Strogatz) | **2 min** (2:30 - 4:30) |
| **4. Análise Adicional 2** | Seção 6 | Distribuição de Graus e Comparação Visual Topológica | **2 min** (4:30 - 6:30) |
| **5. Síntese e Conclusão** | Seções 7 e 8 | Tabela Resumo, Conclusões Teórico-Práticas e Perguntas | **1.5 min** (6:30 - 8:00) |

---

## 🎤 Roteiro Fala por Fala (Fala em 1ª Pessoa - Individual)

### 1. Introdução e Apresentação do Dataset (0:00 - 1:00)
> **O que mostrar na tela:** Células 1 e 2 do Notebook (`projeto_redes.ipynb`).  
> **Fala do apresentador:**  
> *"Boa noite a todos e ao professor. No meu **Projeto Prático**, escolhi analisar uma rede complexa real utilizando a linguagem Python e a biblioteca **NetworkX**.*  
> *A rede real que escolhi analisa o **conectoma cortical do cérebro de um gato** (`bn-cat-mixed-species_brain_1`). É um grafo não-direcionado composto por **65 nós** (que representam as áreas corticais do cérebro) e **730 arestas** (que representam os feixes de conexões neurais entre essas áreas). Carreguei essa rede a partir de uma lista de arestas no formato `.edges`."*

---

### 2. Análise Básica e Comparação com Rede Aleatória (1:00 - 2:30)
> **O que mostrar na tela:** Células 3 a 9 (Cálculo de $N$, $C$, $\rho$ e geração da rede Erdős-Rényi).  
> **Fala do apresentador:**  
> *"Na **análise básica**, extraí as três métricas solicitadas no trabalho:*  
> *- A **Ordem ($N$)**: 65 nós.*  
> *- A **Densidade ($\rho$)**: 0.3510, o que significa que 35,1% de todas as conexões possíveis estão ativas.*  
> *- O **Coeficiente de Agrupamento Médio ($C$)**: 0.3575.*  
>  
> *Para entender se esses números são especiais ou fruto do acaso, criei uma **Rede Aleatória pelo modelo de Erdős-Rényi** com **exatamente a mesma ordem (65)** e **mesmo tamanho (730 arestas)**.  
> Notei que a densidade é exatamente igual (0.3510), mas o agrupamento na rede aleatória é menor (0.3470). Isso já nos dá a primeira pista de que o cérebro possui uma organização modular estruturada, não aleatória."*

---

### 3. Análise Adicional 1: Modelo de Pequeno Mundo (2:30 - 4:30)
> **O que mostrar na tela:** Células 10 e 11 (Rede Watts-Strogatz).  
> **Fala do apresentador:**  
> *"Como minha **primeira análise adicional**, escolhi investigar o **Modelo de Pequeno Mundo (Watts-Strogatz)**.*  
> *Em redes biológicas e sociais, o conceito de 'Pequeno Mundo' é fundamental: ele descreve redes que possuem **alto agrupamento local** (vizinhos bem conectados entre si), mas mantêm **caminhos curtos** para atravessar toda a rede.*  
>  
> *Gerei uma rede Watts-Strogatz com a mesma ordem $N=65$, grau médio equivalente $k=22$ e probabilidade de reconexão $p=0.1$. Observei que o agrupamento subiu significativamente para **0.5762**, demonstrando como pequenas reconexões aleatórias em uma grade regular criam atalhos eficientes sem destruir os aglomerados locais."*

---

### 4. Análise Adicional 2: Distribuição de Graus e Topologia (4:30 - 6:30)
> **O que mostrar na tela:** Células 12 a 15 (Gráficos `distribuicao_graus.png` e `comparacao_topologia.png`).  
> **Fala do apresentador:**  
> *"Como **segunda análise adicional**, calculei o **Diâmetro**, o **Grau Médio de Separação (Caminho Mínimo Médio $L$)** e plotei o **Gráfico de Distribuição de Graus**.*  
>  
> *1. **Caminho Mínimo Médio ($L$)**: Na rede real, o caminho médio é de apenas **1.6495 saltos**, com diâmetro 3. Isso significa que qualquer região do cérebro consegue transmitir sinal para qualquer outra área em menos de 2 passos em média!*  
> *2. **Distribuição de Graus**: Ao olhar o histograma, vemos que enquanto a rede aleatória segue uma distribuição uniforme centrada na média, a rede real possui **nós com alto grau (hubs corticais)** que atuam como centrais de roteamento de informação no cérebro.*  
> *3. **Visualização Topológica**: O gráfico com as 3 redes desenhadas lado a lado deixa clara a diferença visual de estrutura entre a rede real, a aleatória e a de pequeno mundo."*

---

### 5. Tabela Resumo e Conclusões (6:30 - 8:00)
> **O que mostrar na tela:** Células 16 a 18 (Tabela comparativa do Pandas e texto de conclusão).  
> **Fala do apresentador:**  
> *"Para concluir minha apresentação, sintetizei todas as métricas nesta **tabela comparativa**:*  
>  
> | Modelo de Rede | Ordem ($N$) | Arestas ($M$) | Densidade ($\rho$) | Agrupamento ($C$) | Diâmetro | Caminho Médio ($L$) |
> | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
> | **Rede Real (Cat Brain)** | 65 | 730 | 0.3510 | **0.3575** | 3 | **1.6495** |
> | **Rede Aleatória** | 65 | 730 | 0.3510 | 0.3470 | 2 | 1.6490 |
> | **Pequeno Mundo** | 65 | 715 | 0.3438 | **0.5762** | 3 | 1.6846 |
>  
> *As **3 grandes conclusões** do meu trabalho são:*  
> *1. O cérebro do gato funciona como uma **Rede de Pequeno Mundo**: combina alto agrupamento local com caminho médio mínimo baixíssimo ($L \approx 1.65$).*  
> *2. Essa arquitetura otimiza a integração de informações com o menor custo energético de fiação neural possível.*  
> *3. A presença de **hubs corticais** garante resiliência e velocidade no processamento sensorial e motor do animal.*  
>  
> *Agradeço a atenção de todos e fico à disposição para perguntas!"*

---

## ❓ Possíveis Perguntas do Professor e Como Responder

### ❓ Pergunta 1: *"Por que você escolheu comparar a rede real com uma rede de Erdős-Rényi com o mesmo N e M?"*
> **Resposta Modelo:**  
> *"Comparei com o modelo Erdős-Rényi de mesmo $N$ e $M$ para ter uma **linha de base nula** (null model). Como a densidade é a mesma em ambas, qualquer diferença no Coeficiente de Agrupamento ou na Distribuição de Graus prova que a rede real possui uma estrutura interna organizada (modular/hierárquica) e não foi formada aleatoriamente."*

### ❓ Pergunta 2: *"O que é o Coeficiente de Agrupamento e qual o seu significado prático no cérebro?"*
> **Resposta Modelo:**  
> *"O coeficiente de agrupamento mede a probabilidade de dois vizinhos de um nó também serem vizinhos entre si (formando triângulos). No cérebro, um alto agrupamento significa a presença de **módulos ou comunidades locais de neurônios** altamente especializados em tarefas específicas (como visão ou audição)."*

### ❓ Pergunta 3: *"O que significa o Caminho Mínimo Médio ($L = 1.65$) ser tão baixo?"*
> **Resposta Modelo:**  
> *"O caminho médio de 1.65 indica o número médio de conexões que um sinal elétrico precisa percorrer para ir de qualquer região cortical a outra. Um valor tão baixo garante **rapidez na resposta motora e cognitiva**, permitindo que diferentes sentidos se integrem quase instantaneamente."*

### ❓ Pergunta 4: *"Como o arquivo `.edges` foi lido no NetworkX?"*
> **Resposta Modelo:**  
> *"Utilizei a função `nx.read_edgelist('bn-cat-mixed-species_brain_1.edges', create_using=nx.Graph(), nodetype=int)`. Ela interpreta cada linha do arquivo como um par de vértices e constrói o objeto de grafo em memória de forma não-direcionada."*
