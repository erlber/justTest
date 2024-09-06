# funksjon for å legge til leietaker
# funksjon for legg til bøker
# funksjon for boksøk
# funksjon for søk opp leietaker
# funksjon for lei ei bok
# funksjon for levere inn bok
# funksjon for tilgjengelige bøker
# funksjon for Se alle utleide bøker
# funksjon for å se alle bøker
# 
# Trenger en meny
def menu():
    pass
# hovedprogram
def main():
    pass


    
   



















users = []

def addUser():
    newUser = {}
    newUser["firstName"] = input("fornavn: ")
    newUser["lastName"] = input("etternavn: ")
    newUser["age"] = input("alder: ")
    newUser["address"] = input("adresse: ")
    users.append(newUser)
    print(newUser["firstName"] + " Er lagt til i brukere")


def menu():
    print("-----------hovedmeny------------")
    print("--------------------------------")
    print("1. for å legge til bruker")
    print("2. for å se alle brukere")
    print("0. avslutt")
    valg = input("velg ett nummer fra listen: ")
    return valg

def main():
    run = True
    while run:
        mittValg = menu()
        if(mittValg == "1"):
            addUser()
        elif(mittValg == "2"):
            print(users)
        elif(mittValg == 0):
            run = False
