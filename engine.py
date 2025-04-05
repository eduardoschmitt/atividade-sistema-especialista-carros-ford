# engine.py
from experta import KnowledgeEngine, Rule, P
from facts import ClienteProfile, Orcamento, CarModel

class CarExpert(KnowledgeEngine):

    @Rule(
        ClienteProfile(faixa_etaria=1, estado_civil=1, estilo_vida=1),
        Orcamento(valor=P(lambda v: v <= 30000)),
        CarModel(modelo="Ford Ka", portas=4)
    )
    def rule_ford_ka(self):
        print("Recomendação: Ford Ka - compacto e econômico, ideal para jovens com orçamento limitado.")

    @Rule(
        ClienteProfile(faixa_etaria=2, estado_civil=2, estilo_vida=1),
        Orcamento(valor=P(lambda v: 30000 < v <= 50000)),
        CarModel(modelo="Ford Focus", portas=4)
    )
    def rule_ford_focus(self):
        print("Recomendação: Ford Focus - confortável, ideal para famílias com orçamento intermediário.")

    @Rule(
        ClienteProfile(faixa_etaria=2, estado_civil=2, estilo_vida=2),
        Orcamento(valor=P(lambda v: 30000 < v <= 60000)),
        CarModel(modelo="Ford EcoSport", portas=4)
    )
    def rule_ford_ecosport(self):
        print("Recomendação: Ford EcoSport - ideal para famílias que vivem na zona rural e precisam de um SUV robusto.")

    @Rule(
        ClienteProfile(faixa_etaria=3, estado_civil=4, estilo_vida=1),
        Orcamento(valor=P(lambda v: 50000 < v <= 80000)),
        CarModel(modelo="Ford Fusion", portas=4)
    )
    def rule_ford_fusion(self):
        print("Recomendação: Ford Fusion - sedan sofisticado, ideal para conforto urbano para seniores.")

    @Rule(
        ClienteProfile(faixa_etaria=1, estado_civil=1, estilo_vida=1),
        Orcamento(valor=P(lambda v: 80000 < v <= 130000)),
        CarModel(modelo="Ford Mustang", portas=2)
    )
    def rule_ford_mustang(self):
        print("Recomendação: Ford Mustang - esportivo de alto desempenho, ideal para jovens que buscam adrenalina e status.")

    @Rule(
        ClienteProfile(faixa_etaria=2, estado_civil=2, estilo_vida=2),
        Orcamento(valor=P(lambda v: 70000 < v <= 100000)),
        CarModel(modelo="Ford Ranger", portas=2)
    )
    def rule_ford_ranger(self):
        print("Recomendação: Ford Ranger - picape robusta, perfeita para quem vive no campo e precisa de utilitário forte.")

    @Rule(
        ClienteProfile(faixa_etaria=2, estado_civil=3, estilo_vida=1),
        Orcamento(valor=P(lambda v: 60000 < v <= 90000)),
        CarModel(modelo="Ford Edge", portas=4)
    )
    def rule_ford_edge(self):
        print("Recomendação: Ford Edge - SUV espaçoso e confortável para quem busca estabilidade e espaço.")