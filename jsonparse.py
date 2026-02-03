import requests
import json
import matplotlib.pyplot as plt

database = []
base_url = 'https://pokeapi.co/api/v2/'
limit = 10
url = f'{base_url}pokemon?limit={limit}'
data = eval(str(json.loads(requests.get(url).content)))
data = data.get("results")
for i in data:
    d = {}
    context = eval(str(json.loads(requests.get(i.get("url")).content)))
    d['id'] = (context.get("id"))
    d['name'] = (context.get("name"))
    d['height'] = (context.get("height"))
    d['weight'] = (context.get("weight"))
    context = context.get("stats")
    
    for x in context:
        if x.get("stat").get("name") == "hp":
            d['hp'] = (x.get("base_stat"))
        if x.get("stat").get("name") == "attack":
            d['attack'] = (x.get("base_stat"))
        if x.get("stat").get("name") == "defense":
            d['defense'] = (x.get("base_stat"))
        if x.get("stat").get("name") == "speed":
            d['speed'] = (x.get("base_stat"))
    database.append(d)
print(database)

names = [i['name'] for i in database]
hps = [i['hp'] for i in database]
attacks = [i['attack'] for i in database]
defenses = [i['defense'] for i in database]
weights = [i['weight'] for i in database]
heights = [i['height'] for i in database]
speeds = [i['speed'] for i in database]



plt.figure()
plt.plot(names, hps, marker='o')
plt.title('HP покемонов')
plt.xlabel('Pokemon')
plt.ylabel('HP')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. Точечная диаграмма с подписями (Атака vs Защита)
plt.figure()
plt.scatter(attacks, defenses)

for i, name in enumerate(names):
    plt.text(attacks[i], defenses[i], name, fontsize=8, ha='right')

plt.title('Атака vs Защита')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.tight_layout()
plt.show()



plt.figure()
plt.bar(names, weights)
plt.title('Вес покемонов')
plt.xlabel('Pokemon')
plt.ylabel('Weight')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure()
plt.barh(names, heights)
plt.title('Рост покемонов')
plt.xlabel('Height')
plt.ylabel('Pokemon')
plt.show()


plt.figure()
plt.hist(speeds, bins=len(speeds))
plt.title('Гистограмма скорости покемонов')
plt.xlabel('Speed')
plt.ylabel('Количество покемонов')
plt.show()



plt.figure()
plt.pie(hps, labels=names, autopct='%1.1f%%')
plt.title('Доля HP')
plt.show()
