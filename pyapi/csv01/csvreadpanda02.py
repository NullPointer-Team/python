import pandas

def main():
    my_data = [
        {'hostname': 'dumbledore', 'ip':'192.168.9.22', 'service':'objectstorage'},
        {'hostname': 'hermione', 'ip':'10.0.2.66', 'service':'httpd'}
    ]

    df = pandas.DataFrame(my_data)

    df.to_csv("inventorypandas.csv", index=False)

if __name__ == "__main__":
    main()
