import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Amazon", layout="wide", page_icon="🛒")

st.title("📊 Análise de Produtos - Amazon Índia")
st.markdown("Explore os dados de preços, descontos e avaliações. Utilize os filtros à esquerda para refinar a análise.")

@st.cache_data 
def carregar_dados():
    tabela = pd.read_csv("amazon_limpo.csv")
    
    
    if 'custo_beneficio' not in tabela.columns:
        tabela['custo_beneficio'] = tabela['notas'] / tabela['preco_desconto']
        
    return tabela

df = carregar_dados()

st.sidebar.header("🔍 Filtros")
categorias_disponiveis = sorted(df["categoria_plot"].unique())
categorias_selecionadas = st.sidebar.multiselect(
    "Filtrar por Categoria", 
    categorias_disponiveis, 
    default=categorias_disponiveis
)

df_filtrado = df[df["categoria_plot"].isin(categorias_selecionadas)]

st.subheader("Métricas Gerais")

if not df_filtrado.empty:
    total_produtos = df_filtrado.shape[0]
    preco_medio = df_filtrado["preco_desconto"].mean()
    desconto_medio = df_filtrado["porcentagem_desconto"].mean()
    nota_media = df_filtrado["notas"].mean()
else:
    total_produtos, preco_medio, desconto_medio, nota_media = 0, 0, 0, 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Produtos", total_produtos)
col2.metric("Preço Médio Pago", f"₹ {preco_medio:,.2f}")
col3.metric("Desconto Médio", f"{desconto_medio:.1f}%")
col4.metric("Avaliação Média", f"⭐ {nota_media:.2f}")

st.markdown("---")

# --- Gráficos ---
st.subheader("Análise Gráfica")

if not df_filtrado.empty:
    
    col_graf1, col_graf2 = st.columns(2)
    
    with col_graf1:
        contagem = df_filtrado['categoria_plot'].value_counts().reset_index()
        contagem.columns = ['Categoria', 'Quantidade']
        fig_bar = px.bar(contagem, x='Categoria', y='Quantidade', color='Categoria', title='Distribuição de Produtos por Categoria')
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with col_graf2:
        fig_box = px.box(df_filtrado, x='categoria_plot', y='preco_atual', color='categoria_plot', title='Distribuição de Preços Originais')
        st.plotly_chart(fig_box, use_container_width=True)

    
    col_graf3, col_graf4 = st.columns(2)
    
    with col_graf3:
        desconto_medio_df = df_filtrado.groupby('categoria_plot')['porcentagem_desconto'].mean().sort_values(ascending=False).reset_index()
        fig_desc = px.bar(desconto_medio_df, x='categoria_plot', y='porcentagem_desconto', color='categoria_plot', title='Média de Desconto por Categoria', text_auto='.2f')
        st.plotly_chart(fig_desc, use_container_width=True)
        
    with col_graf4:
        fig_scatter = px.scatter(df_filtrado, x='porcentagem_desconto', y='notas', color='categoria_plot', hover_data=['nome_produto'], title='Relação: Desconto vs Avaliação')
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown("---")
    
    
    st.subheader("🏆 Top 10 Produtos - Melhor Custo-Benefício")
    top_10 = df_filtrado[['nome_produto', 'categoria_plot', 'notas', 'preco_desconto', 'custo_beneficio']].sort_values(by='custo_beneficio', ascending=False).head(10)
    st.dataframe(top_10, use_container_width=True)

else:
    st.warning("Nenhum dado para exibir. Selecione pelo menos uma categoria no filtro lateral.")