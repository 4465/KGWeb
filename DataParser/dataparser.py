import csv

class FILEParser():
    def __init__(self):
        self.SPO = []

    def ParserCVS(self, path):

        print(path)
        with open('data/triples.csv', 'r', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                line = {}
                line['head'] = row[0]
                line['tail'] = row[1]
                line['relation'] = row[3]
                line['label'] = row[2]
                self.SPO.append(line)



