from engine import CarExpert
from facts import ClienteProfile, Orcamento, CarModel

def obter_input_inteiro(prompt: str, opcoes: range) -> int:
    try:
        valor = int(input(prompt))
        if valor not in opcoes:
            raise ValueError
        return valor
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        exit()

def obter_input_float(prompt: str) -> float:
    try:
        return float(input(prompt))
    except ValueError:
        print("Valor inválido. Use apenas números.")
        exit()

def main():
    print("\n=== Sistema de Recomendação de Veículos ===")

    faixa_etaria = obter_input_inteiro(
        "Qual a sua faixa etária? (1 = jovem, 2 = adulto, 3 = sênior): ", range(1, 4)
    )
    estado_civil = obter_input_inteiro(
        "Qual é o seu estado civil? (1 = solteiro, 2 = casado com filhos, 3 = divorciado, 4 = viúvo): ", range(1, 5)
    )
    estilo_vida = obter_input_inteiro(
        "Qual é o seu estilo de vida? (1 = urbano, 2 = rural): ", range(1, 3)
    )
    valor = obter_input_float("Qual é o seu orçamento disponível (em reais)? ")

    engine = CarExpert()
    engine.reset()
    engine.declare(ClienteProfile(faixa_etaria=faixa_etaria, estado_civil=estado_civil, estilo_vida=estilo_vida))
    engine.declare(Orcamento(valor=valor))
    modelos_disponiveis = [
        {"modelo": "Ford Ka", "portas": 4},
        {"modelo": "Ford Focus", "portas": 4},
        {"modelo": "Ford Fiesta", "portas": 4},
        {"modelo": "Ford Fusion", "portas": 4},
        {"modelo": "Ford EcoSport", "portas": 4},
        {"modelo": "Ford Edge", "portas": 4},
        {"modelo": "Ford Ranger", "portas": 2},
        {"modelo": "Ford Territory", "portas": 4},
        {"modelo": "Ford Mustang", "portas": 2},
        {"modelo": "Ford Maverick", "portas": 4},
        {"modelo": "Ford Bronco", "portas": 2},
    ]

    for carro in modelos_disponiveis:
        engine.declare(CarModel(**carro))

    print("\nAnalisando seu perfil...\n")
    engine.run()

if __name__ == "__main__":
    main()
