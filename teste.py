# -*- coding: utf-8 -*-
from geopy.geocoders import Nominatim
from geopy import distance
from geopy.extra.rate_limiter import RateLimiter
import pycep_correios

# lista de latitude e longitude dos pontos usados.
lista_latitude = [-22.90960695482419, -22.961589033721893, -22.895783162242807, -22.94191480203785, -22.885390241942066, -22.977346943429804, -22.8916416403587]
lista_longitude = [-47.067624773108015, -47.19183587550159, -47.15577551598152, -47.02967678159626, -47.127989301944176, -47.176806659614066,  -47.10025645461092]

#lista com os endereços convertidos para retorno ao usuário.
lista_ecoponto = ["Ecoponto Região Central (Rua Francisco Theodoro, 1050, Vila Industrial)", "Ecoponto Parque Itajaí (Rua Celso Soares Couto)","Ecoponto Parque São Jorge  (R. Plácida Pretini, 196-270 - Parque São Jorge, Campinas - SP, 13064-812", "Ecoponto Jardim São Gabriel  (R. José Martins Lourenço, 140-284 - Jardim São Gabriel, Campinas - SP, 13045-310", "Ecoponto Parque Via Norte  (Rua dos Cambarás, 200 - Vila Boa Vista, Campinas - SP, 13064-740", "Ecoponto Vida Nova   (R. Lídia Martins de Assis - Conj. Hab. Vida Nova, Campinas - SP, 13057-558","Ecoponto Jardim Eulina (Av. Mal. Rondon, 2296-2382 - Jardim Chapadão, Campinas - SP, 13063-490"]

# lista com o calculo do usuário com as lista de latitude e longitude
lista_dist = []

def menu_initial():
    
    print('''     -------------MENU-------------------
    |  (1) - Materiais                   |
    |  (2) - Ecopontos                   |
    |  (3) - Endereço mais próximo       |
    |  (4) - Pontos Negativos            |
    |  (5) - Sair                        |
     ------------------------------------
    ''')
    
    
    
menu_initial()

opcao = int(input("Digite a sua escolha: "))

    
if opcao == 1:
    
    def menu_mat():
        
        print('''
        ------ Materiais -------
        |  (1) Metal           |
        |  (2) Plástico        |
        |  (3) Eletrônico      |
        |  (4) Baterias        |
        |  (5) Vidros          |
         ----------------------
        ''')

    menu_mat()

    funcao = int(input("Escolha o material desejado: "))

    
    if funcao == 1:
        print("- Algumas das principais características dos metais é a alta capacidade para conduzir calor e eletricidade e quando polidos eles ganham um brilho característico, também possuindo alta densidade eles podem ser usados como reforço para estruturas e como utensílios para cozinha ou como ferramentas para obras. Metais também são formadores de cátions que são moléculas com o número de cátions maior que o de ânions.")
        
    
    elif funcao == 2:
        print("- O plástico está presente em quase todos os lugares do mundo moderno, sendo criado no final do século xx e tendo seu nome derivado do grego que significa aquilo que pode ser moldado sendo barato e de fácil manuseio esse material foi ganhando espaço durante os anos sendo criado a partir da resina do petróleo e pertencendo ao grupo dos polimeros também existem plásticos que são derivados de plantas como do algodão porém sua produção é mais complexa resultando em uma produção em menor escala")

    elif funcao == 3:
        print("- Na reciclagem do lixo eletrônico nem tudo que está la pode ser considerado descartável pois dentro de cada eletrônico ainda existem componentes que podem ser reciclados esses componentes que ainda podem ser reciclados são enviados para a industria onde são derretidos e transformados em matéria prima novamente o lixo eletrônico é um amontoado de todos os outros materiais oque acaba dificultando em sua reciclagem.")

    elif funcao == 4:
        print("- As baterias como as pilhas por exemplo são formadas por dois eletrodos e um eletrolito e suas matéias primas são zinco metálico, pasta de cloreto de amonio, água, dióxido de manganês e grafita tendo a capacidade de transformar a energia quimica em energia eletrica ja a bateria de carro precisa de chumbo, ácido sulfúrico e plástico ja para o ativo da bateria são usados oxidos de chumbo em pó, agua e dependendo da sua carga será adicionado aditivos diferentes.")

    elif funcao == 5:
        print("- O vidro é um dos poucos materiais que podem ser 100% reciclados não perdendo nada no processo, existe também um tipo de vidro chamado de insulado que é capaz de impedir o som e o calor de entrar no ambiente sem perder a luminosidade no processo, em fachadas de estruturas os tipos de vidro que devem ser usados são laminados, aramados e insulados para a fabricação do vidro são usados areia, sódio, cálcio e magnésio e todos eles são misturados em um forno podendo chegar até temperaturas de 1600°C.")
    
    else:
        funcao != "1" and funcao != "2" and funcao != "3" and funcao != "4" and funcao != "5"
        print("Opção inválida!!")

        

