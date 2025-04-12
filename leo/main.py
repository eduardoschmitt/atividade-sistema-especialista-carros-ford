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

class Experiencia(Fact):
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
            "Qual é o seu estado civil? (1 = solteiro, 2 = casado, 3 = divorciado):",
            [1, 2, 3]
        ))

    @Rule(NOT(EstiloVida()))
    def perguntar_estilo_vida(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.perguntas_pendentes.append((
            EstiloVida,
            "Qual é o seu estilo de vida? (1 = urbano, 2 = rural):",
            [1, 2]
        ))

    @Rule(FaixaEtaria(valor=1),
          EstadoCivil(valor=1),
          EstiloVida(valor=1),
          NOT(Experiencia()))
    def perguntar_experiencia(self):
        self.perguntas_pendentes.append((
            Experiencia,
            "Qual a sua experiência desejada? (1 = esportividade, 2 = conforto):",
            [1, 2]
        ))

    @Rule(FaixaEtaria(valor=2),
          EstadoCivil(valor=2),
          EstiloVida(valor=1),
          NOT(Experiencia()))
    def perguntar_experiencia_casado(self):
        self.perguntas_pendentes.append((
            Experiencia,
            "Qual a sua experiência desejada? (1 = esportividade, 2 = conforto):",
            [1, 2]
        ))

    # Regras de recomendação usando fatos separados
    @Rule(FaixaEtaria(valor=1),
          EstadoCivil(valor=1),
          EstiloVida(valor=1),
          Experiencia(valor=1))
    def recomendar_volkswagen_golf(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print(
            "Recomendação: Volkswagen Golf – Esportivo para jovens solteiros no meio urbano.")

    @Rule(FaixaEtaria(valor=1),
          EstadoCivil(valor=1),
          EstiloVida(valor=1),
          Experiencia(valor=2))
    def recomendar_ford_ka(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford Ka – Confortável para jovens solteiros no meio urbano.")

    @Rule(FaixaEtaria(valor=1),
          EstadoCivil(valor=1),
          EstiloVida(valor=2))
    def recomendar_saveiro(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Volkswagen Saveiro – Para jovens solteiros no meio rural.")

    @Rule(FaixaEtaria(valor=1),
          EstadoCivil(valor=2),
          EstiloVida(valor=1))
    def recomendar_voyage(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Volkswagen Voyage – Para jovens casados no meio urbano.")

    @Rule(FaixaEtaria(valor=1),
          EstadoCivil(valor=2),
          EstiloVida(valor=2))
    def recomendar_amarok(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Volkswagen Amarok – Para jovens casados no meio rural.")

    @Rule(FaixaEtaria(valor=2),
          EstadoCivil(valor=1),
          EstiloVida(valor=1))
    def recomendar_hatch(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford Focus Hatch – Para adultos solteiros no meio urbano.")

    @Rule(FaixaEtaria(valor=2),
          EstadoCivil(valor=1),
          EstiloVida(valor=2))
    def recomendar_maverick(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford Maverick – Para adultos solteiros no meio rural.")

    @Rule(FaixaEtaria(valor=2),
          EstadoCivil(valor=2),
          EstiloVida(valor=1),
          Experiencia(valor=1))
    def recomendar_volkswagen_jetta(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print(
            "Recomendação: Volkswagen Jetta – Esportivo para adultos casados no meio urbano.")

    @Rule(FaixaEtaria(valor=2),
          EstadoCivil(valor=2),
          EstiloVida(valor=1),
          Experiencia(valor=2))
    def recomendar_ford_focus(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print(
            "Recomendação: Ford Focus – Confortável para adultos casados no meio urbano.")

    @Rule(FaixaEtaria(valor=2),
          EstadoCivil(valor=2),
          EstiloVida(valor=2))
    def recomendar_ford_eco_sport(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford EcoSport – Para adultos casados no meio rural.")

    @Rule(FaixaEtaria(valor=2),
          EstadoCivil(valor=3),
          EstiloVida(valor=1))
    def recomendar_ford_edge(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford Edge – Para adultos divorciados no meio urbano.")

    @Rule(FaixaEtaria(valor=2),
          EstadoCivil(valor=3),
          EstiloVida(valor=2))
    def recomendar_ford_ranger(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford Ranger – Para adultos divorciados no meio rural.")

    @Rule(FaixaEtaria(valor=3),
          EstadoCivil(valor=1),
          EstiloVida(valor=1))
    def recomendar_ford_nivus(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Volkswagen Nivus – Para sêniors solteiros no meio urbano.")

    @Rule(FaixaEtaria(valor=3),
          EstadoCivil(valor=1),
          EstiloVida(valor=2))
    def recomendar_fiat_toro(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Fiat Toro – Para sêniors solteiros no meio rural.")

    @Rule(FaixaEtaria(valor=3),
          EstadoCivil(valor=2),
          EstiloVida(valor=1))
    def recomendar_volkswagen_virtus(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Volkswagen Virtus – Para sêniors casados no meio urbano.")

    @Rule(FaixaEtaria(valor=3),
          EstadoCivil(valor=2),
          EstiloVida(valor=2))
    def recomendar_ford_raptor(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford Raptor – Para sêniors casados no meio rural.")

    @Rule(FaixaEtaria(valor=3),
          EstadoCivil(valor=3),
          EstiloVida(valor=1))
    def recomendar_ford_fusion(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Ford Fusion – Para sêniors divorciados no meio urbano.")

    @Rule(FaixaEtaria(valor=3),
          EstadoCivil(valor=3),
          EstiloVida(valor=2))
    def recomendar_fiat_strada(self):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        self.declare(Recomendado())
        print("Recomendação: Fiat Strada – Para sêniors divorciados no meio rural.")

    # Regra genérica caso nenhuma recomendação específica tenha sido feita
    @Rule(FaixaEtaria(valor=MATCH.fe),
          EstadoCivil(valor=MATCH.ec),
          EstiloVida(valor=MATCH.ev),
          Experiencia(valor=MATCH.e),
          NOT(Recomendado()),
          salience=-1
          )
    def sem_recomendacao(self, fe, ec, ev):
        self.regrasUsadas.append(inspect.currentframe().f_code.co_name)
        print(f"Nenhuma recomendação para o perfil: faixa_etaria={fe}, estado_civil={ec}, estilo_vida={ev}, experiencia={e}")

# Execução
engine = SistemaCarros()
engine.reset()

while True:
    engine.run()
    if not engine.proxima_pergunta():
        break

#print(engine.regrasUsadas)