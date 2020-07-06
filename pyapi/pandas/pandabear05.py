import pandas as pd

def main():
    flight_csv = pd.read_csv("airline_flights.csv")

    flight_csv_tofrom = flight_csv.groupby(['ORG_AIR', 'DEST_AIR']).size()
    print(flight_csv_tofrom.head())

    print("\nFlight frmo ATL to IAH and IAH to ATL")
    print(flight_csv_tofrom.loc[[("ATL", "IAH"), ("IAH", "ATL")]])

    print(flight_csv_tofrom.head())

if __name__ == "__main__":
    main()