elif opcao == 2:
    print("- Ecoponto Região Central (Rua Francisco Theodoro, 1050, Vila Industrial)")
    print("- Ecoponto Parque Itajaí (Rua Celso Soares Couto)")
    print("- Ecoponto Parque São Jorge  (R. Plácida Pretini, 196-270 - Parque São Jorge, Campinas - SP, 13064-812)")
    print("- Ecoponto Jardim São Gabriel (R. José Martins Lourenço, 140-284 - Jardim São Gabriel, Campinas - SP, 13045-310)")
    print("- Ecoponto Parque Via Norte (Rua dos Cambarás, 200 - Vila Boa Vista, Campinas - SP, 13064-740)")
    print("- Ecoponto Vida Nova (R. Lídia Martins de Assis - Conj. Hab. Vida Nova, Campinas - SP, 13057-558)")
    print("- Ecoponto Jardim Eulina (Av. Mal. Rondon, 2296-2382 - Jardim Chapadão, Campinas - SP, 13063-490)")

elif opcao == 3:
    endereco = pycep_correios.get_address_from_cep(str(input("Insira seu CEP: \n(Exemplo 0000-0000)" )))
    geolocator = Nominatim(user_agent="APP")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(endereco["logradouro"] + "," + endereco["cidade"] + "," + endereco["uf"])
    
    user = (location.latitude, location.longitude)
    
    x = 0
    while x <=6:
        distancia = distance.distance(user, (lista_latitude[x], lista_longitude[x])).km
        lista_dist.append(distancia)
        x = x + 1

    posicao = lista_dist.index(min(lista_dist))

    print("O local de descarte mais próximo é:", lista_ecoponto[posicao])

elif opcao == 4:
    print("Malefícios")
    print("----------------------------")
    print("Escreva o nome do material desejado \n( Metal, Plástico, Eletrônico, Baterias, Vidros)")
    
    funcao1 = input("Digite o item que deseja saber os maleficios no meio ambiente: ")
    
    if funcao1 == "metal":
        print("----------- METAL -----------")
        print("Os locais onde ocorrem a maior fixação destes metais são os solos\n e os sedimentos, mas podem ser poluentes das águas e alimentos.\n Além disso, podem ser transportados pela ar através de partículas\n em suspensão, podendo contaminar o homem pelas via aéreas.")

    if funcao1 == "plastico":
        print("----------- PLÁSTICO -----------")
        print("No meio ambiente, os problemas são bem graves. O plástico é difícil\n de ser compactado e gera um grande volume de lixo.\n Portanto, ele ocupa um grande espaço no meio ambiente, o que dificulta\n a decomposição de outros materiais orgânicos. A durabilidade e resistência do plástico viram problemas após o descarte.")
    
    if funcao1 == "papel":
        print("----------- PAPEL -----------")
        print("Você sabia que a fabricação de papel é um dos processos mais poluentes que existem?\n Produzir uma tonelada de papel emite mais de 1.5 toneladas de CO2 equivalente.\n Ou seja, usá-lo menos vai ajudar a reduzir a quantidade de substâncias nocivas na atmosfera.")
    
    if funcao1 == "eletronico":
        print("----------- ELETRÔNICO -----------")
        print("O lixo eletrônico libera substâncias tóxicas no solo e no ar. Os maiores problemas a saúde são os problemas respiratórios e ao sistema nervoso que é feita pela contaminação do organismo com o mercúrio, chumbo, cádmio que estão presentes na maioria destes produtos. ")
    
    if funcao1 == "baterias":
        print("----------- BATERIAS -----------")
        print("O descarte de baterias e pilhas de maneira incorreta, podem contaminar o solo e os lençóis freáticos. Algumas destas baterias são feitas com chumbo, mercúrio, níquel e cadmio que podem acarretar em doenças renais, câncer e problemas ao sistema nervoso.")
    
    if funcao1 == "vidros":
        print("----------- VIDROS -----------")
        print("Em períodos onde há mais chuvas, como o verão, o risco da leptospirose aumenta, pois há maior\n probabilidade de haver enchentes, inundações e, consequentemente, maior contato com o transmissor da doença.\n A leptospirose é uma doença grave, que pode levar até a morte,\n mas que pode ser tratada.")

elif opcao == 5:
    print("Obrigado por utilizar nosso APP!!")
    exit()

else:
    opcao != "1" and opcao != "2" and opcao != "3" and opcao != "4" and opcao != "5"
    print("Opção inválida!!")
    