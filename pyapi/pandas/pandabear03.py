import pandas as pd

def main():
    cisco_csv = pd.read_csv("ciscodata.csv")
    cisco_json = pd.read_json("ciscodata2.json")

    ciscodf = pd.concat([cisco_csv, cisco_json], ignore_index=True, sort=False)

    print(ciscodf)
    print()

    ciscodf.to_json("combined_ciscodata.json")
    ciscodf.to_csv("combined_ciscodata.csv")
    ciscodf.to_excel("combined_ciscodata.xls")

    x = ciscodf.to_dict()
    print(x)

if __name__ == "__main__":
    main()
