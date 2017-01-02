

text_file=open("nazwapdf.txt.txt","r")
someString = text_file.read()
text_file.close()
#print(text_file.read() )

totalA = 0
totalB = 0
totalC = 0
totalD = 0
totalE = 0
totalF = 0
totalG = 0
totalH = 0
totalI = 0
totalJ = 0
totalK = 0
totalL = 0
totalM = 0
totalN = 0
totalO = 0
totalP = 0
totalR = 0
totalS = 0
totalG = 0
totalT = 0
totalU = 0
totalW = 0
totalY = 0
totalZ = 0

totala = 0
totalb = 0
totalc = 0
totald = 0
totale = 0
totalf = 0
totalg = 0
totalh = 0
totali = 0
totalj = 0
totalk = 0
totall = 0
totalm = 0
totaln = 0
totalo = 0
totalp = 0
totalr = 0
totals = 0
totalt = 0
totalu = 0
totalw = 0
totaly = 0
totalz = 0

letterInText = 0 
totalA = int(totalA)

for letter in someString:
        print(letter)
        letterInText += 1
        if letter.find("A")!= -1: totalA += 1
        if letter.find("B")!= -1: totalB += 1
        if letter.find("C")!= -1: totalC += 1
        if letter.find("D")!= -1: totalD += 1
        if letter.find("E")!= -1: totalE += 1
        if letter.find("F")!= -1: totalF += 1
        if letter.find("G")!= -1: totalG += 1
        if letter.find("H")!= -1: totalH += 1
        if letter.find("I")!= -1: totalI += 1
        if letter.find("J")!= -1: totalJ += 1
        if letter.find("K")!= -1: totalK += 1
        if letter.find("L")!= -1: totalL += 1
        if letter.find("M")!= -1: totalM += 1
        if letter.find("N")!= -1: totalN += 1
        if letter.find("O")!= -1: totalO += 1
        if letter.find("P")!= -1: totalP += 1
        if letter.find("R")!= -1: totalR += 1
        if letter.find("S")!= -1: totalS += 1
        if letter.find("T")!= -1: totalT += 1
        if letter.find("U")!= -1: totalU += 1
        if letter.find("W")!= -1: totalW += 1
        if letter.find("Y")!= -1: totalY += 1
        if letter.find("Z")!= -1: totalZ += 1
        if letter.find("a")!= -1: totala += 1
        if letter.find("b")!= -1: totalb += 1
        if letter.find("c")!= -1: totalc += 1
        if letter.find("d")!= -1: totald += 1
        if letter.find("e")!= -1: totale += 1
        if letter.find("f")!= -1: totalf += 1
        if letter.find("g")!= -1: totalg += 1
        if letter.find("h")!= -1: totalh += 1
        if letter.find("i")!= -1: totali += 1
        if letter.find("j")!= -1: totalj += 1
        if letter.find("k")!= -1: totalk += 1
        if letter.find("l")!= -1: totall += 1
        if letter.find("m")!= -1: totalm += 1
        if letter.find("n")!= -1: totaln += 1
        if letter.find("o")!= -1: totalo += 1
        if letter.find("p")!= -1: totalp += 1
        if letter.find("r")!= -1: totalr += 1
        if letter.find("s")!= -1: totals += 1
        if letter.find("t")!= -1: totalt += 1
        if letter.find("u")!= -1: totalu += 1
        if letter.find("w")!= -1: totalw += 1
        if letter.find("y")!= -1: totaly += 1
        if letter.find("z")!= -1: totalz += 1



print("Liter w tekscie", letterInText)
print("\nLiter A", totalA, "\nLiter B", totalB,"\nLiter C",
      totalC, "\nLiter D", totalD, "\nLiter E", totalE, "\nLiter F", totalF,
      "\nLiter G", totalG, "\nLiter H", totalH,"\nLiter I", totalI,
      "\nLiter J", totalJ,"\nLiter K", totalK, "\nLiter L", totalL,"\nLiter M",
      totalM, "\nLiter N", totalO, "\nLiter P", totalP, "\nLiter R", totalR,
      "\nLiter S", totalS, "\nLiter T", totalT,"\nLiter U", totalU,
      "\nLiter W", totalW,"\nLiter Y", totalY, "\nLiter Z", totalZ,"\nLiter a",
      totala, "\nLiter b", totalb, "\nLiter c", totalc, "\nLiter d", totald,
      "\nLiter e", totale, "\nLiter f", totalf,"\nLiter g", totalg, "\nLiter h", totalh,"\nLiter i", totali,
      "\nLiter j", totalj,"\nLiter k", totalk, "\nLiter l", totall,"\nLiter m",
      totalm, "\nLiter n", totalo, "\nLiter p", totalp, "\nLiter r", totalr,
      "\nLiter s", totals, "\nLiter t", totalt,"\nLiter u", totalu,
      "\nLiter w", totalw,"\nLiter y", totaly, "\nLiter z", totalz,)
input("Wcisnij enter")
