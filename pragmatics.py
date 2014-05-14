import re
import flags
operation = ''
assemlist=[]
assembegin = []
bss = ['SECTION .bss\nz1:    resd    1']
reals = []
realno = []
tempregcontent = []
var1 =''
var2 =''



registers = ['ebx','ecx','esi','edi','ebp','esp'] 
reg = {'eax':'','ebx':'','ecx':'','edx':'','esp':'','ebp':'','esi':'','edi':''} # dictionary
regex = re.compile('([a-z][a-zA-Z0-9]*)|([0-9]+)|([IR$]+[0-9]+)')


        
        
   
def real_addition(var1,var2,var3) :
    if var1 in flags.global_list :
        instruction = 'fld\tdword ['+var1+']'
        assemlist.append(instruction)
        #print(instruction)
    instruction = 'fld\tdword ['+var2+']'
    assemlist.append(instruction)
   # print(instruction)
    instruction1 = 'faddp\tst1,st0\nsub\tesp,8\nfstp\tqword [esp]\n'
    instruction2='push ' + 'stmt' + str(flags.print_counter+1)
    instruction = instruction1 + instruction2 + '\ncall\tprintf\nadd\tesp,12'
    assemlist.append(instruction)
    #print(instruction)
            
   
def real_subtraction(var1,var2,var3) :
    if var1 in flags.global_list :
        instruction = 'fld\tdword ['+var1+']'
        assemlist.append(instruction)
        #print(instruction)
    instruction = 'fld\tdword ['+var2+']'
    assemlist.append(instruction)
   # print(instruction)
    instruction1= 'fsubp\tst1,st0\nsub\tesp,8\nfstp\tqword [esp]\n'
    instruction2='push ' + 'stmt' + str(flags.print_counter+1)
    instruction= instruction1 + instruction2 + '\ncall\tprintf\nadd\tesp,12'
    assemlist.append(instruction) 
    #print(instruction)

def findreg(nam,var):
	
    for x in registers:
        if reg[x] == '':
            reg[x] = var
            flags.var_reg[nam] = x
            return x
    #print ('all registers full')
 
def remove(nam,var):
    reg[flags.var_reg[nam]] = ''
    flags.var_reg.pop(nam)

def regclear():

    flags.var_reg = {}
    flags.local_list = []
    global reg
    reg = {'eax':'','ebx':'','ecx':'','edx':'','esi':'','edi':'','ebp':'','esp':''}    

def search(var_name):
    if var_name in flags.local_list :
       pass
    elif var_name in flags.global_list :
       pass        
    else :                                  #load intermediate result in register,or any other variable not in register
        flags.local_list.append(var_name)
        foundreg = findreg(var_name,'0123')
        remove(var_name,'')
        findreg(var_name,foundreg)

def gen_final_instruction(var_name):
    if var_name in flags.local_list :
        instruction='mov\t'+ reg[flags.var_reg[var_name]] + ',eax'
        assemlist.append(instruction)
        #print(instruction)
    elif var_name in flags.global_list :
        instruction='mov\tdword ['+ var_name + '],eax'
        assemlist.append(instruction)
        #print(instruction)
    else :                                        #intermediate result
        foundreg = findreg(var_name,'0123')
        instruction='mov\t'+ foundreg + ',eax'
        assemlist.append(instruction)
       # print(instruction)
        
