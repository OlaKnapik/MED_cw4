import math
import numpy


users = {
        "Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }



def pearson(osoba1,osoba2):

    kl1=[]
    kl2=[]
    w1=0
    w2=0
    klucze1=osoba1.keys()
    klucze2=osoba2.keys()

    for klucz in klucze1:
        if klucz in klucze2:
            kl1.append(osoba1[klucz])
            kl2.append(osoba2[klucz])

    sr1=sum(kl1)/len(kl1)
    sr2=sum(kl2)/len(kl2)

    iloczyn=[kl1[i]*kl2[i] for i in range(0,len(kl1))]
    sr_iloczyn=sum(iloczyn)/len(iloczyn)

    kow=sr_iloczyn-sr1*sr2
    
    for i in kl1:
        w1+=(i-sr1)**2
    for i in kl2:
        w2+=(i-sr2)**2
        
    w1=w1/len(kl1)
    w2=w2/len(kl2) 
    
    sig1=math.sqrt(w1)
    sig2=math.sqrt(w2)
    
    r1=kow/(sig1*sig2)
    
    return r1

def pearson_numpy(osoba1,osoba2):

    kl1=[]
    kl2=[]

    klucze1=osoba1.keys()
    klucze2=osoba2.keys()

    for klucz in klucze1:
        if klucz in klucze2:
            kl1.append(osoba1[klucz])
            kl2.append(osoba2[klucz])

    r2=numpy.corrcoef(kl1,kl2)
    
    return r2[0,1]


def manhattan(rating1, rating2):
    
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in klucze2:
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1


print pearson(users["Ania"], users["Bonia"])
print pearson_numpy(users["Ania"], users["Bonia"])
print manhattan(users["Ania"], users["Bonia"])
