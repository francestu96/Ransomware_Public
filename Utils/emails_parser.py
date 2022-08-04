from bs4 import BeautifulSoup
import json
import urllib.request
import urllib.parse

def parse_unibo():
    with urllib.request.urlopen("https://corsi.unibo.it/laurea/Podologia/docenti") as htmlPage:
        html = htmlPage.read().decode("utf-8")

    hub_html = BeautifulSoup(html, "html.parser")

    with open("unibo_targets.csv", "a") as targets:
        for person in hub_html.findAll("div", {"class": "people-item"}):
            with urllib.request.urlopen(person.find("a")["href"]) as htmlPage:
                html = htmlPage.read().decode("utf-8")
            parsed_html = BeautifulSoup(html, "html.parser")
            email = parsed_html.find("div", {"class": "box-contact"}).find("a")["href"].replace("mailto:", "")
            targets.write(email + "\n")

def parse_unipi():
    with urllib.request.urlopen("https://www.ec.unipi.it/dipartimento/persone/") as htmlPage:
        html = htmlPage.read().decode("utf-8")

    parsed_html = BeautifulSoup(html, "html.parser")

    with open("unipi_targets.csv", "a") as targets:
        for person in parsed_html.findAll("span", {"class": "text-email"}):
            email = person.find("a")["href"].replace("mailto:", "")
            targets.write(email + "\n")

def parse_unina():
    with urllib.request.urlopen("http://www.giurisprudenza.unina.it/it/_custom/personaledocente.php") as htmlPage:
        html = htmlPage.read().decode("utf-8", "ignore")

    parsed_html = BeautifulSoup(html, "html.parser")

    with open("unina_targets.csv", "a") as targets:
        for person in parsed_html.find("table").findAll("a"):
            if(person["href"].startswith("mailto:")):
                email = person["href"].replace("mailto:", "")
                targets.write(email + "\n")
            
def parse_unipa():
    with urllib.request.urlopen("https://www.unipa.it/dipartimenti/sc.psicol.pedag.edellaformazione/?pagina=personale&ruolo=docenti") as htmlPage:
        html = htmlPage.read().decode("utf-8", "ignore")

    parsed_html = BeautifulSoup(html, "html.parser")

    with open("unipa_targets.csv", "a") as targets:
        for person in parsed_html.findAll("div", {"class": "row equal"}):
            elements = person.findAll("a")
            for element in elements:
                if(element["href"].startswith("mailto:")):
                    email = element["href"].replace("mailto:", "")
                    targets.write(email + "\n")

def parse_uniroma():
    for page in range(3, 8):
        with urllib.request.urlopen("https://www.lettere.uniroma1.it/elenco-completo-docenti?page=" + str(page)) as htmlPage:
            html = htmlPage.read().decode("utf-8")

        hub_html = BeautifulSoup(html, "html.parser")

        with open("uniroma_targets.csv", "a") as targets:
            for person in hub_html.findAll("td", {"class": "views-field-field-user-cognome"}):
                with urllib.request.urlopen("https://www.lettere.uniroma1.it" + person.find("a")["href"]) as htmlPage:
                    html = htmlPage.read().decode("utf-8", "ignore")
                parsed_html = BeautifulSoup(html, "html.parser")
                email = parsed_html.find("div", {"id": "mail_profilo"}).find("a")["href"].replace("mailto:", "")
                targets.write(email + "\n")

def parse_unito():
    for page in range(0, 400, 100):
        with urllib.request.urlopen("https://www.lingue.unito.it/do/docenti.pl/Search?title=In%20ordine%20alfabetico;first=" + str(page)) as htmlPage:
            html = htmlPage.read().decode("utf-8")

        hub_html = BeautifulSoup(html, "html.parser")

        with open("unito_targets.csv", "a") as targets:
            for person in hub_html.find("main", {"id": "mainContent"}).findAll("div",{"class", "col-md-11"}):
                with urllib.request.urlopen("https://www.lingue.unito.it" + person.find("a")["href"]) as htmlPage:
                    html = htmlPage.read().decode("utf-8", "ignore")
                parsed_html = BeautifulSoup(html, "html.parser")
                check = parsed_html.find("div", {"id": "panel_profilo"})
                if (check.find("li", {"class": "icon-envelope"})):
                    email = check.find("li", {"class": "icon-envelope"}).find("a")["href"].replace("mailto:", "")
                    targets.write(email + "\n")

