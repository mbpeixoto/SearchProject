import requests
from pymongo import MongoClient
from minio import Minio
from io import BytesIO

# Configurações
ES_URL = "http://elasticsearch:9200/contents/_doc"  # Host do container ElasticSearch
MONGO_URL = "mongodb://mongodb:27017"  # Host do container MongoDB
MINIO_URL = "minio:9000"  # Host do container Minio
MINIO_ACCESS_KEY = "admin"
MINIO_SECRET_KEY = "password"
MINIO_BUCKET = "media"

# Conexão ao MongoDB
print("Conectando ao Mongo")
mongo_client = MongoClient(MONGO_URL)
db = mongo_client["content_db"]
collection = db["contents"]

# Conexão ao Minio
minio_client = Minio(
    MINIO_URL,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

# Criar bucket no Minio, se não existir
print("Criando bucket Minio")
if not minio_client.bucket_exists(MINIO_BUCKET):
    minio_client.make_bucket(MINIO_BUCKET)

# Conteúdos fictícios de esportes
sports_contents = [
    {
        "title": "A Emoção do Windsurf",
        "summary": "Descubra o mundo emocionante do windsurf.",
        "tags": ["windsurf", "esportes aquáticos", "aventura"],
        "author": "Mateus Onda",
        "details": "O windsurf combina os elementos do surfe e da vela, oferecendo uma experiência única de esporte aquático.",
        "media_url": "https://nxboats.com.br/wp-content/uploads/2023/10/windsurf.jpg"
    },
    {
        "title": "Futebol: O Esporte do Mundo",
        "summary": "Uma visão geral do futebol, o esporte mais popular do planeta.",
        "tags": ["futebol", "esportes", "paixão mundial"],
        "author": "Lucas Artilheiro",
        "details": "O futebol é jogado em quase todos os países e une pessoas ao redor do mundo.",
        "media_url": " https://www.folhadelondrina.com.br/img/Facebook/3260000/O-futebol-brasileiro-emburreceu0326460100202409081617.jpg?xid=6117711"
        
    },
    {
        "title": "A Elegância da Equitação",
        "summary": "Explorando a elegância e habilidade da equitação.",
        "tags": ["equitação", "hipismo", "esportes ao ar livre"],
        "author": "João Cavalo",
        "details": "A equitação não é apenas um esporte, mas também uma arte que exige graça e conexão com o cavalo.",
        "media_url": "https://s2.static.brasilescola.uol.com.br/be/2024/04/mulher-loira-em-pratica-de-hipismo-durante-salto-com-cavalo.jpg"
        
    },
    {
        "title": "Introdução ao Basquete",
        "summary": "Um guia para iniciantes no jogo de basquete.",
        "tags": ["basquete", "esportes coletivos", "NBA"],
        "author": "Leo Enterrada",
        "details": "O basquete é um esporte dinâmico e coletivo que combina habilidade atlética e estratégia.",
        "media_url": "https://www.cnnbrasil.com.br/wp-content/uploads/sites/12/2024/07/Pre_Olimpico_de-_Basquete-Masculino_Brasil_vence_Filipinas_vai_a_final_e_fica_a_um_jogo_de_Paris-e1720273472112.jpg?w=886"
        
    },
    {
        "title": "O Mundo do Tênis",
        "summary": "Uma introdução ao emocionante jogo de tênis.",
        "tags": ["tênis", "raquetes", "grandes torneios", "esportes"],
        "author": "Klayton Match Point",
        "details": "O tênis é um esporte popular jogado globalmente, conhecido por torneios icônicos como Wimbledon e o US Open.",
        "media_url": "https://ogimg.infoglobo.com.br/in/20562139-b2e-055/FT1086A/2016-913645906-2016-913497361-201606021122227011_AFP.jpg_20160602.jpg_201606.jpg"
    
    }
]

# Populando os serviços
print("Populando serviços com conteúdos fictícios...")
for i, content in enumerate(sports_contents, start=1):
    content_id = str(i)
    
    # Adicionar ao ElasticSearch
    print(f"Adicionando conteúdo {i} ao ElasticSearch...")
    es_response = requests.post(f"{ES_URL}/{content_id}", json=content)
    if es_response.status_code == 201:
        print(f"Conteúdo {i} adicionado ao ElasticSearch com sucesso.")
    else:
        print(f"Erro ao adicionar conteúdo {i} ao ElasticSearch: {es_response.text}")
    
    # Adicionar ao MongoDB
    print(f"Adicionando conteúdo {i} ao MongoDB...")
    mongo_payload = {"_id": content_id, **content}
    collection.insert_one(mongo_payload)
    
    # Download e upload de mídia ao Minio
    print(f"Baixando e fazendo upload da mídia para o Minio para conteúdo {i}...")
    image_response = requests.get(content["media_url"])
    if image_response.status_code == 200:
        image_content = BytesIO(image_response.content)
        minio_client.put_object(
            MINIO_BUCKET,
            f"{content_id}.jpg",
            image_content,
            length=image_content.getbuffer().nbytes,
            content_type="image/jpeg"
        )
    else:
        print(f"Erro ao baixar a imagem do conteúdo {i}.")

print("População concluída!")

