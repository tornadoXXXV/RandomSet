import json
import random

# バーガー(id:1~17), サイド(id:18~28), ドリンク(id:29~73), スイーツ(id:74~90)
# json_open = open('dataset/regular.json', 'r', encoding="utf-8")
# j = json.load(json_open)

# セット用リスト
# list_set = list(range(90, 103))
# list_drink = [29,32,35,38,41,44,47,50,53,56,59,61,63,65,68,70,71,73,75,77]
# list_side = [18,20,22,23,24]

# limit_burger = 100
# limit_side = 100
# limit_drink = 1
# limit_price = 1000
# burger = 0
# side = 0
# drink = 0
# total = 0
# cal = 0

# set_number = random.choice(list_set)
# drink_number = random.choice(list_drink)
# side_number = random.choice(list_side)

# set = j[set_number]
# set_drink = j[drink_number]
# set_side = j[side_number]

# print(set["name"],set_drink["name"],set_side["name"])
# print(set["price"],j[set_number-90]["cal"]+set_drink["cal"]+set_side["cal"])

# while True:
#     choice = random.choice(j)
#     print(f'{choice["name"]}, {choice["price"]}円, {choice["cal"]}kcal')
#     total += choice["price"]
#     cal += choice["cal"]

#     j = [x for x in j if x["price"] <= 1000-total]

#     if len(j) == 0:
#         print(f'合計{total}円, {cal}kcal')
#         break

list = []
list.append([1,2,34])
print(list)
print(len(list))