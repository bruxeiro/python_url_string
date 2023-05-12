import re


class ExtratorCep:
    def __init__(self, endereco):
        self.busca = self.regularizar_expressao(endereco)

    @staticmethod
    def regularizar_expressao(endereco):
        padrao = re.compile("[0-9]{4}-?[0-9]{3}")
        buscar = padrao.search(endereco)
        cep = buscar.group()
        return cep


Endereco1 = ExtratorCep("Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120")
print(Endereco1.busca)