def move(var_name,var_value,var_index):
    var_value = str(var_value)
    var_name = str(var_name)
    var_index = str(var_index)
    if var_index == '-' :
        if var_name in flags.local_list :
            if var_value in flags.local_list :
                instruction='mov\t'+reg[flags.var_reg[var_name]]+','+ reg[flags.var_reg[var_value]]
                assemlist.append(instruction)
                #print(instruction)
                instruction='mov\tdword [z1],'+ reg[flags.var_reg[var_value]]
                assemlist.append(instruction)
                #print(instruction)
            elif var_value in flags.global_list :
                instruction='mov\t'+reg[flags.var_reg[var_name]]+',['+var_value+']'
                assemlist.append(instruction)
                #print(instruction)
                instruction='mov\tdword [z1],['+var_value+']'
                assemlist.append(instruction)
                prin(instruction)
            else :
                instruction='mov\t'+reg[flags.var_reg[var_name]]+','+ str(var_value)
                assemlist.append(instruction)
                #print(instruction)
                instruction='mov\tdword [z1],'+ var_value
                assemlist.append(instruction)
                #print(instruction)
        elif var_name in flags.global_list :
            if var_value in flags.local_list :
                instruction='mov\tdword ['+var_name+'],'+ reg[flags.var_reg[var_value]]
                assemlist.append(instruction)
               # print(instruction)
            elif var_value in flags.global_list :
                var_in_global(var_value)
                instruction='mov\tdword ['+var_name+'],eax'
                assemlist.append(instruction)
                prin(instruction)
            else :
                instruction='mov\tdword ['+var_name+'],'+ var_value
                assemlist.append(instruction)
               # print(instruction)
        else :
            foundreg=findreg(var_name,'1234')
            if var_value in flags.local_list :
                instruction='mov\t'+z+','+ reg[flags.var_reg[var_value]]
                assemlist.append(instruction)
                #print(instruction)
                instruction='mov\tdword [z1],'+ reg[flags.var_reg[var_value]]
                assemlist.append(instruction)
                #print(instruction)
            elif var_value in flags.global_list :
                var_in_global(var_value)
                instruction='mov\t'+z+',eax'
                assemlist.append(instruction)
                #print(instruction)
                instruction='mov\tdword [z1],eax'
                assemlist.append(instruction)
                #print(instruction)
            else :
                instruction='mov\t'+z+','+ var_value
                assemlist.append(instruction)
               # print(instruction)
                instruction='mov\tdword [z1],'+ var_value
                assemlist.append(instruction)
                #print(instruction)
    else :
        if var_name in flags.global_list :
            if var_index in flags.local_list :
                instruction='mov\teax,'+ reg[flags.var_reg[var_index]]
                assemlist.append(instruction)
                #print(instruction)
                instruction='imul\teax,4'
                assemlist.append(instruction)
               # print(instruction) 
            elif var_index in flags.global_list :
                instruction='mov\teax,['+var_index+']'
                assemlist.append(instruction)
                #print(instruction)
                instruction='imul\teax,4'
                assemlist.append(instruction)
                #print(instruction)
            else :
                instruction='mov\teax,' + var_index
                assemlist.append(instruction)
                #print(instruction)
                instruction='imul\teax,4'
                assemlist.append(instruction)
               # print(instruction)
                
            if var_value in flags.local_list :
                instruction='mov\tdword ['+var_name+' + eax],'+ reg[flags.var_reg[var_value]]
                assemlist.append(instruction)
                #print(instruction)
            elif var_value in flags.global_list :
                instruction='mov\tedx,['+var_value+']'
                assemlist.append(instruction)
                #print(instruction)
                instruction='mov\tdword ['+var_name+' + eax],edx'
                assemlist.append(instruction)
                #print(instruction)
            else :
                instruction='mov\tdword ['+var_name+' + eax],'+ str(var_value)
                assemlist.append(instruction)
               # print(instruction)
                        
        
