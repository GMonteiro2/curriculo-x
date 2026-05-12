from pydantic import BaseModel

class CurriculoInput(BaseModel):
    curriculo: str

class AnaliseOutput(BaseModel):
    pontos_fortes: list[str]
    pontos_fracos: list[str]
    sugestoes: list[str]
    nota_geral: int