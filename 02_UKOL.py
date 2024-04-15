
#___CAST 1
import requests
import json

ICO = input("zadej ICO: ")

res = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ICO}")
data = res.json()

with open("ukol_2.json", mode="w", encoding="utf-8") as output_file:
    json.dump(data, output_file, ensure_ascii=False, indent= 4)


print(f"{data["obchodniJmeno"]} \n{data["sidlo"]["textovaAdresa"]}")


#___CAST 2

vyhledat = input("zadej text: ")


headers = {
    "accept": "application/json",
    "Content-Type": "application/json",

}

data_dve = f'{{"obchodniJmeno": "{vyhledat}"}}'
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data_dve)


with open("ukol_2a.json", mode="w", encoding="utf-8") as file:
    json.dump(res.json(), file, ensure_ascii=False, indent= 4)


with open("ukol_2a.json", encoding="utf-8",) as file:
    vypis= json.load(file)
print(f"Nalezeno subjektů: {vypis["pocetCelkem"]}")
 
data_pop = vypis['ekonomickeSubjekty']

for item in data_pop:
    print(f'{item["obchodniJmeno"]}, {item["ico"]}')