def printvar(var_name):
    if var_name in flags.local_list :                                                
        if var_name in flags.globalintegers or var_name in flags.localintegers:         
            instruction='push\tdword [z1]'
            assemlist.append(instruction)
            #print(instruction)
	    instruction='push ' + 'stmt' + str(flags.print_counter)
            assemlist.append(instruction)
            #print(instruction)
            instruction='call printf'
            assemlist.append(instruction)
            #print(instruction)
        elif var_name in realno :
	    instruction='push ' + 'stmt' + str(flags.print_counter)
    elif var_name in flags.global_list :
        if var_name in flags.globalintegers or var_name in flags.localintegers :
            instruction='push\tdword ['+ var_name +']'
            assemlist.append(instruction)
            #print(instruction)
	    instruction='push ' + 'stmt' + str(flags.print_counter)
            assemlist.append(instruction)
            #print(instruction)
            instruction='call printf'
            assemlist.append(instruction)
            #print(instruction)
        elif var_name in realno :
	    instruction='push ' + 'stmt' + str(flags.print_counter)
    else :
        if var_name in flags.globalintegers or var_name in flags.localintegers :
            instruction='push\t[z1]'
            assemlist.append(instruction)
           # print(instruction)
	    instruction='push ' + 'stmt' + str(flags.print_counter)
            assemlist.append(instruction)
            #print(instruction)
            instruction='call printf'
            assemlist.append(instruction)
            #print(instruction)
        elif var_name in realno :
	    instruction='push ' + 'stmt' + str(flags.print_counter)
            
                        
def printarray(arr_name,index):
    
    if arr_name in flags.global_list :
        if arr_name in flags.globalintegers or arr_name in flags.localintegers :
            if index in flags.local_list :
                instruction='mov\teax,'+ reg[flags.var_reg[index]]
                assemlist.append(instruction)
                #print(instruction)
                instruction='imul\teax,4'
                assemlist.append(instruction)
                #print(instruction)
            elif index in flags.global_list :
                instruction='mov\teax,['+index+']'
                assemlist.append(instruction)
                #print(instruction)
                instruction='imul\teax,4'
                assemlist.append(instruction)
                #print(instruction) 
            else :
                instruction='mov\teax,' + index
                assemlist.append(instruction)
                #print(instruction)
                instruction='imul\teax,4'
                assemlist.append(instruction)
                #print(instruction)  
            instruction='push\tdword ['+ arr_name +' + eax]'
            assemlist.append(instruction)
            #print(instruction)
	    instruction='push ' + 'stmt' + str(flags.print_counter)
            assemlist.append(instruction)
           # print(instruction)
            instruction='call printf'
            assemlist.append(instruction)
            #print(instruction)
        elif arr_name in realno :
	    instruction='push ' + 'stmt' + str(flags.print_counter)


def sub_load_red(var_name,index) :

    if var_name in flags.global_list :
        if index in flags.local_list :
            instruction='mov\teax,'+ reg[flags.var_reg[index]]
            assemlist.append(instruction)
            #print(instruction)
            instruction='imul\teax,4'
            assemlist.append(instruction)
            #print(instruction)
            instruction='mov\teax,['+ var_name +' + eax]'
            assemlist.append(instruction)
           # print(instruction)
        elif index in flags.global_list :
            instruction='mov\teax,['+index+']'
            assemlist.append(instruction)
            #print(instruction)
            instruction='imul\teax,4'
            assemlist.append(instruction)
            #print(instruction)
            instruction='mov\teax,['+ var_name +' + eax]'
            assemlist.append(instruction)
            #print(instruction)
        else :
            instruction='mov\teax,' + index
            assemlist.append(instruction)
            #print(instruction)
            instruction='imul\teax,4'
            assemlist.append(instruction)
            prin(tinstruction)
            instruction='mov\teax,['+ var_name + ' + eax]'
            assemlist.append(instruction)
            #print(instruction)

