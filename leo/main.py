from experta import *
import inspect

class FaixaEtaria(Fact): 
    class Meta:
        unique = True
class EstadoCivil(Fact): 
    class Meta:
        unique = True
class EstiloVida(Fact):
    class Meta:
        unique = True

class Recomendado(Fact): pass
class Pergunta(Fact): pass

class SistemaCarros(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.perguntas_pendentes = []
        self.regrasUsadas = []

    def proxima_pergunta(self):
        if self.perguntas_pendentes:
            fato_class, texto, valores_validos = self.perguntas_pendentes.pop(0)
            while True:
                try:
                    resposta = int(input(texto + " "))
                    if resposta in valores_validos:
                        break
                    else:
                        print(f"Valor inválido. Escolha entre: {valores_validos}")
                except ValueError:
                    print("Digite um número válido.")
            self.declare(fato_class(valor=resposta))
            return True
        return False

    # Adiciona perguntas se os fatos ainda não foram declarados
    @Rule(NOT(FaixaEtaria()))
    def perguntar_faixa_etaria(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.perguntas_pendentes.append((
            FaixaEtaria,
            "Qual a sua faixa etária? (1 = jovem, 2 = adulto, 3 = sênior):",
            [1, 2, 3]
        ))

    @Rule(NOT(EstadoCivil()))
    def perguntar_estado_civil(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.perguntas_pendentes.append((
            EstadoCivil,
            "Qual é o seu estado civil? (1 = solteiro, 2 = casado com filhos, 3 = divorciado, 4 = viúvo):",
            [1, 2, 3, 4]
        ))

    @Rule(NOT(EstiloVida()))
    def perguntar_estilo_vida(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.perguntas_pendentes.append((
            EstiloVida,
            "Qual é o seu estilo de vida? (1 = urbano, 2 = rural):",
            [1, 2]
        ))

    # Regras de recomendação usando fatos separados
    @Rule(AND(FaixaEtaria(valor=1), EstadoCivil(valor=1), EstiloVida(valor=1)))
    def recomendar_ford_ka(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford Ka – Compacto e econômico para jovens solteiros urbanos.")

    @Rule(FaixaEtaria(valor=2), EstadoCivil(valor=2), EstiloVida(valor=1))
    def recomendar_fiat_cronos(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Fiat Cronos – Sedan confortável para adultos com família na cidade.")

    @Rule(FaixaEtaria(valor=3), EstadoCivil(valor=4), EstiloVida(valor=2))
    def recomendar_fiat_strada(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Fiat Strada – Ideal para seniores que vivem no campo.")

    @Rule(FaixaEtaria(valor=2), EstadoCivil(valor=3), EstiloVida(valor=2))
    def recomendar_ford_ranger(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford Ranger – Robusto e confiável para adultos divorciados no meio rural.")

    # Regra genérica caso nenhuma recomendação específica tenha sido feita
    @Rule(FaixaEtaria(valor=MATCH.fe),
          EstadoCivil(valor=MATCH.ec),
          EstiloVida(valor=MATCH.ev),
          NOT(Recomendado()),
          salience=-1
          )
    def sem_recomendacao(self, fe, ec, ev):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        print(f"Nenhuma recomendação para o perfil: faixa_etaria={fe}, estado_civil={ec}, estilo_vida={ev}")

# Execução
engine = SistemaCarros()
engine.reset()

while True:
    engine.run()
    if not engine.proxima_pergunta():
        break

#print(engine.regrasUsadas)