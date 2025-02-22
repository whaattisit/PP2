import json
import os

with open(r"lab4\json\sample-data.json", 'r') as file:
    data = json.load(file)

interfaces = data["imdata"]

print("Interface status")
print("=" * 80)
print("DN".ljust(40), "Description".ljust(20), "Speed".ljust(10), "MTU")
print("-" * 40, "-" * 20, "-" * 7, "-" * 10)

for index, item in enumerate(data["imdata"]):
    if index >= 3:  # Ограничиваем количество строк
        break
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    description = attributes.get("descr", "")
    speed = attributes.get("speed", "inherit")
    mtu = attributes["mtu"]
    print(dn.ljust(40), description.ljust(18), speed.ljust(10), mtu)
