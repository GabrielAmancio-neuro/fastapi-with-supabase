from colab.models import Empresa
from fastapi import FastAPI, Body, HTTPException, Query
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('url')
KEY = os.getenv('key')

app = FastAPI(
    title="Colab API",
    description="API para consumo de dados no supabase",
    openapi_url=f"/openapi.json",
    docs_url=f"/docs",
    redoc_url=f"/redoc",
)

supa: Client = create_client(URL, KEY)


@app.post("/empresa/")
def create_empresa(
    id_empresa: str = Body(None, title="Id da empresa"),
    nome: str = Body(..., title="Nome da Empresa"),
    ):

    empresa = Empresa(
        idempresa=id_empresa,
        nome=nome
    )

    try:
        data = supa.table("empresas").insert(empresa.model_dump()).execute()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "code": e.code,
                "message": e.message,
                "details": e.details
            }
        )
    return data

@app.get("/empresa/")
def get_empresa(
    nome: str = Query(..., title="Nome da Empresa"),
    ):

    try:
        data = supa.table("empresas").select("*").eq("nome", nome).execute()
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail={
                "code": e.code,
                "message": e.message,
                "details": e.details
            }
        )
    return data  
    

@app.get(f"/")
async def read_root():
    """Hello World message."""
    return {"message": "Hello World"}
