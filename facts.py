# facts.py
from experta import Fact, Field

class CarModel(Fact):
    """Modelo de carro disponível."""
    modelo = Field(str, mandatory=True)
    portas = Field(int, mandatory=True)

class ClienteProfile(Fact):
    """Perfil do cliente para recomendação."""
    faixa_etaria = Field(int, mandatory=True)
    estado_civil = Field(int, mandatory=True)
    estilo_vida = Field(int, mandatory=True)

class Orcamento(Fact):
    """Orçamento disponível do cliente."""
    valor = Field(float, mandatory=True)
