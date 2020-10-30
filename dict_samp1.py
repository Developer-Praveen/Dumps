thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)

print(thisdict["model"])

print(thisdict.get("model"))

print(thisdict["model"] + " car")

x = 2020 - thisdict.get("year")

print(x, " Years!!!")

thisdict["year"] = 1961

x = 2020 - thisdict.get("year")

print(x, " Years!!!")

for i in thisdict:
    print (i, "-", thisdict[i])