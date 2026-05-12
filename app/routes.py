from fastapi import APIRouter, HTTPException, UploadFile, File
from app.models import CurriculoInput, AnaliseOutput
from app.analyzer import analisar_curriculo
import PyPDF2
import io

router = APIRouter()

@router.post("/analisar", response_model=AnaliseOutput)
async def analisar(input: CurriculoInput):
    try:
        resultado = analisar_curriculo(input.curriculo)
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na análise: {str(e)}")

@router.post("/analisar-arquivo", response_model=AnaliseOutput)
async def analisar_arquivo(arquivo: UploadFile = File(...)):
    try:
        conteudo = await arquivo.read()

        if arquivo.filename.endswith(".pdf"):
            leitor = PyPDF2.PdfReader(io.BytesIO(conteudo))
            texto = ""
            for pagina in leitor.pages:
                texto += pagina.extract_text()
        elif arquivo.filename.endswith(".txt"):
            texto = conteudo.decode("utf-8")
        else:
            raise HTTPException(status_code=400, detail="Formato não suportado. Use PDF ou TXT.")

        if not texto.strip():
            raise HTTPException(status_code=400, detail="Não foi possível extrair texto do arquivo.")

        resultado = analisar_curriculo(texto)
        return resultado

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na análise: {str(e)}")