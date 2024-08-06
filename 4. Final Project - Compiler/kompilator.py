# Jarosław Socha
# polecenia maszyny wirtualnej

label = -1

def genLabel():
    """
    set, call
    """
    global label
    label += 1
    
    return "{"+str(label)+"}", "<"+str(label)+">"

def size(fun):
    return fun.__getattribute__("size")


# Rejestry
class r:
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"

class c:
    def read():
        """    r_a <-- input    """
        return "READ" + '\n'

    def write():
        """    r_a --> output    """
        return "WRITE" + '\n'

    def load(x):
        """    r_a <-- p[r_x]    """
        return "LOAD " + str(x) + '\n'

    def store(x):
        """    r_a --> p[r_x]    """
        return "STORE " + str(x) + '\n'

    def add(x):
        """    r_a <-- r_a + r_x    """
        return "ADD " + str(x) + '\n'

    def sub(x):
        """    r_a <-- max(r_a - r_x, 0)    """
        return "SUB " + str(x) + '\n'

    def get(x):
        """    r_a <-- r_x    """
        return "GET " + str(x) + '\n'

    def put(x):
        """    r_a --> r_x    """
        return "PUT " + str(x) + '\n'

    def rst(x):    
        """    r_x <-- 0    """
        return "RST " + str(x) + '\n'

    def inc(x):    
        """    r_x <-- r_x + 1    """
        return "INC " + str(x) + '\n'

    def dec(x):    
        """    r_x <-- max(r_x - 1, 0)    """
        return "DEC " + str(x) + '\n'

    def shl(x):    
        """    r_x <-- 2 * r_x    """
        return "SHL " + str(x) + '\n'

    def shr(x):    
        """    r_x <-- r_x // 2    """
        return "SHR " + str(x) + '\n'


    def jump(j):    
        """    k <-- j   """
        return "JUMP " + str(j) + '\n'


    def jpos(j):    
        """    
        if r_a > 0:
            k <-- j   
        """
        return "JPOS " + str(j) + '\n'


    def jzero(j):    
        """    
        if r_a == 0:
            k <-- j   
        """
        return "JZERO " + str(j) + '\n'

    def halt():    
        """    
        koniec programu
        """
        return "HALT "


# def get(x):
#     return "GET " + str(x) + '\n'
# def get(x):
#     return "GET " + str(x) + '\n'
# def get(x):
#     return "GET " + str(x) + '\n'
# def get(x):
#     return "GET " + str(x) + '\n'

def rep(S:str):
    return S

def read():
    """    r_a <-- input    """
    return rep("READ" + '\n')

def write():
    """    r_a --> output    """
    return rep("WRITE" + '\n')

def load(x):
    """    r_a <-- p[r_x]    """
    return rep("LOAD " + str(x) + '\n')

def store(x):
    """    r_a --> p[r_x]    """
    return rep("STORE " + str(x) + '\n')

def add(x):
    """    r_a <-- r_a + r_x    """
    return rep("ADD " + str(x) + '\n')

def sub(x):
    """    r_a <-- max(r_a - r_x, 0)    """
    return rep("SUB " + str(x) + '\n')

def get(x):
    """    r_a <-- r_x    """
    return rep("GET " + str(x) + '\n')

def put(x):
    """    r_a --> r_x    """
    return rep("PUT " + str(x) + '\n')

def rst(x):    
    """    r_x <-- 0    """
    return rep("RST " + str(x) + '\n')

def inc(x):    
    """    r_x <-- r_x + 1    """
    return rep("INC " + str(x) + '\n')

def dec(x):    
    """    r_x <-- max(r_x - 1, 0)    """
    return rep("DEC " + str(x) + '\n')

def shl(x):    
    """    r_x <-- 2 * r_x    """
    return rep("SHL " + str(x) + '\n')

def shr(x):    
    """    r_x <-- r_x // 2    """
    return rep("SHR " + str(x) + '\n')


def jump(j):    
    """    k <-- j   """
    return rep("JUMP " + str(j) + '\n')


def jpos(j):    
    """    
    if r_a > 0:
        k <-- j   
    """
    return rep("JPOS " + str(j) + '\n')


def jzero(j):    
    """    
    if r_a == 0:
        k <-- j   
    """
    return rep("JZERO " + str(j) + '\n')

def strk(x):    
    """    
    r_x <-- k   
    """
    return rep("STRK " + str(x) + '\n')

def jumpr(x):    
    """    
    k <-- r_x  
    """
    return rep("JUMPR " + str(x) + '\n')

def halt():    
    """    
    koniec programu
    """
    return rep("HALT ")




def const(n,x):
    """
    n - stała
    x - rejestr w którym ma się znaleźć
    """
    # return x+" <-- "+str(n)+'\n'
    com = []
    com.append(rst(x))
    # print("CNST",n)
    if n==0:
        return ''.join(com)
    stack = []
    while n != 1:
        stack.append(n%2)
        n //= 2
    # stack.append(1)
    com.append(inc(x))
    
    stack.reverse()
    for el in stack:
        com.append(shl(x))
        if el == 1:
            com.append(inc(x))
    
    return ''.join(com)
        
def swap(d,e,f):
    """
    swap d <--> e przy użyciu f
    """
    
    return ''.join([
        get(e), put(f),
        get(d), put(e),
        get(f), put(d)
    ])

def divisibleBy2(d,f, whereToJump):
    """
    if 2|d jump <whereToJump>
    f to temp
    """
    return ''.join([
        get(d),
        shr(r.a), shl(r.a),
        put(f), get(d),
        sub(f),
        jzero(whereToJump)
    ])
    


def multConstant(n,x):
    com = [rst(r.a)]
    if n==0:
        return ''.join(com)
    
    stack = []
    while n != 1:
        stack.append(n%2)
        n //= 2
    stack.append(1)
    
    # stack.reverse()
    
    for el in stack:
        if el == 1:
            com.append(add(x))
        com.append(shl(x))
    return ''.join(com)

