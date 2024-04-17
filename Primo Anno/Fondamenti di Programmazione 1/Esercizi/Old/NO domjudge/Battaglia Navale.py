from random import randint
import os

def clear(): os.system('cls')

DIM_GRIGLIA = 10
MAX_NAVI = 9

NAVI =    [
            (1, "Sommergibile"),
            (2, "Vedette"),
            (3, "Incrociatori"),
            (4, "PortaAerei"),
            (0, "")
           ]
            
A, B = [[0 for i in range(DIM_GRIGLIA)] for i in range(DIM_GRIGLIA)], [[0 for i in range(DIM_GRIGLIA)] for i in range(DIM_GRIGLIA)]
A_attacco, B_attacco = [[0 for i in range(DIM_GRIGLIA)] for i in range(DIM_GRIGLIA)], [[0 for i in range(DIM_GRIGLIA)] for i in range(DIM_GRIGLIA)]

NaviA_rimanenti = int(MAX_NAVI)
NaviB_rimanenti = int(MAX_NAVI)

N_NAV_SEL = [4,3,2,1]

barca = chr(12)

def printMappa(griglia, grigliaAttacco) -> None:
    for y in range(DIM_GRIGLIA):
        for x in range(DIM_GRIGLIA):
            _chr = barca + " " if griglia[y][x] >= 1 else "~ " if griglia[y][x] == 0 else  "O "
            print(_chr,end="")

        if grigliaAttacco != None:
            print("\t\t",end="")
            for x in range(DIM_GRIGLIA):
                _chr = "X " if grigliaAttacco[y][x] < 0 else "~ " if grigliaAttacco[y][x] == 0 else  "O "
                print(_chr,end="")
                
        print()

def ControlloPosizioneNave(tipo,pos,vert,grid) -> bool:
    _min = pos[vert]
    _max = pos[vert] + NAVI[tipo][0]

    if _max > DIM_GRIGLIA:
        #print("fuori mappa")
        return False
    
    for p in range(_min,_max-1):
        x, y = (pos[0], p) if vert else (p,pos[1])

        if grid[y][x] == 1:
            return False
        
        if (x < DIM_GRIGLIA-1) and grid[y][x + 1] == 1 and vert:
            return False
        
        if (x > 0) and grid[y][x - 1] == 1 and vert:
            return False
        

        if (y < DIM_GRIGLIA-1) and grid[y + 1][x] == 1 and not vert:
            return False

        if (y > 0) and grid[y - 1][x] == 1 and not vert:
            return False
        
        
    if _max < DIM_GRIGLIA-1:
        x, y = (pos[0], _max + 1) if vert else (_max + 1,pos[1])                               
        if grid[y][x] == 1:
            return False

    if _min > 0:
        x, y = (pos[0], _min - 1) if vert else (_min - 1,pos[1])
        if grid[y][x] == 1:
            return False
        

    return True

def controllaAffondata(x,y,griglia) -> bool:
    
    def _controlla(x,y,griglia,_dir,found):
        
        if _dir == 0:
            if (x+1) >= DIM_GRIGLIA:
                return found
            
            if griglia[y][x+1] == 1:
                return False
            elif griglia[y][x+1] == 0:
               return _controlla(x,y,griglia,_dir+1,False)
            elif griglia[y][x+1] == -1:
                return _controlla(x+1,y,griglia,_dir,True)

        elif _dir == 1:

            if (x-1) < 0:
                return found
            
            if griglia[y][x-1] == 1:
                return False
            elif griglia[y][x-1] == 0:
                return _controlla(x,y,griglia,_dir+1,False)
            elif griglia[y][x-1] == -1:
                return _controlla(x-1,y,griglia,_dir,True)
            
        elif _dir == 2:

            if (y+1) >= DIM_GRIGLIA:
                return found
            
            if griglia[y+1][x] == 1:
                return False
            elif griglia[y+1][x] == 0:
                return _controlla(x,y,griglia,_dir+1,False)
            elif griglia[y+1][x] == -1:
                return _controlla(x,y + 1,griglia,_dir,True)
            
        elif _dir == 3:
            
            if (y - 1) < 0:
                return found
            
            if griglia[y - 1][x] == 1:
                return False
            elif griglia[y - 1][x] == 0:
                return _controlla(x,y,griglia,_dir+1,False)
            elif griglia[y - 1][x] == -1:
                return _controlla(x,y - 1,griglia,_dir,True)
            
        if _dir > 3: return True

        return _controlla(x,y,griglia,_dir+1,False)

    
    return _controlla(x,y,griglia,0,False)

