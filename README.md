# 📊 Análise de Produtos - Amazon Índia

Este projeto é uma análise exploratória de dados (EDA) usando um dataset de produtos da Amazon Índia. A ideia aqui foi entender como preço, desconto e avaliação se relacionam na prática.

No final, organizei tudo em um dashboard interativo com Streamlit.

## 🎯 O que eu quis analisar

Pensando como alguém de negócio, foquei em algumas perguntas que poderiam fazer diferença em um e-commerce:

- Como os preços estão distribuídos? Existem produtos muito fora do padrão?
- Dar desconto realmente melhora a avaliação dos produtos?
- Quais categorias mais usam desconto como estratégia?
- Quais categorias têm clientes mais satisfeitos?
- Existe algum padrão claro de “custo-benefício”?

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- Plotly (visualização)
- Streamlit (dashboard)

## 💡 Principais aprendizados

- **Desconto ≠ qualidade:** A correlação entre desconto e avaliação foi praticamente inexistente (-0.15). Ou seja, dar desconto não garante boas avaliações.
  
- **Tecnologia lidera promoções:** Categorias como eletrônicos e acessórios têm os maiores descontos médios.

- **Custo-benefício está nos baratos:** Produtos muito baratos (₹39–₹59), principalmente acessórios simples, concentram as melhores percepções de valor.

## 🚀 Como rodar o projeto

```bash
git clone https://github.com/borgez777/amazon-sales-analysis.git
cd amazon-sales-analysis
pip install -r requirements.txt
streamlit run app.py