def mult(x,y,f,b):
    """
    potrzebuje 4 rejestrów!
    x, y - rejestry w których są mnożone liczby
    [wynik w r_a]
    """
    d = x
    e = y
    a = r.a

    set_1, call_1 = genLabel()
    set_2, call_2 = genLabel()
    set_3, call_3 = genLabel()
    set_4, call_4 = genLabel()
    set_5, call_5 = genLabel()
    set_end, call_end = genLabel()
    res = [
        get(y),
        sub(d), # == 0 -> d > e - dobrze
    ]
    res.extend([
        rst(f),
        jzero(call_4),
            swap(d,e,f)
    ])
    res.extend([
        set_4, rst(f),
        get(e), jzero(call_end), # * 0
        dec(a), jzero(call_5) # * 1

    ])
    # w r_d jest lewy, w r_e jest prawy
    # stare:
    # res.extend([
    # set_1, divisibleBy2(r.d,r.f,call_2),
    #     shl(r.d), shr(r.e),
    #     jump(call_1)
    # ])
    # debug: -----------
    res.extend([
    set_1 , #printRegisters(),
    divisibleBy2(e,b,call_2),
        # rst(b),
        get(d),
        add(f), put(f),
        shl(d), shr(e),
        # add(d), put(r.d),
        jump(call_3)
    ])
    # ------------------

    res.extend([
    set_2, 
        shl(d), shr(e)
    ])
    res.extend([
    set_3, get(e), dec(a),
        jpos(call_1),
        get(d), add(f), put(d),
    set_5, get(d),
    set_end,
    ])
    
    return ''.join(res)

def div(x,y,f,b,c):
    """
    WSZYSTKIE 5 REJESTRÓW
    x, y - rejestry w których są dzielone liczby
    [wynik w r_a]
    """
    s_end, c_end = genLabel()
    s1, c1 = genLabel()
    s2, c2 = genLabel()
    # s3, c3 = genLabel()
    sloop, cloop = genLabel()
    scond, ccond = genLabel()

    d = x
    e = y
    a = r.a

    res = [
        get(y), jzero(c_end), put(b), # x / 0 = 0
        rst(f),
        sub(d), jpos(c_end) # e > d
    ]

    

    # inkrementacja e poza d
    res.extend([
        inc(f),
    s1, shl(e), shl(f),
        get(e), sub(d), jzero(c1),
        shr(e), shr(f)#,printRegisters()
    ])

    res.extend([
        get(f), put(c), # c := f
        get(d), sub(e), put(d), # d = d-e
    scond, get(d), sub(b), jzero(c2),
    sloop, shr(c), shr(e),
        get(e), sub(d), jpos(cloop), # if e-d > 0
        get(f),add(c),put(f), # f = f+c
        get(d),sub(e),put(d), # d = d - e
        jump(ccond),
    s2, get(b),sub(d),jpos(c_end),
        inc(f),
    ])


    res.extend([
        s_end, get(f)
    ])

    return ''.join(res)

def mod(x,y,b):
    """
    3 rejestry
    x, y - rejestry w których są dzielone liczby
    [wynik w r_a]
    """
    s_end, c_end = genLabel()
    s1, c1 = genLabel()
    s2, c2 = genLabel()
    # s3, c3 = genLabel()
    sloop, cloop = genLabel()
    scond, ccond = genLabel()
    s0, c0 = genLabel()

    d = x
    e = y
    a = r.a

    res = [
        get(y), jpos(c0),
        rst(d),
        jump(c_end),        
    s0, put(b), # x / 0 = 0
        # rst(f),
        sub(d), jpos(c_end) # e > d
    ]

    

    # inkrementacja e poza d
    res.extend([
        # inc(f),
    s1, shl(e), #shl(f),
        get(e), sub(d), jzero(c1),
        shr(e) #, shr(r.f),printRegisters()
    ])

    res.extend([
        #get(r.f), put(r.c), # c := f
        get(d), sub(e), put(d), # d = d-e
    scond, get(d), sub(b), jzero(c2),
    sloop, shr(e),
        get(e), sub(d), jpos(cloop), # if e-d > 0
        #get(r.f),add(r.c),put(r.f), # f = f+c
        get(d),sub(e),put(d), # d = d - e
        jump(ccond),
    s2, get(b),sub(d),jpos(c_end),
        rst(d)
        #inc(r.f),
    ])


    res.extend([
        s_end, get(d) #get(r.f)
    ])

    return ''.join(res)

def transfer(x,y):
    """
    x -> y (przez a)
    """
    return ''.join([
        get(x),put(y)
    ])





def relabel(prog):
    # global label
    # label = vmc.label
    # global label
    # print("FUNS LABEL: ",label)
    # prog = [line + '\n' for line in program.split("\n")]
    # print(prog)
    lineIndeces = []
    for lab in range(label+1):
        for line in range(len(prog)):
            if "{"+str(lab)+"}" in prog[line]:
                lineIndeces.append(line)
                prog[line] = prog[line].replace("{"+str(lab)+"}","")
                break
    # print(prog)
    for lab in range(label+1):
        for line in range(len(prog)):
            if "<"+str(lab)+">" in prog[line]:
                # print(lab,label)
                prog[line] = prog[line].replace("<"+str(lab)+">",str(lineIndeces[lab]))
    
    return ''.join(prog)




















from sly import Lexer, Parser

from sys import argv

# POSTPROCESSING 1 --------------------------------------------
def const_store_alias(id,freeRegister):
    return "$ "+str(id)+" "+freeRegister + "\n"

def delete_const_store_alias(id, prog):
    i = 0
    while i < len(prog):
        if "$ "+str(id)+" " in prog[i]:
            ''
            prog[i] = prog[i].replace(prog[i][prog[i].find('$'):],'')

        i += 1
    return prog

def replace_const_store_alias(id, prog):
    i = 0
    while i < len(prog):
        if "$ "+str(id)+" " in prog[i]:
            line = prog[i].split(" ")
            freeRegister = line[2]
            prog[i] = prog[i].replace(prog[i][prog[i].find('$'):],const(id,freeRegister) + store(freeRegister))

        i += 1
    return prog


def postProcess(program, memoryManager):
    prog = [line + '\n' for line in program.split("\n")]
    for i in range(len(memoryManager.memoryStates)):
        cell = memoryManager.memoryStates[i]
        timesLoaded = NDM.memoryStatesLoads[i]
        if cell["isDeclared"] == True and timesLoaded == 0:
            prog = delete_const_store_alias(i,prog)
        else:
            prog = replace_const_store_alias(i,prog)
    p = ''.join(prog)

    # usuwanie getputów
    for reg in NDM.registerList:
        prevlen = len(p)+1
        while prevlen != len(p):
            prevlen = len(p)
            p.replace(put(reg)+get(reg),put(reg))
            p.replace(get(reg)+put(reg),get(reg))

    prog = []
    for line in p.split("\n"):
        if line !='':
            prog.append(line + '\n')
    
            

    return relabel(prog)
            


# -------------------------------------------------------------

