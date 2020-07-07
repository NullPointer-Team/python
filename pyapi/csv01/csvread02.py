import csv

def main():
    line_count = 0
    with open('superbirthday.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            if line_count == 0:

                print('Column names are {}'.format(", ".join(row)))
                line_count +=1

            print('\t{} aka {} was born in {}.'.format(row["name"], row["heroname"], row["birthday month"]))
            line_count +=1

    print('Processed {} lines.'.format(line_count))

if __name__ == "__main__":
    main()
