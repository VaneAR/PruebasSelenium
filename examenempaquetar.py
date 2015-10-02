class examenempaquetar():




    def empaquetar(self, lista):
        lista_resultado = []
        contador = 1



        for i in range(len(lista) - 1):

            if lista[i] == lista[i + 1]:
                contador = contador + 1
            else:


                lista_resultado.append((lista[i], contador))
                contador = 1
        lista_resultado.append(((lista[len(lista) - 1]), contador))

        return lista_resultado
