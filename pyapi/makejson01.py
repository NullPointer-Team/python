import json

def main():
  hitchhikers = [{"name":"Zaphod Beeblebrox", "species": "Betelgeusian"}, {"name":"Arthur Dent", "species":"human"}]

  print(hitchhikers)

  with open("galaxyguide.json", "w") as outfile:

    json.dump(hitchhikers, outfile)

if __name__ == "__main__":
  main()
