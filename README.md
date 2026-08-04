# Projeto Prático: Análise de Redes Complexas com NetworkX

Este repositório contém a implementação individual do **Projeto Prático da disciplina de Comunicação e Redes**, desenvolvido em **Python** utilizando a biblioteca **NetworkX**.

O trabalho consiste na análise estrutural e estatística de uma rede social (amostra de conexões estilo Instagram) comparada a modelos teóricos de **Redes Aleatórias (Erdős-Rényi)** e **Redes de Pequeno Mundo (Watts-Strogatz)**.

**Autor:** Rodrigo Ramos  

---

## 📌 Conteúdo do Repositório

- **[`projeto_redes.ipynb`](./projeto_redes.ipynb)**: Jupyter Notebook principal contendo o código executado, explicações teóricas intercaladas e visualizações gráficas.
- **[`instagram_sample.edges`](./instagram_sample.edges)**: Dataset da rede real em formato de lista de arestas (*edgelist*).
- **[`roteiro_apresentacao.md`](./roteiro_apresentacao.md)**: Guia passo a passo com a fala da apresentação individual de 8 minutos.
- **[`distribuicao_graus.png`](./distribuicao_graus.png)**: Gráfico de distribuição de graus ($P(k)$).
- **[`comparacao_topologia.png`](./comparacao_topologia.png)**: Visualização topológica dos 3 modelos de redes.

---

## 📊 Métricas e Resultados Obtidos

| Modelo de Rede | Ordem ($N$) | Tamanho ($M$) | Densidade ($\rho$) | Coef. Agrupamento ($C$) | Diâmetro | Caminho Médio ($L$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Rede Real (Amostra Instagram)** | 300 | 2046 | 0.0456 | 0.5401 | 6 | 2.5020 |
| **Rede Aleatória (Erdős-Rényi)** | 300 | 2046 | 0.0456 | 0.0450 | 4 | 2.2210 |
| **Pequeno Mundo (Watts-Strogatz)** | 65 | 715 | 0.3438 | 0.5762 | 3 | 1.6846 |

---

## 🚀 Como Executar

### No Google Colab
1. Baixe os arquivos `projeto_redes.ipynb` e `instagram_sample.edges`.
2. Acesse o [Google Colab](https://colab.research.google.com/) e faça upload do notebook.
3. Faça upload do arquivo `instagram_sample.edges` no painel de arquivos à esquerda.
4. Execute as células sequencialmente.

### Localmente (Jupyter Notebook / VS Code)
```bash
# Clone o repositório
git clone https://github.com/ramosRdgo/ProjetoC.R.git
cd ProjetoC.R

# Instale as dependências necessárias
pip install networkx matplotlib pandas scipy notebook

# Abra o Jupyter Notebook
jupyter notebook projeto_redes.ipynb
```
