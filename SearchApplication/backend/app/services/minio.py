from minio import Minio

minio_client = Minio(
    "minio:9000",
    access_key="admin",
    secret_key="password",
    secure=False
)

def get_media_url(content_id: str):
    bucket_name = "media"
    object_name = f"{content_id}.jpg"  # Supondo que as mídias sejam imagens JPEG

    try:
        # Gera uma URL assinada válida
        url = minio_client.presigned_get_object(bucket_name, object_name)
        return url
    except Exception as e:
        # Retorna uma mensagem de erro se algo der errado
        return f"Erro ao gerar URL assinada: {e}"