def parse_unimore():
    with urllib.request.urlopen("https://www.giurisprudenza.unimore.it/site/home/personale-docente.html") as htmlPage:
        html = htmlPage.read().decode("utf-8", "ignore")

    parsed_html = BeautifulSoup(html, "html.parser")

    with open("unimore_targets.csv", "a") as targets:
        for person in parsed_html.find("table").findAll("a"):
            if(person["href"].startswith("mailto:")):
                email = person["href"].replace("mailto:", "")
                targets.write(email + "\n")

def parse_univpm():
    with urllib.request.urlopen("https://www.univpm.it/Entra/Professors/Sciences_1") as htmlPage:
        html = htmlPage.read()

    hub_html = BeautifulSoup(html, "html.parser")

    with open("univpm_targets.csv", "a") as targets:
        for person in hub_html.findAll("a", {"class": "RALink RALinkIn"}):
            with urllib.request.urlopen(person["href"]) as htmlPage:
                html = htmlPage.read().decode("utf-8")
            parsed_html = BeautifulSoup(html, "html.parser")
            email = parsed_html.findAll("a", {"class": "RALink img-responsive RALinkOut"})[9]["href"].replace("mailto:", "")
            targets.write(email + "\n")

def parse_unisi(): 
    for page in range(0, 65): 
        data = urllib.parse.urlencode({"page": page, "view_name": "ugovpersona_elenco", "view_display_id": "block"}).encode()
        req =  urllib.request.Request("https://docenti.unisi.it/it/views/ajax", data=data)
        with urllib.request.urlopen(req) as response:
            json_data = response.read().decode("utf-8")

        hub_html = BeautifulSoup(json.loads(json_data)[1]["data"], "html.parser")

        with open("unisi_targets.csv", "a") as targets:
            for person in hub_html.findAll("div",{"class", "views-row"}):
                with urllib.request.urlopen("https://docenti.unisi.it" + person.find("a")["href"]) as htmlPage:
                    html = htmlPage.read().decode("utf-8", "ignore")
                parsed_html = BeautifulSoup(html, "html.parser")
                if (parsed_html.find("div", {"class": "gr-contatti"}).find("a")):
                    email = parsed_html.find("div", {"class": "gr-contatti"}).find("a")["href"].replace("mailto:", "")
                    targets.write(email + "\n")

def parse_unitn():
    for page in range(1, 10):
        with urllib.request.urlopen("https://webapps.unitn.it/api/du/v1/struttura/STO0008633/membri/all?items=100&page=" + str(page)) as response:
            json_data = response.read().decode("utf-8")

        with open("unitn_targets.csv", "a") as targets:
            for person in json.loads(json_data)["data"]:
                email = person["email"]
                if(email):
                    targets.write(email + "\n")

def parse_units():
    with urllib.request.urlopen("https://dsm.units.it/it/dipartimento/persone/personale-docente") as htmlPage:
        html = htmlPage.read()

    hub_html = BeautifulSoup(html, "html.parser")

    with open("units_targets.csv", "a") as targets:
        for person in hub_html.find("table", {"class": "views-table"}).find("tbody").findAll("tr"):
            with urllib.request.urlopen("https://dsm.units.it/it/dipartimento/persone/personale-docente" + person.find("a")["href"]) as htmlPage:
                html = htmlPage.read().decode("utf-8")
            parsed_html = BeautifulSoup(html, "html.parser")
            if(parsed_html.find("div", {"class": "field-name-field-all-pers-email"})):
                email = parsed_html.find("div", {"class": "field-name-field-all-pers-email"}).find("a")["href"].replace("mailto:", "")
                targets.write(email + "\n")

# parse_unibo()
# parse_unipi()
# parse_uniroma()
# parse_unina()
# parse_unipa()
# parse_unito()
# parse_unimore()
# parse_univpm()
# parse_unisi()
# parse_unitn()
# parse_units()