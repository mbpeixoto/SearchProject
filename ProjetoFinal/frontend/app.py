import streamlit as st
import requests

# Configurações
API_URL = "http://backend:8000"

st.title("Sistema de Busca de Conteúdos")

# Busca inicial
query = st.text_input("Pesquise por conteúdos:")
if query:
    response = requests.get(f"{API_URL}/search?query={query}")
    if response.status_code == 200:
        results = response.json()
        for item in results:
            if st.button(f"Ver detalhes: {item['title']}"):
                # Detalhes do conteúdo selecionado
                content_response = requests.get(f"{API_URL}/content/{item['id']}")
                if content_response.status_code == 200:
                    content = content_response.json()
                    st.write("### Informações do Conteúdo")
                    st.write(f"**Título:** {content.get('title', 'Não disponível')}")
                    st.write(f"**Resumo:** {content.get('summary', 'Não disponível')}")
                    st.write(f"**Tags:** {', '.join(content.get('tags', []))}")
                    st.write(f"**Autor:** {content.get('author', 'Não disponível')}")
                    st.write(f"**Detalhes:** {content.get('details', 'Não disponível')}")
                    
                    media_url = content.get("media_url", None)
                    if media_url:
                        try:
                            # Tenta obter a imagem para exibição
                            image_response = requests.get(media_url)
                            if image_response.status_code == 200:
                                st.image(
                                    image_response.content, 
                                    caption=content.get("title", "Imagem"), 
                                    use_container_width=True
                                )
                                # Botão de download
                                st.download_button(
                                    label="Baixar Imagem",
                                    data=image_response.content,
                                    file_name=f"{item['id']}.jpg",
                                    mime="image/jpeg"
                                )
                            else:
                                st.warning("Imagem não disponível para exibição.")
                        except Exception as e:
                            st.error(f"Erro ao carregar a imagem: {e}")
                    else:
                        st.warning("Imagem não disponível.")
                else:
                    st.error("Erro ao buscar os detalhes do conteúdo.")
    else:
        st.error("Erro ao buscar os resultados.")

