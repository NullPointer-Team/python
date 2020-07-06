import pandas as pd

def main():
    cisco_csv = pd.read_csv("ciscodata.csv")
    cisco_json = pd.read_json("ciscodata2.json")

    print(cisco_csv.head())
    print(cisco_json.head())

    ciscodf = pd.concat([cisco_csv, cisco_json])

    print(ciscodf)

if __name__ == "__main__":
    main()
