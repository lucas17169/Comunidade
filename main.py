import json

with open('geo.json', 'r') as file0:
  geojson = json.load(file0);

with open('trees.json', 'r') as file1:
  treesjson = json.load(file1);

features = geojson["features"]
trees = treesjson["trees"]
featuresDic = dict()
treesDic = dict()

for item in features:
  numero = int(item["properties"]["name"]);
  featuresDic[numero] = item

for item in trees:
  numero = int(item["number"]);
  treesDic[numero] = item

for n in featuresDic:
  item = featuresDic[n]
  try:
    tree = treesDic[n]
  except:
    print("Except", n)

  if(tree and item):
    ip = item["properties"]
    ip["name"] = "Árvore"
    ip["number"] = numero
    ip["description"] = tree["name"]
    ip["DAP"] = tree["dap"]
    ip["hT"] = tree["hT"]
    ip["DPC"] = tree["DPC"]
    ip["EF"] = tree["EF"]
    ip["GE"] = tree["ge"]
    ip["origem"] = tree["origem"]
    ip["manejo"] = tree["manejo"]
    ip["compensacao"] = tree["compensacao"]
    ip["obs"] = tree["obs"]

#print(item)

#print(json.dumps(geojson))

path = 'out.txt'
days_file = open(path,'r')
days = days_file.read()

new_path = 'out.txt'
new_days = open(new_path,'w')
new_days.write(json.dumps(geojson))
days_file.close()
new_days.close()