class NonDeterministicMemory:
    memoryStatesLoads = []
    time = 0
    registerList = [
        r.b,
        r.c,
        r.d,
        r.e,
        r.f
    ]
    registerVariable = { 
        r.b: ('','',0),
        r.c: ('','',0),
        r.d: ('','',0),
        r.e: ('','',0),
        r.f: ('','',0),
    }
    accessAsignTime = {
        r.b: -1,
        r.c: -1,
        r.d: -1,
        r.e: -1,
        r.f: -1,
    }
    def resetAllRegs(self):
        for reg in self.registerList:
            self.resetReg(reg)

    def updateReg(self,r, procedureName, variableName, index = 0):
        self.registerVariable[r] = (procedureName,variableName,index)
        
        self.accessAsignTime[r] = self.time
        self.time += 1

    def resetReg(self,r):
        self.accessAsignTime[r] = min([self.accessAsignTime[i] for i in self.accessAsignTime]) - 1
        self.registerVariable[r] = ("","",0)
        

    def getFreeRegs(self, n, exceptions=[]):
        order = [(self.accessAsignTime[reg],reg) for reg in self.accessAsignTime]
        res = sorted(order)
        res = [reg for (time,reg) in res]
        result = []
        i=0
        while len(result) < n:
            if res[i] not in exceptions:
                result.append(res[i])
            i+=1
        return result


    
NDM = NonDeterministicMemory() 


