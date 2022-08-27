while True:
  
  # Im new at ṕython progamming.
  
            print('\nOpções:\n1) 2x2\n2) 3x3\n3) Matriz a - b (2x2)\n4) Matriz a + b (2x2)\n5) matriz a x b (2x2\n6) Calculo de juros simples\n7) Calculo de juros compostos')
            matriz = float(input('Escolha o tipo de matriz: '))
            if matriz == 1:
                print('|a b|\n|c d|')
                n1 = float(input('Digite o valor de a:'))
                n2 = float(input('Digite o valor de b: '))
                n3 = float(input('Digite o valor de c: '))
                n4 = float(input('Digite o valor de d: '))
                print(f'A matriz a ser calculada é:\n\n{n1} {n2}\n{n3} {n4}\n')
                calc = (n1 * n4) - (n2 * n3)
                princ = n1 * n4
                secun = n2 * n3
                print(f'Diagonal principal: {n1}*{n4}\nDiagonal secundaria: {n2}*{n3}\nSubstração para descobrir o determinante (Principal - secundaria): {princ} - {secun}\nO determinante da matriz é: {calc}')
            elif matriz == 2:
                print('|a b c|\n|d e f|\n|g h i|')
                n1 = float(input('Digite o valor de a: '))
                n2 = float(input('Digite o valor de b: '))
                n3 = float(input('Digite o valor de c: '))
                n4 = float(input('Digite o valor de d: '))
                n5 = float(input('Digite o valor de e: '))
                n6 = float(input('Digite o valor de f: '))
                n7 = float(input('Digite o valor de g: '))
                n8 = float(input('Digite o valor de h: '))
                n9 = float(input('Digite o valor de i: '))
                print(f'A matriz a ser calculada é:\n|{n1} {n2} {n3}|\n|{n4} {n5} {n6}|\n|{n7} {n8} {n9}|\n')
                calc = ((n1 * n5) * n9) + ((n2 * n6) * n7) + ((n3 * n4) * n8) - (((n3 * n5) * n7) + ((n1 * n6) * n8) + ((n2 * n4) * n9))
                princ = ((n1 * n5) * n9) + ((n2 * n6) * n7) + ((n3 * n4) * n8)
                secun = ((n3 * n5) * n7) + ((n1 * n6) * n8) + ((n2 * n4) * n9)
                print(f'Diagonal principal: {n1}*{n5}*{n9} + {n2}*{n6}*{n7} + {n3}*{n4}*{n8} = {princ}\nDiagonal secundária: {n3}*{n5}*{n7} + {n1}*{n6}*{n8} + {n2}*{n4}*{n9} = {secun}\nSubtração para descobrir o determinante (principal - secundaria): {princ} - {secun}\n\nO determinante é: {calc}')
            elif matriz == 3:
                print('|a b| |a2 b2|\n|c d|-|c2 d2|')
                n1 = float(input('Digite o valor de a: '))
                n2 = float(input('Digite o valor de b: '))
                n3 = float(input('Digite o valor de c: '))
                n4 = float(input('Digite o valor de d: '))
                n5 = float(input('Digite o valor de a2: '))
                n6 = float(input('Digite o valor de b2: '))
                n7 = float(input('Digite o valor de c2: '))
                n8 = float(input('Digite o valor de d2: '))
                a = n1 - n5
                b = n2 - n6
                c = n3 - n7
                d = n4 - n8
                print(f'A matriz gerada é:\n|{a} {b}|\n|{c} {d}|')
            elif matriz == 4:
                print('|a b| |a2 b2|\n|c d|+|c2 d2|')
                n1 = float(input('Digite o valor de a: '))
                n2 = float(input('Digite o valor de b: '))
                n3 = float(input('Digite o valor de c: '))
                n4 = float(input('Digite o valor de d: '))
                n5 = float(input('Digite o valor de a2: '))
                n6 = float(input('Digite o valor de b2: '))
                n7 = float(input('Digite o valor de c2: '))
                n8 = float(input('Digite o valor de d2: '))
                a = n1 + n5
                b = n2 + n6
                c = n3 + n7
                d = n4 + n8
                print(f'A matriz gerada é:\n|{a} {b}|\n|{c} {d}|')
            elif matriz == 5:
                print('|a b| |a2 b2|\n|c d|*|c2 d2|')
                n1 = float(input('Digite o valor de a: '))
                n2 = float(input('Digite o valor de b: '))
                n3 = float(input('Digite o valor de c: '))
                n4 = float(input('Digite o valor de d: '))
                n5 = float(input('Digite o valor de a2: '))
                n6 = float(input('Digite o valor de b2: '))
                n7 = float(input('Digite o valor de c2: '))
                n8 = float(input('Digite o valor de d2: '))
                l1c1 = (n1 * n5) + (n2 * n7)
                l1c2 = (n1 * n6) + (n2 * n8)
                l2c1 = (n3 * n5) + (n4 * n7)
                l2c2 = (n3 * n6) + (n4 * n8)
                print(f'A matriz gerada é:\n|{l1c1} {l1c2}|\n|{l2c1} {l2c2}|')
            elif matriz == 6:
                print('Formula juros simples: J = C*i*t (J= Juros | C= capital | i= taxa de juros | t= tempo)')
                c = float(input('Digite o valor do capital: '))
                taxa = float(input('Digite a taxa de juros: '))
                t = float(input('Digite o tempo (em meses): '))
                i = taxa/100
                juros = c * i * t
                montante = c + juros
                print(f'O valor dos juros da aplicação é de {juros}\nE o montante a ser resgatado é de {montante}.')
            elif matriz == 7:
                print('Formula juros compostos: M = C * (1 + i)n (M= Montante | C= capital | i= taxa de juros | n= tempo)')
                c = float(input('Digite o valor do capital: '))
                taxa = float(input('Digite a taxa de juros (use . no lugar de ,): '))
                t = float(input('Digite o tempo (em meses): '))
                i = taxa/100
                juros = c * ((1 + i) ** t)
                montante = c + juros
                print(f'O valor dos juros da aplicação é de {juros:1f}\nE o montante a ser resgatado é de {montante:1f}.')
