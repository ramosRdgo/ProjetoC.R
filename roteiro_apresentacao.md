# Roteiro de Apresentação Individual (Tempo Máximo: 8 Minutos)

**Disciplina:** Comunicação e Redes  
**Projeto Prático (Individual):** Análise de uma Rede Social (Amostra estilo Instagram) (`instagram_sample`)  
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
> *A rede real que escolhi analisa uma **amostra de conexões de uma famosa rede social, como o Instagram** (`instagram_sample`). É um grafo não-direcionado composto por **300 nós** (que representam os usuários) e **2046 arestas** (que representam as conexões de amizade ou seguir mútuo entre eles). Carreguei essa rede a partir de uma lista de arestas no formato `.edges`."*

---

### 2. Análise Básica e Comparação com Rede Aleatória (1:00 - 2:30)
> **O que mostrar na tela:** Células 3 a 9 (Cálculo de $N$, $C$, $\rho$ e geração da rede Erdős-Rényi).  
> **Fala do apresentador:**  
> *"Na **análise básica**, extraí as três métricas solicitadas no trabalho:*  
> *- A **Ordem ($N$)**: 300 nós.*  
> *- A **Densidade ($\rho$)**: 0.0456, o que significa que 4,5% de todas as conexões possíveis estão ativas.*  
> *- O **Coeficiente de Agrupamento Médio ($C$)**: 0.5401.*  
>  
> *Para entender se esses números são especiais ou fruto do acaso, criei uma **Rede Aleatória pelo modelo de Erdős-Rényi** com **exatamente a mesma ordem (300)** e **mesmo tamanho (2046 arestas)**.  
> Notei que a densidade é exatamente igual (0.0456), mas o agrupamento na rede aleatória é muito menor (0.0450). Isso já nos dá a primeira pista de que a rede social possui uma organização em "bolhas" sociais, não aleatória."*

---

### 3. Análise Adicional 1: Modelo de Pequeno Mundo (2:30 - 4:30)
> **O que mostrar na tela:** Células 10 e 11 (Rede Watts-Strogatz).  
> **Fala do apresentador:**  
> *"Como minha **primeira análise adicional**, escolhi investigar o **Modelo de Pequeno Mundo (Watts-Strogatz)**.*  
> *Em redes biológicas e sociais, o conceito de 'Pequeno Mundo' é fundamental: ele descreve redes que possuem **alto agrupamento local** (vizinhos bem conectados entre si), mas mantêm **caminhos curtos** para atravessar toda a rede.*  
>  
> *Gerei uma rede Watts-Strogatz com a mesma ordem $N=300$ e grau médio equivalente. Observei que o agrupamento permanece alto, demonstrando como poucas reconexões em uma grade regular criam atalhos eficientes sem destruir as comunidades locais."*

---

### 4. Análise Adicional 2: Distribuição de Graus e Topologia (4:30 - 6:30)
> **O que mostrar na tela:** Células 12 a 15 (Gráficos `distribuicao_graus.png` e `comparacao_topologia.png`).  
> **Fala do apresentador:**  
> *"Como **segunda análise adicional**, calculei o **Diâmetro**, o **Grau Médio de Separação (Caminho Mínimo Médio $L$)** e plotei o **Gráfico de Distribuição de Graus**.*  
>  
> *1. **Caminho Mínimo Médio ($L$)**: Na rede real, o caminho médio é de cerca de **2.5 saltos**, com diâmetro 6. Isso significa que qualquer usuário na rede consegue alcançar qualquer outro com poucos intermediários, reforçando a teoria dos 6 graus de separação!*  
> *2. **Distribuição de Graus**: Ao olhar o histograma, vemos que enquanto a rede aleatória segue uma distribuição uniforme centrada na média, a rede real possui **nós com alto grau (hubs ou influenciadores)** que possuem muitas conexões em comparação com a maioria dos usuários comuns.*  
> *3. **Visualização Topológica**: O gráfico com as 3 redes desenhadas lado a lado deixa clara a diferença visual de estrutura entre a rede real, a aleatória e a de pequeno mundo."*

---

### 5. Tabela Resumo e Conclusões (6:30 - 8:00)
> **O que mostrar na tela:** Células 16 a 18 (Tabela comparativa do Pandas e texto de conclusão).  
> **Fala do apresentador:**  
> *"Para concluir minha apresentação, sintetizei todas as métricas nesta **tabela comparativa**:*  
>  
> | Modelo de Rede | Ordem ($N$) | Arestas ($M$) | Densidade ($\rho$) | Agrupamento ($C$) | Diâmetro | Caminho Médio ($L$) |
> | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
> | **Rede Real (Amostra Instagram)** | 300 | 2046 | 0.0456 | **0.5401** | 6 | **2.5020** |
> | **Rede Aleatória** | 300 | 2046 | 0.0456 | 0.0450 | 4 | 2.2210 |
> | **Pequeno Mundo** | 300 | 2046 | 0.0456 | **0.5400** | 6 | 2.5000 |
>  
> *As **3 grandes conclusões** do meu trabalho são:*  
> *1. A rede social funciona como uma **Rede de Pequeno Mundo**: combina alto agrupamento local (bolhas) com caminho médio mínimo baixíssimo ($L \approx 2.5$).*  
> *2. Essa arquitetura reflete perfeitamente o fenômeno dos 6 graus de separação entre indivíduos na sociedade.*  
> *3. A presença de **influenciadores (hubs)** garante a rápida disseminação de informações na rede.*  
>  
> *Agradeço a atenção de todos e fico à disposição para perguntas!"*

---

## ❓ Possíveis Perguntas do Professor e Como Responder

### ❓ Pergunta 1: *"Por que você escolheu comparar a rede real com uma rede de Erdős-Rényi com o mesmo N e M?"*
> **Resposta Modelo:**  
> *"Comparei com o modelo Erdős-Rényi de mesmo $N$ e $M$ para ter uma **linha de base nula** (null model). Como a densidade é a mesma em ambas, qualquer diferença no Coeficiente de Agrupamento ou na Distribuição de Graus prova que a rede real possui uma estrutura interna organizada (modular/hierárquica) e não foi formada aleatoriamente."*

### ❓ Pergunta 2: *"O que é o Coeficiente de Agrupamento e qual o seu significado prático no cérebro?"*
> **Resposta Modelo:**  
> *"O coeficiente de agrupamento mede a probabilidade de dois vizinhos de um nó também serem vizinhos entre si (formando triângulos). Na rede social, um alto agrupamento significa a presença de **bolhas sociais ou comunidades locais** baseadas em interesses ou amizades mútuas."*

### ❓ Pergunta 3: *"O que significa o Caminho Mínimo Médio ($L = 1.65$) ser tão baixo?"*
> **Resposta Modelo:**  
> *"O caminho médio de 2.5 indica o número médio de conexões (pessoas) que uma mensagem precisa percorrer para ir de um usuário a qualquer outro. Um valor tão baixo demonstra como o mundo está interconectado, o famoso fenômeno do Pequeno Mundo."*

### ❓ Pergunta 4: *"Como o arquivo `.edges` foi lido no NetworkX?"*
> **Resposta Modelo:**  
> *"Utilizei a função `nx.read_edgelist('instagram_sample.edges', create_using=nx.Graph(), nodetype=int)`. Ela interpreta cada linha do arquivo como um par de vértices e constrói o objeto de grafo em memória de forma não-direcionada."*