class MemoryManager:
    memoryAddress = 0
    memoryStates = [] # stany komórek pamięci
    NameToAddressMap = { } 

    argNumber = { } # ile argumentów ma procedura


    procedureCallAliases = { }
    procedureOrder = []


    newestProcedure = ""
    
    

    def createProcedure(self,procedureName,head,declarations):
        
        self.procedureOrder.append(procedureName)
        self.newestProcedure = procedureName
        if procedureName in self.NameToAddressMap:
            return {"res":False, "error": "Powtórzenie nazwy procedury "+procedureName}
        self.NameToAddressMap[procedureName] = { }

        # gdzie przetrzymywany jest powrót
        self.NameToAddressMap[procedureName]["$Callback"] = self.memoryAddress
        self.memoryAddress += 1
        self.memoryStates.append({"isDeclared":False})
        NDM.memoryStatesLoads.append(0)
        
        self.argNumber[procedureName] = 0
        for variableName, isArray in head:
            #Error
            if variableName in self.NameToAddressMap[procedureName]:
                return {"res":False, "error": "Powtórzenie nazwy zmiennej "+variableName+" "}
            self.NameToAddressMap[procedureName][variableName] = { }
            self.NameToAddressMap[procedureName][variableName]["Address"] = self.memoryAddress
            self.NameToAddressMap[procedureName][variableName]["isArray"] = isArray
            self.NameToAddressMap[procedureName][variableName]["isParameter"] = True
            self.memoryStates.append({
                    "isDeclared": False
                })
            self.argNumber[procedureName] += 1
            NDM.memoryStatesLoads.append(-1)
            self.memoryAddress += 1
            
        for variableName,size in declarations:
            #Error
            if variableName in self.NameToAddressMap[procedureName]:
                return {"res":False, "error": "Powtórzenie nazwy zmiennej "+variableName+" "}
            self.NameToAddressMap[procedureName][variableName] = { }
            self.NameToAddressMap[procedureName][variableName]["Address"] = self.memoryAddress
            self.NameToAddressMap[procedureName][variableName]["isArray"] = False if size == -1 else True
            self.NameToAddressMap[procedureName][variableName]["isParameter"] = False
            n = (1 if size == -1 else size)
            self.NameToAddressMap[procedureName][variableName]["size"] = n
            self.memoryAddress += n
            for i in range(n):
                # rozróżniamy to, bo istnieją tablice
                self.memoryStates.append({
                    "Initialized": False,
                    "TimesItWasLoaded": 0,
                    "isDeclared": True
                })
                
                NDM.memoryStatesLoads.append(0)

        NDM.resetAllRegs()
        

        return {"res": True}
    
    def call(self, calledProcedureName, args, procedureName,freeRegister):
        if calledProcedureName not in self.procedureOrder[:-1]:
            if calledProcedureName == self.procedureOrder[-1]:
                return {"res":False, "error": "Niewłaściwe wywołanie procedury "+calledProcedureName+" "}

            return {"res":False, "error": "Niezdefiniowana procedura "+calledProcedureName+" "}
        addr = self.NameToAddressMap[calledProcedureName]["$Callback"]

        i = 0
        for variable in self.NameToAddressMap[calledProcedureName]:
            if variable != "$Callback":
                if self.NameToAddressMap[calledProcedureName][variable]["isParameter"]:
                    if len(args) < i:
                        return {"res":False, "error": "Za mało argumentów w procedurze "+calledProcedureName+" "}
                    if self.NameToAddressMap[calledProcedureName][variable]["isArray"] != self.NameToAddressMap[procedureName][args[i]]["isArray"]:
                        return {"res":False, "error": "Niewłaściwy parametr "+args[i]+" w wywołaniu "+calledProcedureName+" "}
                        
                    i += 1
        if len(args) > i:
            return {"res":False, "error": "Za dużo argumentów w wywołaniu "+calledProcedureName+" "}
                        
        offset = 0

        code = [ const(self.NameToAddressMap[calledProcedureName]["$Callback"] + offset ,freeRegister) ]
        # wsadzić w $Callback wzywanej procedury to, gdzie ma wrócić
        

        i=offset
        # ustawić zmienne w kolejności adresów


        for variableName in args:
            # jeśli jest w procedurze jest argument to przyjmujemy że jest zainicjowany
            i += 1
            code.append(inc(freeRegister))
            
            if self.NameToAddressMap[procedureName][variableName]["isParameter"] == True:
                code.extend([const(self.NameToAddressMap[procedureName][variableName]["Address"], r.a), # MUSI być zainicjalizowana bo jest parametrem
                             load(r.a),store(freeRegister)])
               
            else: # nie jest parametrem
                # jeśli to tablica to zainicjalizuj całą
                for s in range(self.NameToAddressMap[procedureName][variableName]["size"]):
                    self.memoryStates[self.NameToAddressMap[procedureName][variableName]["Address"]+s]["Initialized"] = True
                
                NDM.memoryStatesLoads[self.NameToAddressMap[procedureName][variableName]["Address"]] += 1
                code.extend([const(self.NameToAddressMap[procedureName][variableName]["Address"], r.a), # MUSI być zainicjalizowana bo jest parametrem
                             store(freeRegister)])
        code.extend([const(self.NameToAddressMap[calledProcedureName]["$Callback"] ,freeRegister),
                    strk(r.a), store(freeRegister)]) # wpisz k w callback
        
        code.extend([jump(self.procedureCallAliases[calledProcedureName])])
        NDM.resetAllRegs()
        return {"res":True, "text": ''.join(code)}
        # wsadzone zgodnie z notatkami
                   

    def accessVariable(self, procedureName, variableName, freeRegister):
        if variableName == "$Callback":
            return {"res":True, "text": const(self.NameToAddressMap[procedureName]["$Callback"],r.a) + load(r.a) + put(freeRegister)}
        if variableName not in self.NameToAddressMap[procedureName]:
            return {"res":False, "error": "Nie ma takiej zmiennej jak "+ variableName + " w procedurze " + procedureName+" "}
        if self.NameToAddressMap[procedureName][variableName]["isArray"] == True:
            return {"res":False, "error": "Zmienna "+ variableName + " jest tablicą "}
        address = self.NameToAddressMap[procedureName][variableName]["Address"]

        # DWIE Ścieżki
        #   -   parametr
        #   -   zadeklarowana

        # zadeklarowana
        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:
            if self.memoryStates[address]["Initialized"] == False:
                return {"res":False, "error": "Zmienna "+variableName+" nie zainicjalizowana "}
            
        
        for register in NDM.registerList:
            if NDM.registerVariable[register] == (procedureName, variableName, 0):
                NDM.updateReg(freeRegister,procedureName,variableName)
                NDM.resetReg(register)
                return {"res":True, "text": get(register) + put(freeRegister)}
        

            # self.memoryStates[address]["TimesItWasLoaded"] += 1
        NDM.memoryStatesLoads[address] += 1
        NDM.updateReg(freeRegister,procedureName,variableName)

        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:    
            return {"res":True, "text": const(address,r.a) + load(r.a) + put(freeRegister)}
        else: # parametr
            return {"res":True, "text": const(address,r.a) + load(r.a) + load(r.a) + put(freeRegister)}

            # referujemy do args, którego na tym etapie kompilacji nie znamy i może się zmienić


    def accessTable(self,procedureName, variableName, index, freeRegister):
        if variableName not in self.NameToAddressMap[procedureName]:
            return {"res":False, "error": "Nie ma takiej zmiennej jak "+ variableName + " w procedurze " + procedureName+" "}
        if self.NameToAddressMap[procedureName][variableName]["isArray"] == False:
            return {"res":False, "error": "Zmienna "+ variableName + " nie jest tablicą "}
        address = self.NameToAddressMap[procedureName][variableName]["Address"] + index

        # DWIE Ścieżki
        #   -   parametr
        #   -   zadeklarowana

        # zadeklarowana
        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:
            if index > self.NameToAddressMap[procedureName][variableName]["size"]:
                return {"res":False, "error": "Indeks "+ str(index) + " większy od rozmiaru tablicy "+variableName}
            if self.memoryStates[address]["Initialized"] == False:
                return {"res":False, "error": "Zmienna "+variableName+"["+str(index)+"] nie zainicjalizowana "}
            
            for register in NDM.registerList:
                if NDM.registerVariable[register] == (procedureName, variableName, index):
                    
                    NDM.updateReg(freeRegister,procedureName,variableName,index)
                    NDM.resetReg(register)
                    return {"res":True, "text": get(register) + put(freeRegister)}
        
            # NDM.memoryStatesLoads[address] += 1
            NDM.memoryStatesLoads[address] += 1
            
            NDM.updateReg(freeRegister,procedureName,variableName,index)
            
            return {"res":True, "text": const(address,r.a) + load(r.a) + put(freeRegister)}
            
        else: # parametr
            
            NDM.updateReg(freeRegister,procedureName,variableName,index)
        
            text = [const(address-index,r.a), load(r.a),const(index,freeRegister),add(freeRegister), load(r.a), put(freeRegister)]

            return {"res":True, "text": ''.join(text)}
        
    def accessTableVariable(self,procedureName, variableName, indexVariable, freeRegister, freeRegister2):
        if variableName not in self.NameToAddressMap[procedureName]:
            return {"res":False, "error": "Nie ma takiej zmiennej jak "+ variableName + " w procedurze " + procedureName+" "}
        if self.NameToAddressMap[procedureName][variableName]["isArray"] == False:
            return {"res":False, "error": "Zmienna "+ variableName + " nie jest tablicą "}
        if indexVariable not in self.NameToAddressMap[procedureName]:
            return {"res":False, "error": "Nie ma takiej zmiennej jak "+ indexVariable + " w procedurze " + procedureName+" "}
        if self.NameToAddressMap[procedureName][indexVariable]["isArray"] == True:
            return {"res":False, "error": "Zmienna "+ indexVariable + " jest tablicą "}
        # address = self.NameToAddressMap[procedureName][variableName]["Address"] + index

        # DWIE Ścieżki
        #   -   parametr
        #   -   zadeklarowana

        # NIE DA SIĘ SPRAWDZIĆ ZADEKLAROWANIA -> wszystko odwiedzone
        address = self.NameToAddressMap[procedureName][variableName]["Address"]
        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:
           
            for i in range(self.NameToAddressMap[procedureName][variableName]["size"]):
                NDM.memoryStatesLoads[address+i] += 1
            NDM.resetReg(freeRegister)
            res = self.accessVariable(procedureName, indexVariable,freeRegister2)
            NDM.updateReg(freeRegister,"","")
            if res["res"] == False:
                return res
            text = res["text"] + \
            const(address,r.a) + add(freeRegister2) + load(r.a) + put(freeRegister)
            # RESETUJE FREEREGA
            return {"res":True, "text": text}
        else:
            
            NDM.resetReg(freeRegister)
            res = self.accessVariable(procedureName, indexVariable,freeRegister2)
            NDM.updateReg(freeRegister,"","")
            if res["res"] == False:
                return res
            text = res["text"] + \
            const(address,r.a) + load(r.a) + add(freeRegister2) + load(r.a) + put(freeRegister)
            
            return {"res":True, "text": text}



    # wartość wpisywana jest w rejestrze a
    def assignVariable(self,procedureName, variableName, freeRegister, freeRegister2):
        if variableName not in self.NameToAddressMap[procedureName]:
            return {"res":False, "error": "Nie ma takiej zmiennej jak "+ variableName + " w procedurze " + procedureName+" "}
        if self.NameToAddressMap[procedureName][variableName]["isArray"] == True:
            return {"res":False, "error": "Zmienna "+ variableName + " jest tablicą "}
        
        address = self.NameToAddressMap[procedureName][variableName]["Address"] 
        # print("ADdr: "+str(address))
        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:
            #deklarowane
            self.memoryStates[address]["Initialized"] = True
            # NDM

        text = ''
        ad = 0
        regset = []
        for reg in NDM.registerList:
            if NDM.registerVariable[reg] == (procedureName,variableName,0):
                NDM.updateReg(reg,procedureName,variableName)
                text += put(reg)
                ad += 1
                regset.append(reg)

        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:
            if ad > 0:
                return {"res":True, "text": const_store_alias(address,freeRegister) + text }
            else:
                NDM.updateReg(freeRegister,procedureName,variableName)
                return {"res":True, "text": const_store_alias(address,freeRegister) + put(freeRegister) }
        else:
        
            # if freeRegister in regset:
            if freeRegister2 not in regset:
                NDM.resetReg(freeRegister2)
            NDM.updateReg(freeRegister,procedureName,variableName)
            text = put(freeRegister) + const(address,r.a) + load(r.a) + \
            put(freeRegister2) + get(freeRegister) + store(freeRegister2) + text
            return {"res":True, "text": text }


    def assignTable(self,procedureName, variableName, index, freeRegister,freeRegister2):
        if variableName not in self.NameToAddressMap[procedureName]:
            return {"res":False, "error": "Nie ma takiej zmiennej jak "+ variableName + " w procedurze " + procedureName+" "}
        if self.NameToAddressMap[procedureName][variableName]["isArray"] == False:
            return {"res":False, "error": "Zmienna "+ variableName + " nie jest tablicą "}
        # stores += 1
        address = self.NameToAddressMap[procedureName][variableName]["Address"] + index
        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:
            if index > self.NameToAddressMap[procedureName][variableName]["size"]:
                return {"res":False, "error": "Indeks "+ str(index) + " większy od rozmiaru tablicy "+variableName}

            self.memoryStates[address]["Initialized"] = True

        text = ''
        ad = 0
        regset = []
        for reg in NDM.registerList:
            if NDM.registerVariable[reg] == (procedureName,variableName,index):
                NDM.updateReg(reg,procedureName,variableName,index)
                text += put(reg)
                ad += 1
                regset.append(reg)

        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:
            if ad > 0:
                return {"res":True, "text": const_store_alias(address,freeRegister) + text }
            else:
                NDM.updateReg(freeRegister,procedureName,variableName,index)
                return {"res":True, "text": const_store_alias(address,freeRegister) + put(freeRegister) }
        else:
        
            # if freeRegister in regset:
            if freeRegister2 not in regset:
                NDM.resetReg(freeRegister2)
            NDM.updateReg(freeRegister,procedureName,variableName,index)
            text = put(freeRegister) + const(address-index,r.a) + load(r.a) + \
            const(index,freeRegister2) + add(freeRegister2) + put(freeRegister2) + get(freeRegister) + store(freeRegister2) + text
            return {"res":True, "text": text }

       
    def assignTableVariable(self,procedureName, variableName, indexVariable, freeRegister,freeRegister2):
        if variableName not in self.NameToAddressMap[procedureName]:
            return {"res":False, "error": "Nie ma takiej zmiennej jak "+ variableName + " w procedurze " + procedureName+" "}
        if self.NameToAddressMap[procedureName][variableName]["isArray"] == False:
            return {"res":False, "error": "Zmienna "+ variableName + " nie jest tablicą "}
        if indexVariable not in self.NameToAddressMap[procedureName]:
            return {"res":False, "error": "Nie ma takiej zmiennej jak "+ indexVariable + " w procedurze " + procedureName+" "}
        if self.NameToAddressMap[procedureName][indexVariable]["isArray"] == True:
            return {"res":False, "error": "Zmienna "+ indexVariable + " jest tablicą "}
        
        address = self.NameToAddressMap[procedureName][variableName]["Address"]
        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:
            for i in range(self.NameToAddressMap[procedureName][variableName]["size"]):
                self.memoryStates[address+i]["Initialized"] = True

        if self.NameToAddressMap[procedureName][variableName]["isParameter"] == False:
            text = put(freeRegister2) + self.accessVariable(procedureName, indexVariable,freeRegister)["text"] + \
            const(address,r.a) + add(freeRegister) + put(freeRegister) + get(freeRegister2) + \
            store(freeRegister)
            NDM.resetReg(freeRegister)
            NDM.resetReg(freeRegister2)
            
            return {"res":True, "text": text}
        else:
            text = put(freeRegister2) + self.accessVariable(procedureName, indexVariable,freeRegister)["text"] + \
            put(freeRegister) + const(address,r.a) + load(r.a) + add(freeRegister) + put(freeRegister) + get(freeRegister2) + \
            store(freeRegister)
            NDM.resetReg(freeRegister)
            NDM.resetReg(freeRegister2)
            
            return {"res":True, "text": text}
        