def compare(var1,var2) :
    var1 = str(var1)
    var2 = str(var2)
    if var1 in flags.local_list :
        if var2 in flags.local_list :
            instruction='cmp\t'+reg[flags.var_reg[var1]]+','+ reg[flags.var_reg[var2]]
            assemlist.append(instruction)
            #print(instruction)
        elif var2 in flags.global_list :
            instruction='cmp\t'+reg[flags.var_reg[var1]]+',['+var2+']' 
            assemlist.append(instruction)
            #print(instruction)
            remove(var2,'')
        else :
            instruction='cmp\t'+reg[flags.var_reg[var1]]+','+ var2
            assemlist.append(instruction)
            #print(instruction)
    elif var1 in flags.global_list :
        if var2 in flags.local_list :
            instruction='cmp\t['+var1+'],'+ reg[flags.var_reg[var2]]
            assemlist.append(instruction)
            #print(instruction)
        elif var2 in flags.global_list :
            instruction='mov\teax,['+var1+']'
            assemlist.append(instruction)
           # print(instruction)
            instruction='cmp\teax,['+ var2 +']'
            assemlist.append(instruction)
            #print(instruction)
        else :
            instruction='cmp\tdword ['+var1+'],'+ var2
            assemlist.append(instruction)
            #print(instruction)
    else :
        if var2 in flags.local_list :
            #print('var2 in local',var2)
            instruction='mov\teax,'+ var1
            assemlist.append(instruction)
           # print(instruction)
            instruction='cmp\teax,'+ reg[flags.var_reg[var2]]
            assemlist.append(instruction)
            #print(instruction)
        elif var2 in flags.global_list :
            #print('var2 in global',var2)
            instruction='mov\teax,'+ var1
            assemlist.append(instruction)
            #print(instruction)
            instruction='cmp\teax,['+ var2+']'
            assemlist.append(instruction)
            #print(instruction)
        else :
            instruction='mov\teax,'+ var1
            assemlist.append(instruction)
           # print(instruction)
            instruction='cmp\teax,'+ var2
            assemlist.append(instruction)
           # print(instruction)
    
    output = regex.findall(var1)
    if output[0][2] != '' :
        remove(var1,'')
    output = regex.findall(var2)
    if output[0][2] != '' :
        remove(var2,'')



def addition(var1,var2):
    var1 = str(var1)
    var2 = str(var2)
    if var1 in flags.local_list :
        if var2 in flags.local_list :
            instruction='mov\teax,'+ reg[flags.var_reg[var1]]
            assemlist.append(instruction)
            #print(instruction)
            instruction='add\teax,'+ reg[flags.var_reg[var2]]
            assemlist.append(instruction)
            #print(instruction)
        elif var2 in flags.global_list :
            instruction='mov\teax,'+ reg[flags.var_reg[var1]]
            assemlist.append(instruction)
            #print(instruction)
            instruction='add\teax,['+var2+']' 
            assemlist.append(instruction)
            #print(instruction)
        else :
            instruction='mov\teax,'+ reg[flags.var_reg[var1]]
            assemlist.append(instruction)
            #print(instruction)
            instruction='add\teax,'+ var2
            assemlist.append(instruction)
           # print(instruction)
    elif var1 in flags.global_list :
        if var2 in flags.local_list :
            instruction='mov\teax,['+ var1 +']'
            assemlist.append(instruction)
            #print(instruction)
            instruction='add\teax,'+ reg[flags.var_reg[var2]]
            assemlist.append(instruction)
            #print(instruction)
        elif var2 in flags.global_list :
            instruction='mov\teax,['+var1+']'
            assemlist.append(instruction)
           # print(instruction)
            instruction='add\teax,['+ var2 +']'
            assemlist.append(instruction)
            #print(instruction)
        else :
            instruction='mov\teax,['+ var1 +']'
            assemlist.append(instruction)
            #print(instruction)
            instruction='add\teax,'+ var2
            assemlist.append(instruction)
           # print(instruction)
    else :
        if var2 in flags.local_list :
            instruction='mov\teax,'+ var1
            assemlist.append(instruction)
           # print(instruction)
            instruction='add\teax,'+ reg[flags.var_reg[var2]]
            assemlist.append(instruction)
           # print(instruction)
        elif var2 in flags.global_list :
            instruction='mov\teax,'+ var1
            assemlist.append(instruction)
           # print(instruction)
            instruction='add\teax,['+var2+']' 
            assemlist.append(instruction)
            #print(instruction)
        else :
            instruction='mov\teax,'+ var1
            assemlist.append(instruction)
           # print(instruction)
            instruction='add\teax,'+ var2
            assemlist.append(instruction)
           # print(instruction)