def Attaca(pos,grigliaAttacco,grigliaAvv,Nnavi):
    
    X,Y = int(pos[0]), int(pos[1])          

    grigliaAttacco[Y][X] = 1

    if grigliaAvv[Y][X] >= 1:
        print("Nave Avversaria colpita",end="")
        
        if controllaAffondata(X,Y,grigliaAvv):
            print(" e affondata")
            Nnavi -= 1
        else:
            print()
            
        grigliaAttacco[Y][X] = -1
        grigliaAvv[Y][X] = -1

    return grigliaAttacco, grigliaAvv, Nnavi


def ControllaPosizioneAttacco(pos,grigliaAtt):
    X,Y = int(pos[0]), int(pos[1])
    
    if grigliaAtt[Y][X] < 0:
        print("Hai già attaccato in questa posizione")
            
        buona = False
        
        while not buona:
            pos = input("Inserisci posizione: ").split(",")
            X,Y = int(pos[0]), int(pos[1])

            if grigliaAtt[Y][X] >= 0:
                buona = True
    return (X,Y)


    
LastMovB1 = [-1, -1]
LastMovB2 = [-1, -1]

found = False
lastDir = 0
DirAttack = -1

def ControllaPosAttaccoBot(pos,grigliaAtt):
    X, Y = pos
    if grigliaAtt[Y][X] < 0:
       
        buona = False
        
        while not buona:
            X,Y = (randint(0,9),randint(0,9))

            if grigliaAtt[Y][X] >= 0:
                buona = True
        
    return (X,Y)


def BOT_ATTAK(grigliaAttacco,grigliaAvv,Nnavi):
    X,Y = ControllaPosAttaccoBot((randint(0,9),randint(0,9)),grigliaAttacco)

    if grigliaAvv[Y][X] >= 1:
        LastMovB1 = (X,Y)

        if not found:
            found = True
            lastDir = 0
            DirAttack = 0
        else:
            if DirAttack == -1:
                lastDir = randint(0,3)
            else:
                if DirAttack == 0:
                    
                
            
            if lastDir == 0:
                 if grigliaAvv[Y][X] >= 1:
                     DirAttack = 0
                     
                
            

    
        
                
        
        
            
    

def distribuisciNavi(griglia, autoBuild = True) -> None:
    countNaveRim = N_NAV_SEL.copy()
    
    for i in range(MAX_NAVI):
        X, Y = -1, -1
        
        tipo = -1
        
        while True:                
            tipo = -1

            if autoBuild:
              tipo = randint(0,3)
            else:
                
              for i in range(len(NAVI)-1):
                print(str(countNaveRim[i]) + "x", NAVI[i][1])
                
              tipo = int(input("Seleziona nave: "))
            
            if tipo >= len(NAVI)-1 or tipo < 0:
                continue
            
            if countNaveRim[tipo] <= 0:
                continue
            
            countNaveRim[tipo] = countNaveRim[tipo]-1
            break
            

        posValida = False
        
        while (X >= DIM_GRIGLIA or X < 0) and (Y >= DIM_GRIGLIA or Y < 0) or not posValida:
            verticale = -1
            POS = ""
    
            if autoBuild:
                verticale = randint(0,1)
                POS = (randint(0,9),randint(0,9))
            else:
                verticale = int(input("0: Orizzontale\n1: Verticale\n"))
                POS = input("Inserisci posizione: ").split(",")

            X, Y = int(POS[0]), int(POS[1])

            posValida = ControlloPosizioneNave(tipo,(X,Y),verticale,griglia)

            if not posValida:
                if not autoBuild:
                    print("Posizione non Valida")
                continue

            if verticale:
                for y in range(Y, Y + NAVI[tipo][0]):
                    griglia[y][X] = 1
            else:
                for x in range(X, X + NAVI[tipo][0]):
                    griglia[Y][x] = 1

        if not autoBuild:
            printMappa(griglia,None)
        

distribuisciNavi(A)
distribuisciNavi(B)

ISbot1 = True
ISbot2 = True

print("___________________")
printMappa(A,None)
print("___________________")
printMappa(B,None)
print("___________________")

input("Inizia partita")

turno = randint(0,1)

while True:

   POS = ""

   bot = (ISbot1 and turno) or (ISbot2 and not turno)

   print("Turno " + ("A" if turno else "B"))
   
   if not bot:
    POS = input("Inserisci posizione: ").split(",")
     

   print("___________________")

   if bot:
       A_attacco, B, NaviB_rimanenti = BOT_ATTAK(A_attacco,B,NaviB_rimanenti)
       printMappa(A,A_attacco)
   else:
       B_attacco, A, NaviA_rimanenti = Attaca(ControllaPosizioneAttacco(POS,B_attacco,bot),B_attacco,A,NaviA_rimanenti)
       printMappa(B,B_attacco)

   print("___________________")
       

   if NaviA_rimanenti <= 0:
      print("B vince")
      break
   elif NaviB_rimanenti <= 0:
      print("A vince")
      break

   turno = not turno




