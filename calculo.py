class Calculo:

    def __init__(self):
        self.__Gasolina_aditivada = 4.80
        self.__Alcool = 3.80
        self.__Disel = 3.90

    #(distancia / consumo) * self.__valor_gasolina, 2)
    
    def Calcula_consumo(self, Distancia, consumo):
        if Distancia <= 0 or consumo <= 0:
            print('Valor invalido')
            exit()

        Consumo_gasolina = round(
            (Distancia / consumo) * self.__Gasolina_aditivada, 2)
        Consumo_Alcool = round(
            (Distancia / consumo) * self.__Alcool, 2)
        Consumo_disel = round(
            (Distancia / consumo) * self.__Disel, 2)

        return print(
            '''
            Os gastos referentes a cada combustivel seriam:
            Gasolina > R$ {} 
            Alcool > R$  {}
            Disel > R$  {}
            '''
            .format(Consumo_gasolina, Consumo_Alcool, Consumo_disel)
        )