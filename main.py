from Database.DB import DB
from DataParser.dataparser import FILEParser
import rdflib

if __name__ =="__main__":
    '''
    实现建立数据库：tripleskg
    内有一张表：main
        字段：subject:char(30) predicate:char(30) object:char(30)
    '''
    # db = DB()
    # file = FILEParser()
    # # file.ParserCVS('data/triples.csv')
    # # db.Insert('main',file.SPO)
    # db.SelectAll()
    g = rdflib.Graph()
    result = g.parse("data\medline09n3-breastcancer\medline09n0034\medline09n0034.xml.1.nt", format= "n3")
    with open('nt.txt', 'w', encoding='utf-8') as file:
        for subject, predicate, object in g:
            file.write(subject + ' ' + predicate + ' ' + object)
            file.write('\n')