# Lexer

class CompLexer(Lexer):
    tokens = { PROCEDURE, IS, IN, END, PROGRAM, IF, THEN, ELSE, ENDIF,
              WHILE, DO, ENDWHILE, REPEAT, UNTIL, READ, WRITE,
              ID, NUMBER, ASSIGN, LPAREN, RPAREN, LSQUARE, RSQUARE,
              PLUS, MINUS, TIMES, DIVIDE, MODULO,
              EQUAL, NOTEQUAL, GREATER, GEQ, LESS, LEQ,
              N,T, COL }
    
    PROGRAM = 'PROGRAM'
    ELSE = 'ELSE'
    IS = 'IS'
    ENDWHILE = 'ENDWHILE'
    ENDIF = 'ENDIF'
    WHILE = 'WHILE'

    UNTIL = 'UNTIL'

    THEN = 'THEN'

    END = 'END'
    READ = 'READ'
    PROCEDURE = 'PROCEDURE'
    T = 'T'
    IF = 'IF'
    REPEAT = 'REPEAT'
    WRITE = 'WRITE'
    IN = 'IN'
    DO = 'DO'
    


    ignore = ' \t'
    # Tokens
    ID = r'[_a-z]+'
    NUMBER = r'\d+'

    # Arytmetyka / Logika
    ASSIGN = r':='
    LPAREN = r'\('
    RPAREN = r'\)'
    LSQUARE = r'\['
    RSQUARE = r'\]'

    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    MODULO = r'%'

    NOTEQUAL = r'!='
    GEQ = r'>='
    LEQ = r'<='
    EQUAL = r'='
    GREATER = r'>'
    LESS = r'<'
    N = r';'
    
    COL = r','
    

    @_(r'\n')
    def NL(self, t):
        self.lineno += 1
    ignore_comment = r'\#.*'

    def NUMBER(self, t):
        t.value = int(t.value)
        return t
    

    def error(self, t):
        print("Niepoprawny symbol '%s'" % t.value[0])
        exit()

