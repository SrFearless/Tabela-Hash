class Nodo:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None

class HashEmplacamento:
    def __init__(self):
        self.tabela = [None] * 10

    def funcao_hash(self, sigla):
        if sigla == 'DF':
            return 7
        return (ord(sigla[0]) + ord(sigla[1])) % 10

    def inserir(self, sigla, nome):
        pos = self.funcao_hash(sigla)
        novo = Nodo(sigla, nome)
        novo.proximo = self.tabela[pos]
        self.tabela[pos] = novo

    def imprimir(self):
        for i, head in enumerate(self.tabela):
            print(f"{i} →", end="")
            atual = head
            while atual:
                print(f" {atual.sigla} →", end="")
                atual = atual.proximo
            print(" None")

if __name__ == "__main__":
    tabela = HashEmplacamento()

    estados = [
        ('MA','Maranhão'), ('MT','Mato Grosso'), ('MS','Mato Grosso do Sul'),
        ('RO','Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'),
        ('SP','São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'),
        ('MG','Minas Gerais'), ('PA','Pará'), ('PB','Paraíba'), ('PR','Paraná'),
        ('AC','Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'),
        ('BA','Bahia'), ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
        ('PE','Pernambuco'), ('PI','Piauí'), ('RJ','Rio de Janeiro'),
        ('RN','Rio Grande do Norte'), ('RS','Rio Grande do Sul'),
        ('DF','Distrito Federal')
    ]

    for sigla, nome in estados:
        tabela.inserir(sigla, nome)

    tabela.inserir('TM', 'Tiago de Freitas Machado')

    print("\nEmplacamentos Representados pelos Estados:")
    tabela.imprimir()
