from calculo import Calculo

def main():
    print(
    '''
    Este programa irá servir para lhe auxiliar a descobrir quanto seu carro está
    gastando por Km percorrido
    '''
    )

    print("Os combustíveis disponíveis para este cálculo são:")
    print("\t° Álcool")
    print("\t° Díesel")
    print("\t° Gasolina")

    print(" ")

    try:
        distancia = float(input("Digite a distancia percorrida ou que ira percorrer > "))
        Consumo = float(input("Digite o quanto o combustivel consome por Km/h > "))
        calculo = Calculo()

        print(
            calculo.Calcula_consumo(distancia, Consumo)
        )
    except ValueError as error:
        print(
            'Você digitou um valor errado !'
        )

if __name__ == '__main__':
    main()