def accessId(data, memoryManager:MemoryManager, lineno):
    id, type, special = data
    if type == -1:
        fregs = NDM.getFreeRegs(1)
        NDM.resetReg(fregs[0])
        NDM.updateReg(fregs[0],"","")
        return const(id,fregs[0]), fregs[0]
    elif type == 0: #zmienna
        fregs = NDM.getFreeRegs(1)
        res = memoryManager.accessVariable(memoryManager.newestProcedure,id,fregs[0])
        if res["res"] == False:
            print(res["error"] + "w linii "+str(lineno))
            exit()
        
        return res["text"], fregs[0]
    elif type == 1: #zmienna i stały indeks 
        fregs = NDM.getFreeRegs(1)
        res = memoryManager.accessTable(memoryManager.newestProcedure,id,special,fregs[0])
        if res["res"] == False:
            print(res["error"] + "w linii "+str(lineno))
            exit()
        # NDM.registerMemory[fregs[0]] = address
        # NDM.updateReg(fregs[0])
        return res["text"]+put(fregs[0]), fregs[0]
    else: #zmienna i zmienny indeks
        fregs = NDM.getFreeRegs(2)
        res = memoryManager.accessTableVariable(memoryManager.newestProcedure,id,special,fregs[0],fregs[1])
        if res["res"] == False:
            print(res["error"] + "w linii "+str(lineno))
            exit()
        # NDM.updateReg(fregs[0])
        return res["text"]+put(fregs[0]), fregs[0]

