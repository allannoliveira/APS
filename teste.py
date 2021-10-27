from geopy.geocoders import Nominatim
from geopy import distance
from geopy.extra.rate_limiter import RateLimiter
import pycep_correios



lista_latitude = [-22.90960695482419, -22.961589033721893, -22.895783162242807, -22.94191480203785, -22.885390241942066, -22.977346943429804, -22.8916416403587]
lista_longitude = [-47.067624773108015, -47.19183587550159, -47.15577551598152, -47.02967678159626, -47.127989301944176, -47.176806659614066,  -47.10025645461092]

lista_ecoponto = ["Ecoponto Região Central (Rua Francisco Theodoro, 1050, Vila Industrial)", "Ecoponto Parque Itajaí (Rua Celso Soares Couto)","Ecoponto Parque São Jorge  (R. Plácida Pretini, 196-270 - Parque São Jorge, Campinas - SP, 13064-812", "Ecoponto Jardim São Gabriel  (R. José Martins Lourenço, 140-284 - Jardim São Gabriel, Campinas - SP, 13045-310", "Ecoponto Parque Via Norte  (Rua dos Cambarás, 200 - Vila Boa Vista, Campinas - SP, 13064-740", "Ecoponto Vida Nova   (R. Lídia Martins de Assis - Conj. Hab. Vida Nova, Campinas - SP, 13057-558","Ecoponto Jardim Eulina (Av. Mal. Rondon, 2296-2382 - Jardim Chapadão, Campinas - SP, 13063-490"]

lista_dist = []

def menu():
    print("----MENU----")
    print("(1) - Materiais")
    print("(2) - Ecopontos")
    print("(3) - Endereço mais próximo")
    print("(4) - Pontos Negativos")
menu()

opcao = int(input("Digite a sua escolha: "))

