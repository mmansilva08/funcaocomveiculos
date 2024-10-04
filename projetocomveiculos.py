class Veiculo:
    def __init__(self, capacidade_tanque=0, numero_passageiros=0, preco=0.0):
        self.capacidade_tanque = capacidade_tanque
        self.numero_passageiros = numero_passageiros
        self.preco = preco

    def get_capacidade_tanque(self):
        return self.capacidade_tanque

    def set_capacidade_tanque(self, capacidade_tanque):
        self.capacidade_tanque = capacidade_tanque

    def get_numero_passageiros(self):
        return self.numero_passageiros

    def set_numero_passageiros(self, numero_passageiros):
        self.numero_passageiros = numero_passageiros

    def get_preco(self):
        return self.preco

    def set_preco(self, preco):
        self.preco = preco

    def reajustar_preco(self, percentual):
        self.preco += self.preco * (percentual / 100)

    def imprimir(self):
        print(f"Capacidade do Tanque: {self.capacidade_tanque}")
        print(f"Número de Passageiros: {self.numero_passageiros}")
        print(f"Preço: {self.preco}")

    def entrada(self):
        raise NotImplementedError("Subclasses devem implementar este método")


class Aviao(Veiculo):
    def __init__(self, capacidade_tanque=0, numero_passageiros=0, preco=0.0, prefixo="", data_revisao=""):
        super().__init__(capacidade_tanque, numero_passageiros, preco)
        self.prefixo = prefixo
        self.data_revisao = data_revisao

    def get_prefixo(self):
        return self.prefixo

    def set_prefixo(self, prefixo):
        self.prefixo = prefixo

    def get_data_revisao(self):
        return self.data_revisao

    def set_data_revisao(self, data_revisao):
        self.data_revisao = data_revisao

    def imprimir(self):
        super().imprimir()
        print(f"Prefixo: {self.prefixo}")
        print(f"Data de Revisão: {self.data_revisao}")

    def entrada(self):
        try:
            self.capacidade_tanque = int(input("Capacidade do Tanque: "))
            self.numero_passageiros = int(input("Número de Passageiros: "))
            self.preco = float(input("Preço: "))
            self.prefixo = input("Prefixo: ")
            self.data_revisao = input("Data de Revisão: ")
        except ValueError as e:
            print("Erro de entrada: ", e)


class Navio(Veiculo):
    def __init__(self, capacidade_tanque=0, numero_passageiros=0, preco=0.0, nome="", numero_tripulantes=0, data_lancamento=""):
        super().__init__(capacidade_tanque, numero_passageiros, preco)
        self.nome = nome
        self.numero_tripulantes = numero_tripulantes
        self.data_lancamento = data_lancamento

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_numero_tripulantes(self):
        return self.numero_tripulantes

    def set_numero_tripulantes(self, numero_tripulantes):
        self.numero_tripulantes = numero_tripulantes

    def get_data_lancamento(self):
        return self.data_lancamento

    def set_data_lancamento(self, data_lancamento):
        self.data_lancamento = data_lancamento

    def passageiros_por_tripulantes(self):
        return self.numero_passageiros / self.numero_tripulantes

    def imprimir(self):
        super().imprimir()
        print(f"Nome: {self.nome}")
        print(f"Número de Tripulantes: {self.numero_tripulantes}")
        print(f"Data de Lançamento: {self.data_lancamento}")

    def entrada(self):
        try:
            self.capacidade_tanque = int(input("Capacidade do Tanque: "))
            self.numero_passageiros = int(input("Número de Passageiros: "))
            self.preco = float(input("Preço: "))
            self.nome = input("Nome: ")
            self.numero_tripulantes = int(input("Número de Tripulantes: "))
            self.data_lancamento = input("Data de Lançamento: ")
        except ValueError as e:
            print("Erro de entrada: ", e)


if __name__ == "__main__":
    print("Entrada de dados para Avião:")
    aviao = Aviao()
    aviao.entrada()
    aviao.imprimir()

    print("\nEntrada de dados para Navio:")
    navio = Navio()
    navio.entrada()
    navio.imprimir()
