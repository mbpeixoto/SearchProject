from minio import Minio

minio_client = Minio(
    "localhost:9000",  # Substitua por "minio:9000" se estiver acessando de outro container
    access_key="admin",
    secret_key="password",
    secure=False
)

bucket_name = "media"
object_name = "5.jpg"

try:
    # Gera uma URL assinada com validade de 7 dias
    url = minio_client.presigned_get_object(bucket_name, object_name)
    print(f"URL assinada: {url}")
except Exception as e:
    print(f"Erro ao gerar URL assinada: {e}")
