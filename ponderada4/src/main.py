import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request, Body
from fastapi.responses import FileResponse, StreamingResponse
import os
from supabase import create_client, Client
import asyncio
import aiofiles
import time
app = FastAPI()
# URL e Chave de acesso

url: str = "https://ofwqiyfbxigjotbczyqs.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9md3FpeWZieGlnam90YmN6eXFzIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4Njc3MTU2OSwiZXhwIjoyMDAyMzQ3NTY5fQ.0sDV_prefRg1MYbv4q5QrxBmGYetMCQccj-PPfxhRoY"
supabase: Client = create_client(url, key)
#Nome do bucket utilizado
bucket_name: str = "pond4"
@app.get("/list")
async def list():
    # Lista todas as imagens do Bucket
    res = supabase.storage.from_(bucket_name).list()
    print(res)

@app.post("/upload")
def upload(content: UploadFile = fastapi.File(...)):
    with open(f"recebido/imagens{time.time()}.png", 'wb') as f:
        dados = content.file.read()
        f.write(dados)
        #pass
    return {"status": "ok"}

list_files = os.listdir("recebido")

@app.post("/images")
def images():
    for arquivo in list_files:
        with open(os.path.join("recebido", arquivo), 'rb+') as f:
            dados = f.read()
            res = supabase.storage.from_(bucket_name).upload(f"{time.time()}_{arquivo}", dados)
    return {"message": "Image uploaded successfully"}












