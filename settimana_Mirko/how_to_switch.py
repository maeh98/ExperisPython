
def switch(lang, opzioni, risultati):
    for i in range(len(opzioni)):
        if lang == opzioni[i]:
            if risultati[i] == "break":
                break
            elif risultati[i] == "continue":
                continue
            else:
                return risultati[i]
    return None



lang = "ok"
opzioni = ["JavaScript", "PHP", "Python", "Solidity", "Java", "esci"]
risultati = ["You can become a web developer",
    "You can become a backend developer",
    "You can become a Data Scientist",
    "You can become a Blockchain developer",
    "You can become a mobile app developer",
    "break"]

while lang != "esci":
    lang = input( "inserisci elemento\n")
    print(switch(lang, opzioni, risultati))