if opcao == 1:
    funcao =int(input("Escolha um dester materiais \n((1) Metal, (2) Plástico, (3) Eletrônico, (4) Baterias, (5)  Vidro)"))
    
    if funcao == 1:
        print("O primeiro metal descoberto foi o cobre, ainda na pré-história, no oriente médio. Com a descoberta deste material e posteriormente de outros metais foi possível desenvolver ferramentas mais eficientes que as de pedra. Com o uso do metal também foi possível fabricar a roda. Hoje em dia ele é encontrado em nossa casa (ex: panelas, armários, talheres), nos automóveis, nas embalagens de alimentos, etc. Ele é sólido, não deixa passar luz (é opaco) e conduz bem a eletricidade e o calor, possuindo um brilho especial chamado de metálico. Quando aquecido é maleável, podendo ser moldado em várias formas, desde fios até chapas e barras. Os metais podem ser encontrados misturados no solo e nas rochas, sendo chamados de minérios. Composição do Metal Os minérios são substâncias encontradas em solos e rochas de onde é possível extrair os metais. Alguns metais, tais como o ferro e o cobre, são extraídos dos minérios já na forma a se utilizada. Outros, como o aço e o bronze, precisam ser associados a outras substâncias (ex: aço = ferro + carvão).")
    if funcao == 2:
        print("O primeiro plástico sintético foi desenvolvido no início do século XX, e registrou um desenvolvimento acelerado a partir de 1920. Este material, relativamente novo se comparado a outros como o vidro e o papel, passou a estar presente em grande parte dos nossos utensílios. O plástico vem das resinas derivadas do petróleo e pertence ao grupo dos polímeros (moléculas muito grandes, com características especiais e variadas). A palavra plástico tem origem grega e significa aquilo que pode ser moldado. Além disso, uma importante característica do plástico é manter a sua forma após a moldagem. alguns dos tipos de Plásticos são: Os mais rígidos, os fininhos e fáceis de amassar, os transparentes, etc… Eles são divididos em dois grupos de acordo com as suas características de fusão ou derretimento: termoplásticos e termorrígidos. Os termoplásticos são aqueles que amolecem ao serem aquecidos, podendo ser moldados, e quando resfriados ficam sólidos e tomam uma nova forma. Esse processo pode ser repetido várias vezes. Correspondem a 80% dos plásticos consumidos. Ex: polipropileno, polietileno. Os termorrígidos ou termofixos são aqueles que não derretem quando aquecidos, o que impossibilita a sua reutilização através dos processos convencionais de reciclagem. Ex: poliuretano rígido. Em alguns casos, estes materiais podem ser reciclados parcialmente através de moagem prévia e incorporação no material virgem em pequenas quantidades, como ocorre com os elastômeros (borracha).")
    if funcao == 3:
        print("O lixo eletrônico é um dos grandes desafios da sociedade atual graças à obsolescência programada e nossa natureza consumista, há muitos dispositivos eletrônicos no lixo causando grandes danos ao meio ambiente. O lixo eletrônico ou Resíduos de Equipamentos Elétricos e Eletrônicos (REEE) são todos os dispositivos eletroeletrônicos, de celulares, tablets e computadores a TVs, lavadoras de louça e de roupa, geladeiras e etc., que foram descartados por seus donos. Há uma preocupação com certos dispositivos descartados de forma irregular (jogados no lixo comum, por exemplo), como celulares, tablets, computadores e outros com baterias, pois estas contêm elementos altamente danosos ao meio ambiente, que não podem ser jogados em qualquer lugar. Além disso, esses aparelhos contém materiais valiosos e metais raros, úteis para fabricar outros eletrônicos com material reciclado.")
    if funcao == 4:
        print("Não é novidade para quase ninguém que utilizamos cada vez mais aparelhos eletrônicos em nossas rotinas diárias: smartphones, notebooks, controles remotos diversos...A maioria deles, se não todos, têm como fonte de energia as baterias e pilhas.  Mas, você sabe como fazer o descarte correto desses componentes e como é feita a reciclagem de pilhas e baterias usadas? Apesar de existirem diversos modelos, as pilhas e baterias são dispositivos praticamente iguais. Uma bateria nada mais é do que uma sequência de pilhas formadas por agrupamentos em série ou em paralelo. Antes de mais nada, é preciso entender os motivos pelos quais estes resíduos não devem ser descartados no lixo comum (já que vão parar em aterros sanitários) ou deixados nas ruas para que catadores o recolham. As pilhas e as baterias possuem componentes tóxicos prejudiciais ao meio ambiente e à saúde, tais quais mercúrio (a maioria das pilhas botão, alcalinas e de óxido de prata), cádmio (pilhas recarregáveis), chumbo, zinco e níquel. Caso sejam incineradas, os gases resultantes darão lugar a elementos tóxicos voláteis, ou seja, que contaminam o ar. Se descartadas em aterros ou nas ruas, podem intoxicar o solo, os rios e, por consequência, vegetais e animais, além de causar problemas à saúde humana, já que nossos organismos não metabolizam essas substâncias. Com isso, podemos ter problemas graves no sistema nervoso e até câncer. Cada tipo de pilha contém, pelo menos, dois metais presentes em duas formas químicas diferentes, como metais puros e óxidos. Desta forma, ainda que nem todas as pilhas sejam iguais e nem apresentem o mesmo risco ao meio ambiente e à saúde, toda pilha que possui alta concentração de metais deve ser considerada um elemento potencialmente perigoso.")
    if funcao == 5:
        print("O vidro é feito de uma mistura de matérias-primas naturais. Conta-se que ele foi descoberto por acaso, quando, ao fazerem fogueiras na praia, os navegadores perceberam que a areia e o calcário (conchas) se combinaram através da ação da alta temperatura. Há registros de sua utilização desde 7.000 a.C. por sírios, fenícios e babilônios. Hoje o vidro está muito presente em nossa civilização e pode ser moldado de qualquer maneira: nos pára-brisas e janelas dos automóveis, lâmpadas, garrafas, compotas, garrafões, frascos, recipientes, copos, janelas, lentes, tela de televisores e monitores, fibra ótica e etc. As matérias-primas do vidro sempre foram as mesmas há milhares de anos. Somente a tecnologia é que mudou, acelerando o processo e possibilitando maior diversidade para seu uso. O vidro é composto por areia, calcário, barrilha (carbonato de sódio), alumina (óxido de alumínio) e corantes ou descorantes.")

if opcao == 2:
    print("Ecoponto Região Central (Rua Francisco Theodoro, 1050, Vila Industrial", "Ecoponto Parque Itajaí (Rua Celso Soares Couto" "Ecoponto Parque São Jorge  (R. Plácida Pretini, 196-270 - Parque São Jorge, Campinas - SP, 13064-812", "Ecoponto Jardim São Gabriel (R. José Martins Lourenço, 140-284 - Jardim São Gabriel, Campinas - SP, 13045-310", "Ecoponto Parque Via Norte (Rua dos Cambarás, 200 - Vila Boa Vista, Campinas - SP, 13064-740", "Ecoponto Vida Nova (R. Lídia Martins de Assis - Conj. Hab. Vida Nova, Campinas - SP, 13057-558", "Ecoponto Jardim Eulina (Av. Mal. Rondon, 2296-2382 - Jardim Chapadão, Campinas - SP, 13063-490)")

if opcao == 3:
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

if opcao == 4:
    print("error")