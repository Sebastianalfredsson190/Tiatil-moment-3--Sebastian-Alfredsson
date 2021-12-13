#Här ställer jag bara frågan hur mycket lön man har och gör det till en varibel med namnet "LÖN"
lön = int(input("Hur många kr tjänar du varje månad?"))
kommunalskatt=lön*0.2136
landstingsskatt=lön*0.1148
lönefterskatt=lön-kommunalskatt-landstingsskatt
årslön = lön*12

#från rad 2-7 gör jag bara simpla berkäningar som är beroende på lönen som användaren väljer

#Här gör jag en if sats som säger att om årslönen är mindre än 19247kr så är all skatt = 0 eftersom man betalar inte skatt om årslönen är soppas liten.
#Och så uppdaterar jag även varibeln lönefterskatt eftersom att innan var skatten på 21% och 11% och och då berkänade man bort skatten från lönen för att få lön efterskatt.
#men eftersom den nu ligger på 0% så måste jag göra beräkningen igen. 
if årslön < 19247:
    kommunalskatt=0
    landstingsskatt=0
    lönefterskatt=lön-kommunalskatt-landstingsskatt
    
#I denna if måste båda vilkorer vara sanna eftersom jag använder en "and" sats
#Här uppdaterar jag varibalen lön efterskatt igen eftersom att if satsen lägger till en statetax som jag måste räkna in i den totala skatten
if årslön > 468700 and årslön < 675700:
    statligskatt=lön*0.2
    lönefterskatt=lön-statligskatt-landstingsskatt-kommunalskatt
    print(f"Du betalar: {round(statligskatt)}kr i statligskatt")
#Samma sak här uppdaterar jag variabeln lönefterskatter eftersom nu blir statetax 0.25 istället för 0.2
if årslön > 675700:
    statligskatt=lön*0.25
    lönefterskatt=lön-statligskatt-landstingsskatt-kommunalskatt
    print(f"Du betalar: {round(statligskatt)}kr i statligskatt")
    
#Anledningen till jag göra dessberäkningar efter ifsatsen är att skatten är annorlunda beroende på var årslönen är.
totalskatt=statligskatt+kommunalskatt+landstingsskatt
bruttolön1=totalskatt/lön
bruttolön2=bruttolön1*100

print(f"Din lön: {round(lön)}kr")
print(f"Din kommunalaskatt ligger på: {round(kommunalskatt)}kr")
print(f"Din landstingsskatt ligger på: {round(landstingsskatt)}kr")
print(f"Din totalt betala skatt ligger på: {round(totalskatt)}kr")
print(f"Andel betald skatt: {round(bruttolön2,2)}%")
print(f"Din lön efter skatt: {round(lönefterskatt)}kr")