def subtraction(var1,var2):
    var1 = str(var1)
    var2 = str(var2)
    if var1 in flags.local_list :
        if var2 in flags.local_list :
            instruction='mov\teax,'+ reg[flags.var_reg[var1]]
            assemlist.append(instruction)
            #print(instruction)
            instruction='sub\teax,'+ reg[flags.var_reg[var2]]
            assemlist.append(instruction)
           # print(instruction)
        elif var2 in flags.flags.global_listl_list :
            instruction='mov\teax,'+ reg[flags.var_reg[var1]]
            assemlist.append(instruction)
            #print(instruction)
            instruction='sub\teax,['+var2+']' 
            assemlist.append(instruction)
           # print(instruction)
        else :
            instruction='mov\teax,'+ reg[flags.var_reg[var1]]
            assemlist.append(instruction)
           # print(instruction)
            instruction='sub\teax,'+ var2
            assemlist.append(instruction)
           # print(instruction)
    elif var1 in flags.flags.global_listl_list :
        if var2 in flags.local_list :
            instruction='mov\teax,['+ var1 +']'
            assemlist.append(instruction)
           # print(instruction)
            instruction='sub\teax,'+ reg[flags.var_reg[var2]]
            assemlist.append(instruction)
            #print(instruction)
        elif var2 in flags.global_list :
            instruction='mov\teax,['+var1+']'
            assemlist.append(instruction)
           # print(instruction)
            instruction='sub\teax,['+ var2 +']'
            assemlist.append(instruction)
            #print(instruction)
        else :
            instruction='mov\teax,['+ var1 +']'
            assemlist.append(instruction)
           # print(instruction)
            instruction='sub\teax,'+ var2
            assemlist.append(instruction)
           # print(instruction)
    else :
        if var2 in flags.local_list :
            instruction='mov\teax,'+ var1
            assemlist.append(instruction)
           # print(instruction)
            instruction='sub\teax,'+ reg[flags.var_reg[var2]]
            assemlist.append(instruction)
            #print(instruction)
        elif var2 in flags.global_list :
            instruction='mov\teax,'+ var1
            assemlist.append(instruction)
            #print(instruction)
            instruction='sub\teax,['+var2+']' 
            assemlist.append(instruction)
           # print(instruction)
        else :
            instruction='mov\teax,'+ var1
            assemlist.append(instruction)
           # print(instruction)
            instruction='sub\teax,'+ var2
            assemlist.append(instruction)
           # print(instruction)                

def var_in_global(var):
    instruction = 'mov\teax,'+'['+var+']'
    assemlist.append(instruction)
    #print(instruction)
            