class CompParser(Parser):
    tokens = CompLexer.tokens
    # debugfile = 'parser.out'
    
    memoryManager = MemoryManager()


    @_('procedures main')
    def program(self, p):
        return jump(self.memoryManager.procedureCallAliases["$main"]) + \
        p.procedures + p.main + halt(), self.memoryManager
       
    @_('procedures PROCEDURE proc_neck IN commands END')
    def procedures(self, p):
        name = p.proc_neck
        setProcedure, callProcedure = genLabel()
        # print(setProcedure,callProcedure)
        self.memoryManager.procedureCallAliases[name] = callProcedure
        # commands = self.replace_proc_call_alias(name, p.commands)
        return p.procedures + setProcedure + p.commands + self.memoryManager.accessVariable(name,"$Callback",r.b)["text"] + inc(r.a) + inc(r.a) + inc(r.a)+ jumpr(r.a)
        
    @_('')
    def procedures(self, p):
        return ''
    
    # main ---------------------------
    

    @_('main_head commands END')
    def main(self, p):
        setProcedure, callProcedure = genLabel()
        self.memoryManager.procedureCallAliases["$main"] = callProcedure
        # commands = self.replace_proc_call_alias("$main", p.commands)
        return setProcedure + p.commands


    @_('PROGRAM IS IN commands END')
    def main(self, p):
        setProcedure, callProcedure = genLabel()
        self.memoryManager.procedureCallAliases["$main"] = callProcedure
        # commands = self.replace_proc_call_alias("$main", p.commands)
        NDM.resetAllRegs()
        return setProcedure + p.commands

    @_('PROGRAM IS declarations IN')
    def main_head(self,p):
        res = self.memoryManager.createProcedure("$main",[],p.declarations) # declarations = (varname, size)
        if res["res"] == False:
            print(res["error"]+ "W linii "+str(p.lineno ))
            exit()
    # commands ----------------------
        
    @_('commands command')
    def commands(self, p):
        return p.commands + p.command

    @_('command')
    def commands(self, p):
        return p.command
    
    # command -----------------------
    

    @_('identifier ASSIGN expression N')
    def command(self, p):
        # wartość expression jest w rejestrze r.a
        # w zależności od tego czym jest identifier mamy różne funkcje
        
        exp = ""
        sign, data1, data2 = p.expression
        if sign == 'v': # number
            id, type, special = data1
            # print(sign,type)
            if type == -1:
                exp =  const(id,r.a)
            elif type == 0: #zmienna
                fregs = NDM.getFreeRegs(1)
                res = self.memoryManager.accessVariable(self.memoryManager.newestProcedure,id,fregs[0])
                if res["res"] == False:
                    print(res["error"]+ "w linii "+str(p.lineno))
                    exit()
                exp = res["text"]
            elif type == 1: #zmienna i stały indeks 
                fregs = NDM.getFreeRegs(1)
                res = self.memoryManager.accessTable(self.memoryManager.newestProcedure,id,special,fregs[0])
                if res["res"] == False:
                    print(res["error"]+ "w linii "+str(p.lineno))
                    exit()
                exp = res["text"]
            else: #zmienna i zmienny indeks
                fregs = NDM.getFreeRegs(2)
                res = self.memoryManager.accessTableVariable(self.memoryManager.newestProcedure,id,special,fregs[0],fregs[1])
                if res["res"] == False:
                    print(res["error"]+ "w linii "+str(p.lineno))
                    exit()
                exp = res["text"]
                # print("RES:",res["text"])
        elif sign == "+":
            # print("Acc1")
            
            text, freg0 = accessId(data1,self.memoryManager,p.lineno)
            
            exp += text
            text, freg1 = accessId(data2,self.memoryManager,p.lineno)
            # print(data2)
            # print("Acc2")
            exp += text
            exp += get(freg0) + add(freg1)
            # exp += add(freg0)
        elif sign == "-":
            text, freg1 = accessId(data2,self.memoryManager,p.lineno)
            exp += text
            text, freg0 = accessId(data1,self.memoryManager,p.lineno)
            exp += text
            exp += get(freg0) + sub(freg1)
        elif sign == "*":
            # -------- razy stała -----------
            id1, type1, special1 = data1
            id2, type2, special2 = data2
            if type1 == -1:
                if type2 == -1:
                    exp += const(id1*id2,r.a)
                else:
                    text, freg1 = accessId(data2,self.memoryManager,p.lineno)
                    exp += text + multConstant(id1,freg1)
                    NDM.resetReg(freg1)
            else:
                if type2 == -1:
                    text, freg0 = accessId(data1,self.memoryManager,p.lineno)
                    exp += text + multConstant(id2,freg0)
                    NDM.resetReg(freg0)
                else:
                    # -------------------------------
                    text, freg0 = accessId(data1,self.memoryManager,p.lineno)
                    exp += text
                    text, freg1 = ("","")
                    if data1 == data2:
                        f = NDM.getFreeRegs(1)
                        NDM.updateReg(f[0],"","")
                        text, freg1 = get(freg0) + put(f[0]), f[0]
                    else:
                        text, freg1 = accessId(data2,self.memoryManager,p.lineno)

                    exp += text
                    regs = NDM.getFreeRegs(2,[freg0,freg1])
                    # exp += get(freg0) + write() + get(freg1) + write()
                    # exp += get(regs[0]) + write() + get(regs[1]) + write()
                    exp += mult(freg0,freg1,regs[0],regs[1]) 
                    for reg in [freg0,freg1,regs[0],regs[1]]:
                        NDM.resetReg(reg)
        elif sign == "/":
            text, freg0 = accessId(data1,self.memoryManager,p.lineno)
            exp += text
            text, freg1 = ("","")
            if data1 == data2:
                f = NDM.getFreeRegs(1)
                NDM.updateReg(f[0],"","")
                text, freg1 = get(freg0) + put(f[0]), f[0]
            else:
                text, freg1 = accessId(data2,self.memoryManager,p.lineno)
            
            exp += text
            regs = NDM.getFreeRegs(3,[freg0,freg1])
            
            exp += div(freg0,freg1,regs[0],regs[1],regs[2])
            for reg in [freg0,freg1,regs[0],regs[1],regs[2]]:
                NDM.resetReg(reg)
        elif sign == "%":
            text, freg0 = accessId(data1,self.memoryManager,p.lineno)
            exp += text
            text, freg1 = ("","")
            if data1 == data2:
                f = NDM.getFreeRegs(1)
                NDM.updateReg(f[0],"","")
                text, freg1 = get(freg0) + put(f[0]), f[0]
            else:
                text, freg1 = accessId(data2,self.memoryManager,p.lineno)
            exp += text
            regs = NDM.getFreeRegs(1,[freg0,freg1])
            exp += mod(freg0,freg1,regs[0])
            for reg in [freg0,freg1,regs[0]]:
                NDM.resetReg(reg)

        id, type, special = p.identifier
        # print(id,type,special)
        
        # print(exp)
        # assignment
        if type == 0: #zmienna
            fregs = NDM.getFreeRegs(2)
            res = self.memoryManager.assignVariable(self.memoryManager.newestProcedure,id,fregs[0],fregs[1])
            if res["res"] == False:
                print(res["error"] + "w linii "+str(p.lineno))
                exit()
            # print(exp)
            return exp + res["text"]
        elif type == 1: #zmienna i stały indeks 
            fregs = NDM.getFreeRegs(2)
            res = self.memoryManager.assignTable(self.memoryManager.newestProcedure,id,special,fregs[0],fregs[1])
            if res["res"] == False:
                print(res["error"] + "w linii "+str(p.lineno))
                exit()
            return exp + res["text"]
        else: #zmienna i zmienny indeks
            fregs = NDM.getFreeRegs(2)
            # print(p.lineno)
            # print(id,type,special)
            res = self.memoryManager.assignTableVariable(self.memoryManager.newestProcedure,id,special,fregs[0],fregs[1])
            if res["res"] == False:
                print(res["error"] + "w linii "+str(p.lineno))
                exit()
            return exp + res["text"]
        
    

    @_('IF condition THEN commands eelse commands ENDIF')
    def command(self, p):
        #cond
        sTrue, sFalse, con = p.condition
        send,cend = genLabel()
        text = con + sTrue + p.commands0 + jump(cend) + \
            sFalse + p.commands1 + \
            send
        #...
        NDM.resetAllRegs()
        return text

    @_('ELSE')
    def eelse(self,p):
        NDM.resetAllRegs()
        
    @_('IF condition THEN commands ENDIF')
    def command(self, p):
        #cond
        sTrue, sFalse, con = p.condition
        text = con + sTrue + p.commands + sFalse
        #...
        NDM.resetAllRegs()
        return text


    @_('wwhile condition DO commands ENDWHILE')
    def command(self, p):
        #cond
        sTrue, sFalse, con = p.condition

        sloop,cloop = genLabel()
        text = sloop + con + sTrue + p.commands + jump(cloop) + \
            sFalse 
        #...
        NDM.resetAllRegs()
        return text

    @_("WHILE")
    def wwhile(self, p):
        0
        # NDM.resetAllRegs()

    @_('rpp commands UNTIL condition N')
    def command(self, p):
        #cond
        sTrue, sFalse, con = p.condition
        
        text = sFalse + p.commands + con + sTrue
        #...
        NDM.resetAllRegs()
        return text

    @_('REPEAT')
    def rpp(self,p):
        NDM.resetAllRegs()

    @_('proc_call N')
    def command(self, p):
        NDM.resetAllRegs()
        return p.proc_call

    @_('READ identifier N')
    def command(self, p):
        id, type, special = p.identifier
        
        if type == 0: #zmienna
            fregs = NDM.getFreeRegs(2)
            # print("NP: "+self.memoryManager.newestProcedure+" "+id)
            res = self.memoryManager.assignVariable(self.memoryManager.newestProcedure,id,fregs[0],fregs[1])
            if res["res"] == False:
                print(res["error"] + "w linii "+str(p.lineno))
                exit()
            return read() + res["text"]
        elif type == 1: #zmienna i stały indeks 
            fregs = NDM.getFreeRegs(2)
            res = self.memoryManager.assignTable(self.memoryManager.newestProcedure,id,special,fregs[0],fregs[1])
            if res["res"] == False:
                print(res["error"] + "w linii "+str(p.lineno))
                exit()
            return read() + res["text"]
        else: #zmienna i zmienny indeks
            fregs = NDM.getFreeRegs(2)
            res = self.memoryManager.assignTableVariable(self.memoryManager.newestProcedure,id,special,fregs[0],fregs[1])
            if res["res"] == False:
                print(res["error"] + "w linii "+str(p.lineno))
                exit()
            return read() + res["text"]

    @_('WRITE value N')
    def command(self, p):
        text,reg0 = accessId(p.value,self.memoryManager,p.lineno)
        return text + get(reg0) + write()


    # NECK -------------------------------------------------------

    @_('proc_head IS declarations')
    def proc_neck(self, p):
        name, elements = p.proc_head
        
        res = self.memoryManager.createProcedure(name,elements,p.declarations) # declarations = (varname, size)
        if res["res"] == False:
            print(res["error"] + "w linii "+str(p.lineno))
            exit()
        return name

    @_('proc_head IS')
    def proc_neck(self, p):
        name, elements = p.proc_head
        
        res = self.memoryManager.createProcedure(name,elements,[])
        if res["res"] == False:
            print(res["error"] + "w linii "+str(p.lineno))
            exit()
        return name
        
    @_('ID LPAREN args_decl RPAREN') # args_decl to tablica elementów (nazwa, czyJestTablicą)
    def proc_head(self, p):
        return (p.ID, p.args_decl)

    @_('ID LPAREN args RPAREN')
    def proc_call(self, p):
        # wszystkie rejestry są od teraz nieokreślone...?
        res = self.memoryManager.call(p.ID,p.args,self.memoryManager.newestProcedure,r.b)
        if res["res"] == False:
            print(res["error"] + "w linii "+str(p.lineno))
            exit()
        return res["text"]

    # declarations -------------------------------------------------------

    @_('declarations COL ID')
    def declarations(self, p):
        p.declarations.append((p.ID, -1))
        return p.declarations

    @_('declarations COL ID LSQUARE NUMBER RSQUARE')
    def declarations(self, p):
        if p.NUMBER == 0:
            print("Tablica wielkości 0 " + "w linii "+str(p.lineno))
            exit()
        p.declarations.append((p.ID, p.NUMBER))
        return p.declarations

    @_('ID')
    def declarations(self, p):
        return [(p.ID, -1)]

    @_('ID LSQUARE NUMBER RSQUARE')
    def declarations(self, p):
        if p.NUMBER == 0:
            print("Tablica wielkości 0 " + "w linii "+str(p.lineno))
            exit()
        return [(p.ID, p.NUMBER)]

    # args_decl ---------------------------------------------------------

    @_('args_decl COL ID')
    def args_decl(self, p):
        p.args_decl.append((p.ID, False))
        return p.args_decl

    @_('args_decl COL T ID')
    def args_decl(self, p):
        p.args_decl.append((p.ID, True))
        return p.args_decl
        

    @_('ID')
    def args_decl(self, p):
        return [(p.ID, False)] # czy jest tablicą

    @_('T ID')
    def args_decl(self, p):
        return [(p.ID, True)] # czy jest tablicą
        

    # args --------------------------

    @_('args COL ID')
    def args(self, p):
        z = p.args
        z.append(p.ID)
        return z

    @_('ID')
    def args(self, p):
        return [p.ID]

    # expression --------------------------
    # po wykonaniu w rejestrze a ma być wartość expressiona

    @_('value')
    def expression(self, p):
        return ("v",p.value,p.value)

    @_('value PLUS value')
    def expression(self, p):
        return ("+",p.value0,p.value1)

    @_('value MINUS value')
    def expression(self, p):
        return ("-",p.value0,p.value1)

    @_('value TIMES value')
    def expression(self, p):
        return ("*",p.value0,p.value1)

    @_('value DIVIDE value')
    def expression(self, p):
        return ("/",p.value0,p.value1)

    @_('value MODULO value')
    def expression(self, p):
        return ("%",p.value0,p.value1)

    # condition --------------------
        

    @_('value EQUAL value')
    def condition(self, p):
        NDM.resetAllRegs()
        com = ""
        text, reg0 = accessId(p.value0,self.memoryManager,p.lineno)
        com += text
        text, reg1 = accessId(p.value1,self.memoryManager,p.lineno)
        com += text

        sFalse,cFalse = genLabel()
        sTrue, cTrue = genLabel()

        com +=''.join([
            get(reg0), sub(reg1), jpos(cFalse),
            get(reg1), sub(reg0), jpos(cFalse),
            jump(cTrue)
        ])
        NDM.resetAllRegs()
        return sTrue, sFalse, com


    @_('value NOTEQUAL value')
    def condition(self, p):
        NDM.resetAllRegs()
        com = ""
        text, reg0 = accessId(p.value0,self.memoryManager,p.lineno)
        com += text
        text, reg1 = accessId(p.value1,self.memoryManager,p.lineno)
        com += text

        sFalse,cFalse = genLabel()
        sTrue, cTrue = genLabel()

        com +=''.join([
            get(reg0), sub(reg1), jpos(cTrue),
            get(reg1), sub(reg0), jpos(cTrue),
            jump(cFalse)
        ])
        NDM.resetAllRegs()

        return sTrue, sFalse, com

    @_('value GREATER value')
    def condition(self, p):
        NDM.resetAllRegs()
        com = ""
        text, reg0 = accessId(p.value0,self.memoryManager,p.lineno)
        com += text
        text, reg1 = accessId(p.value1,self.memoryManager,p.lineno)
        com += text

        sFalse,cFalse = genLabel()
        sTrue, cTrue = genLabel()

        com +=''.join([
            get(reg0), sub(reg1), jpos(cTrue),
            jump(cFalse)
        ])
        NDM.resetAllRegs()

        return sTrue, sFalse, com

    @_('value LESS value')
    def condition(self, p):
        NDM.resetAllRegs()
        com = ""
        text, reg0 = accessId(p.value0,self.memoryManager,p.lineno)
        com += text
        text, reg1 = accessId(p.value1,self.memoryManager,p.lineno)
        com += text

        sFalse,cFalse = genLabel()
        sTrue, cTrue = genLabel()

        com +=''.join([
            get(reg1), sub(reg0), jpos(cTrue),
            jump(cFalse)
        ])

        NDM.resetAllRegs()
        return sTrue, sFalse, com

    @_('value GEQ value')
    def condition(self, p):
        NDM.resetAllRegs()
        com = ""
        text, reg0 = accessId(p.value0,self.memoryManager,p.lineno)
        com += text
        text, reg1 = accessId(p.value1,self.memoryManager,p.lineno)
        com += text

        sFalse,cFalse = genLabel()
        sTrue, cTrue = genLabel()

        com +=''.join([
            get(reg1), sub(reg0), jpos(cFalse),
            jump(cTrue)
        ])

        NDM.resetAllRegs()
        return sTrue, sFalse, com

    @_('value LEQ value')
    def condition(self, p):
        NDM.resetAllRegs()
        com = ""
        text, reg0 = accessId(p.value0,self.memoryManager,p.lineno)
        com += text
        text, reg1 = accessId(p.value1,self.memoryManager,p.lineno)
        com += text

        sFalse,cFalse = genLabel()
        sTrue, cTrue = genLabel()

        com +=''.join([
            get(reg0), sub(reg1), jpos(cFalse),
            jump(cTrue)
        ])

        NDM.resetAllRegs()
        return sTrue, sFalse, com

    # value ------------------------------

    @_('NUMBER')
    def value(self, p):
        return (p.NUMBER,-1,p.NUMBER)

    @_('identifier')
    def value(self, p):
        return p.identifier
    

    # identifier ------------------------------

    @_('ID')
    def identifier(self, p):
        return (p.ID,0, -1)

    @_('ID LSQUARE NUMBER RSQUARE')
    def identifier(self, p):
        return (p.ID,1, p.NUMBER)

    @_('ID LSQUARE ID RSQUARE')
    def identifier(self, p):
        return (p.ID0,2, p.ID1)

    

    def error(self,p):
        print("Błąd składniowy w linii ",p.lineno)
        exit()

if __name__ == '__main__':
    lexer = CompLexer()
    parser = CompParser()
    
    if len(argv) < 3:
        print("Za mało argumentów")
        exit()

    text = ""
    
    with open(argv[1]) as f:
        for line in f:
            text+=line
    
    
    program, memoryManager = parser.parse(lexer.tokenize(text))
    
    # text = program
    text = postProcess(program, memoryManager)

    with open(argv[2],'w') as f:
        f.write(text)
