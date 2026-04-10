class Calculadora:
    def adicionar (self, a, b):
        return a + b
    def subtrair (self, a, b):
        return a - b
    def multiplicacao (self, a, b):
        return a * b
    def divisao (self, a, b):
        if a == 0 or b == 0:
            print("Não dividimos por 0")
        self.primeiro = a
        self.segundo = b
        dividir = self.primeiro / self.segundo
        return dividir

calc = Calculadora()
print(calc.adicionar(10, 5))
print(calc.subtrair(10, 5))
print(calc.multiplicacao(10, 5))
print(calc.divisao(10, 0))