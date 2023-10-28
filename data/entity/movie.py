class Movie:
    def __init__(self,id,
                 title,year,
                 age,rating,
                 category,subcategory,
                 netflix,hulu,
                 amazon_prime,disney):
        self.__id=id
        self.__title=title
        self.__year=year
        self.__age=age
        self.__rating=rating
        self.__category=category
        self.__subcategory=subcategory
        self.__netflix=netflix
        self.__hulu=hulu
        self.__amazon_prime=amazon_prime
        self.__disney=disney

    def imprimir(self):
        print('ID: ',self.__id)
        print('Title: ',self.__title)
        print('Year: ',self.__year)
        print('Age: ',self.__age)
        print('Rating: ',self.__rating)
        print('Category: ',self.__category)
        print('Sub-Category: ',self.__subcategory)
        print('Netflix: ',self.__netflix)
        print('Hulu: ',self.__hulu)
        print('Prime Video: ',self.__amazon_prime)
        print('Disney+:',self.__disney)
        return "----------------"
    
    def getName(self):
        return self.__title
    def getYear(self):
        return self.__year
    def getAge(self):
        return self.__age
    def getRating(self):
        return self.__rating
    def getCategory(self):
        return self.__category
    def getsubCategory(self):
        return self.__subcategory
    def getnetflix(self):
        return self.__netflix
    def gethulu(self):
        return self.__hulu
    def getPrime(self):
        return self.__amazon_prime
    def getDisney(self):
        return self.__disney


            #print('ID: {0},Title: {1},Year: {2},Age: {3},Rating: {4},Category: {5},Sub-Category: {6},Netflix: {7},Hulu: {8},Prime Video: {9},Disney+: {10}'
            #      .format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))