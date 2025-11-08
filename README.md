[![author](https://img.shields.io/badge/Author-Francisco&nbsp;Bustamante-red.svg)](https://www.linkedin.com/in/flsbustamante/)
[![](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)

# Segmentação de clientes de um supermercado

Um supermercado, através de cartões de fidelidade, possui alguns dados básicos sobre seus clientes, como idade, gênero, renda anual e pontuação de gastos. Tal pontuação é algo que o supermercado atribui ao cliente com base em parâmetros definidos, como comportamento do cliente e dados de compra. O supermercado deseja entender melhor seus clientes, de modo a formular estratégias de negócios, e para isso contratou um cientista de dados para realizar uma segmentação dos clientes.

![segmentacao_pca_3d](..relatorios/imagens/grafico3d.png)

[Link original para o dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)

Projeto de clusterização utilizando dados de clientes de supermercado utilizando bibliotecas como scikit learn, pandas, matplotlib...

<p align="center"> 
  <a href="https://www.linkedin.com/in/flsbustamante" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
</p>

## Objetivos

O objetivo deste projeto é realizar a segmentação de clientes de um supermercado utilizando técnicas de aprendizado não supervisionado, com foco em identificar grupos com comportamentos de consumo semelhantes.

Por meio da aplicação do algoritmo K-Means, buscou-se descobrir padrões ocultos nos dados e compreender melhor o perfil dos consumidores — considerando variáveis como idade, renda anual e pontuação de gastos.

Com esses insights, o supermercado pode:

* Desenvolver estratégias de marketing personalizadas;

* Criar campanhas direcionadas a diferentes perfis de clientes;

* Melhorar a fidelização e satisfação dos consumidores;

* Otimizar o uso de recursos em ações promocionais e programas de benefícios.

Em suma, o projeto visa transformar dados brutos em informações estratégicas, auxiliando na tomada de decisões baseadas em dados (Data-Driven Decision Making) e na compreensão do comportamento do cliente.

## Estrutura do repositório

O repositório está estruturado da seguinte forma:

```
├── dados
├── modelos
├── notebooks
├── relatorios / imagens
```

- Na pasta `dados` estão os dados utilizados no projeto. O arquivo `Mall_Customers.csv` é o dataset utilizado originalmente. Os demais arquivos são os datasets gerados durante o projeto.
- Na pasta `imagens` estão as imagens utilizadas neste README.
- Na pasta `modelos` estão os modelos gerados durante o projeto. 
- Na pasta `notebooks` estão os notebooks com o desenvolvimento do projeto.

## Detalhes do dataset utilizado e resumo dos resultados

O dataset utilizado é o contido no arquivo [`Mall_Customers.csv`](dados/Mall_Customers.csv), que contém os seguintes dados:

- `CustomerID`: ID do cliente
- `Gender`: sexo do cliente
- `Age`: idade do cliente
- `Annual Income (k$)`: renda anual do cliente
- `Spending Score (1-100)`: pontuação de gastos do cliente

Com o pipeline realizando pré-processamento, PCA e K-Means, a base foi segmentada em 5 clusters, como mostrado nas figuras abaixo:

![pairplot](../relatorios/imagens/pairplot.png)

![boxplot](../relatorios/imagens/boxplot.png)

* **Cluster 0**: Pontuação de gastos moderada, renda baixa, idade idoso.
* **Cluster 1**: Pontuação de gastos moderada, renda baixa, idade jovem.
* **Cluster 2**: Pontuação de gastos baixa, renda alta, idade moderada.
* **Cluster 3**: Pontuação de gastos alta, renda baixa, idade jovem.
* **Cluster 4**: Pontuação de gastos alta, renda alta, idade jovem.


## Como reproduzir o projeto

O projeto foi desenvolvido utilizando o Python 3.11.4. Para reproduzir o projeto, crie um ambiente virtual com o Conda, ou ferramenta similar, com o Python 3.11.4 e instale as bibliotecas abaixo:

| Biblioteca   | Versão |
| ------------ | ------ |
| Matplotlib   | 3.7.1  |
| NumPy        | 1.24.3 |
| Pandas       | 1.5.3  |
| Scikit-Learn | 1.3.0  |
| Seaborn      | 0.12.2 |

Essas são as bibliotecas principais utilizadas no projeto. O relatório foi gerado com a biblioteca [ydata-profiling](https://github.com/ydataai/ydata-profiling), instale-a se quiser reproduzir o relatório. Para ter um gráfico em 3 dimensões interativo, instale a biblioteca [ipympl](https://matplotlib.org/ipympl/).
