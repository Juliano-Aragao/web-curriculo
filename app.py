import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração da página
st.set_page_config(
    page_title="Juliano Aragão | Data Science & Python Developer",
    page_icon="📊",
    layout="wide"
)

# Estilo CSS customizado
st.markdown("""
    <style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #4B5563;
        margin-bottom: 20px;
    }
    .highlight {
        background-color: #EFF6FF;
        padding: 15px;
        border-radius: 8px;
        border-left: 5px solid #2563EB;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Barra Lateral (Perfil e Contato)
with st.sidebar:
    st.image("julian.png", width=180) # Ícone / Sua foto aqui
    st.title("Juliano Aragão")
    st.write("💻 **Desenvolvedor Python | Cientista de Dados | Eng. de Infraestrutura**")
    st.write("📍 Belo Horizonte, MG - Brasil")
    
    st.markdown("---")
    st.markdown("### 📬 Contato")
    st.write("📧 **E-mail:** julianoesa@gmail.com")
    st.write("📞 **Telefone:** (31) 99920-2094")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/juliano-aragao/)")
    st.write("💻 [GitHub](https://github.com/Juliano-Aragao)")

    st.markdown("---")
    # Botão de Download do PDF (coloque o arquivo Curriculo_Juliano_Aragao.pdf na mesma pasta)
    try:
        with open("Curriculo_Juliano_Aragao.pdf", "rb") as pdf_file:
            st.download_button(
                label="📄 Baixar CV em PDF",
                data=pdf_file,
                file_name="Curriculo_Juliano_Aragao.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.caption("⚠️ Adicione 'Curriculo_Juliano_Aragao.pdf' na pasta para habilitar o download.")

# 3. Cabeçalho Principal
st.markdown('<p class="main-header">Juliano Aragão</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Cientista de Dados & Desenvolvedor Python Backend</p>', unsafe_allow_html=True)

# Destaque de Resumo
st.markdown("""
<div class="highlight">
 Profissional com mais de 7 anos de experiência consolidada em Infraestrutura, Redes e Suporte Técnico Especializado, atuando fortemente no desenvolvimento de sistemas com foco em <b>Python, APIs REST, Ciência de Dados e Machine Learning</b>. União de estabilidade/observabilidade de infraestrutura à construção de códigos eficientes, escaláveis e automatizados em produção.
</div>
""", unsafe_allow_html=True)

# Métricas rápidas (KPIs)
col_kpi1, col_kpi2, col_kpi3, col_kpi4 = st.columns(4)
col_kpi1.metric("Anos de Experiência em TI", "7+ anos")
col_kpi2.metric("Redução de Erros em Pipelines", "25%")
col_kpi3.metric("Resolução no 1º Contato", "95%")
col_kpi4.metric("Especializações", "3 Pós-Graduações")

st.markdown("---")

# 4. Navegação por Abas
tab_skills, tab_exp, tab_edu = st.tabs(["📊 Habilidades Técnicas", "💼 Experiência Profissional", "🎓 Formação Acadêmica"])

# --- ABA 1: HABILIDADES TÉCNICAS ---
with tab_skills:
    st.subheader("Análise de Competências Técnicas")
    
    col_chart, col_details = st.columns([3, 2])
    
    with col_chart:
        # Gráfico Interativo com Plotly
        skills_data = {
            'Competência': ['Python', 'SQL / Bancos Relacionais', 'Docker & DevOps', 'Machine Learning & IA', 'Visão Computacional', 'APIs REST / Django', 'Redes & Infraestrutura'],
            'Nível de Domínio (%)': [95, 90, 85, 80, 80, 85, 95],
            'Categoria': ['Backend/Dados', 'Dados', 'Infra/DevOps', 'IA/Dados', 'IA/Dados', 'Backend/Dados', 'Infra/DevOps']
        }
        df_skills = pd.DataFrame(skills_data)
        
        fig = px.bar(
            df_skills, 
            x='Nível de Domínio (%)', 
            y='Competência', 
            orientation='h',
            color='Categoria',
            text='Nível de Domínio (%)',
            title='Nível de Proficiência por Tecnologia',
            color_discrete_sequence=px.colors.qualitative.Prism
        )
        fig.update_layout(yaxis={'categoryorder':'total ascending'}, height=400)
        st.plotly_chart(fig, use_container_width=True)

    with col_details:
        st.write("### 🛠️ Tech Stack Principal")
        st.markdown("""
        * **Linguagens:** Python (Avançado), Java (Conceitos OO/APIs).
        * **Backend & Frameworks:** Django, Django REST Framework (DRF), Spring Boot, FastApi, Flask.
        * **Engenharia & Dados:** PostgreSQL, SQL Avançado, Spark, Pipelines de Dados, Streamlit.
        * **Visão Computacional & IA:** OpenCV, YOLO, PyTorch, CVAT, Modelos de ML/DL.
        * **Infraestrutura & DevOps:** Docker, Kubernetes (conceitos), AWS, Linux (Pop!_OS/Kali), Redes.
        * **Automação & Integração:** APIs REST, Webhooks, RPA, BotCity, RegEx.
        """)

# --- ABA 2: EXPERIÊNCIA PROFISSIONAL ---
with tab_exp:
    st.subheader("Histórico Profissional")
    
    with st.expander("🚀 **Engineering Brasil** | Cientista de Dados / Dev Python Júnior (04/2022 - 05/2024)", expanded=True):
        st.markdown("""
        * **Desenvolvimento Backend:** Criação de rotas e APIs utilizando Python e Django para suporte a aplicações inteligentes e análise de dados.
        * **Pipelines de Dados:** Construção, otimização e manutenção de pipelines automatizados de dados, **reduzindo em 25% erros de processamento e detecção**.
        * **Conteinerização:** Garantia de isolamento de ambientes de dev/prod através de **Docker**.
        * **Dashboards:** Criação de dashboards interativos em **Streamlit** integrados a estruturas de dados complexas.
        """)
        
    with st.expander("🛠️ **Intertrack Software e Hardware** | Analista de Sistemas e Suporte Especializado (07/2018 - 10/2022)"):
        st.markdown("""
        * Diagnóstico de falhas em sistemas críticos de rastreamento (GSM/GPRS/Satélites), **reduzindo incidentes em produção em 20%**.
        * Manipulação, consultas complexas e extração de dados usando **SQL** diretamente em bases relacionais.
        * Homologação de hardwares e microsserviços integrados via Java com plataformas de telemetria.
        * Gestão de conectividade em larga escala em Plataforma M2M.
        """)

    with st.expander("🖥️ **NextCorp** | Analista de TI e Monitoramento de Infraestrutura (01/2018 - 05/2018)"):
        st.markdown("""
        * Monitoramento ativo de servidores e análise preditiva de métricas de infraestrutura.
        * Liderança técnica operacional cumprindo SLAs rígidos, com **95% de resolução no primeiro contato**.
        """)

    with st.expander("🏛️ **TRE-MG** | Analista de Suporte Técnico - Estágio (07/2016 - 12/2016)"):
        st.markdown("""
        * Troubleshooting de falhas em sistemas operacionais e redes corporativas com foco em segurança e disponibilidade dos serviços.
        """)

# --- ABA 3: FORMAÇÃO ACADÊMICA ---
with tab_edu:
    st.subheader("Formação & Especializações")
    
    col_edu1, col_edu2 = st.columns(2)
    
    with col_edu1:
        st.markdown("""
        #### 🎓 Pós-Graduações (Especializações)
        * 🔮 **Machine Learning e Inteligência Artificial**  
          *PUC Minas* (Concluído: 2022)
        * 🐍 **Desenvolvimento de Sistemas com Python**  
          *UniCesumar* (Concluído: 2024)
        * 🗄️ **Administração e Modelagem de Banco de Dados**  
          *Faculdade Metropolitana* (Previsão: 2027)
        """)
        
    with col_edu2:
        st.markdown("""
        #### 📜 Graduação
        * 🌐 **Redes de Computadores**  
          *Faculdade Pitágoras* (Concluído: 2017)
          
        #### 🤝 Trabalho Voluntário
        * **Instrutor de Esportes e Idiomas** (Escola Municipal Mestre Ataíde): Liderança, comunicação adaptativa e trabalho em equipe com jovens da comunidade local.
        """)

# Rodapé
st.markdown("---")
st.caption("Aplicação desenvolvida em Python + Streamlit por Juliano Aragão.")