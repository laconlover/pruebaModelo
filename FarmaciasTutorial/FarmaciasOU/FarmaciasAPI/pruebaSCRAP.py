from bs4 import BeautifulSoup
import requests
 
url = 'https://registro.cofourense.com/publica/ver_guardias.php'
pagina = requests.get(url, timeout=5)
contenido = BeautifulSoup(pagina.content, 'html.parser')

guardias = contenido.find_all('div', class_='datos_guardia')

#print(contenido)

#farmacias = list()

for i in guardias:
    first_p = i.find("p")
    et_p = i.findChildren("p" , recursive=False)
    if not first_p.text.startswith("Del "):
        d = dict([])
        d["type"] = "diurna"
        d["name"] = et_p[0].text
        d["phone"] = et_p[2].text
        d["address"] = et_p[1].text
        print(d)
        #for child in et_p:
            #print(child.text)
    #farmacias.append(c.text)

#print(farmacias)