def pragmatic(tuplelist, localvar):
	
    if tuplelist[1] == "BEGINPROGRAM":
        name = tuplelist[0] + ".asm"
        assemlist.append(name)
       # print(name)
        assembegin.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")

	
    elif  tuplelist[1] == "ENDPROGRAM":
        instruction = 'mov esp, ebp\npop dword ebp'  
        assemlist.append(instruction)
        #print(instruction)
        instruction = 'ret\n'
        assemlist.append(instruction)
       # print(instruction)
        pragma = open(assemlist[0],'w+')
        assemlist.pop(0)
        for x in assembegin:
            x = x + '\n'
            pragma.write(x)
        pragma.write('global main\nextern printf\n')
        pragma.write("SECTION .data\n")
        for x in flags.realnos:
            x = x +  ':\tresd\t1'
            bss.append(x)
	for x in flags.datasection:
            pragma.write(x)
        for x in bss:
            x = x + '\n'
            pragma.write(x)
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
       
        for x in assemlist:
            x = x + '\n'
            pragma.write(x)

        for x in flags.printregcontent:
            x = x + '\n'
            pragma.write(x)
        pragma.close()
		
    elif tuplelist[1] == 'ENDDECLARATIONS' and localvar == 0:
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")       
        assemlist.append('SECTION .text\n') 
        #print('SECTION .text\n')
	
    elif tuplelist[1] == 'MEMORY' and localvar == 0 and tuplelist[4] == 'INTEGER' :       #global  integer  , localvar is 0 for global

        bss.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")        
        flags.globalintegers.append(tuplelist[0])
        if tuplelist[2] == '1':                                                          #scalar
            instruction = tuplelist[0] + ':\tresd\t' + str(tuplelist[2])
        elif tuplelist[3] == '-':                                                
            instruction = tuplelist[0] + ':\tresd\t' + str(int(tuplelist[2]))   
        else:                                                                           #vector
            instruction = tuplelist[0]+':\tresd\t'+str(int(tuplelist[2])*int(tuplelist[3]))
                
        flags.global_list.append(tuplelist[0])
        bss.append(instruction)
        #print(instruction)
		
    elif tuplelist[1] == 'MEMORY' and localvar == 1 and tuplelist[4] == 'INTEGER':    #local integer , localvar is 1 for local
        bss.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")      
        flags.localintegers.append(tuplelist[0])
        k=0
        if tuplelist[2] == '1':                    
            foundreg = findreg(tuplelist[0], '0123')      #find an empty register and assign dummy value
            remove(tuplelist[0],'')               #clear the dummy value in the register assigned above
            findreg(tuplelist[0],foundreg)               
            flags.local_list.append(tuplelist[0])
                    

	
    elif tuplelist[1] == 'MEMORY' and localvar == 0 and tuplelist[4] == 'REAL':      #global REAL
        flags.globalreal.append(tuplelist[0])
        if tuplelist[2] == '1':
             flags.global_list.append(tuplelist[0])
             flags.realnos.append(tuplelist[0])
		
    elif tuplelist[1] == 'ENDPROCEDURE':
		
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")     
        regclear()
        instruction = 'mov esp, ebp\npop dword ebp'
        assemlist.append(instruction)
       # print(instruction) 
        instruction = 'ret'
        assemlist.append(instruction)
       # print(instruction)
        
    elif tuplelist[1] == 'BEGINPROCEDURE':
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")     
        regclear()
        instruction = tuplelist[2] + ':\t'
        assemlist.append(instruction)
        #print(instruction)
        instruction = 'push ebp\nmov ebp, esp'
        assemlist.append(instruction)
        #print(instruction)
		 
    elif tuplelist[1] == 'LABEL':
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")       
        if tuplelist[0] == 'MAIN':
            instruction = tuplelist[0].lower() + ':\t'
            assemlist.append(instruction)
            #print(instruction)
            instruction = 'push ebp\nmov ebp, esp' 
            assemlist.append(instruction)
           # print(instruction)
        else:
            instruction = tuplelist[0] + ':\t'
            assemlist.append(instruction)
           # print(instruction)

		
    elif tuplelist[1] == 'JUMP':
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        instruction = 'jmp\t'+tuplelist[0]
        assemlist.append(instruction)
       # print(instruction)


    elif tuplelist[1] == 'SUBSTORE' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        search(tuplelist[0])
        move(tuplelist[0],tuplelist[2],tuplelist[3])
        output = regex.findall(str(tuplelist[2]))
        if output[0][2] != '' :
            remove(tuplelist[2],'')
        output = regex.findall(str(tuplelist[3]))
        if output[0][2] != '' :
            remove(tuplelist[3],'')


    elif tuplelist[1] == 'STORE':
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")") 
        if tuplelist[4] == 'REAL':
            tuplelist[2] = str(tuplelist[2])
            if tuplelist[2][1] == '$':
                
              #  print('real')
                search(str(tuplelist[0]))
                global var1
                global var2
                global operation
                if operation == 'realaddition' :
                    real_addition(str(var1),str(var2),str(tuplelist[0]))
                elif operation == 'realsubtraction' :
                    real_subtraction(str(var1),str(var2),str(tuplelist[0]))
                output = regex.findall(str(tuplelist[2]))
                if output[0][2] != '' :
                    remove(tuplelist[2],'')
            else:
                search(tuplelist[0])
                if tuplelist[0] in flags.realnos :
                    instruction = tuplelist[0]+':\t dd\t'+tuplelist[2] + '\n'
                    flags.datasection.append(instruction)
                    for index in range(len(flags.realnos)) :
                        if flags.realnos[index] == tuplelist[0] :
                            index1 = index
                    flags.realnos.pop(index1)
                output = regex.findall(tuplelist[2])
                if output[0][2] != '' :
                    remove(tuplelist[2],'')


        elif tuplelist[4] == 'INTEGER':
            search(tuplelist[0])
            move(tuplelist[0],tuplelist[2],tuplelist[3])
            output = regex.findall(str(tuplelist[2]))
            if output[0][2] != '' :
                remove(tuplelist[2],'')
   

                    
    elif tuplelist[1] == 'CALLPROCEDURE' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        if tuplelist[0] == 'printf' :
            flags.printf_flag  = 1
               		 

    elif tuplelist[1] == 'VALUEACTUALPARAMETER' and tuplelist[0] == '#'  :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        if tuplelist[2] != '" "' and flags.printf_flag == 1 :
            if tuplelist[3] != '-':
                printarray(tuplelist[2],str(tuplelist[3]))
            elif tuplelist[3] == '-':
                printvar(tuplelist[2])
        flags.printf_flag = 0        

		 
    elif tuplelist[1] == 'SUBLOAD' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        if tuplelist[4] == 'INTEGER':
            search(tuplelist[0])
            sub_load_red(tuplelist[2],tuplelist[3])
            gen_final_instruction(tuplelist[0])
            output = regex.findall(str(tuplelist[2]))
            if output[0][2] != '' :
               # print('output',output[0][2][2])
                remove(tuplelist[2],'')
            output = regex.findall(str(tuplelist[3]))
            if output[0][2] != '' :
                if output[0][2][1] == '$' :
                 #   print('output',output[0][2][1])
                    remove(tuplelist[3],'')		 

             
    elif tuplelist[1] == 'ILT' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        flags.condition = 'LT'
        compare(tuplelist[2],tuplelist[3])

                                                
    elif tuplelist[1] == 'IGT' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        flags.condition = 'GT'
        compare(tuplelist[2],tuplelist[3])
                                                
    elif tuplelist[1] == 'ILTEQ' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        flags.condition = 'LTEQ'
        compare(tuplelist[2],tuplelist[3])
                                                
    elif tuplelist[1] == 'IGTEQ' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        flags.condition = 'GTEQ'
        compare(tuplelist[2],tuplelist[3])                
                                
    elif tuplelist[1] == 'IEQ' :
        flags.condition = 'EQ'
        compare(tuplelist[2],tuplelist[3])
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
                                                
    elif tuplelist[1] == 'INOTEQ' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        flags.condition = 'NOTEQ'
        compare(tuplelist[2],tuplelist[3])
        
        
    elif tuplelist[1] == 'CJUMPT':
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        if flags.condition == 'LT' :
            instruction = 'jl\t'+tuplelist[0]
            assemlist.append(instruction)
           # print(instruction)
        elif flags.condition == 'GT' :
            instruction = 'jg\t'+tuplelist[0]
            assemlist.append(instruction)
           # print(instruction)
        elif flags.condition == 'LTEQ' :
            instruction = 'jle\t'+tuplelist[0]
            assemlist.append(instruction)
            #print(instruction)
        elif flags.condition == 'GTEQ' :
            instruction = 'jge\t'+tuplelist[0]
            assemlist.append(instruction)
           # print(instruction)
        elif flags.condition == 'EQ' :
            instruction = 'je\t'+tuplelist[0]
            assemlist.append(instruction)
            #print(instruction)
        elif flags.condition == 'NOTEQ' :
            instruction = 'jne\t'+tuplelist[0]
            assemlist.append(instruction)
           # print(instruction)	

    elif tuplelist[1] == 'CJUMPF' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        if flags.condition == 'LT' :
            instruction = 'jge\t'+tuplelist[0]
            assemlist.append(instruction)
            #print(instruction)
        elif flags.condition == 'GT' :
            instruction = 'jle\t'+tuplelist[0]
            assemlist.append(instruction)
            #print(instruction)
        elif flags.condition == 'LTEQ' :
            instruction = 'jg\t'+tuplelist[0]
            assemlist.append(instruction)
            #print(instruction)
        elif flags.condition == 'GTEQ' :
            instruction = 'jl\t'+tuplelist[0]
            assemlist.append(instruction)
           # print(instruction)
        elif flags.condition == 'EQ' :
            instruction = 'jne\t'+tuplelist[0]
            assemlist.append(instruction)
           # print(instruction)
        elif flags.condition == 'NOTEQ' :
            instruction = 'je\t'+tuplelist[0]
            assemlist.append(instruction)
           # print(instruction)		 
                    
    elif tuplelist[1] == 'IADD' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        search(tuplelist[0])
        addition(tuplelist[2],tuplelist[3])
        gen_final_instruction(tuplelist[0])
        output = regex.findall(tuplelist[2])
        if output[0][2] != '' :
            remove(tuplelist[2],'')
        output = regex.findall(str(tuplelist[3]))
        if output[0][2] != '' :
            remove(tuplelist[3],'')
                    
    elif tuplelist[1] == 'INCREMENT' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        search(tuplelist[0])
        addition(tuplelist[0],tuplelist[2])
        gen_final_instruction(tuplelist[0])
        output = regex.findall(tuplelist[2])
        if output[0][2] != '' :
            remove(list1[2],'')


    elif tuplelist[1] == 'VALUE' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        foundreg = findreg(tuplelist[0],'0123')
        remove(tuplelist[0],'')
        findreg(tuplelist[0],foundreg)
        flags.local_list.append(tuplelist[0])


    elif tuplelist[1] == 'PROCCALL' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        instruction ='call\t'+ tuplelist[0]
        assemlist.append(instruction)
       # print(instruction)

                
    elif tuplelist[1] == 'REFERENCE' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        output = regex.findall(str(tuplelist[0]))
        if output[0][2] != '' :
            remove(tuplelist[0],'')


    elif tuplelist[1] == 'IMINUS' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        search(tuplelist[0])
        subtraction(tuplelist[2],tuplelist[3])
        gen_final_instruction(tuplelist[0])
        output = regex.findall(str(tuplelist[2]))
        if output[0][2] != '' :
            remove(tuplelist[2],'')
        output = regex.findall(tuplelist[3])
        if output[0][2] != '' :
            remove(tuplelist[3],'')


    elif tuplelist[1] == 'VALUEACTUALPARAMETER':
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        flags.print_counter = flags.print_counter + 1
	flags.datasection.append("stmt"+str(flags.print_counter)+":\t"+"db\t"+str(tuplelist[2])+",10,0\n");

    elif tuplelist[1] == 'FLAG':
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")

    elif tuplelist[1] == 'RMINUS' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        search(tuplelist[0])
        global var1
        global var2
        global operation
        operation = 'realsubtraction'
        var1 = tuplelist[2]
        var2 = tuplelist[3]
        output = regex.findall(tuplelist[2])
        if output[0][2] != '' :
            remove(tuplelist[2],'')
        output = regex.findall(tuplelist[3])
        if output[0][2] != '' :
            remove(tuplelist[3],'')

    elif tuplelist[1] == 'RADD' :
        assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")")
        search(tuplelist[0])
        global var1
        global var2
        global operation
        operation = 'realaddition'
        var1 = tuplelist[2]
        var2 = tuplelist[3]
        output = regex.findall(tuplelist[2])
        if output[0][2] != '' :
            remove(tuplelist[2],'')
        output = regex.findall(tuplelist[3])
        if output[0][2] != '' :
            remove(tuplelist[3],'')

    elif tuplelist[1] == "BEGINACTUALPARAMETERLIST":
	assemlist.append(";("+str(tuplelist[0])+","+str(tuplelist[1])+","+str(tuplelist[2])+","+str(tuplelist[3])+")") 

