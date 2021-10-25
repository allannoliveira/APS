from geopy.geocoders import Nominatim
from geopy import distance
from geopy.extra.rate_limiter import RateLimiter
import pycep_correios
import requests

#user = [] 
lista_latitude = [-22.90960695482419, -22.961589033721893, -22.895783162242807, -22.94191480203785, -22.885390241942066, -22.977346943429804, -22.8916416403587]
lista_longitude = [-47.067624773108015, -47.19183587550159, -47.15577551598152, -47.02967678159626, -47.127989301944176, -47.176806659614066,  -47.10025645461092]

lista_ecoponto = ["Ecoponto Região Central (Rua Francisco Theodoro, 1050, Vila Industrial)", "Ecoponto Parque Itajaí (Rua Celso Soares Couto)","Ecoponto Parque São Jorge  (R. Plácida Pretini, 196-270 - Parque São Jorge, Campinas - SP, 13064-812", "Ecoponto Jardim São Gabriel  (R. José Martins Lourenço, 140-284 - Jardim São Gabriel, Campinas - SP, 13045-310", "Ecoponto Parque Via Norte  (Rua dos Cambarás, 200 - Vila Boa Vista, Campinas - SP, 13064-740", "Ecoponto Vida Nova   (R. Lídia Martins de Assis - Conj. Hab. Vida Nova, Campinas - SP, 13057-558","Ecoponto Jardim Eulina (Av. Mal. Rondon, 2296-2382 - Jardim Chapadão, Campinas - SP, 13063-490"]

lista_dist = []

def menu():
    print("----MENU----")
    print("(1) Materiais")
    print("(2) Ecopontos")
    print("(3) Endereço mais próximo")
    print("(4) Pontos Negativos")
menu()

opcao = int(input("Digite a sua escolha: "))

if opcao == 1:
    print("error")

if opcao == 2:
    print("Ecoponto Região Central (Rua Francisco Theodoro, 1050, Vila Industrial", "Ecoponto Parque Itajaí (Rua Celso Soares Couto" "Ecoponto Parque São Jorge  (R. Plácida Pretini, 196-270 - Parque São Jorge, Campinas - SP, 13064-812", "Ecoponto Jardim São Gabriel (R. José Martins Lourenço, 140-284 - Jardim São Gabriel, Campinas - SP, 13045-310", "Ecoponto Parque Via Norte (Rua dos Cambarás, 200 - Vila Boa Vista, Campinas - SP, 13064-740", "Ecoponto Vida Nova (R. Lídia Martins de Assis - Conj. Hab. Vida Nova, Campinas - SP, 13057-558", "Ecoponto Jardim Eulina (Av. Mal. Rondon, 2296-2382 - Jardim Chapadão, Campinas - SP, 13063-490)")

if opcao == 3:
    endereco = pycep_correios.get_address_from_cep(str(input("Insira seu CEP, (Exemplo 0000-0000)")))
    geolocator = Nominatim(user_agent="APP")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.geocode(endereco["logradouro"] + "," + endereco["cidade"] + "," + endereco["uf"])
    
    user = (location.latitude, location.longitude)
    
    y = 0
    while y <=6:
        distancia = distance.distance(user, (lista_latitude[y], lista_longitude[y])).km
        lista_dist.append(distancia)
        y = y + 1

    posicao = lista_dist.index(min(lista_dist))

    print("O local de descarte mais próximo é:", lista_ecoponto[posicao])

    
    
 



    

    

