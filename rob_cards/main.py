import urllib.request
import re
from pprint import pprint

count = 1;
response = None

def files_BinaryToText(file_name):
    file_open = open(file_name, 'rb')
    file_open_texto = open(file_name + ".txt", 'w')
    if(file_open):
        file_open_texto.write(str(file_open.read()))
    file_open.close()
    file_open_texto.close()

def data_ListaToString(lista):
    texto = ""
    for item in lista:
        texto += str(item)
        texto += "\n"
    return texto

def url_realms():
    print("URLS")
    url_man = "http://seesaawiki.jp/mnga_bahamut/d/%bf%cd%c2%b0%c0%ad%20%b2%e8%c1%fc%b0%ec%cd%f7"
    url_gods = "http://seesaawiki.jp/mnga_bahamut/d/%bf%c0%c2%b0%c0%ad%20%b2%e8%c1%fc%b0%ec%cd%f7"
    url_demons = "http://seesaawiki.jp/mnga_bahamut/d/%cb%e2%c2%b0%c0%ad%20%b2%e8%c1%fc%b0%ec%cd%f7"
    list_realms = {url_man: 'man.html', url_gods: 'gods.html', url_demons: 'demons.html'}
    for realm, realm_arq in list_realms.items():
        req = urllib.request.Request(realm)
        try :
            response = urllib.request.urlopen(req)
        except urllib.error.URLError as error:
            print(error.reason)

        if(response != None):
            file = 'F://Download//Images//RoB' + realm_arq
            file_open = open(file, 'wb')
            file_open.write(response.read())
            print('ARQUIVO SALVO')
            file_open.close()
            files_BinaryToText(file)
            #url_cards(file)
        print(" ----- ")
    print('{FINISHED ALL}')

def offline():
    print("HTML")
    list_realms =['man.html','gods.html', 'demons.html']
    for realm in list_realms:
        file = 'F://Download//Images//RoB' + realm + '.txt'
        url_cards(file)
        print(" ----- ")
    print('{FINISHED ALL}')

def url_cards(file):
    print("SEARCHING CARDS")

    pattern_parent = re.compile('http://seesaawiki.jp/mnga_bahamut/d/[%\w\w]*')
    # print("Expressao regular: %s " % (pattern_parent.pattern))
    
    file_open = open(file, 'r')
    file_string = file_open.read()
    if(file_string):
        # print(file_string)
        # print("ARQUIVO %s" % (file))
        result_set = pattern_parent.findall(file_string)
        if(result_set):
            # pprint(result_set)
            result_set_string = data_ListaToString(result_set)
            file_results = open(file + "_results.txt", 'w')
            file_results.write(result_set_string)
            file_results.close()
            each_card(result_set)
    file_open.close()
    print('{FINISHED 1}')

def each_card(lista):
    print("SEARCHING EACH CARD")
    pattern_card = re.compile('http://image\d\d.seesaawiki.jp/m/t/mnga_bahamut/[\w]*\.')
    print("Expressao regular: %s " % (pattern_card.pattern))

    for item in lista:
        url = str(item)
        print(url)

        req = urllib.request.Request(url)
        try :
            response = urllib.request.urlopen(req)
        except urllib.error.URLError as error:
            print(error.reason)
        if(response != None):
            page = response.read()
            page_str = str(page)
            pattern_card = re.compile('http://image\d\d.seesaawiki.jp/m/t/mnga_bahamut/[\w]*\.jp[e]?g')
            result_set = pattern_card.findall(page_str)
            if(result_set):
                #pprint(result_set)
                download_cards(result_set)
        print(" ----- ")
    print('{FINISHED 2}')

def download_cards(cards):
    for card in cards:
        url = str(card)
        req = urllib.request.Request(url)
        try :
            response = urllib.request.urlopen(req)
        except urllib.error.URLError as error:
            print(error.reason)
        if(response != None):
            pattern_name = re.compile('[\w]*\.jp[e]?g')
            nome = pattern_name.findall(card)
            file = "F://Download//Images//RoB//" + nome[0]
            file_open = open(file, 'wb')
            file_open.write(response.read())
            print('ARQUIVO SALVO')
            file_open.close()
        print(" ----- ")
    print('{FINISHED 3}')

def regex():
    padrao = re.compile('[\w]*\.jp[e]?g')
    print("Padrao: " + padrao.pattern)
    #result = padrao.findall('abc abd aba abcate')
    #result = padrao.findall("http://seesaawiki.jp/mnga_bahamut/d/%cb%e2%c2%b0%c0%ad%20%b2%e8%c1%fc%b0%ec%cd%f7, http://seesaawiki.jp/mnga_bahamut/d/%8e%cd%8e%de%8e%cb%8e%de%8e%b0%8e%b3%8e%de%8e%a7%8e%dd%8e%ca%8e%df%8e%b2%8e%b1%20%28%8e%c9%8e%b0%8e%cf%8e%d9%29")
    result = padrao.findall('http://image01.seesaawiki.jp/m/t/mnga_bahamut/35ee5bc3b9147c99.jpg')
    if(result != None):
        print(result[0])

def arquivos():
    from pprint import pprint as pp
    pattern_parent = re.compile('http://image\d\d.seesaawiki.jp/m/t/mnga_bahamut/[\w]*\.jp[e]?g')
    
    arquivo = open('C://Downloads//RoB//teste.txt', 'r')
    temp = arquivo.read()
    print(temp)
    result = pattern_parent.findall(temp)
    pp(result)
    arquivo.close()

#url_realms()
offline()
#regex()
#arquivos()

''''
pattern_images = re.compile('http://image\d{2}.seesaawiki.jp/m/t/mnga_bahamut/\w{16}\.\w{3}')

req = urllib.request.Request('http://image01.seesaawiki.jp/m/t/mnga_bahamut/00508ce483560b4b.JPG')
try :
    response = urllib.request.urlopen(req)
except urllib.error.URLError as e:
        print(e.reason)
        
#html = response.read()
folder = "G://Download//Images//RoB//" + str(count) + ".jpg"
file = open(folder, 'wb')
if(response != None):
    file.write(response.read())
file.close()
'''
