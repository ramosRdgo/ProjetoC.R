# Projeto Prático: Análise de Redes Complexas com NetworkX

Este repositório contém a implementação individual do **Projeto Prático da disciplina de Comunicação e Redes**, desenvolvido em **Python** utilizando a biblioteca **NetworkX**.

O trabalho consiste na análise estrutural e estatística de uma rede biológica real (mapa de conexões corticais de felino) comparada a modelos teóricos de **Redes Aleatórias (Erdős-Rényi)** e **Redes de Pequeno Mundo (Watts-Strogatz)**.

**Autor:** Rodrigo Ramos  

---

## 📌 Conteúdo do Repositório

- **[`projeto_redes.ipynb`](./projeto_redes.ipynb)**: Jupyter Notebook principal contendo o código executado, explicações teóricas intercaladas e visualizações gráficas.
- **[`bn-cat-mixed-species_brain_1.edges`](./bn-cat-mixed-species_brain_1.edges)**: Dataset da rede real em formato de lista de arestas (*edgelist*).
- **[`roteiro_apresentacao.md`](./roteiro_apresentacao.md)**: Guia passo a passo com a fala da apresentação individual de 8 minutos.
- **[`distribuicao_graus.png`](./distribuicao_graus.png)**: Gráfico de distribuição de graus ($P(k)$).
- **[`comparacao_topologia.png`](./comparacao_topologia.png)**: Visualização topológica dos 3 modelos de redes.

---

## 📊 Métricas e Resultados Obtidos

| Modelo de Rede | Ordem ($N$) | Tamanho ($M$) | Densidade ($\rho$) | Coef. Agrupamento ($C$) | Diâmetro | Caminho Médio ($L$) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Rede Real (Cat Brain)** | 65 | 730 | 0.3510 | 0.3575 | 3 | 1.6495 |
| **Rede Aleatória (Erdős-Rényi)** | 65 | 730 | 0.3510 | 0.3470 | 2 | 1.6490 |
| **Pequeno Mundo (Watts-Strogatz)** | 65 | 715 | 0.3438 | 0.5762 | 3 | 1.6846 |

---

## 🚀 Como Executar

### No Google Colab
1. Baixe os arquivos `projeto_redes.ipynb` e `bn-cat-mixed-species_brain_1.edges`.
2. Acesse o [Google Colab](https://colab.research.google.com/) e faça upload do notebook.
3. Faça upload do arquivo `bn-cat-mixed-species_brain_1.edges` no painel de arquivos à esquerda.
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
