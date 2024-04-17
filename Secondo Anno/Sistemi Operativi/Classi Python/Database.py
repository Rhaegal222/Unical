class Database:
    def __init__(self):
        self._database = []
    
    def addPerson(self, person):
        self._database.append(person)

    def removePerson(self, person):
        check = False
        print('Stai per eliminare un elemento dal database')

        for i in self._database:
            if i.getData() == person.getData():
                self._database.remove(i)
                check = True
                break
        
        print('Modifica applicata con successo' if check else 'Record non trovato')
            
    def printDatabase(self):
        for i in self._database:
            print(i.getData())

class Person():
    
    def __init__(self):
        pass
    
    def setName(self, name):
        self.name = name
    
    def setSurname(self, surname):
        self.surname = surname
    
    def setAge(self, age):
        self.age = age
    
    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname
    
    def getAge(self):
        return self.age

    def getData(self):
        return (self.name, self.surname, self.age)

def insert():
    person = Person()
    person.setName(input('Inserisci il nome: '))
    person.setSurname(input('Inserisci il cognome: '))
    person.setAge(input("Inserisci l'etá: "))
    return person

def main():
    database = Database()
    database.addPerson(insert())
    database.addPerson(insert())
    database.removePerson(insert())
    database.printDatabase()

main()

"""
Francesco
Vecchio
21
Domenico
Vecchio
19
"""