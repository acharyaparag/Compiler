import flags
from sys import stdout
from time import sleep
from dict import*
from pragmatics import*


def printlist(list1):
    print "("
    
    for i in range(0,len(list1)):
        if(i==(len(list1)-1)):
            stdout.write(str(list1[i]))
        else:
            stdout.write(str(list1[i]) + ", ")

    stdout.write("\n")
        
    print ")"
    
def searchglobal(x):
    found = 0
    k = len(flags.global_symbol_table)-1
    while k>=0:
        if flags.global_symbol_table[k][0] == x:
            found = 1
            break
        else:
            k = k - 1
    return found

def searchlocal(x):
    found = 0;
    k = len(flags.local_symbol_table)-1
    while k>=0:
        if flags.local_symbol_table[k][0] == x:
            found=1
            break
        else:
            k = k - 1
    return found

def indexglobal(x):

    k = len(flags.global_symbol_table)-1
    while k>=0:
        if flags.global_symbol_table[k][0] == x:
            break
        else:
            k = k - 1
    return k

def indexlocal(x):

    k = len(flags.local_symbol_table)-1
    while k>=0:
        if flags.local_symbol_table[k][0] == x:
            break
        else:
            k = k - 1
    return k

             

def printlocalsymboltable():
    print "Local Symbol Table Entry"
    print ("Name: " + flags.local_symbol_table[-1][0] + " Type: " + flags.local_symbol_table[-1][1] + " Shape: " + flags.local_symbol_table[-1][2] + " : "+
    flags.local_symbol_table[-1][3] + " Columns: " + flags.local_symbol_table[-1][4] + " Call Type: " + flags.local_symbol_table[-1][5])
    print " "
    
def printglobalsymboltable():
    print "Global Symbol Table Entry"
    print ("Name: " + flags.global_symbol_table[-1][0] + " Type: " + flags.global_symbol_table[-1][1] + " Shape: " + flags.global_symbol_table[-1][2] + " Rows: "+
    flags.global_symbol_table[-1][3] + " Columns: " + flags.global_symbol_table[-1][4] + " Call Type: " + flags.global_symbol_table[-1][5])
    print " "

    
def poplist(i):
    k = 1                                                        #After Reduction 
    while k<=i:
        flags.semantic_stack.pop()
        flags.print_semantic_stack.pop()
        k = k + 1



def semantic_fun(red_no):
    
    if red_no == 2:
        flags.semantic_stack.append("-")                                  #Before Reduction
        flags.semantic_stack.append(len(flags.original_identifier)-1)     #Appending the top element index of original identifier

        flags.print_semantic_stack.append("-")                             #Load semantic stack for printing      
        flags.print_semantic_stack.append(flags.original_identifier[-1])

        if flags.flag[12] == 1:
            print "Semantic Stack before reduction:"
            printlist(flags.print_semantic_stack)
        
        poplist(2)
        
        flags.semantic_stack.append(len(flags.original_identifier)-1)
        flags.print_semantic_stack.append(flags.original_identifier[-1])
        flags.semantic_type.append('A')

        if flags.flag[12] == 1:
            print "Semantic Stack after reduction:"
            printlist(flags.print_semantic_stack)
                
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + flags.original_identifier[flags.semantic_stack[-1]] + "," + "BEGINPROGRAM" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append(flags.original_identifier[flags.semantic_stack[-1]])
        temp_tuples.append("BEGINPROGRAM")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")        
        
        flags.tuples.append(temp_tuples)

        localvar = 0
        pragmatic(temp_tuples, localvar)

        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)
     	    temp_tuples = []
     	    temp_tuples.append("20")
      	    temp_tuples.append("FLAG")
      	    temp_tuples.append("-")
      	    temp_tuples.append("-")
      	    temp_tuples.append("-") 
       	    localvar = 0
      	    pragmatic(temp_tuples, localvar)

                
    if red_no == 1:
        k = len(flags.syntax_stack)-1
        while k>=0:                                                                        #find the latest "prog" index in the syntax stack                 
            if flags.syntax_stack[k] == 2:
                break
            else:
                k = k - 1
        k = k-1
        while k>=0:                                                                        #find the second latest "prog" index in the syntax stack                 
            if flags.syntax_stack[k] == 2:
                break
            else:
                k = k - 1
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.semantic_stack.append("-")
        flags.semantic_stack.append("-")

        name = flags.original_identifier[flags.semantic_stack[-3]]

        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-3]])                        # load semantic stack for printing
        flags.print_semantic_stack.append("-")
        flags.print_semantic_stack.append("-")

        if flags.flag[12] == 1:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
      
        poplist(3)
            
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append("-")
        flags.semantic_type.append('D')        

        if flags.flag[12] == 1:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
 
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is(" + name + "," + "ENDPROGRAM" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append(name)
        temp_tuples.append("ENDPROGRAM")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-") 
        flags.tuples.append(temp_tuples)
        

        if flags.flag[16]:
            print "GLOBAL SYMBOL TABLE"
            for m in range(0,len(flags.global_symbol_table)):
                print ("Name: " + flags.global_symbol_table[m][0] + " Type: " + flags.global_symbol_table[m][1] + " Shape: " + flags.global_symbol_table[m][2] +
                       " Rows: " + flags.global_symbol_table[m][3] + " Columns: " + flags.global_symbol_table[m][4] + " Call Type: " + flags.global_symbol_table[m][5])

        localvar = 0
        pragmatic(temp_tuples, localvar)

        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)
     	    temp_tuples = []
     	    temp_tuples.append("20")
      	    temp_tuples.append("FLAG")
      	    temp_tuples.append("-")
      	    temp_tuples.append("-")
      	    temp_tuples.append("-") 
       	    localvar = 0
      	    pragmatic(temp_tuples, localvar)


    if red_no == 5:
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ "-" + "," + "ENDDECLARATIONS" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)            

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("ENDDECLARATIONS")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-") 
        flags.tuples.append(temp_tuples)
        
        if flags.flag[12]:    
            print" No change in Semantic change"    
            print "Semantic stack after/before reduction:"
            printlist(flags.print_semantic_stack)

        localvar = flags.procedure_start
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)
     	    temp_tuples = []
     	    temp_tuples.append("20")
      	    temp_tuples.append("FLAG")
      	    temp_tuples.append("-")
      	    temp_tuples.append("-")
      	    temp_tuples.append("-") 
       	    localvar = 0
      	    pragmatic(temp_tuples, localvar)
                       

    if red_no == 10:
        if flags.procedure_start == 1:
            temp = len(flags.local_symbol_table)-1
            flags.print_semantic_stack.append(flags.local_symbol_table[temp][0])                  # Load print_semantic_stack for printing
        else:
            temp = len(flags.global_symbol_table)-1
            flags.print_semantic_stack.append(flags.global_symbol_table[temp][0])
            
            
        flags.semantic_stack.append(temp)                          # Appending the index of the last symbol table element(local or global)
        flags.semantic_stack.append("-")
        flags.semantic_stack.append(len(flags.original_identifier)-1)

                  
        flags.print_semantic_stack.append("-")                      
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)            

        temp_list = []
        if flags.procedure_start == 1:
            temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])         # Si variable
            temp_list.append(flags.local_symbol_table[temp][1])                           # type at S.T location temp
            temp_list.append(flags.local_symbol_table[temp][2])                           # shape SCALAR
            temp_list.append(flags.local_symbol_table[temp][3])                           # SIZE is 1 
            temp_list.append(flags.local_symbol_table[temp][4])                           # Columns 
            temp_list.append(flags.local_symbol_table[temp][5])                           # Call type
        else:
            temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
            temp_list.append(flags.global_symbol_table[temp][1])                           # type at S.T location temp
            temp_list.append(flags.global_symbol_table[temp][2])                           # shape SCALAR
            temp_list.append(flags.global_symbol_table[temp][3])                           # SIZE is 1 
            temp_list.append(flags.global_symbol_table[temp][4])                           # Columns 
            temp_list.append(flags.global_symbol_table[temp][5])                           # Call type

        if flags.procedure_start == 1:
            if(int(searchlocal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in local symbol table"
            else:
                flags.local_symbol_table.append(temp_list)
                if flags.flag[15]:
                    printlocalsymboltable()
                    
        else:
            if(int(searchglobal(temp_list[0])) == 1):
                print "Symbol " + temp_list[0] + " already exists in global symbol table"
            else:
                flags.global_symbol_table.append(temp_list)
                if flags.flag[15]:
                    printglobalsymboltable()
                    
        poplist(3)
             

        
        if flags.procedure_start == 1:
            flags.print_semantic_stack.append(flags.local_symbol_table[-1][0])                  # Load print_semantic_stack for printing after reduction
            flags.semantic_stack.append(len(flags.local_symbol_table)-1)                            #Appending the index of last element in local symbol table            
            flags.semantic_type.append('LST')
        else:
            flags.print_semantic_stack.append(flags.global_symbol_table[-1][0])        
            flags.semantic_stack.append(len(flags.global_symbol_table)-1)                            #Appending the index of last element in symbol table               
            flags.semantic_type.append('GST')        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
            
        if flags.procedure_start == 1:
            if flags.flag[13]:
                prntstr= "                                       Tuple is  ("+ flags.local_symbol_table[-1][0] + "," + "MEMORY" + "," + flags.local_symbol_table[-1][3] + ","+ "-" + ")"
                print str(prntstr)
            temp_tuples = []
            temp_tuples.append(flags.local_symbol_table[-1][0])
            temp_tuples.append("MEMORY")
            temp_tuples.append(flags.local_symbol_table[-1][3])
            temp_tuples.append("-")
            temp_tuples.append(flags.local_symbol_table[-1][1])
            flags.tuples.append(temp_tuples)
            localvar = 1
            pragmatic(temp_tuples, localvar)
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

                pragmatic(temp_tuples, localvar)
        else:
            if flags.flag[13]:
                prntstr= "                                       Tuple is  ("+ flags.global_symbol_table[-1][0] + "," + "MEMORY" + "," + flags.global_symbol_table[-1][3] + ","+ "-" + ")"
                print str(prntstr)
            temp_tuples = []
            temp_tuples.append(flags.global_symbol_table[-1][0])
            temp_tuples.append("MEMORY")
            temp_tuples.append(flags.global_symbol_table[-1][3])
            temp_tuples.append("-")
            temp_tuples.append(flags.global_symbol_table[-1][1])
            flags.tuples.append(temp_tuples)
            localvar = 0
            pragmatic(temp_tuples, localvar)
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

                pragmatic(temp_tuples, localvar)


    if red_no == 11:
        flags.semantic_stack.append(flags.original_reserve[-2])                  #Before Reduction   Appending the second last element of original_reserve (REAL/INTEGER)
        flags.semantic_stack.append("-")                                         #SCALAR 
        flags.semantic_stack.append(len(flags.original_identifier)-1)            #Appending the last element index of original_identifier  (var)

        flags.print_semantic_stack.append(flags.semantic_stack[-3])               # Load print_semantic_stack for printing
        flags.print_semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.original_identifier[-1])
        
       
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)      

        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append(flags.semantic_stack[-3])                                     # type at Si - 2
        temp_list.append("SCALAR")                                                     # shape SCALAR
        temp_list.append("1")                                                          # SIZE is 1 
        temp_list.append("-")                                                          # Columns 
        temp_list.append("-")                                                          # Call type

        if flags.procedure_start == 1:
            if(int(searchlocal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in local symbol table"
            else:
                flags.local_symbol_table.append(temp_list)
                if flags.flag[15]:
                    printlocalsymboltable()
        else:
            if(int(searchglobal(temp_list[0])) == 1):
                print "Symbol " + temp_list[0] + " already exists in global symbol table"
            else:
                flags.global_symbol_table.append(temp_list)
                if flags.flag[15]:
                    printglobalsymboltable()            
                    

        poplist(3)


        if flags.procedure_start == 1:
            print "HI"
            flags.semantic_stack.append(len(flags.local_symbol_table)-1)                   #Appending the last element local_symbol_table index   
            flags.print_semantic_stack.append(flags.local_symbol_table[-1][0])
            flags.semantic_type.append('LST')            
            if flags.flag[13]:
                prntstr= "                                       Tuple is (" + flags.local_symbol_table[-1][0] + "," + "MEMORY" + "," + "1" + ","+ "-" + ")"
                print str(prntstr)

            temp_tuples = []
            temp_tuples.append(flags.local_symbol_table[-1][0])
            temp_tuples.append("MEMORY")
            temp_tuples.append("1")
            temp_tuples.append("-")
            temp_tuples.append(flags.local_symbol_table[-1][1])
            flags.tuples.append(temp_tuples)                           
            localvar = 1
          #  print "temptuple" , localvar
           # for k in range(0,len(temp_tuples)):
              #  print temp_tuples[k] + " "
                           
            pragmatic(temp_tuples, localvar)
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

                pragmatic(temp_tuples, localvar)
        else:
            flags.semantic_stack.append(len(flags.global_symbol_table)-1)                   #Appending the last element global_symbol_table index   
            flags.print_semantic_stack.append(flags.global_symbol_table[-1][0])
            flags.semantic_type.append('GST')
            if flags.flag[13]:
                prntstr= "                                       Tuple is  ("+ flags.global_symbol_table[-1][0] + "," + "MEMORY" + "," + "1" + ","+ "-" + ")"
                print str(prntstr)

            temp_tuples = []
            temp_tuples.append(flags.global_symbol_table[-1][0])
            temp_tuples.append("MEMORY")
            temp_tuples.append("1")
            temp_tuples.append("-")
            temp_tuples.append(flags.global_symbol_table[-1][1])
            flags.tuples.append(temp_tuples)
            localvar = 0
            pragmatic(temp_tuples, localvar)
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

                pragmatic(temp_tuples, localvar)
 
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
                


    if red_no == 12:
        flags.semantic_stack.append(flags.original_reserve[-2])                  #Before Reduction   Appending the second last element of original_reserve (REAL/INTEGER)
        flags.semantic_stack.append("-")                                         #VECTOR 
        flags.semantic_stack.append(len(flags.original_integer)-1)                    #Appending the last element index of original_integer  (integer)
        flags.semantic_stack.append(len(flags.original_identifier)-1)                 #Appending the last element index of original_identifier  (var)

        flags.print_semantic_stack.append(flags.semantic_stack[-4])                # Load print_semantic_stack for printing semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-3])              
        flags.print_semantic_stack.append( flags.original_integer[flags.semantic_stack[-2]])
        flags.print_semantic_stack.append( flags.original_identifier[flags.semantic_stack[-1]]) 

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)                            

        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append(flags.semantic_stack[-4])                                     # type at Si - 3
        temp_list.append("VECTOR")                                                     # shape VECTOR
        temp_list.append(flags.original_integer[flags.semantic_stack[-2]])             # SIZE at Si-1
        temp_list.append("-")                                                          # Columns 
        temp_list.append("-")                                                          # Call type

        if flags.procedure_start == 1:
            if(int(searchlocal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in local symbol table"
            else:
                flags.local_symbol_table.append(temp_list)
                if flags.flag[15]:
                    printlocalsymboltable()
        else:
            if(int(searchglobal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in global symbol table"
            else:
                flags.global_symbol_table.append(temp_list)
                if flags.flag[15]:
                    printglobalsymboltable()

        poplist(4)

        if flags.procedure_start == 1:
            flags.semantic_stack.append(len(flags.local_symbol_table)-1)                   #Appending the last element local_symbol_table index
            flags.print_semantic_stack.append(flags.local_symbol_table[-1][0])
            flags.semantic_type.append('LST')            
            if flags.flag[13]:
                prntstr= "                                       Tuple is  ("+ flags.local_symbol_table[-1][0] + "," + "MEMORY" + "," + flags.local_symbol_table[-1][3] + ","+ "-" + ")"
                print str(prntstr)

            temp_tuples = []
            temp_tuples.append(flags.local_symbol_table[-1][0])
            temp_tuples.append("MEMORY")
            temp_tuples.append(flags.local_symbol_table[-1][3])
            temp_tuples.append("-")
            temp_tuples.append(flags.local_symbol_table[-1][1])
            flags.tuples.append(temp_tuples)
            localvar = 1
            pragmatic(temp_tuples, localvar)  
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

                pragmatic(temp_tuples, localvar) 
        else:
            flags.semantic_stack.append(len(flags.global_symbol_table)-1)                   #Appending the last element global_symbol_table index
            flags.print_semantic_stack.append(flags.global_symbol_table[-1][0])
            flags.semantic_type.append('GST')            
            if flags.flag[13]:
                prntstr= "                                       Tuple is  ("+ flags.global_symbol_table[-1][0] + "," + "MEMORY" + "," + flags.global_symbol_table[-1][3] + ","+ "-" + ")"
                print str(prntstr)

            temp_tuples = []
            temp_tuples.append(flags.global_symbol_table[-1][0])
            temp_tuples.append("MEMORY")
            temp_tuples.append(flags.global_symbol_table[-1][3])
            temp_tuples.append("-")
            temp_tuples.append(flags.global_symbol_table[-1][1])
            flags.tuples.append(temp_tuples)
            localvar = 0
            pragmatic(temp_tuples, localvar)              
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

      	        pragmatic(temp_tuples, localvar)
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

      
        

    if red_no == 13:
        flags.semantic_stack.append(flags.original_reserve[-2])                    #Before Reduction   Appending the second last element of original_reserve(INTEGER/REAL)
        flags.semantic_stack.append("-")                                              # MATRIX
        flags.semantic_stack.append(len(flags.original_integer)-2)                    #Appending the second last element index of original_integer  (integer)
        flags.semantic_stack.append("-")                                              #:: 
        flags.semantic_stack.append(len(flags.original_integer)-1)                    #Appending the last element index of original_integer         (integer)
        flags.semantic_stack.append(len(flags.original_identifier)-1)                 #Appending the last element index of original_identifier       (var)

        flags.print_semantic_stack.append(flags.semantic_stack[-6])                   # Load print_semantic_stack for printing semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-5])             
        flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-4]])             
        flags.print_semantic_stack.append(flags.semantic_stack[-3])           
        flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-2]])
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]]) 
                                               
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
                
        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append(flags.semantic_stack[-6])                                     # type at Si - 5 
        temp_list.append("MATRIX")                                                     # shape MATRIX
        temp_list.append(flags.original_integer[flags.semantic_stack[-4]])             # Rows at Si-3
        temp_list.append(flags.original_integer[flags.semantic_stack[-2]])             # Columns at Si- 1
        temp_list.append("-")                                                          # Call type


        if flags.procedure_start == 1:
            if(int(searchlocal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in local symbol table"
            else:
                flags.local_symbol_table.append(temp_list)
                if flags.flag[15]:
                    printlocalsymboltable()


        else:
            if(int(searchglobal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in global symbol table"
            else:
                flags.global_symbol_table.append(temp_list)
                if flags.flag[15]:
                    printglobalsymboltable()
                    
        poplist(6)
             
        if flags.procedure_start == 1:
            flags.semantic_stack.append(len(flags.local_symbol_table)-1)                   #Appending the last element local_symbol_table index
            flags.print_semantic_stack.append(flags.local_symbol_table[-1][0])
            flags.semantic_type.append('LST')            
            if flags.flag[13]:
                prntstr= "                                       Tuple is  ("+ flags.local_symbol_table[-1][0] + "," + "MEMORY" + "," + flags.local_symbol_table[-1][3] + ","+ flags.local_symbol_table[-1][4] + ")"
                print str(prntstr)

            temp_tuples = []
            temp_tuples.append(flags.local_symbol_table[-1][0])
            temp_tuples.append("MEMORY")
            temp_tuples.append(flags.local_symbol_table[-1][3])
            temp_tuples.append(flags.local_symbol_table[-1][4])
            temp_tuples.append(flags.local_symbol_table[-1][1])
            flags.tuples.append(temp_tuples)
            localvar = 1
            pragmatic(temp_tuples, localvar)
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

                pragmatic(temp_tuples, localvar)            
        else:
            flags.semantic_stack.append(len(flags.global_symbol_table)-1)                   #Appending the last element global_symbol_table index   
            flags.print_semantic_stack.append(flags.global_symbol_table[-1][0])
            flags.semantic_type.append('GST')            
            if flags.flag[13]:
                prntstr= "                                       Tuple is (" + flags.global_symbol_table[-1][0] + "," + "MEMORY" + "," + flags.global_symbol_table[-1][3] + ","+ flags.global_symbol_table[-1][4] + ")"
                print str(prntstr)

            temp_tuples = []
            temp_tuples.append(flags.global_symbol_table[-1][0])
            temp_tuples.append("MEMORY")
            temp_tuples.append(flags.global_symbol_table[-1][3])
            temp_tuples.append(flags.global_symbol_table[-1][4])
            temp_tuples.append(flags.global_symbol_table[-1][1])    
            flags.tuples.append(temp_tuples)
            localvar = 0
            pragmatic(temp_tuples, localvar)
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

                pragmatic(temp_tuples, localvar)
            
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
            
 
        

    if red_no == 15:
        flags.semantic_stack.append("-")                                            #Before Reduction
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
        flags.semantic_stack.pop()
        flags.print_semantic_stack.pop()
        
        flags.semantic_stack.append(get_value(reservedt,flags.syntax_stack[-1]))                         # REAL is taken from syntax stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('V')        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)  



        
    if red_no == 14:
        flags.semantic_stack.append("-")                                            #Before Reduction
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)          
        
        flags.semantic_stack.pop()
        flags.print_semantic_stack.pop()
        
        flags.semantic_stack.append(get_value(reservedt,flags.syntax_stack[-1]))                         # INTEGER is taken from syntax stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('V')    

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
            


    if red_no == 19:
        k = len(flags.syntax_stack)-1
        while k>=0:                                                                        #find the latest "procname" index in the syntax stack                 
            if flags.syntax_stack[k] == 14:
                break
            else:
                k = k - 1
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.semantic_stack.append("-")
        flags.semantic_stack.append("-")
        flags.semantic_stack.append("-")
 
       
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-4])])   # Load print_semantic_stack for printing semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-3])
        flags.print_semantic_stack.append(flags.semantic_stack[-2])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        name =  flags.original_identifier[int(flags.semantic_stack[-4])]

        poplist(4)
             
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')                                          
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                                          

        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" + "-" + "," + "ENDPROCEDURE" + "," + name + "," + "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("ENDPROCEDURE")
        temp_tuples.append(name)
        temp_tuples.append("-")
        temp_tuples.append("-")     
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        if flags.flag[14]:
            print
            print "LOCAL SYMBOL TABLE"
            for m in range(0,len(flags.local_symbol_table)):
                print ("Name: " + flags.local_symbol_table[m][0] + " Type: " + flags.local_symbol_table[m][1] + " Shape: " + flags.local_symbol_table[m][2] +
                       " Rows: " + flags.local_symbol_table[m][3] + " Columns: " + flags.local_symbol_table[m][4] + " Call Type: " + flags.local_symbol_table[m][5])
        print " "
        flags.local_symbol_table = []
        flags.procedure_start = 0
        flags.used_list = []
        flags.used_flag = 0
            



    if red_no == 20:
        k = len(flags.syntax_stack)-1
        while k>=0:                                                                        #find the latest "procname" index in the syntax stack                 
            if flags.syntax_stack[k] == 14:
                break
            else:
                k = k - 1
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.semantic_stack.append("-")
        flags.semantic_stack.append("-")

        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-3]])   # load print_semantic_stack for printing semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-2])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
                
        name = flags.original_identifier[flags.semantic_stack[-3]]

        poplist(3)

             
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ "-" + "," + "ENDPROCEDURE" + "," + name + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("ENDPROCEDURE")
        temp_tuples.append(name)
        temp_tuples.append("-")
        temp_tuples.append("-")  
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        if flags.flag[14]:
            print "LOCAL SYMBOL TABLE"
            for m in range(0,len(flags.local_symbol_table)):
                print ("Name: " + flags.local_symbol_table[m][0] + " Type: " + flags.local_symbol_table[m][1] + " Shape: " + flags.local_symbol_table[m][2] +
                      " Rows: " + flags.local_symbol_table[m][3] + " Columns: " + flags.local_symbol_table[m][4] + " Call Type: " + flags.local_symbol_table[m][5])
        print " "
        flags.local_symbol_table = []
        flags.procedure_start = 0
        flags.used_list = []
        flags.used_flag = 0

            

    if red_no == 23:
        flags.procedure_start = 1
        flags.semantic_stack.append("-")
        flags.semantic_stack.append(len(flags.original_identifier)-1)      # Appending the last element index of original_identifier  (var)

        flags.print_semantic_stack.append(flags.semantic_stack[-2])        # loading print_semantic_stack
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append("PROCEDURE")                                                  # type PROCEDURE
        temp_list.append("-")                                                          # Shape 
        temp_list.append("-")                                                          # Rows
        temp_list.append("-")                                                          # Columns 
        temp_list.append("-")                                                          # Call type
       
        if(int(searchlocal(temp_list[0])) == 1):
            print "Symbol " + temp_list[0] + " already exists in local symbol table"
        else:
            flags.local_symbol_table.append(temp_list)
            if flags.flag[15]:
                printlocalsymboltable()
                    
      
        if(int(searchglobal(temp_list[0])) == 1):
            print "Symbol " + temp_list[0] + " already exists in global symbol table"
        else:
            flags.global_symbol_table.append(temp_list)
            if flags.flag[15]:
                printglobalsymboltable()

        poplist(2)

        flags.semantic_stack.append(len(flags.original_identifier)-1)                   #Storing the procedure name index
        flags.print_semantic_stack.append(flags.semantic_stack[-1])                 
        flags.semantic_type.append('A')        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "BEGINPROCEDURE" + "," + flags.original_identifier[flags.semantic_stack[-1]] + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("BEGINPROCEDURE")
        temp_tuples.append(flags.original_identifier[flags.semantic_stack[-1]])
        temp_tuples.append("-")
        temp_tuples.append("-")  
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)        
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
        

    if red_no == 24:
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "NOFORMALPARAMETERLIST" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("NOFORMALPARAMETERLIST")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")          
        flags.tuples.append(temp_tuples)
   
        if flags.flag[12]:
            print " No change in semantic stack"
            print "Semantic stack after/before reduction:"
            printlist(flags.print_semantic_stack)           
        localvar = 0
        pragmatic(temp_tuples, localvar)        
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

    if red_no == 25:
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "ENDFORMALPARAMETERLIST" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("NOFORMALPARAMETERLIST")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")  
        flags.tuples.append(temp_tuples)
        
        if flags.flag[12]:
            print " No change in semantic stack"
            print "Semantic stack after/before reduction:"
            printlist(flags.print_semantic_stack)           
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

    if red_no == 26:

        k = len(flags.syntax_stack)-1
        while k>=0:                                                                        #find the latest "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
        k = k - 1        
        while k>=0:                                                                        #find the second last "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1       
    
        temp1 = k                                                                         # Search for the second last "callby"(18) in the syntax stack,take that index and 
                                                                                          # using that index get the corressponding value from the semantics stack 
                                                                                            
        k = len(flags.syntax_stack)-1                                                      #find the latest "type" index in the syntax stack 
        while k>=0:                                          
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
        k = k-1        
        while k>=0:                                          
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1         
        temp2 = k                                                                      # Search for the second last "type"(9) in the syntax stack,take that index and
                                                                                       # using that index get the corressponding value from the semantics stack 

        flags.semantic_stack.append("-")                                              # fparmlist-
        flags.semantic_stack.append("-")                                              # ,
        flags.semantic_stack.append(flags.semantic_stack[temp1])                                             # callby value taken from the syntax_stack
        flags.semantic_stack.append(flags.semantic_stack[temp2])                                             # type value taken from the syntax_stack
        flags.semantic_stack.append("-")                                              # SCALAR                                           
        flags.semantic_stack.append(len(flags.original_identifier)-1)                 #Appending the last element index of original_identifier      (var)

        flags.print_semantic_stack.append(flags.semantic_stack[-6])                                              # Loading print_semantic_stack
        flags.print_semantic_stack.append(flags.semantic_stack[-5])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-4])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-3])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-2])                                                                       
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                 

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack) 
                                        
        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append(flags.semantic_stack[-3])                                      # type at Si - 2
        temp_list.append("SCALAR")                                                     # shape SCALAR
        temp_list.append("1")                                                          # Size is 1
        temp_list.append("-")                                                          # Columns 
        temp_list.append(flags.semantic_stack[-4])                                     # calltype at Si-3

        if(int(searchlocal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in local symbol table"
        else:
            flags.local_symbol_table.append(temp_list)
            if flags.flag[15]:
                printlocalsymboltable()
            
        poplist(6)
             
        flags.semantic_stack.append("-")                   #Appending "-" in the semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')       
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
            
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ flags.local_symbol_table[-1][0] + "," + flags.local_symbol_table[-1][5] + "," + flags.local_symbol_table[-1][3] + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append(flags.local_symbol_table[-1][0])
        temp_tuples.append(flags.local_symbol_table[-1][5])
        temp_tuples.append(flags.local_symbol_table[-1][3])
        temp_tuples.append("-")
        temp_tuples.append(flags.local_symbol_table[-1][1])  
        flags.tuples.append(temp_tuples)
        localvar = 1
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

    if red_no == 27:
  
        k = len(flags.syntax_stack)-1
        while k>=0:
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
        k = k - 1        
        while k>=0:
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
        temp1 = k                                                                            # Search for the second latest callby in the syntax stack,take that index and 
                                                                                              #  using that index to get the value from the semantics stack
        k = len(flags.syntax_stack)-1
        while k>=0:
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
        k = k-1        
        while k>=0:
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
        temp2 = k                                                                            # Search for the second last type in the syntax stack,take that index and 
                                                                                             #  using that index to get the value from the semantics stack

        flags.semantic_stack.append("-")                                              #fparmlist-
        flags.semantic_stack.append("-")                                              # ,               
        flags.semantic_stack.append(flags.semantic_stack[temp1])                                            # callby value taken from syntax_stack
        flags.semantic_stack.append(flags.semantic_stack[temp2])                                            # type value taken from syntax_stack 
        flags.semantic_stack.append("-")                                              #VECTOR
        flags.semantic_stack.append(len(flags.original_integer)-1)                    #Appending the last element index of original_integer  (integer)                                              #:: 
        flags.semantic_stack.append(len(flags.original_identifier)-1)                 #Appending the last element index of original_identifier       (var)


        flags.print_semantic_stack.append(flags.semantic_stack[-7])                   # Loading print_semantic_stack
        flags.print_semantic_stack.append(flags.semantic_stack[-6])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-5])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-4])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-3])                                                                       
        flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-2]])
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
                                     
        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append(flags.semantic_stack[-4])                                      # type at Si - 3
        temp_list.append("VECTOR")                                                     # shape VECTOR
        temp_list.append(flags.original_integer[flags.semantic_stack[-2]])             # Size at Si-1
        temp_list.append("-")                                                          # Columns 
        temp_list.append(flags.semantic_stack[-5])                                     # calltype at Si-4


        if(int(searchlocal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in local symbol table"
        else:
            flags.local_symbol_table.append(temp_list)
            if flags.flag[15]:
                printlocalsymboltable()        
    
        poplist(7)
             
        flags.semantic_stack.append("-")                   #Appending - in the semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')       
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack) 
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ flags.local_symbol_table[-1][0] + "," + flags.local_symbol_table[-1][5] + "," + flags.local_symbol_table[-1][3] + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append(flags.local_symbol_table[-1][0])
        temp_tuples.append(flags.local_symbol_table[-1][5])
        temp_tuples.append(flags.local_symbol_table[-1][3])
        temp_tuples.append("-")
        temp_tuples.append(flags.local_symbol_table[-1][1])
        flags.tuples.append(temp_tuples)
        localvar = 1
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

    if red_no == 28:

        k = len(flags.syntax_stack)-1
        while k>=0:                                                                        #find the latest "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
        k = k - 1        
        while k>=0:                                                                        #find the second last "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1         
        temp1 = k                                                   # Search for the last "callby"(18) in the syntax stack,take that index and 
                                                                                          # using that index get the corressponding value from the semantics stack 
                                                                                            
        k = len(flags.syntax_stack)-1                                                      #find the latest "type" index in the syntax stack 
        while k>=0:                                          
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
        k = k - 1        
        while k>=0:                                                                                    
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1         
        temp2 = k                                                # Search for the last "type"(9) in the syntax stack,take that index and
                                                                                       # using that index get the corressponding value from the semantics stack 

        flags.semantic_stack.append("-")                                              # fparmlist-
        flags.semantic_stack.append("-")                                              # ,
        flags.semantic_stack.append(flags.semantic_stack[temp1])                                             # callby value taken from the syntax_stack
        flags.semantic_stack.append(flags.semantic_stack[temp2])                                             # type value taken from the syntax_stack
        flags.semantic_stack.append("-")                                              # MATRIX                                           
        flags.semantic_stack.append(len(flags.original_integer)-2)                    #Appending the second last element index of original_integer  (integer)
        flags.semantic_stack.append("-")                                              #:: 
        flags.semantic_stack.append(len(flags.original_integer)-1)                    #Appending the last element index of original_integer         (integer)
        flags.semantic_stack.append(len(flags.original_identifier)-1)                 #Appending the last element index of original_identifier       (var)

        flags.print_semantic_stack.append(flags.semantic_stack[-9])                   # Loading print_semantic_stack
        flags.print_semantic_stack.append(flags.semantic_stack[-8])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-7])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-6])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-5])                                                                       
        flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-4]])
        flags.print_semantic_stack.append(flags.semantic_stack[-3])                                    
        flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-2]])
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])

        
                                          

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
                                                                                  
        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append(flags.semantic_stack[-6])                                     # type at Si - 5 
        temp_list.append("MATRIX")                                                     # shape MATRIX
        temp_list.append(flags.original_integer[flags.semantic_stack[-4]])             # Rows at Si-3
        temp_list.append(flags.original_integer[flags.semantic_stack[-2]])             # Columns at Si- 1
        temp_list.append(flags.semantic_stack[-7])                                     # calltype at Si-6

        if(int(searchlocal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in local symbol table"
        else:
            flags.local_symbol_table.append(temp_list)
            if flags.flag[15]:
                printlocalsymboltable()
            
        poplist(9)
             
        flags.semantic_stack.append("-")                   #Appending "-" in the semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')    
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + flags.local_symbol_table[-1][0] + "," + flags.local_symbol_table[-1][5] + "," + flags.local_symbol_table[-1][3] + ","+ flags.local_symbol_table[-1][4] + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append(flags.local_symbol_table[-1][0])
        temp_tuples.append(flags.local_symbol_table[-1][5])
        temp_tuples.append(flags.local_symbol_table[-1][3])
        temp_tuples.append(flags.local_symbol_table[-1][4])
        temp_tuples.append(flags.local_symbol_table[-1][1])
        flags.tuples.append(temp_tuples)
        
        localvar = 1
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

    if red_no == 29:

        k = len(flags.syntax_stack)-1

        while k>=0:                                                                        #find the latest "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
        k = k-1 
        while k>=0:                                                                        #find the second last "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
                
       # temp1 = flags.semantic_stack[k]                                                   # Search for the last "callby"(18) in the syntax stack,take that index and 
        temp1 = k                                                                          # using that index get the corressponding value from the semantics stack 
                                                                                            
        k = len(flags.syntax_stack)-1                                                      #find the latest "type" index in the syntax stack 
        while k>=0:                                          
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
        k = k - 1
        while k>=0:                                                                          #find the second last "type" index in the syntax stack               
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
                
        temp2 = k                                                                      # Search for the last "type"(9) in the syntax stack,take that index and
                                                                                       # using that index get the corressponding value from the semantics stack 

        flags.semantic_stack.append("-")                                              # {
        flags.semantic_stack.append(flags.semantic_stack[temp1])                                             # callby value taken from the syntax_stack
        flags.semantic_stack.append(flags.semantic_stack[temp2])                                             # type value taken from the syntax_stack
        flags.semantic_stack.append("-")                                              # SCALAR                                           
        flags.semantic_stack.append(len(flags.original_identifier)-1)                 #Appending the last element index of original_identifier      (var)
        
        flags.print_semantic_stack.append(flags.semantic_stack[-5])                   # Loading print_semantic_stack
        flags.print_semantic_stack.append(flags.semantic_stack[-4])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-3])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-2])                                            
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                                                       

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)     
                                        
        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append(flags.semantic_stack[-3])                                      # type at Si - 2
        temp_list.append("SCALAR")                                                     # shape SCALAR
        temp_list.append("1")                                                          # Size is 1
        temp_list.append("-")                                                          # Columns 
        temp_list.append(flags.semantic_stack[-4])                                     # calltype at Si-3

        if(int(searchlocal(temp_list[0])) == 1):
            print "Symbol " + temp_list[0] + " already exists in local symbol table"
        else:
            flags.local_symbol_table.append(temp_list)
            if flags.flag[15]:
                printlocalsymboltable()
                
        poplist(5)
             
        flags.semantic_stack.append("-")                   #Appending "-" in the semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "BEGINFORMALPARAMETERLIST" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)
        
            prntstr= "                                           Tuple is (" + flags.local_symbol_table[-1][0] + "," + flags.local_symbol_table[-1][5] + "," + flags.local_symbol_table[-1][3] + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("BEGINFORMALPARAMETERLIST")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        temp_tuples = []
        temp_tuples.append(flags.local_symbol_table[-1][0])
        temp_tuples.append(flags.local_symbol_table[-1][5])
        temp_tuples.append(flags.local_symbol_table[-1][3])
        temp_tuples.append("-")
        temp_tuples.append(flags.local_symbol_table[-1][1])
        flags.tuples.append(temp_tuples)
        localvar = 1
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

    if red_no == 30:
  
        k = len(flags.syntax_stack)-1
        while k>=0:
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
        k = k - 1        
        while k>=0:
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
        temp1 = k                                                       # Search for the latest callby in the syntax stack,take that index and 
                                                                        #  using that index to get the value from the semantics stack
        k = len(flags.syntax_stack)-1
        while k>=0:
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
        k = k-1        
        while k>=0:
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
        temp2 = k                                                      # Search for the latest type in the syntax stack,take that index and 
                                                                       #  using that index to get the value from the semantics stack
                                                                                             
        flags.semantic_stack.append("-")                                              #{          
        flags.semantic_stack.append(flags.semantic_stack[temp1])                                            # callby value taken from syntax_stack
        flags.semantic_stack.append(flags.semantic_stack[temp2])                                            # type value taken from syntax_stack 
        flags.semantic_stack.append("-")                                              #VECTOR
        flags.semantic_stack.append(len(flags.original_integer)-1)                    #Appending the last element index of original_integer  (integer)                                              #:: 
        flags.semantic_stack.append(len(flags.original_identifier)-1)                 #Appending the last element index of original_identifier       (var)


        flags.print_semantic_stack.append(flags.semantic_stack[-6]) 
        flags.print_semantic_stack.append(flags.semantic_stack[-5])                   # Loading print_semantic_stack
        flags.print_semantic_stack.append(flags.semantic_stack[-4])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-3])                                            
        flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-2]])                                            
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])  

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
                           
        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append(flags.semantic_stack[-4])                                      # type at Si - 3
        temp_list.append("VECTOR")                                                     # shape VECTOR
        temp_list.append(flags.original_integer[flags.semantic_stack[-2]])             # Size at Si-1
        temp_list.append("-")                                                          # Columns 
        temp_list.append(flags.semantic_stack[-5])                                     # calltype at Si-4

        if(int(searchlocal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in local symbol table"
        else:
            flags.local_symbol_table.append(temp_list)
            if flags.flag[15]:
                printlocalsymboltable()
           
        poplist(6)
             
        flags.semantic_stack.append("-")                   #Appending - in the semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "BEGINFORMALPARAMETERLIST" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)
            prntstr= "                                           Tuple is (" + flags.local_symbol_table[-1][0] + "," + flags.local_symbol_table[-1][5] + "," + flags.local_symbol_table[-1][3] + ","+ "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("BEGINFORMALPARAMETERLIST")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        temp_tuples = []
        temp_tuples.append(flags.local_symbol_table[-1][0])
        temp_tuples.append(flags.local_symbol_table[-1][5])
        temp_tuples.append(flags.local_symbol_table[-1][3])
        temp_tuples.append("-")
        temp_tuples.append(flags.local_symbol_table[-1][1])
        flags.tuples.append(temp_tuples)
        
        localvar = 1
        pragmatic(temp_tuples, localvar)        
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
    if red_no == 31:

        k = len(flags.syntax_stack)-1
        while k>=0:
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
        k = k-1        
        while k>=0:
            if flags.syntax_stack[k] == 18:
                break
            else:
                k = k - 1
        temp1 = k                                                                             # Search for the latest callby(18) in the syntax stack,take that index and 
                                                                                              #  using that index get the value from the semantics stack
        k = len(flags.syntax_stack)-1
        while k>=0:
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
        k = k-1  
        while k>=0:
            if flags.syntax_stack[k] == 9:
                break
            else:
                k = k - 1
        temp2 = k                                                                             # Search for the latest type(9) in the syntax stack,take that index and 
                                                                                              #  using that index get the value from the semantics stack
        
        flags.semantic_stack.append("-")                                              #{
        flags.semantic_stack.append(flags.semantic_stack[temp1])                                            # Search for latest callby in the syntax stack
        flags.semantic_stack.append(flags.semantic_stack[temp2])                                            # Search for latest type in the syntax stack  
        flags.semantic_stack.append("-")                                              #MATRIX
        flags.semantic_stack.append(len(flags.original_integer)-2)                    #Appending the second last element index of original_integer  (integer)
        flags.semantic_stack.append("-")                                              #:: 
        flags.semantic_stack.append(len(flags.original_integer)-1)                    #Appending the last element index of original_integer         (integer)
        flags.semantic_stack.append(len(flags.original_identifier)-1)                 #Appending the last element index of original_identifier       (var)


        flags.print_semantic_stack.append(flags.semantic_stack[-8])                   # Loading print_semantic_stack
        flags.print_semantic_stack.append(flags.semantic_stack[-7])
        flags.print_semantic_stack.append(flags.semantic_stack[-6]) 
        flags.print_semantic_stack.append(flags.semantic_stack[-5])                   
        flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-4]])                                            
        flags.print_semantic_stack.append(flags.semantic_stack[-3])                                            
        flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-2]])                                            
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])  

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
                                        
        temp_list = [] 
        temp_list.append(flags.original_identifier[flags.semantic_stack[-1]])          # Si variable
        temp_list.append(flags.semantic_stack[-6])                                     # type at Si - 5 
        temp_list.append("MATRIX")                                                     # shape MATRIX
        temp_list.append(flags.original_integer[flags.semantic_stack[-4]])             # Rows at Si-3
        temp_list.append(flags.original_integer[flags.semantic_stack[-2]])             # Columns at Si- 1
        temp_list.append(flags.semantic_stack[-7])                                     # calltype at Si-6

        if(int(searchlocal(temp_list[0])) == 1):
               print "Symbol " + temp_list[0] + " already exists in local symbol table"
        else:
            flags.local_symbol_table.append(temp_list)
            if flags.flag[15]:
                printlocalsymboltable()
            
        poplist(8)
             
        flags.semantic_stack.append("-")                   #Appending - in the semantic stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')    
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ "-" + "," + "BEGINFORMALPARAMETERLIST" + "," + "-" + ","+ "-" + ")"
            print str(prntstr)
            prntstr= "                                           Tuple is  ("+ flags.local_symbol_table[-1][0] + "," + flags.local_symbol_table[-1][5] + "," + flags.local_symbol_table[-1][3] + ","+ flags.local_symbol_table[-1][4] + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("BEGINFORMALPARAMETERLIST")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        temp_tuples = []
        temp_tuples.append(flags.local_symbol_table[-1][0])
        temp_tuples.append(flags.local_symbol_table[-1][5])
        temp_tuples.append(flags.local_symbol_table[-1][3])
        temp_tuples.append(flags.local_symbol_table[-1][4])
        temp_tuples.append(flags.local_symbol_table[-1][1])
        flags.tuples.append(temp_tuples)
        localvar = 1
        pragmatic(temp_tuples, localvar)        
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
 
    if red_no == 32:
        flags.semantic_stack.append("-")                                            #Before Reduction
        flags.print_semantic_stack.append(flags.semantic_stack[-1])                                                                                    

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(1)
                                          
        flags.semantic_stack.append(get_value(reservedt,flags.syntax_stack[-1]))                         # VALUE is taken from syntax stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('V')
        
                                          
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

  


    if red_no == 33:
        flags.semantic_stack.append("-")                                            #Before Reduction
        flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(1)
                                          
        flags.semantic_stack.append(get_value(reservedt,flags.syntax_stack[-1]))                         # VALUE is taken from syntax stack
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('V')        
                                          
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)


    if red_no == 34:
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "ENDEXECUTION" + "," + "-" + "," + "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("ENDEXECUTION")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        

    if red_no == 35:
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "MAIN" + "," + "LABEL" + "," + "-" + "," + "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("MAIN")
        temp_tuples.append("LABEL")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        
    if red_no == 45:
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "\"scanf\"" + "," + "ENDPROCEDURECALL" + "," + "-" + "," + "-" + ")"
            print str(prntstr)
        temp_tuples = []
        temp_tuples.append("\"scanf\"")
        temp_tuples.append("ENDPROCEDURECALL")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        

    if red_no == 46:
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "instathd" index in the syntax stack                 
            if flags.syntax_stack[k] == 25:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        k1 = len(flags.original_identifier) - 1
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
        var1 = flags.print_semantic_stack[-1]
        poplist(3)
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_type.append("A")
        
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "REFERENCEPARAMETER" + "," +var1+ "," + "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("REFERENCEPARAMETER")
        temp_tuples.append(var1)
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)


    if red_no == 47:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
               
        if flags.total_list[k+1] == '[':                                           # k[100]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == '[' and flags.total_list[k+1] == ']':      # k[i] 
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index
            temp = 2
           
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "instat-" index in the syntax stack                 
            if flags.syntax_stack[k] == 25:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])  
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        name = flags.original_identifier[flags.semantic_stack[-2]]
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-1)            # vector size
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
            size = len(flags.original_integer)-1                                 
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                                                                       
                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-1)        #vector size
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            size = flags.original_identifier[flags.semantic_stack[-1]]                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        poplist(6)

           
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])        
        flags.semantic_type.append('A');

        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "REFERENCEPARAMETER" + "," +name+ "," + size + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("REFERENCEPARAMETER")
        temp_tuples.append(name)
        temp_tuples.append(size)
        flags.tuples.append(temp_tuples)


    if red_no == 48:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
               
        if flags.total_list[k+1] == '[':                                           # tre[1:2]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' and flags.total_list[k-3] == '['  :      # tre[i:x] *
           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index
            temp = 2
           
        elif flags.total_list[k+1] == ':' and flags.total_list[k-1] == '[' :     # tre[a:100] *

            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index            
            temp = 3
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' :   # tre[100:a] *
           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index  
            temp = 4
            
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "instat-" index in the syntax stack                 
            if flags.syntax_stack[k] == 25:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])       
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-2)            # rows
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
            flags.semantic_stack.append(len(flags.original_integer)-1)             #cols
            cols = flags.original_integer[flags.semantic_stack[-1]]                                             
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-2)
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                             
            flags.semantic_stack.append(len(flags.original_identifier)-1)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            cols = flags.original_identifier[flags.semantic_stack[-1]]                                                        

        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

                                             
        if flags.procedure_start == 1:
            if(searchlocal(flags.original_identifier[var_index])):
                index = indexlocal(flags.original_identifier[var_index])
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]                
                
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0]                                            
        
        if flags.flag[13]:               
            flags.integer_count = flags.integer_count + 1
                                              
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IMULT" + "," + rows + ","+ colST + ")"
            print str(prntstr)                                             

        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IMULT")
        temp_tuples.append(rows)
        temp_tuples.append(colST)
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:           
            flags.integer_count = flags.integer_count + 1
            temp_count = flags.integer_count
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IADD" + "," +  "I$" + str(flags.integer_count-1)  + ","+ cols + ")"
            print str(prntstr)                                             

        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IADD")
        temp_tuples.append("I$" + str(flags.integer_count-1))
        temp_tuples.append(cols)
        flags.tuples.append(temp_tuples)
        
        if typeval == 'REAL':
            flags.real_count = flags.real_count + 1
            value = 'R$' + str(flags.real_count)          
        elif typeval == 'INTEGER':
            flags.integer_count = flags.integer_count + 1
            value = 'I$' + str(flags.integer_count)
                                          
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "REFERENCEPARAMETER" + "," +name+ "," + "I$" + str(temp_count) + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("REFERENCEPARAMETER" )
        temp_tuples.append(name)
        temp_tuples.append("I$" + str(temp_count))
        flags.tuples.append(temp_tuples)
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(8)

           
        flags.semantic_stack.append(var_index)                                       
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_type.append('A')
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
       

    if red_no == 49:
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "instathd" index in the syntax stack                 
            if flags.syntax_stack[k] == 26:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        k1 = len(flags.original_identifier) - 1
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
        var1 = flags.print_semantic_stack[-1]
        poplist(3)
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_type.append('A')
        
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "REFERENCEPARAMETER" + "," +var1+ "," + "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("REFERENCEPARAMETER" )
        temp_tuples.append(var1)
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)            

    if red_no == 50:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
               
        if flags.total_list[k+1] == '[':                                           # k[100]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == '[' and flags.total_list[k+1] == ']':      # k[i] 
           
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index
            temp = 2
           
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "instathd" index in the syntax stack                 
            if flags.syntax_stack[k] == 26:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])  
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        name = flags.original_identifier[flags.semantic_stack[-2]]
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-1)            # vector size
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
            size = len(flags.original_integer)-1                                 
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                                                                       
                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-1)        #vector size
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            size = flags.original_identifier[flags.semantic_stack[-1]]                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        poplist(6)
           
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])        
        flags.semantic_type.append('A');

        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "REFERENCEPARAMETER" + "," +name+ "," + size + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("REFERENCEPARAMETER" )
        temp_tuples.append(name)
        temp_tuples.append(size)
        flags.tuples.append(temp_tuples)

        
    if red_no == 51:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
               
        if flags.total_list[k+1] == '[':                                           # tre[1:2]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' and flags.total_list[k-3] == '['  :      # tre[i:x] *
           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index
            temp = 2
           
        elif flags.total_list[k+1] == ':' and flags.total_list[k-1] == '[' :     # tre[a:100] *
           
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index            
            temp = 3
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' :   # tre[100:a] *
           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index  
            temp = 4
            
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "instathd" index in the syntax stack                 
            if flags.syntax_stack[k] == 26:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1                
        
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])       
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-2)            # rows
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
            flags.semantic_stack.append(len(flags.original_integer)-1)             #cols
            cols = flags.original_integer[flags.semantic_stack[-1]]                                             
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-2)
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                             
            flags.semantic_stack.append(len(flags.original_identifier)-1)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            cols = flags.original_identifier[flags.semantic_stack[-1]]                                                        

        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

                                             
        if flags.procedure_start == 1:
            if(searchlocal(flags.original_identifier[var_index])):
                index = indexlocal(flags.original_identifier[var_index])
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]                                
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0]                                    
                
        if flags.flag[13]:               
            flags.integer_count = flags.integer_count + 1                                              
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IMULT" + "," + rows + ","+ colST + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IMULT" )
        temp_tuples.append(rows)
        temp_tuples.append(colST)
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:     
            flags.integer_count = flags.integer_count + 1
            temp_count = flags.integer_count
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IADD" + "," +  "I$" + str(flags.integer_count-1)  + ","+ cols + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IADD" )
        temp_tuples.append( "I$" + str(flags.integer_count-1))
        temp_tuples.append(cols)
        flags.tuples.append(temp_tuples)
        
        if typeval == 'REAL':
            flags.real_count = flags.real_count + 1
            value = 'R$' + str(flags.real_count)          
        elif typeval == 'INTEGER':
            flags.integer_count = flags.integer_count + 1
            value = 'I$' + str(flags.integer_count)
                                          
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "REFERENCEPARAMETER" + "," +name+ "," + "I$" + str(temp_count) + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("REFERENCEPARAMETER" )
        temp_tuples.append(name)
        temp_tuples.append("I$" + str(temp_count))
        flags.tuples.append(temp_tuples)

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        poplist(8)
        
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
        flags.semantic_type.append('A')
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)


    if red_no == 52:        
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(flags.total_list[-2])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        poplist(2)
        
        flags.semantic_stack.append(flags.total_list[-2])        
        flags.print_semantic_stack.append(flags.semantic_stack[-1])            
        flags.semantic_type.append('STRNG')
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                    
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "\"scanf\"" + "," + "CALLPROCEDURE"+ "," + "-"+ "," + "-" + ")"            
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("\"scanf\"")
        temp_tuples.append("CALLPROCEDURE" )
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "BEGINACTUALPARAMETERLIST"+ "," + "-"+ "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("BEGINACTUALPARAMETERLIST")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "VALUEACTUALPARAMETER"+ "," + flags.total_list[-2] + "," + "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("VALUEACTUALPARAMETER")
        temp_tuples.append(flags.total_list[-2])
        temp_tuples.append("-")
        temp_tuples.append("-")        
        flags.tuples.append(temp_tuples)
        
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
    if red_no == 54:
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "\"printf\"" + "," + "ENDPROCEDURECALL" + "," + "-" + "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("printf")
        temp_tuples.append("ENDPROCEDURECALL")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
   

    if red_no == 55:
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "outstat-" index in the syntax stack                 
            if flags.syntax_stack[k] == 28:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        k1 = len(flags.original_identifier) - 1
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
        var1 = flags.print_semantic_stack[-1]
        poplist(3)
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_type.append('A')
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
        
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "VALUEACTUALPARAMETER" + "," +var1+ "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("VALUEACTUALPARAMETER")
        temp_tuples.append(var1)
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        
        
    if red_no == 56:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
               
        if flags.total_list[k+1] == '[':                                           # k[100]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == '[' and flags.total_list[k+1] == ']':      # k[i] 
           
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index
            temp = 2
           
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "outstat-" index in the syntax stack                 
            if flags.syntax_stack[k] == 28:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])  
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        name = flags.original_identifier[flags.semantic_stack[-2]]
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-1)            # vector size
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
            size = len(flags.original_integer)-1                                 
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                                                                       
                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-1)        #vector size
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            size = flags.original_identifier[flags.semantic_stack[-1]]
                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)            

        poplist(6)
           
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])        
        flags.semantic_type.append('A');
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "VALUEACTUALPARAMETER" + "," +name+ "," + size + ")"
            print str(prntstr)
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("VALUEACTUALPARAMETER")
        temp_tuples.append(name)
        temp_tuples.append(size)
        flags.tuples.append(temp_tuples) 



    if red_no == 57:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
               
        if flags.total_list[k+1] == '[':                                           # tre[1:2]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' and flags.total_list[k-3] == '['  :      # tre[i:x] *           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index
            temp = 2
           
        elif flags.total_list[k+1] == ':' and flags.total_list[k-1] == '[' :     # tre[a:100] *
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index            
            temp = 3
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' :   # tre[100:a] *
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index  
            temp = 4
            
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "outstat-" index in the syntax stack                 
            if flags.syntax_stack[k] == 28:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                        
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])       
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-2)            # rows
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
            flags.semantic_stack.append(len(flags.original_integer)-1)             #cols
            cols = flags.original_integer[flags.semantic_stack[-1]]                                             
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-2)
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                             
            flags.semantic_stack.append(len(flags.original_identifier)-1)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            cols = flags.original_identifier[flags.semantic_stack[-1]]                                                         

        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
        if flags.procedure_start == 1:
            if(searchlocal(flags.original_identifier[var_index])):
                index = indexlocal(flags.original_identifier[var_index])
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]                
                
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0]                                    
                        
        if flags.flag[13]:               
            flags.integer_count = flags.integer_count + 1                                              
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IMULT" + "," + rows + ","+ colST + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IMULT")
        temp_tuples.append(rows)
        temp_tuples.append(colST)
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:            
            flags.integer_count = flags.integer_count + 1
            temp_count = flags.integer_count
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IADD" + "," +  "I$" + str(flags.integer_count-1)  + ","+ cols + ")"
            print str(prntstr)                                             

        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IADD")
        temp_tuples.append("I$" + str(flags.integer_count-1))
        temp_tuples.append(cols)
        flags.tuples.append(temp_tuples)
        
        if typeval == 'REAL':
            flags.real_count = flags.real_count + 1
            value = 'R$' + str(flags.real_count)          
        elif typeval == 'INTEGER':
            flags.integer_count = flags.integer_count + 1
            value = 'I$' + str(flags.integer_count)
                                          
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "VALUEACTUALPARAMETER" + "," +name+ "," + "I$" + str(temp_count) + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("VALUEACTUALPARAMETER")
        temp_tuples.append(name)
        temp_tuples.append("I$" + str(temp_count))
        flags.tuples.append(temp_tuples)
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(8)
           
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]]) 
        flags.semantic_type.append('A')
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)


    if red_no == 58:
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "outstathd" index in the syntax stack                 
            if flags.syntax_stack[k] == 29:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        k1 = len(flags.original_identifier) - 1
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
        var1 = flags.print_semantic_stack[-1]
        poplist(3)
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_type.append("A")
        
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"#"+ "," + "VALUEACTUALPARAMETER" + "," +var1+ "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("#")
        temp_tuples.append("VALUEACTUALPARAMETER")
        temp_tuples.append(var1)
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
    if red_no == 59:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
               
        if flags.total_list[k+1] == '[':                                           # k[100]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == '[' and flags.total_list[k+1] == ']':      # k[i]            
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index
            temp = 2
           
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "outstathd" index in the syntax stack                 
            if flags.syntax_stack[k] == 29:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])  
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        name = flags.original_identifier[flags.semantic_stack[-2]]
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-1)            # vector size
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
            #size = len(flags.original_integer)-1                                 
            size = flags.original_integer[flags.semantic_stack[-1]] 
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                                                                       
                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-1)        #vector size
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            size = flags.original_identifier[flags.semantic_stack[-1]]                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        poplist(6)
           
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])        
        flags.semantic_type.append('A');
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"#"+ "," + "VALUEACTUALPARAMETER" + "," +name+ "," + str(size) + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("#")
        temp_tuples.append("VALUEACTUALPARAMETER")
        temp_tuples.append(name)
        temp_tuples.append(str(size))
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
    if red_no == 60:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
               
        if flags.total_list[k+1] == '[':                                           # tre[1:2]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' and flags.total_list[k-3] == '['  :      # tre[i:x] *           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index
            temp = 2
           
        elif flags.total_list[k+1] == ':' and flags.total_list[k-1] == '[' :     # tre[a:100] *           
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index            
            temp = 3
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' :   # tre[100:a] *           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index  
            temp = 4
            
        k = len(flags.syntax_stack)-1
        count=0
        while k>=0:                                                                        #find the latest "outstathd" index in the syntax stack                 
            if flags.syntax_stack[k] == 29:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                        
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])       
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-2)            # rows
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
            flags.semantic_stack.append(len(flags.original_integer)-1)             #cols
            cols = flags.original_integer[flags.semantic_stack[-1]]                                             
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-2)
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                             
            flags.semantic_stack.append(len(flags.original_identifier)-1)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            cols = flags.original_identifier[flags.semantic_stack[-1]]
                                                     
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
        if flags.procedure_start == 1:
            if(searchlocal(flags.original_identifier[var_index])):
                index = indexlocal(flags.original_identifier[var_index])
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]                
                
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0]                                    
        
        if flags.flag[13]:               
            flags.integer_count = flags.integer_count + 1                                              
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IMULT" + "," + rows + ","+ colST + ")"
            print str(prntstr)                                             

        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IMULT")
        temp_tuples.append(rows)
        temp_tuples.append(colST)
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:         
            flags.integer_count = flags.integer_count + 1
            temp_count = flags.integer_count
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IADD" + "," +  "I$" + str(flags.integer_count-1)  + ","+ cols + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IADD")
        temp_tuples.append("I$" + str(flags.integer_count-1))
        temp_tuples.append(cols)
        flags.tuples.append(temp_tuples)
        
        if typeval == 'REAL':
            flags.real_count = flags.real_count + 1
            value = 'R$' + str(flags.real_count)          
        elif typeval == 'INTEGER':
            flags.integer_count = flags.integer_count + 1
            value = 'I$' + str(flags.integer_count)
                                          
        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" +"-"+ "," + "VALUEACTUALPARAMETER" + "," +name+ "," + "I$" + str(temp_count) + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("VALUEACTUALPARAMETER")
        temp_tuples.append(name)
        temp_tuples.append("I$" + str(temp_count))
        flags.tuples.append(temp_tuples)
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(8)
           
        flags.semantic_stack.append(value)    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('A')
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

            

    if red_no == 61:        
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(flags.total_list[-2])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)            
        poplist(2)        
        flags.semantic_stack.append(flags.total_list[-2])        
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('STRNG')            
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
                    
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "\"printf\"" + "," + "CALLPROCEDURE"+ "," + "-"+ "," + "-" + ")"            
            print str(prntstr)
        temp_tuples = []
        temp_tuples.append("printf")
        temp_tuples.append("CALLPROCEDURE")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "BEGINACTUALPARAMETERLIST"+ "," + "-"+ "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-" )
        temp_tuples.append( "BEGINACTUALPARAMETERLIST")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "VALUEACTUALPARAMETER"+ "," + flags.total_list[-2]+ "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-" )
        temp_tuples.append("VALUEACTUALPARAMETER")
        temp_tuples.append(flags.total_list[-2])
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)

        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    

    if red_no == 62:
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "NOACTUALPARAMETERS" + "," + "-" + "," + "-" + ")"
            print str(prntstr)

        temp_tuples = []
        temp_tuples.append("-" )
        temp_tuples.append("NOACTUALPARAMETERS")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        
        count = 0
        k = len(flags.syntax_stack)-1
        while k>=0:                                                                        #find the latest "callname" index in the syntax stack                 
            if flags.syntax_stack[k] == 31:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])  
        flags.semantic_stack.append("-")       
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
 
       
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        name =  flags.original_identifier[int(flags.semantic_stack[-2])]
        poplist(2)             
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append("A");
                                          
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                                          

        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" + name + "," + "ENDACTUALPROCEDURECALL" + "," + "-" + "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(name)
        temp_tuples.append("ENDACTUALPROCEDURECALL")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        

    if red_no == 63:
        count = 0
        k = len(flags.syntax_stack)-1
        while k>=0:                                                                        #find the latest "callname" index in the syntax stack                 
            if flags.syntax_stack[k] == 31:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_stack.append("-")        
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
       
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        name =  flags.original_identifier[int(flags.semantic_stack[-2])]
        poplist(2)             
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append("A");
                                          
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                                          

        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" + name + "," + "ENDPROCEDURECALL" + "," + "-" + "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(name)
        temp_tuples.append("ENDPROCEDURECALL")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
  
    if red_no == 64:
        
        k = len(flags.original_identifier)-1
        index=0
        while k>=0:                                                                        #find the latest "variable"  with type procedure index in the syntax stack
            index = indexglobal(flags.original_identifier[k])
            if flags.global_symbol_table[index][1] == "PROCEDURE":
                break
            else:
                k = k - 1
                
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])          
        flags.semantic_stack.append(k)               
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])   # Load print_semantic_stack for printing semantic stack       

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        name =  flags.original_identifier[int(flags.semantic_stack[-1])]

        poplist(2)
             
        flags.semantic_stack.append(k)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_type.append("A");
                                          
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                                          

        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" + name + "," + "PROCCALL" + "," +"-"+ "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(name)
        temp_tuples.append("PROCCALL")
        temp_tuples.append("-")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
    if red_no == 65:
        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "ENDACTUALPARAMETERLIST" + "," + "-" + "," + "-" + ")"
            print str(prntstr)
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("ENDACTUALPARAMETERLIST" )
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)            


    if red_no == 66:
        count = 0
        k1 = len(flags.original_identifier) - 1
        k = len(flags.syntax_stack)-1
        while k>=0:                                                                        #find the latest "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        i = len(flags.syntax_stack)-1
        count =0
        while i>=0:                                                                        #find the latest "callby" index in the syntax stack                 
            if flags.syntax_stack[i] == 33:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    i=i-1
            else:
                i= i - 1
        
        flags.semantic_stack.append(flags.semantic_stack[i])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])        
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
        name1 = flags.print_semantic_stack[-2]
        var1 = flags.print_semantic_stack[-1]
        poplist(4)

        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append("D");

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                                          

        if flags.flag[13]:                                      
            prntstr= "                                           Tuple is (" + "-" + "," + "SUB"+name1+"ACTUALPARAMETER"+ "," + var1 + "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("SUB"+name1+"ACTUALPARAMETER" )
        temp_tuples.append(var1)
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)

    if red_no == 67:
        var = 0
        temp = 0        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1

        if flags.total_list[k+1] == '[':                                           # k[100]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == '[' and flags.total_list[k+1] == ']':      # k[i] 
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index
            temp = 2

        k = len(flags.syntax_stack)-1
        count =0
        while k>=0:                                                                        #find the latest "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1               
           
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(var_index)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-1)            # vector size
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                                                                                                                    
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-1)        #vector size
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                                      
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
        if flags.procedure_start == 1:
            if(searchlocal(flags.original_identifier[var_index])):
                index = indexlocal(flags.original_identifier[var_index])
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]                
                
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0]
            
        if typeval == 'REAL':
            flags.real_count = flags.real_count + 1            
            value = 'R$' + str(flags.real_count)          
        elif typeval == 'INTEGER':
            flags.integer_count = flags.integer_count + 1            
            value = 'I$' + str(flags.integer_count)

            prntstr= "                                           Tuple is  ("+ value + "," + "SUBLOAD" + "," + name  + "," + str(rows) + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(value)
        temp_tuples.append("SUBLOAD")
        temp_tuples.append(name)
        temp_tuples.append(str(rows))
        flags.tuples.append(temp_tuples)        

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        poplist(7)
           
        flags.semantic_stack.append('-')    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                



    if red_no == 68:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1

        if flags.total_list[k+1] == '[':                                           # tre[1:2]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1

        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' and flags.total_list[k-3] == '['  :      # tre[i:x] *
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index
            temp = 2
        elif flags.total_list[k+1] == ':' and flags.total_list[k-1] == '[' :     # tre[a:100] *
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index            
            temp = 3
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' :   # tre[100:a] *
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index  
            temp = 4
            
        k = len(flags.syntax_stack)-1
        count =0
        while k>=0:                                                                        #find the latest "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
           
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(var_index)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-2)            # rows
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                             
            flags.semantic_stack.append(len(flags.original_integer)-1)             #cols
            cols = flags.original_integer[flags.semantic_stack[-1]]                                             
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-2)
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                             
            flags.semantic_stack.append(len(flags.original_identifier)-1)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            cols = flags.original_identifier[flags.semantic_stack[-1]]
                                                         
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.procedure_start == 1:
            if(searchlocal(flags.original_identifier[var_index])):
                index = indexlocal(flags.original_identifier[var_index])
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]                                         
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0] 
            flags.integer_count = flags.integer_count + 1

        if flags.flag[13]:    
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IMULT" + "," + rows + ","+ colST + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IMULT")
        temp_tuples.append(rows)
        temp_tuples.append(colST)
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:        
            flags.integer_count = flags.integer_count + 1
            temp_count = flags.integer_count
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IADD" + "," +  "I$" + str(flags.integer_count-1)  + ","+ cols + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IADD")
        temp_tuples.append("I$" + str(flags.integer_count-1))
        temp_tuples.append(cols)
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:        
            if typeval == 'REAL':
                flags.real_count = flags.real_count + 1
                value = 'R$' + str(flags.real_count)          
            elif typeval == 'INTEGER':
                flags.integer_count = flags.integer_count + 1
                value = 'I$' + str(flags.integer_count)                                
            
            prntstr= "                                           Tuple is  ("+ value + "," + "SUBLOAD" + "," + name  + ","+ "I$" + str(temp_count) + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(value)
        temp_tuples.append("SUBLOAD")
        temp_tuples.append(name)
        temp_tuples.append("I$" + str(temp_count))
        flags.tuples.append(temp_tuples)
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        poplist(9)           
        flags.semantic_stack.append('-')    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)



    if red_no == 69:
        count = 0
        k1 = len(flags.original_identifier) - 1
        k = len(flags.syntax_stack)-1
        while k>=0:                                                                        #find the latest "callname" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                
        flags.semantic_stack.append("{")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(k1)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)        
        name1 = flags.print_semantic_stack[-2]
        var1 = flags.print_semantic_stack[-1]
        poplist(3)
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append("D");

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                                          

        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "BEGINACTUALPARAMETERLIST"+ "," + "-"+ "," + "-" + ")"
            print str(prntstr)
            prntstr= "                                           Tuple is (" + "-" + "," + "SUB"+name1+"ACTUALPARAMETER"+ "," + var1 + "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("BEGINACTUALPARAMETERLIST")
        temp_tuples.append("-")
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
        
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("SUB"+name1+"ACTUALPARAMETER")
        temp_tuples.append(var1)
        temp_tuples.append("-")
        flags.tuples.append(temp_tuples)
 
    if red_no == 70:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
  
        if flags.total_list[k+1] == '[':                                           # k[100]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == '[' and flags.total_list[k+1] == ']':      # k[i] 
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index
            temp = 2

        k = len(flags.syntax_stack)-1
        count =0
        while k>=0:                                                                        #find the latest "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
           
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(var_index)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-1)            # vector size
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                                                                                                                    
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-1)        #vector size
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                                       
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
        if flags.procedure_start == 1:
            if(searchlocal(flags.original_identifier[var_index])):
                index = indexlocal(flags.original_identifier[var_index])
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]                
                
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0]
            
        if typeval == 'REAL':
            flags.real_count = flags.real_count + 1            
            value = 'R$' + str(flags.real_count)          
        elif typeval == 'INTEGER':
            flags.integer_count = flags.integer_count + 1            
            value = 'I$' + str(flags.integer_count)

        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "BEGINACTUALPARAMETERLIST"+ "," + "-"+ "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("BEGINACTUALPARAMETERLIST")
        temp_tuples.append("-")
        temp_tuples.append("-")        
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:        
            prntstr= "                                           Tuple is  ("+ value + "," + "SUBLOAD" + "," + name  + "," + str(rows) + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(value)
        temp_tuples.append("SUBLOAD" )
        temp_tuples.append(name)
        temp_tuples.append(str(rows))        
        flags.tuples.append(temp_tuples)
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        poplist(6)
           
        flags.semantic_stack.append('-')    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')       
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                

    if red_no == 71:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1

        if flags.total_list[k+1] == '[':                                           # tre[1:2]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1

        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' and flags.total_list[k-3] == '['  :      # tre[i:x] *
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index
            temp = 2
        elif flags.total_list[k+1] == ':' and flags.total_list[k-1] == '[' :     # tre[a:100] *
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index            
            temp = 3
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' :   # tre[100:a] *           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index  
            temp = 4
            
        k = len(flags.syntax_stack)-1
        count =0
        while k>=0:                                                                        #find the latest "callby" index in the syntax stack                 
            if flags.syntax_stack[k] == 18:
                count = count+ 1
                if(count > 1):
                    break
                else:
                    k=k-1
            else:
                k = k - 1
                           
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(flags.semantic_stack[k])
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(var_index)
        flags.print_semantic_stack.append(flags.original_identifier[int(flags.semantic_stack[-1])])
        flags.semantic_stack.append("-")
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-2)            # rows
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                             
            flags.semantic_stack.append(len(flags.original_integer)-1)             #cols
            cols = flags.original_integer[flags.semantic_stack[-1]]                                             
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-2)
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                            
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                             
            flags.semantic_stack.append(len(flags.original_identifier)-1)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            cols = flags.original_identifier[flags.semantic_stack[-1]]                                                         
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.procedure_start == 1:
            if(searchlocal(flags.original_identifier[var_index])):
                index = indexlocal(flags.original_identifier[var_index])
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]                                         
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0]

        if flags.flag[13]:
            prntstr= "                                           Tuple is (" + "-" + "," + "BEGINACTUALPARAMETERLIST"+ "," + "-"+ "," + "-" + ")"
            print str(prntstr)            
            flags.integer_count = flags.integer_count + 1                                          
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IMULT" + "," + rows + ","+ colST + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("-")
        temp_tuples.append("BEGINACTUALPARAMETERLIST" )
        temp_tuples.append("-")
        temp_tuples.append("-")        
        flags.tuples.append(temp_tuples)

        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IMULT" )
        temp_tuples.append(rows)
        temp_tuples.append(colST)        
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:        
            flags.integer_count = flags.integer_count + 1
            temp_count = flags.integer_count
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IADD" + "," +  "I$" + str(flags.integer_count-1)  + ","+ cols + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append("IADD" )
        temp_tuples.append("I$" + str(flags.integer_count-1))
        temp_tuples.append(cols)        
        flags.tuples.append(temp_tuples)
        
        if flags.flag[13]:        
            if typeval == 'REAL':
                flags.real_count = flags.real_count + 1
                value = 'R$' + str(flags.real_count)          
            elif typeval == 'INTEGER':
                flags.integer_count = flags.integer_count + 1
                value = 'I$' + str(flags.integer_count)

            prntstr= "                                           Tuple is  ("+ value + "," + "SUBLOAD" + "," + name  + ","+ "I$" + str(temp_count) + ")"
            print str(prntstr)                                             

        temp_tuples = []
        temp_tuples.append(value)
        temp_tuples.append("SUBLOAD" )
        temp_tuples.append(name)
        temp_tuples.append("I$" + str(temp_count))        
        flags.tuples.append(temp_tuples)
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(8)
           
        flags.semantic_stack.append('-')    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('D')
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)


    if red_no == 72:

        axpr = flags.semantic_stack[-1]
     #   flags.semantic_stack.append("-")    
     #   flags.print_semantic_stack.append(flags.semantic_stack[-1])
      #  flags.semantic_stack.append(axpr)    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
      #  flags.semantic_stack.append("-")    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
      #  poplist(3)
    
    
        tval = 'L$' + str(flags.label_counter)
      #  flags.semantic_stack.append(tval)    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
      #  flags.semantic_type.append("L$")

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)


        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ "L$" + str(flags.label_counter) +"," + "LABEL" + "," + "-" + ","+ "-"   + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("L$" + str(flags.label_counter))
        temp_tuples.append("LABEL")
        temp_tuples.append("-")
        temp_tuples.append("-")        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)        

    if red_no == 74:

        axpr = flags.semantic_stack[-1]
        flags.semantic_stack.append("-")    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(axpr)    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append("-")    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
        poplist(3)
        
        flags.label_counter = flags.label_counter+1



        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ "L$" + str(flags.label_counter) +"," + "JUMP" + "," + "#" + ","+ "#"   + ")"
            print str(prntstr)
     
        flags.label_counter = flags.label_counter-1



        

        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ "L$" + str(flags.label_counter) +"," + "LABEL" + "," + "#" + ","+ "#"   + ")"
            print str(prntstr)
            
        tval = 'L$' + str(flags.label_counter)            
        flags.semantic_stack.append(tval)    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append("L$")

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        

    if red_no == 75:

        axpr = flags.semantic_stack[-1]
     #   flags.semantic_stack.append("-")    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
      #  flags.semantic_stack.append(axpr)    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
      #  flags.semantic_stack.append("-")    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
       # poplist(3)
        flags.label_counter = flags.label_counter+1
        tval = 'L$' + str(flags.label_counter)
      #  flags.semantic_stack.append(tval)    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
      #  flags.semantic_type.append("L$")

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)


        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ tval +"," + "CJUMPF" + "," + str(axpr) + ","+ "-"   + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(tval)
        temp_tuples.append("CJUMPF")
        temp_tuples.append(str(axpr))
        temp_tuples.append("-")        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
    if red_no == 76:

        flags.for_loop = flags.for_loop + 1

        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == '<-':               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
        k = k -1
        k1 = len(flags.original_identifier)-1
        while k1>=0:
            if flags.original_identifier[k1] == flags.total_list[k] :                                                                                                #right of it
               break
            else:
                k1 = k1 - 1
        var = flags.original_identifier[k1]
            

        axpr = flags.semantic_stack[-1]
        flags.semantic_stack.append("-")    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(axpr)    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append("-")    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
   #     flags.semantic_stack.append(len(flags.original_identifier)-1)                                          # Var
        flags.semantic_stack.append(k1) 
     #   flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
     #   var = flags.original_identifier[flags.semantic_stack[-1]]
        flags.print_semantic_stack.append(var)
        flags.semantic_stack.append("-")    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.procedure_start == 1:
            index = indexlocal(flags.original_identifier[-1])
            if index >=0:
                typeval = flags.local_symbol_table[index][1]
                shape2 = flags.local_symbol_table[index][2]                    
                if shape2 == 'MATRIX': 
                    print '                                              ERROR ' + flags.original_identifier[-1] + ' is of shape MATRIX'
                if shape2 == 'VECTOR': 
                    print '                                              ERROR ' + flags.original_identifier[-1]+ ' is of shape VECTOR'      
                if typeval == 'REAL': 
                    print '                                              ERROR ' + flags.original_identifier[-1] + ' is of type REAL' 
            else:
                index = indexglobal(flags.original_identifier[-1])
                shape2 = flags.global_symbol_table[index][2]
                typeval = flags.global_symbol_table[index][1]                
                if shape2 == 'MATRIX': 
                    print '                                              ERROR ' + flags.original_identifier[-1] + ' is of shape MATRIX'
                if shape2 == 'VECTOR': 
                    print '                                              ERROR ' + flags.original_identifier[-1] + ' is of shape VECTOR'
                if typeval == 'REAL': 
                    print '                                              ERROR ' + flags.original_identifier[-1] + ' is of type REAL'


        else:
            index = indexglobal(flags.original_identifier[-1])
            if index>=0:
                typeval = flags.global_symbol_table[index][1]
                shape2 = flags.global_symbol_table[index][2] 
                if shape2 == 'MATRIX': 
                    print '                                              ERROR ' + flags.original_identifier[-1] + ' is of shape MATRIX'
                if shape2 == 'VECTOR': 
                    print '                                              ERROR ' + flags.original_identifier[-1] + ' is of shape VECTOR'
                if typeval == 'REAL': 
                    print '                                              ERROR ' + flags.original_identifier[-1] + ' is of type REAL'



        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        poplist(5)

        if flags.semantic_type[-1] == 'I$':
            if flags.flag[13]:
                prntstr= "                                           Tuple is  ("+ var + "," + "STORE" + "," + flags.semantic_stack[-1] + ","+ "-" + ")"
                print str(prntstr)

            temp_tuples = []
            temp_tuples.append(var)
            temp_tuples.append("STORE")
            temp_tuples.append(flags.semantic_stack[-1])
            temp_tuples.append("-")
            temp_tuples.append(typeval)
            localvar = 0
            pragmatic(temp_tuples, localvar)  
            flags.tuples.append(temp_tuples)
            
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

                pragmatic(temp_tuples, localvar)        
        else:    
            if flags.flag[13]:
                prntstr= "                                           Tuple is  ("+ var + "," + "STORE" + "," + flags.original_integer[flags.semantic_stack[-1]] + ","+ "-" + ")"
                print str(prntstr)
                
            temp_tuples = []
            temp_tuples.append(var)
            temp_tuples.append("STORE")
            temp_tuples.append(flags.original_integer[flags.semantic_stack[-1]])
            temp_tuples.append("-")        
            temp_tuples.append(typeval)
            localvar = 0
            pragmatic(temp_tuples, localvar)
            flags.tuples.append(temp_tuples)
            
            if flags.flag[20]:
                prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                print str(prntstr)
                temp_tuples = []

                temp_tuples.append("20")

                temp_tuples.append("FLAG")

                temp_tuples.append("-")

                temp_tuples.append("-")

                temp_tuples.append("-") 
                localvar = 0

                pragmatic(temp_tuples, localvar)
      	    
        flags.label_counter = flags.label_counter+1
        tval = 'L$' + str(flags.label_counter)
        flags.semantic_stack.append(tval)    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append("L$")

        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        


        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ "L$" + str(flags.label_counter+1)  +"," + "JUMP" + "," + "-" + ","+ "-"   + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("L$" + str(flags.label_counter+1))
        temp_tuples.append("JUMP")
        temp_tuples.append("-")
        temp_tuples.append("-")        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)  
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
        if flags.flag[13]:
            prntstr= "                                           Tuple is  (" + flags.semantic_stack[-1] +"," + "LABEL" + "," + "-" + ","+ "-"   + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(flags.semantic_stack[-1])
        temp_tuples.append("LABEL")
        temp_tuples.append("-")
        temp_tuples.append("-")        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)
        
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)        
            
        flags.label_counter = flags.label_counter+2                   #Reserve label 

    if red_no == 78:
        if flags.semantic_type[-1] != 'B$':
                print "                                              ERROR ",flags.print_semantic_stack[-1] ,' not a boolean expression'   
            

        axpr = flags.semantic_stack[-1]
     #   flags.semantic_stack.append("-")    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
       # flags.semantic_stack.append(axpr)    
        #flags.print_semantic_stack.append(flags.semantic_stack[-1])
        ##flags.semantic_stack.append("-")    
        #flags.print_semantic_stack.append(flags.semantic_stack[-1])
        
     #   poplist(3)


        k = len(flags.semantic_type)-1
        while k>=0:
            if flags.semantic_type[k] == 'L$':               #searching for last label                                                                           
                break
            else:
                k = k - 1
        
        label = flags.semantic_stack[k]
        strlen = len(label)
        labelcount = label[2:strlen]
        labelcount = int(labelcount) + 2
        label = 'L$' + str(labelcount)

        
       # flags.label_counter = flags.label_counter+1
       # tval = 'L$' + str(flags.label_counter)
     #   flags.semantic_stack.append(tval)    
     #   flags.print_semantic_stack.append(flags.semantic_stack[-1])
     #   flags.semantic_type.append("L$")
        

        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ label +"," + "CJUMPT" + "," + str(axpr) + ","+ "-"   + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(label)
        temp_tuples.append("CJUMPT")
        temp_tuples.append(str(axpr))
        temp_tuples.append("-")        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
    if red_no == 79:

        axpr = flags.semantic_stack[-1]
        #flags.semantic_stack.append("-")    
        #flags.print_semantic_stack.append(flags.semantic_stack[-1])
        ##flags.semantic_stack.append(axpr)    
        ##flags.print_semantic_stack.append(flags.semantic_stack[-1])
        #flags.semantic_stack.append("-")    
        #flags.print_semantic_stack.append(flags.semantic_stack[-1])

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        
        #poplist(3)
        #flags.label_counter = flags.label_counter-1

        #flags.label_counter = flags.label_counter+1
        #tval = 'L$' + str(flags.label_counter)
        if flags.for_loop ==1:
            k = len(flags.semantic_type)-1
            while k>=0:
                if flags.semantic_type[k] == 'L$':               #searching for last label                                                                           
                    break
                else:
                    k = k - 1
            k = k-1
            
            while k>=0:
                if flags.semantic_type[k] == 'L$':               #searching for last label                                                                           
                    break
                else:
                    k = k - 1
        else:            
            
            k = len(flags.semantic_type)-1
            while k>=0:
                if flags.semantic_type[k] == 'L$':               #searching for last label                                                                           
                    break
                else:
                    k = k - 1
        
        label = flags.semantic_stack[k]
        strlen = len(label)
        labelcount = label[2:strlen]
        labelcount = int(labelcount) + 2
        label1 = 'L$' + str(labelcount)

        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ label +"," + "JUMP" + "," + "-" + ","+ "-"   + ")"
            print str(prntstr)
     
    #    flags.label_counter = flags.label_counter-1
    
        temp_tuples = []
        temp_tuples.append(label)
        temp_tuples.append("JUMP")
        temp_tuples.append("-")
        temp_tuples.append("-")        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)        
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    

        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ label1 +"," + "LABEL" + "," + "-" + ","+ "-"   + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(label1)
        temp_tuples.append("LABEL")
        temp_tuples.append("-")
        temp_tuples.append("-")        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)
        
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
        #tval = 'L$' + str(flags.label_counter)        
       # flags.semantic_stack.append(tval)    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
       # flags.semantic_type.append("L$")       

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

        flags.for_loop = flags.for_loop - 1
            
    if red_no == 77:

        
        k = len(flags.semantic_type)-1
        while k>=0:
            if flags.semantic_type[k] == 'L$':               #searching for last label                                                                           
               break
            else:
                k = k - 1
        
        label = flags.semantic_stack[k]
        strlen = len(label)
        labelcount = label[2:strlen]
        labelcount = int(labelcount) + 1
        label = 'L$' + str(labelcount)
        
      #  flags.label_counter = flags.label_counter+1
      #  tval = 'L$' + str(flags.label_counter)
      #  flags.semantic_stack.append(tval)    
      #  flags.print_semantic_stack.append(flags.semantic_stack[-1])
      #  flags.semantic_type.append("L$")

        
        axpr = flags.semantic_stack[-1]
        var = flags.original_identifier[-1]
                    
          
        if flags.semantic_type[-1] == 'NI':
            axpr = flags.original_integer[-1]

        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ var + "," + "INCREMENT" +"," + str(axpr) + "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(var)
        temp_tuples.append("INCREMENT")
        temp_tuples.append(str(axpr))
        temp_tuples.append("-")        
        temp_tuples.append("-") 
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)

      	    
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ label + "," + "LABEL" +"," + "-"+ "," + "-" + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(label)
        temp_tuples.append("LABEL")
        temp_tuples.append("-")
        temp_tuples.append("-")        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)            
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
  

    if red_no == 117:                                                               #done it similar to 15
        flags.semantic_stack.append("-")                                            #Before Reduction
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        
        if flags.total_list[-1] == ']' and flags.total_list[-3] == '[':               # tre[1]
            temp = 1
        elif flags.total_list[-1] == ']' and flags.total_list[-3] == ':':      # tre[ :2] 
            temp = 2
        elif flags.total_list[-1] == ':' and flags.total_list[-3] == '[' :     # tre[1: ] *          
            temp = 3 
        else:         
            temp = 4 

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        flags.semantic_stack.pop()
        flags.print_semantic_stack.pop()
            
        flags.semantic_stack.append(len(flags.original_real)-1)                         # Original real value taken from original stack 
        flags.print_semantic_stack.append(flags.original_real[-1])
        if temp == 1 or temp == 2 or temp == 3:
            flags.semantic_type.append('RELIND')
        else:
            flags.semantic_type.append('NR')          
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)



    if red_no == 116:
        temp = 0 
        flags.semantic_stack.append("-")                                            #Before Reduction
        flags.print_semantic_stack.append(flags.semantic_stack[-1]) 

        if flags.total_list[-1] == ']' and flags.total_list[-3] == '[':               # tre[1]
            temp = 1
        elif flags.total_list[-1] == ']' and flags.total_list[-3] == ':':      # tre[ :2] 
            temp = 2
        elif flags.total_list[-1] == ':' and flags.total_list[-3] == '[' :     # tre[1: ] *          
            temp = 3           

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        flags.semantic_stack.pop()
        flags.print_semantic_stack.pop()


        flags.semantic_stack.append(len(flags.original_integer)-1)                         # Original integer value taken from original stack 
        flags.print_semantic_stack.append(flags.original_integer[-1])
        if temp == 1 or temp == 2 or temp == 3:
            flags.semantic_type.append('INTIND')
        else:
            flags.semantic_type.append('NI')
            
            
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)  

        

    if red_no == 115:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
                
        top_second_last = flags.semantic_stack[-2]
        top_last = flags.semantic_stack[-1]
        
        if flags.procedure_start == 1:
            index_last = indexlocal(flags.original_identifier[top_last])
            index_second_last = indexlocal(flags.original_identifier[top_second_last])            
            if index_last >=0:
                typelast = flags.local_symbol_table[index_last][1]
                shapelast = flags.local_symbol_table[index_last][2]
            else:
                typelast = flags.global_symbol_table[index_last][1]               
                shapelast = flags.global_symbol_table[index_last][2] 
            if index_second_last >=0:
                typeseclast = flags.local_symbol_table[index_second_last][1]
                shapeseclast = flags.local_symbol_table[index_second_last][2]
            else:
                typeseclast = flags.global_symbol_table[index_second_last][1]
                shapeseclast = flags.global_symbol_table[index_second_last][2]
        else:
            index_last = indexglobal(flags.original_identifier[top_last])
            index_second_last = indexglobal(flags.original_identifier[top_second_last])
            typelast = flags.global_symbol_table[index_last][1]
            typeseclast = flags.global_symbol_table[index_second_last][1]
            shapelast = flags.global_symbol_table[index_last][2]
            shapeseclast = flags.global_symbol_table[index_second_last][2]
            
            
        if flags.total_list[k+1] == '[':                                           # tre[1:2]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' and flags.total_list[k-3] == '['  :      # tre[i:x] *
           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index
            temp = 2
           
        elif flags.total_list[k+1] == ':' and flags.total_list[k-1] == '[' :     # tre[a:100] *
           
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index            
            temp = 3
           
        elif flags.total_list[k-1] == ':' and flags.total_list[k+1] == ']' :   # tre[100:a] *
           
            var = flags.original_identifier[-3]
            var_index = len(flags.original_identifier) - 3                      # Getting 3rd last index  
            temp = 4
           
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])       
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-2)            # rows
            usedindex1 = flags.semantic_stack[-1]
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
            flags.semantic_stack.append(len(flags.original_integer)-1)             #cols
            usedindex2 = flags.semantic_stack[-1]
            cols = flags.original_integer[flags.semantic_stack[-1]]                                             
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
                                             
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-2)
            usedindex1 = flags.semantic_stack[-1]
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
                                             
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
            flags.semantic_stack.append(len(flags.original_identifier)-1)
            usedindex2 = flags.semantic_stack[-1]
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                             
            cols = flags.original_identifier[flags.semantic_stack[-1]]            
                                             

        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])


        if flags.procedure_start == 1:
            index = indexlocal(flags.original_identifier[var_index])
            if index >=0:
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]                
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0]
                                                  
        
        
 
        flags.integer_count = flags.integer_count + 1
        
        if flags.flag[13]:                                          
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IMULT" + "," + rows + ","+ colST + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append( "IMULT")
        temp_tuples.append(rows)
        temp_tuples.append(colST)        
        flags.tuples.append(temp_tuples)             

        flags.integer_count = flags.integer_count + 1
        temp_count = flags.integer_count
        if flags.flag[13]:        
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IADD" + "," +  "I$" + str(flags.integer_count-1)  + ","+ cols + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append("I$" + str(flags.integer_count))
        temp_tuples.append( "IADD")
        temp_tuples.append("I$" + str(flags.integer_count-1))
        temp_tuples.append(cols)        
        flags.tuples.append(temp_tuples)
        
        if typeval == 'REAL':
            flags.real_count = flags.real_count + 1
            value = 'R$' + str(flags.real_count)          
        elif typeval == 'INTEGER':
            flags.integer_count = flags.integer_count + 1
            value = 'I$' + str(flags.integer_count)

        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ value + "," + "SUBLOAD" + "," + name  + ","+ "I$" + str(temp_count) + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(value)
        temp_tuples.append("SUBLOAD")
        temp_tuples.append(name)
        temp_tuples.append("I$" + str(temp_count))        
        flags.tuples.append(temp_tuples)

        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(6)

           
        flags.semantic_stack.append(value)    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('I$')
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

        flags.used_list.append(usedindex1)
        flags.used_list.append(usedindex2)
        flags.used_flag = 1



    if red_no == 114:
        var = 0
        temp = 0
        
        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == flags.original_identifier[-1]:               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1
               
        if flags.total_list[k+1] == '[':                                           # k[100]                               
            var = flags.original_identifier[-1]
            var_index = len(flags.original_identifier) - 1                      # Getting last index            
            temp = 1
           
        elif flags.total_list[k-1] == '[' and flags.total_list[k+1] == ']':      # k[i] 
            var = flags.original_identifier[-2]
            var_index = len(flags.original_identifier) - 2                      # Getting 2nd last index
            temp = 2
                              
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])       
       
        if temp == 1:
            flags.semantic_stack.append(len(flags.original_integer)-1)            # vector size
            usedindex1 = flags.semantic_stack[-1]
            rows = flags.original_integer[flags.semantic_stack[-1]]
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])                                             
            flags.semantic_stack.append('-')                                       # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                                                                                                                    
        elif temp == 2:
            flags.semantic_stack.append(len(flags.original_identifier)-1)        #vector size
            usedindex1 = flags.semantic_stack[-1]
            rows = flags.original_identifier[flags.semantic_stack[-1]]                                  
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                                        
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                             
        if flags.procedure_start == 1:
            index = indexlocal(flags.original_identifier[var_index])
            if index >=0:
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name = flags.global_symbol_table[index][0]
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name = flags.global_symbol_table[index][0]
            
        if typeval == 'REAL':
            flags.real_count = flags.real_count + 1            
            value = 'R$' + str(flags.real_count)          
        elif typeval == 'INTEGER':
            flags.integer_count = flags.integer_count + 1            
            value = 'I$' + str(flags.integer_count)                                                                                
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ value + "," + "SUBLOAD" + "," + name  + "," + str(rows) + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(value)
        temp_tuples.append("SUBLOAD")
        temp_tuples.append(name)
        temp_tuples.append(str(rows))
        temp_tuples.append(typeval)        
        flags.tuples.append(temp_tuples)
        localvar = 0
        pragmatic(temp_tuples, localvar)        
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        poplist(4)
           
        flags.semantic_stack.append(value)    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('I$')       
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        flags.used_list.append(usedindex1)
        flags.used_flag = 1


    if red_no == 113:
        
        temp = 0
        
        if flags.total_list[-1] == ']' and flags.total_list[-3] == '[':               # tre[j]
            temp = 1
        elif flags.total_list[-1] == ']' and flags.total_list[-3] == ':':      # tre[ :j] 
            temp = 2
        elif flags.total_list[-1] == ':' and flags.total_list[-3] == '[' :     # tre[j: ] *          
            temp = 3
            
        flags.semantic_stack.append(len(flags.original_identifier)-1)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
        if temp == 1 or temp == 2 or temp == 3:
            flags.semantic_type.append('AIND')
        else:
            flags.semantic_type.append('A')
            
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)



    if red_no == 111:

        value = flags.semantic_stack[-1]
        expr = ' '     
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])

        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == ')':               #searching for  )
                open_bracket_index = k       
                break
            else:
                k = k - 1


        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == '(':               #searching for  (
                close_bracket_index = k       
                break
            else:
                k = k - 1


        for i in range(close_bracket_index + 1,open_bracket_index):
            expr = expr + flags.total_list[i]
            
        last = flags.semantic_type[-1]
        if last == 'B$' or last =='I$':
            expr = flags.semantic_stack[-1]
            flags.semantic_stack.append(expr)                # expr
            flags.print_semantic_stack.append(flags.semantic_stack[-1])            
        elif last == 'A':
            flags.semantic_stack.append(flags.original_identifier[value])                # expr  
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
        else:
            flags.semantic_stack.append(flags.original_integer[value])                # expr  
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            
        flags.semantic_stack.append('-')                                     # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])


        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(3)

        if last == 'B$' or last =='I$':
            expr = flags.semantic_stack[-1]
            flags.semantic_stack.append(expr)                # expr
            flags.print_semantic_stack.append(flags.semantic_stack[-1])            
        elif last == 'A':
            flags.semantic_stack.append(flags.original_identifier[value])                # expr  
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
        else:
            flags.semantic_stack.append(flags.original_integer[value])                # expr  
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            
        flags.semantic_type.append('EXPR')           

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
        
       
        
        

    if red_no == 109:
        
        final = ''


        if flags.used_flag:        
            tempcount = 0
            k = len(flags.semantic_stack)-1
            while k>=0:
                usedflag = 0
                tempval = flags.semantic_stack[k]
                temptype = flags.semantic_type[k]   
                for i in range(0,len(flags.used_list)):
                    if tempval == flags.used_list[i] or temptype == 'B' or temptype == 'EXPR':
                        usedflag = 1
                        break             
                if tempcount == 0 and usedflag == 0:
                    last = flags.semantic_type[k]
                    val_last = flags.semantic_stack[k]
                    tempcount = 1
                elif tempcount == 1 and usedflag == 0:
                    second_last = flags.semantic_type[k]
                    val_second_last = flags.semantic_stack[k]
                    break
                k = k-1
        else:
            tempcount = 0
            k = len(flags.semantic_type)-1
            while k>=0:
                tempval = flags.semantic_type[k]
                if tempval == 'EXPR' or tempval[0] =='B':
                    k = k-1
                else:
                    if tempcount == 0:
                        last = flags.semantic_type[k]
                        val_last = flags.semantic_stack[k]
                        tempcount = 1
                    elif tempcount == 1:
                        second_last = flags.semantic_type[k]
                        val_second_last = flags.semantic_stack[k]
                        break
                    k = k-1


        
        if last == 'I$' and second_last =='I$':                                                             # last and second last contain intermediate result  
            if (val_last[0] == 'I' and val_second_last[0] == 'R') or (val_last[0] == 'R' and val_second_last[0] == 'I'): # last and second last of different type.
                flags.real_count = flags.real_count + 1                                                                  #convert integer intermediate result to real
                final = 'R$' + str(flags.real_count)
                if val_last[0] == 'I':

                    temp2 = val_last
                    strlen = len(temp2)
                    name2 = 'R' + temp2[1:strlen] 
                    name1 = val_second_last                    
                elif val_second_last[0] =='I':   

                    temp1 = val_second_last
                    strlen = len(temp1)
                    name1 = 'R' + temp1[1:strlen] 
                    name2 = val_last 
            else:
                if val_last[0] == 'I' and val_second_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                                       # both intermediate result are integer
                    final = 'I$' + str(flags.integer_count)                
                    name1 = val_second_last
                    name2 = val_last
                elif val_last[0] == 'R' and val_second_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                                             # both intermediate result are real
                    final = 'R$' + str(flags.real_count) 
                    name1 = val_second_last
                    name2 = val_last
            usedindex1 = name1
            usedindex2 = name2
         
        elif last == 'I$' and second_last == 'A':                                                           #last intermediate and second last identifier
 
            usedindex1 = val_second_last 
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name1 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_second_last])
                    typeval = flags.global_symbol_table[index][1]
                    name1 = flags.global_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                name1 = flags.global_symbol_table[index][0]
              
            if (typeval == 'INTEGER' and val_last[0] == 'R') or (typeval == 'REAL' and val_last[0] == 'I'):
               flags.real_count = flags.real_count + 1                                                 #convert termediate result to real
               final = 'R$' + str(flags.real_count)
               if val_last[0] == 'I':
                   print "name 2:",val_last

                   temp2 = val_last
                   strlen = len(temp2)
                   name2 = 'R' + temp2[1:strlen]                    
               else:
                   name2 = val_last
            else:
                if typeval == 'INTEGER' and val_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                   # both intermediate result and identifier are integer
                    final = 'I$' + str(flags.integer_count)
                    name2 = val_last  
                elif typeval == 'REAL' and val_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                         # both intermediate result and identifier are real
                    final = 'R$' + str(flags.real_count)
                    name2 = val_last
            usedindex2 = name2
            

        elif last == 'A' and second_last == 'I$':                                                   #second last intermediate and last identifier
            usedindex2 = val_last 
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                typeval = flags.global_symbol_table[index][1]
                name2 = flags.global_symbol_table[index][0]
              
            if (typeval == 'INTEGER' and val_second_last[0] == 'R') or (typeval == 'REAL' and val_second_last[0] == 'I'):
               flags.real_count = flags.real_count + 1                                                 #convert intermediate result to real
               final = 'R$' + str(flags.real_count)
               if val_second_last[0] == 'I':

                   temp1 = val_second_last
                   strlen = len(temp1)
                   name1 = 'R' + temp1[1:strlen]                    
               else:
                   name1 = val_second_last
            else:
                if typeval == 'INTEGER' and val_second_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                   # both intermediate result and identifier are integer
                    final = 'I$' + str(flags.integer_count)
                    name1 = val_second_last 
                elif typeval == 'REAL' and val_second_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                         # both intermediate result and identifier are real
                    final = 'R$' + str(flags.real_count)
                    name1 = val_second_last  
            usedindex1 = name1
        
        elif last == 'A' and second_last == 'A':                                                   #second last and last identifier
            usedindex2 = val_last
            usedindex1 = val_second_last 
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
                name2 = flags.global_symbol_table[index][0]              
            if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
               flags.real_count = flags.real_count + 1                                                 #convert intermediate result to real
               final = 'R$' + str(flags.real_count)                 
            else:
                if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                    flags.integer_count = flags.integer_count + 1                                   # both identifiers are integer
                    final = 'I$' + str(flags.integer_count)                     
                elif typeval == 'REAL' and typeval1 == 'REAL':
                    flags.real_count = flags.real_count + 1                                         # both identifiers are real
                    final = 'R$' + str(flags.real_count)

        flags.semantic_stack.append(name1)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(name2)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
                                          
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(3)
        
        flags.semantic_stack.append(final)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('I$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ final + "," + final[0]+ "DIV" + "," + name1  + "," + name2 + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(final)
        temp_tuples.append(final[0]+ "DIV")
        temp_tuples.append(name1)
        temp_tuples.append(name2)        
        flags.tuples.append(temp_tuples)
        
        flags.used_flag = 1
        flags.used_list.append(usedindex1)
        flags.used_list.append(usedindex2)        
    

    if red_no == 108:
        final = ''




        if flags.used_flag:
            tempcount = 0
            k = len(flags.semantic_stack)-1
            while k>=0:
                usedflag = 0
                tempval = flags.semantic_stack[k]
                temptype = flags.semantic_type[k]   
                for i in range(0,len(flags.used_list)):
                    if tempval == flags.used_list[i] or temptype == 'B' or temptype == 'EXPR':
                        usedflag = 1
                        break             
                if tempcount == 0 and usedflag == 0:
                    last = flags.semantic_type[k]
                    val_last = flags.semantic_stack[k]
                    tempcount = 1
                elif tempcount == 1 and usedflag == 0:
                    second_last = flags.semantic_type[k]
                    val_second_last = flags.semantic_stack[k]
                    break
                k = k-1
        else:              
            tempcount = 0
            k = len(flags.semantic_type)-1
            while k>=0:
                tempval = flags.semantic_type[k]
                if tempval == 'EXPR' or tempval[0] =='B':
                    k = k-1
                else:
                    if tempcount == 0:
                        last = flags.semantic_type[k]
                        val_last = flags.semantic_stack[k]
                        tempcount = 1
                    elif tempcount == 1:
                        second_last = flags.semantic_type[k]
                        val_second_last = flags.semantic_stack[k]
                        break
                    k = k-1

                      
        if last == 'I$' and second_last =='I$':                                                             # last and second last contain intermediate result
            if (val_last[0] == 'I' and val_second_last[0] == 'R') or (val_last[0] == 'R' and val_second_last[0] == 'I'): # last and second last of different type.
                flags.real_count = flags.real_count + 1                                                                  #convert integer intermediate result to real
                final = 'R$' + str(flags.real_count)
                if val_last[0] == 'I':

                    temp2 = val_last
                    strlen = len(temp2)
                    name2 = 'R' + temp2[1:strlen]
                    name1 = val_second_last
                elif val_second_last[0] =='I':   

                    temp1 = val_second_last
                    strlen = len(temp1)
                    name1 = 'R' + temp1[1:strlen]
                    name2 = val_last
            else:
                if val_last[0] == 'I' and val_second_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                                       # both intermediate result are integer
                    final = 'I$' + str(flags.integer_count)
                    name1 = val_second_last
                    name2 = val_last                    
                elif val_last[0] == 'R' and val_second_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                                             # both intermediate result are real
                    final = 'R$' + str(flags.real_count) 
                    name1 = val_second_last
                    name2 = val_last
            usedindex1 = name1
            usedindex2 = name2 
         
        elif last == 'I$' and second_last == 'A':                                                           #last intermediate and second last identifier
            usedindex1 = val_second_last 
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name1 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_second_last])
                    typeval = flags.global_symbol_table[index][1]
                    name1 = flags.global_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                name1 = flags.global_symbol_table[index][0]
              
            if (typeval == 'INTEGER' and val_last[0] == 'R') or (typeval == 'REAL' and val_last[0] == 'I'):
               flags.real_count = flags.real_count + 1                                                 #convert termediate result to real
               final = 'R$' + str(flags.real_count)
               if val_last[0] == 'I':
                   print "name 2:",val_last

                   temp2 = val_last
                   strlen = len(temp2)
                   name2 = 'R' + temp2[1:strlen]
               else:
                   name2 = val_last               
            else:
                if typeval == 'INTEGER' and val_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                   # both intermediate result and identifier are integer
                    final = 'I$' + str(flags.integer_count)
                    name2 = val_last 
                elif typeval == 'REAL' and val_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                         # both intermediate result and identifier are real
                    final = 'R$' + str(flags.real_count)
                    name2 = val_last
            usedindex2 = name2
        
        elif last == 'A' and second_last == 'I$':                                                   #second last intermediate and last identifier
            usedindex2 = val_last
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                typeval = flags.global_symbol_table[index][1]
                name2 = flags.global_symbol_table[index][0]
              
            if (typeval == 'INTEGER' and val_second_last[0] == 'R') or (typeval == 'REAL' and val_second_last[0] == 'I'):
               flags.real_count = flags.real_count + 1                                                 #convert intermediate result to real
               final = 'R$' + str(flags.real_count)
               if val_second_last[0] == 'I':

                   temp1 = val_second_last
                   strlen = len(temp1)
                   name1 = 'R' + temp1[1:strlen] 
               else:
                   name1 = val_second_last               
            else:
                if typeval == 'INTEGER' and val_second_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                   # both intermediate result and identifier are integer
                    final = 'I$' + str(flags.integer_count)
                    name1 = val_second_last                    
                elif typeval == 'REAL' and val_second_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                         # both intermediate result and identifier are real
                    final = 'R$' + str(flags.real_count)
                    name1 = val_second_last
            usedindex1 = name1

        elif last == 'A' and second_last == 'A':                                                   #second last and last identifier
            usedindex1 = val_second_last
            usedindex2 = val_last
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
                name2 = flags.global_symbol_table[index][0]              
            if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
               flags.real_count = flags.real_count + 1                                                 #convert intermediate result to real
               final = 'R$' + str(flags.real_count)                 
            else:
                if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                    flags.integer_count = flags.integer_count + 1                                   # both identifiers are integer
                    final = 'I$' + str(flags.integer_count)                     
                elif typeval == 'REAL' and typeval1 == 'REAL':
                    flags.real_count = flags.real_count + 1                                         # both identifiers are real
                    final = 'R$' + str(flags.real_count)

        flags.semantic_stack.append(name1)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(name2)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(3)    
            
        flags.semantic_stack.append(final)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('I$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ final + "," + final[0]+ "MUL" + "," + name1  + "," + name2 + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(final)
        temp_tuples.append(final[0]+ "MUL")
        temp_tuples.append(name1)
        temp_tuples.append(name2)        
        flags.tuples.append(temp_tuples)       

        flags.used_flag = 1
        flags.used_list.append(usedindex1)
        flags.used_list.append(usedindex2)        

    if red_no == 104:
        final = '' 

        
        if flags.used_flag:                
            tempcount = 0
            k = len(flags.semantic_stack)-1
            while k>=0:
                usedflag = 0
                tempval = flags.semantic_stack[k]
                temptype = flags.semantic_type[k]   
                for i in range(0,len(flags.used_list)):
                    if tempval == flags.used_list[i] or temptype == 'B' or temptype == 'EXPR':
                        usedflag = 1
                        break             
                if tempcount == 0 and usedflag == 0:
                    last = flags.semantic_type[k]
                    val_last = flags.semantic_stack[k]
                    tempcount = 1
                elif tempcount == 1 and usedflag == 0:
                    second_last = flags.semantic_type[k]
                    val_second_last = flags.semantic_stack[k]
                    break
                k = k-1
        else:
            tempcount = 0
            k = len(flags.semantic_type)-1
            while k>=0:
                tempval = flags.semantic_type[k]
                if tempval == 'EXPR' or tempval[0] =='B':
                    k = k-1
                else:
                    if tempcount == 0:
                        last = flags.semantic_type[k]
                        val_last = flags.semantic_stack[k]
                        tempcount = 1
                    elif tempcount == 1:
                        second_last = flags.semantic_type[k]
                        val_second_last = flags.semantic_stack[k]
                        break
                    k = k-1
            

                
        if last == 'I$' and second_last =='I$':                                                             # last and second last contain intermediate result
            if (val_last[0] == 'I' and val_second_last[0] == 'R') or (val_last[0] == 'R' and val_second_last[0] == 'I'): # last and second last of different type.
                flags.real_count = flags.real_count + 1                                                                  #convert integer intermediate result to real
                final = 'R$' + str(flags.real_count)
                if val_last[0] == 'I':

                    temp2 = val_last
                    strlen = len(temp2)
                    name2 = 'R' + temp2[1:strlen]
                    name1 = val_second_last
                elif val_second_last[0] =='I':   

                    temp1 = val_second_last
                    strlen = len(temp1)
                    name1 = 'R' + temp1[1:strlen]
                    name2 = val_last
            else:
                if val_last[0] == 'I' and val_second_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                                       # both intermediate result are integer
                    final = 'I$' + str(flags.integer_count)
                    name1 = val_second_last
                    name2 = val_last                    
                elif val_last[0] == 'R' and val_second_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                                             # both intermediate result are real
                    final = 'R$' + str(flags.real_count)
                    name1 = val_second_last
                    name2 = val_last                    
            usedindex1 = name1
            usedindex2 = name2
         
        elif last == 'I$' and second_last == 'A':                                                           #last intermediate and second last identifier
            usedindex1 = val_second_last
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name1 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_second_last])
                    typeval = flags.global_symbol_table[index][1]
                    name1 = flags.global_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                name1 = flags.global_symbol_table[index][0]
              
            if (typeval == 'INTEGER' and val_last[0] == 'R') or (typeval == 'REAL' and val_last[0] == 'I'):
               flags.real_count = flags.real_count + 1                                                 #convert termediate result to real
               final = 'R$' + str(flags.real_count)
               if val_last[0] == 'I':
                   print "name 2:",val_last

                   temp2 = val_last
                   strlen = len(temp2)
                   name2 = 'R' + temp2[1:strlen]     
               else:
                   name2 = val_last               
            else:
                if typeval == 'INTEGER' and val_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                   # both intermediate result and identifier are integer
                    final = 'I$' + str(flags.integer_count)                     
                    name2 = val_last
                elif typeval == 'REAL' and val_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                         # both intermediate result and identifier are real
                    final = 'R$' + str(flags.real_count)
                    name2 = val_last
            usedindex2 = name2
            
        elif last == 'A' and second_last == 'I$':                                                   #second last intermediate and last identifier
            usedindex2 = val_last   
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                typeval = flags.global_symbol_table[index][1]
                name2 = flags.global_symbol_table[index][0]
              
            if (typeval == 'INTEGER' and val_second_last[0] == 'R') or (typeval == 'REAL' and val_second_last[0] == 'I'):
               flags.real_count = flags.real_count + 1                                                 #convert intermediate result to real
               final = 'R$' + str(flags.real_count)
               if val_second_last[0] == 'I':

                   temp1 = val_second_last
                   strlen = len(temp1)
                   name1 = 'R' + temp1[1:strlen] 
               else:
                   name1 = val_second_last               
            else:
                if typeval == 'INTEGER' and val_second_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                   # both intermediate result and identifier are integer
                    final = 'I$' + str(flags.integer_count)                     
                    name1 = val_second_last
                elif typeval == 'REAL' and val_second_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                         # both intermediate result and identifier are real
                    final = 'R$' + str(flags.real_count)
                    name1 = val_second_last
            usedindex1 = name1
            
        elif last == 'A' and second_last == 'A':                                                   #second last and last identifier
            usedindex1 = val_second_last
            usedindex2 = val_last            
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
                name2 = flags.global_symbol_table[index][0]              
            if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
               flags.real_count = flags.real_count + 1                                                 #convert intermediate result to real
               final = 'R$' + str(flags.real_count)                 
            else:
                if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                    flags.integer_count = flags.integer_count + 1                                   # both identifiers are integer
                    final = 'I$' + str(flags.integer_count)                     
                elif typeval == 'REAL' and typeval1 == 'REAL':
                    flags.real_count = flags.real_count + 1                                         # both identifiers are real
                    final = 'R$' + str(flags.real_count)

        flags.semantic_stack.append(name1)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(name2)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        poplist(3)    
            
        flags.semantic_stack.append(final)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('I$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
                   
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ final + "," + final[0]+ "MINUS" + "," + name1  + "," + name2 + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(final)
        temp_tuples.append(final[0]+ "MINUS")
        temp_tuples.append(name1)
        temp_tuples.append(name2)
        temp_tuples.append("-")  
        flags.tuples.append(temp_tuples) 
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        flags.used_flag = 1
        flags.used_list.append(usedindex1)
        flags.used_list.append(usedindex2)


    if red_no == 103:
        final = ''    


        if flags.used_flag:
            tempcount = 0
            k = len(flags.semantic_stack)-1
            while k>=0:
                usedflag = 0
                tempval = flags.semantic_stack[k]
                temptype = flags.semantic_type[k]   
                for i in range(0,len(flags.used_list)):
                    if tempval == flags.used_list[i] or temptype == 'B' or temptype == 'EXPR':
                        usedflag = 1
                        break             
                if tempcount == 0 and usedflag == 0:
                    last = flags.semantic_type[k]
                    val_last = flags.semantic_stack[k]
                    tempcount = 1
                elif tempcount == 1 and usedflag == 0:
                    second_last = flags.semantic_type[k]
                    val_second_last = flags.semantic_stack[k]
                    break
                k = k-1
        else:
            tempcount = 0
            k = len(flags.semantic_type)-1
            while k>=0:
                tempval = flags.semantic_type[k]
                if tempval == 'EXPR' or tempval[0] =='B':
                    k = k-1
                else:
                    if tempcount == 0:
                        last = flags.semantic_type[k]
                        val_last = flags.semantic_stack[k]
                        tempcount = 1
                    elif tempcount == 1:
                        second_last = flags.semantic_type[k]
                        val_second_last = flags.semantic_stack[k]
                        break
                    k = k-1

        
        if last == 'I$' and second_last =='I$':                                                             # last and second last contain intermediate result
            if (val_last[0] == 'I' and val_second_last[0] == 'R') or (val_last[0] == 'R' and val_second_last[0] == 'I'): # last and second last of different type.
                flags.real_count = flags.real_count + 1                                                                  #convert integer intermediate result to real
                final = 'R$' + str(flags.real_count)
                if val_last[0] == 'I':
                    temp2 = val_last
                    strlen = len(temp2)
                    name2 = 'R' + temp2[1:strlen] 
                    name1 = val_second_last
                elif val_second_last[0] =='I':
                    temp1 = val_second_last

                    strlen = len(temp1)
                    name1 = 'R' + temp1[1:strlen]

                    name2 = val_last
            else:
                if val_last[0] == 'I' and val_second_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                                       # both intermediate result are integer
                    final = 'I$' + str(flags.integer_count)                
                    name1 = val_second_last
                    name2 = val_last
                elif val_last[0] == 'R' and val_second_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                                             # both intermediate result are real
                    final = 'R$' + str(flags.real_count) 
                    name1 = val_second_last
                    name2 = val_last
            usedindex1 = name1
            usedindex2 = name2
                        
        elif last == 'I$' and second_last == 'A':                                                           #last intermediate and second last identifier
            usedindex1 = val_second_last 
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name1 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_second_last])
                    typeval = flags.global_symbol_table[index][1]
                    name1 = flags.global_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                name1 = flags.global_symbol_table[index][0]
              
            if (typeval == 'INTEGER' and val_last[0] == 'R') or (typeval == 'REAL' and val_last[0] == 'I'):
               flags.real_count = flags.real_count + 1                                                 #convert termediate result to real
               final = 'R$' + str(flags.real_count)
               if val_last[0] == 'I':

                   temp2 = val_last
                   strlen = len(temp2)
                   name2 = 'R' + temp2[1:strlen]                 
   
               else:
                   name2 = val_last 
            else:
                if typeval == 'INTEGER' and val_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                   # both intermediate result and identifier are integer
                    final = 'I$' + str(flags.integer_count)                     
                    name2 = val_last
                elif typeval == 'REAL' and val_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                         # both intermediate result and identifier are real
                    final = 'R$' + str(flags.real_count)
                    name2 = val_last
            usedindex2 = name2
            
        elif last == 'A' and second_last == 'I$':                                                   #second last intermediate and last identifier
            usedindex2 = val_last
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                typeval = flags.global_symbol_table[index][1]
                name2 = flags.global_symbol_table[index][0]
              
            if (typeval == 'INTEGER' and val_second_last[0] == 'R') or (typeval == 'REAL' and val_second_last[0] == 'I'):
               flags.real_count = flags.real_count + 1                                                 #convert intermediate result to real
               final = 'R$' + str(flags.real_count)
               if val_second_last[0] == 'I':

                   temp1 = val_second_last
                   strlen = len(temp1)
                   name1 = 'R' + temp1[1:strlen]
               else:
                   name1 = val_second_last               
            else:
                if typeval == 'INTEGER' and val_second_last[0] == 'I':
                    flags.integer_count = flags.integer_count + 1                                   # both intermediate result and identifier are integer
                    final = 'I$' + str(flags.integer_count)                     
                    name1 = val_second_last
                elif typeval == 'REAL' and val_second_last[0] == 'R':
                    flags.real_count = flags.real_count + 1                                         # both intermediate result and identifier are real
                    final = 'R$' + str(flags.real_count)
                    name1 = val_second_last
            usedindex1 = name1
            
        elif last == 'A' and second_last == 'A':                                                   #second last and last identifier
            usedindex1 = val_second_last
            usedindex2 = val_last
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
                name2 = flags.global_symbol_table[index][0]              
            if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
               flags.real_count = flags.real_count + 1                                                 #convert intermediate result to real
               final = 'R$' + str(flags.real_count)                 
            else:
                if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                    flags.integer_count = flags.integer_count + 1                                   # both identifiers are integer
                    final = 'I$' + str(flags.integer_count)                     
                elif typeval == 'REAL' and typeval1 == 'REAL':
                    flags.real_count = flags.real_count + 1                                         # both identifiers are real
                    final = 'R$' + str(flags.real_count)

        elif last == 'NI' and second_last == 'NI':
            name1 = flags.original_integer[flags.semantic_stack[-2]]            
            name2 = flags.original_integer[flags.semantic_stack[-1]]           
            flags.integer_count = flags.integer_count + 1                                  
            final = 'I$' + str(flags.integer_count)
            usedindex1 = ''
            usedindex2 = ''
                     
        elif last == 'NI' and second_last == 'A':                                                   #second last and last identifier
            usedindex1 = ''
            usedindex2 = ''
            if flags.procedure_start == 1:
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
            name2 = flags.original_integer[flags.semantic_stack[-1]]  
            flags.integer_count = flags.integer_count + 1                                  
            final = 'I$' + str(flags.integer_count)
         

        flags.semantic_stack.append(name1)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append(name2)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        poplist(3)    

        flags.semantic_stack.append(final)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('I$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)
            
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ final + "," + final[0]+ "ADD" + "," + name1  + "," + name2 + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(final)
        temp_tuples.append(final[0]+ "ADD")
        temp_tuples.append(name1)
        temp_tuples.append(name2)        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)                                                            
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
        flags.used_flag = 1
        flags.used_list.append(usedindex1)
        flags.used_list.append(usedindex2)
            

    if red_no == 105:

        skipflag = 0

        if (flags.semantic_type[-1] == 'NI' or flags.semantic_type[-1] == 'NR' or flags.semantic_type[-1] == 'A' ):
            skipflag = 1

        if skipflag == 0:
            k = len(flags.semantic_type)-1
            while k>=0:
                tempval = flags.semantic_type[k]
                if tempval == 'I$':
                    break
                else:
                    k = k - 1
               
            val = flags.semantic_stack[k]

            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            flags.semantic_stack.append(val)
            flags.print_semantic_stack.append(flags.semantic_stack[-1])        
                
            if flags.flag[12]:
                print "Semantic stack before reduction:"
                printlist(flags.print_semantic_stack)

            poplist(2)

            if flags.flag[12]:
                print "Semantic stack after reduction:"
                printlist(flags.print_semantic_stack)

                
            if val[0] == 'I':
                flags.integer_count = flags.integer_count + 1
                value = 'I$' + str(flags.integer_count)
            elif val[0] == 'R':
                flags.real_count = flags.real_count + 1
                value = 'R$' + str(flags.real_count)
                
            flags.semantic_stack.append(value)
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            flags.semantic_type.append('I$')

            flags.used_list.append(value)

            if flags.flag[13]:
                prntstr= "                                           Tuple is  ("+ value + "," + value[0]+ "MINUS" + "," + "0"  + "," + val + ")"
                print str(prntstr)

           
        else:
            flags.semantic_stack.append(flags.semantic_stack[-1])
            if (flags.semantic_type[-1] == 'A' ):
                flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
                flags.semantic_type.append('A')
            else:
                flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
                flags.semantic_type.append('NI')
        
            if flags.flag[13]:
                prntstr= "                                           Tuple is  ("+ value + "," + value[0]+ "MINUS" + "," + "0"  + "," + val + ")"
                print str(prntstr)          
         


    if red_no == 99:

        last = flags.semantic_type[-1]
        val_last = flags.semantic_stack[-1]

        second_last = flags.semantic_type[-2]
        val_second_last = flags.semantic_stack[-2]
        
        if last == 'A' and second_last =='A':

            iden1 = flags.original_identifier[val_second_last]
            iden2 = flags.original_identifier[val_last]
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    shape2 = flags.local_symbol_table[index][2]                    
                    if shape2 == 'MATRIX': 
                        print '                                              ERROR ' + iden2 + ' is of shape MATRIX'
                    if shape2 == 'VECTOR': 
                        print '                                              ERROR ' + iden2 + ' is of shape VECTOR'      
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    shape2 = flags.global_symbol_table[index][2] 
                    if shape2 == 'MATRIX': 
                        print '                                              ERROR ' + iden2 + ' is of shape MATRIX'
                    if shape2 == 'VECTOR': 
                        print '                                              ERROR ' + iden2 + ' is of shape VECTOR'
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    shape1 = flags.local_symbol_table[index1][2]     
                    if shape1 == 'MATRIX': 
                        print '                                              ERROR ' + iden1 + ' is of shape MATRIX'
                        name1 = flags.local_symbol_table[index1][0]
                    if shape1 == 'VECTOR': 
                        print '                                              ERROR ' + iden1 + ' is of shape VECTOR'
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    shape1 = flags.global_symbol_table[index1][2]                     
                    if shape1 == 'MATRIX': 
                        print '                                              ERROR ' + iden1 + ' is of shape MATRIX'
                    if shape1 == 'VECTOR': 
                        print '                                              ERROR ' + iden1 + ' is of shape VECTOR'
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])

                if index>=0:
                    typeval = flags.global_symbol_table[index][1]
                    shape2 = flags.global_symbol_table[index][2] 
                    if shape2 == 'MATRIX': 
                        print '                                              ERROR ' + iden2 + ' is of shape MATRIX'
                    if shape2 == 'VECTOR': 
                        print '                                              ERROR ' + iden2 + ' is of shape VECTOR'
                    name2 = flags.global_symbol_table[index][0]
                else:
                    name2 = ''
                if index1>=0:
                    typeval1 = flags.global_symbol_table[index1][1]
                    shape1 = flags.global_symbol_table[index1][2]
                    if shape1 == 'MATRIX': 
                        print '                                              ERROR ' + iden1 + ' is of shape MATRIX'                    
                    if shape1 == 'VECTOR': 
                        print '                                              ERROR ' + iden1 + ' is of shape VECTOR' 
                    name1 = flags.global_symbol_table[index1][0]
                else:
                    name1 = ''
            if name1 != '' and  name2 !='':

                if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
                   final = 'R'                 
                else:
                    if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                        final = 'I'                   
                    elif typeval == 'REAL' and typeval1 == 'REAL':
                        final = 'R' 
                flags.semantic_stack.append(val_second_last)
                flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
                flags.semantic_stack.append('-')
                flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
                flags.semantic_stack.append(val_last)
                flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]]) 
                                           
                                         
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
            
        if name1 != '' and name2 !='':
            poplist(3)                                  
            flags.boolean_count = flags.boolean_count + 1
            string = 'B$' + str(flags.boolean_count)                                  
            flags.semantic_stack.append(string)
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            flags.semantic_type.append('B$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        

        
        if name1 == '':
            print "                                              ERROR Variable " + iden1 + " used but not declared"
        if name2 == '':
            print "                                              ERROR Variable " + iden2 + " used but not declared"
          

        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ string + "," + final[0]+ "EQUAL" + "," + name1  + "," + name2 + ")"
            print str(prntstr) 
           
 
              
    if red_no == 96:

        last = flags.semantic_type[-1]
        val_last = flags.semantic_stack[-1]

        second_last = flags.semantic_type[-2]
        val_second_last = flags.semantic_stack[-2]
        
        if last == 'A' and second_last =='A': 
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
                name2 = flags.global_symbol_table[index][0]              
            if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
               final = 'R'                 
            else:
                if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                    final = 'I'                   
                elif typeval == 'REAL' and typeval1 == 'REAL':
                    final = 'R'
                    

        elif last == 'NI' and second_last =='A': 
            if flags.procedure_start == 1:
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]

            else:
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]              
            if  typeval1 == 'REAL':
                final = 'R'                 
            else:
                final = 'I'
            name2 = flags.original_integer[val_last]    
                    
        flags.semantic_stack.append(val_second_last)
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
        flags.semantic_stack.append(val_last)
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                            
                                     
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(3)                                  
        flags.boolean_count = flags.boolean_count + 1
        string = 'B$' + str(flags.boolean_count)                                  
        flags.semantic_stack.append(string)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('B$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ string + "," + final[0]+ "LTEQ" + "," + name1  + "," + name2 + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(string)
        temp_tuples.append(final[0]+ "LTEQ")
        temp_tuples.append(name1)
        temp_tuples.append(name2)
        temp_tuples.append("-") 
        flags.tuples.append(temp_tuples)                  
        localvar = 0
        pragmatic(temp_tuples, localvar)
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    

    if red_no == 100:

        last = flags.semantic_type[-1]
        val_last = flags.semantic_stack[-1]

        second_last = flags.semantic_type[-2]
        val_second_last = flags.semantic_stack[-2]
        
        if last == 'A' and second_last =='A': 
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
                name2 = flags.global_symbol_table[index][0]              
            if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
               final = 'R'                 
            else:
                if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                    final = 'I'                   
                elif typeval == 'REAL' and typeval1 == 'REAL':
                    final = 'R' 
            flags.semantic_stack.append(val_second_last)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
            flags.semantic_stack.append(val_last)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])                                            
                                         
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(3)                                  
        flags.boolean_count = flags.boolean_count + 1
        string = 'B$' + str(flags.boolean_count)                                  
        flags.semantic_stack.append(string)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('B$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ string + "," + final[0]+ "NOTEQUAL" + "," + name1  + "," + name2 + ")"
            print str(prntstr) 
           
            
                 
    if red_no == 98:
        last = flags.semantic_type[-1]
        val_last = flags.semantic_stack[-1]
        second_last = flags.semantic_type[-2]
        val_second_last = flags.semantic_stack[-2]
        
        if last == 'A' and second_last =='A': 
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
                name2 = flags.global_symbol_table[index][0]              
            if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
               final = 'R'                 
            else:
                if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                    final = 'I'                   
                elif typeval == 'REAL' and typeval1 == 'REAL':
                    final = 'R' 
            flags.semantic_stack.append(val_second_last)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
            flags.semantic_stack.append(val_last)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]]) 
                                                                                    
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(3)                                  
        flags.boolean_count = flags.boolean_count + 1
        string = 'B$' + str(flags.boolean_count)                                  
        flags.semantic_stack.append(string)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('B$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ string + "," + final[0]+ "GTEQ" + "," + name1  + "," + name2 + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(string)
        temp_tuples.append(final[0]+ "GTEQ")
        temp_tuples.append(name1)
        temp_tuples.append(name2)        
        flags.tuples.append(temp_tuples)             

    if red_no == 97:

        final = ''

        if flags.used_flag:        
            tempcount = 0
            k = len(flags.semantic_stack)-1
            while k>=0:
                usedflag = 0
                tempval = flags.semantic_stack[k]
                temptype = flags.semantic_type[k]   
                for i in range(0,len(flags.used_list)):
                    if tempval == flags.used_list[i] or temptype == 'B' or temptype == 'EXPR':
                        usedflag = 1
                        break             
                if tempcount == 0 and usedflag == 0:
                    last = flags.semantic_type[k]
                    val_last = flags.semantic_stack[k]
                    tempcount = 1
                elif tempcount == 1 and usedflag == 0:
                    second_last = flags.semantic_type[k]
                    val_second_last = flags.semantic_stack[k]
                    break
                k = k-1
        else:
            tempcount = 0
            k = len(flags.semantic_type)-1
            while k>=0:
                tempval = flags.semantic_type[k]
                if tempval == 'EXPR' or tempval[0] =='B':
                    k = k-1
                else:
                    if tempcount == 0:
                        last = flags.semantic_type[k]
                        val_last = flags.semantic_stack[k]
                        tempcount = 1
                    elif tempcount == 1:
                        second_last = flags.semantic_type[k]
                        val_second_last = flags.semantic_stack[k]
                        break
                    k = k-1
                    
      #  last = flags.semantic_type[-1]
     #   val_last = flags.semantic_stack[-1]
      #  second_last = flags.semantic_type[-2]
      #  val_second_last = flags.semantic_stack[-2]

        
        if last == 'A' and second_last =='A':
            print " IN A"
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
                name2 = flags.global_symbol_table[index][0]

            if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
               final = 'R'                 
            else:
                if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                    final = 'I'                   
                elif typeval == 'REAL' and typeval1 == 'REAL':
                    final = 'R'

            flags.semantic_stack.append(val_second_last)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
            flags.semantic_stack.append(val_last)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
        
        if last == 'NI' and second_last =='A':
            if flags.procedure_start == 1:
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]              
            if  typeval1 == 'REAL':
                final = 'R'                 
            else:
                final = 'I'
            name2 = flags.original_integer[val_last]
            
            flags.semantic_stack.append(val_second_last)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
            flags.semantic_stack.append(val_last)
            flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])


        if last == 'I$' and second_last =='I$':                                                             # last and second last contain intermediate result  
            if (val_last[0] == 'I' and val_second_last[0] == 'R') or (val_last[0] == 'R' and val_second_last[0] == 'I'): # last and second last of different type.                                                                #convert integer intermediate result to real
                final = 'R'
                
                if val_last[0] == 'I':

                    temp2 = val_last
                    strlen = len(temp2)
                    name2 = 'R' + temp2[1:strlen] 
                    name1 = val_second_last                    
                elif val_second_last[0] =='I':   

                    temp1 = val_second_last
                    strlen = len(temp1)
                    name1 = 'R' + temp1[1:strlen] 
                    name2 = val_last 
            else:
                if val_last[0] == 'I' and val_second_last[0] == 'I':                                                      # both intermediate result are integer
                    final = 'I'                
                    name1 = val_second_last
                    name2 = val_last
                elif val_last[0] == 'R' and val_second_last[0] == 'R':                                                            # both intermediate result are real
                    final = 'R'
                    name1 = val_second_last
                    name2 = val_last
            
            flags.semantic_stack.append(val_second_last)
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
            flags.semantic_stack.append(val_last)
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                            
                                     
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        poplist(3)                                  
        flags.boolean_count = flags.boolean_count + 1
        string = 'B$' + str(flags.boolean_count)                                  
        flags.semantic_stack.append(string)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('B$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ string + "," + final[0]+ "GT" + "," + name1  + "," + name2 + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(string)
        temp_tuples.append(final[0]+ "GT")
        temp_tuples.append(name1)
        temp_tuples.append(name2)        
        temp_tuples.append("-")
        localvar = 0
        pragmatic(temp_tuples, localvar)
        flags.tuples.append(temp_tuples)            
        if flags.flag[20]:
	    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

            print str(prntstr)
     	    temp_tuples = []

     	    temp_tuples.append("20")

      	    temp_tuples.append("FLAG")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-")

      	    temp_tuples.append("-") 
       	    localvar = 0

      	    pragmatic(temp_tuples, localvar)
      	    
            
    if red_no == 95:
        last = flags.semantic_type[-1]
        val_last = flags.semantic_stack[-1]
        second_last = flags.semantic_type[-2]
        val_second_last = flags.semantic_stack[-2]
        
        if last == 'A' and second_last =='A': 
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[val_last])
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    name2 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[val_last])
                    typeval = flags.global_symbol_table[index][1]
                    name2 = flags.global_symbol_table[index][0]
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index = indexglobal(flags.original_identifier[val_last])
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval = flags.global_symbol_table[index][1]
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]
                name2 = flags.global_symbol_table[index][0]              
            if (typeval == 'INTEGER' and typeval1 == 'REAL') or (typeval == 'REAL' and typeval1 == 'INTEGER'):
               final = 'R'                 
            else:
                if typeval == 'INTEGER' and typeval1 == 'INTEGER':
                    final = 'I'                   
                elif typeval == 'REAL' and typeval1 == 'REAL':
                    final = 'R'

        elif last == 'NI' and second_last =='A': 
            if flags.procedure_start == 1:
                index1 = indexlocal(flags.original_identifier[val_second_last])
                if index1 >=0:
                    typeval1 = flags.local_symbol_table[index1][1]
                    name1 = flags.local_symbol_table[index1][0]
                else:
                    index1 = indexglobal(flags.original_identifier[val_second_last])
                    typeval1 = flags.global_symbol_table[index1][1]
                    name1 = flags.global_symbol_table[index1][0]
            else:
                index1 = indexglobal(flags.original_identifier[val_second_last])
                typeval1 = flags.global_symbol_table[index1][1]
                name1 = flags.global_symbol_table[index1][0]              
            if  typeval1 == 'REAL':
                final = 'R'                 
            else:
                final = 'I'
            name2 = flags.original_integer[val_last]    

                    
            flags.semantic_stack.append(val_second_last)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
            flags.semantic_stack.append(val_last)
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]]) 


                                                                                    
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)

        poplist(3)                                  
        flags.boolean_count = flags.boolean_count + 1
        string = 'B$' + str(flags.boolean_count)                                  
        flags.semantic_stack.append(string)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('B$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ string + "," + final[0]+ "LT" + "," + name1  + "," + name2 + ")"
            print str(prntstr)
            
        temp_tuples = []
        temp_tuples.append(string)
        temp_tuples.append(final[0]+ "LT")
        temp_tuples.append(name1)
        temp_tuples.append(name2)        
        flags.tuples.append(temp_tuples) 
        
    if red_no == 93:
        last = flags.semantic_type[-1]
        val_last = flags.semantic_stack[-1]

        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
        flags.semantic_stack.append(val_last)
        flags.print_semantic_stack.append(flags.semantic_stack[-1]) 
                                                                                    
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        poplist(2)                                  
        flags.boolean_count = flags.boolean_count + 1
        string = 'B$' + str(flags.boolean_count)                                  
        flags.semantic_stack.append(string)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('B$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ string + "," + "NOT" + "," + val_last  + "," + "-" + ")"
            print str(prntstr) 

             
    if red_no == 91:
        last = flags.semantic_type[-1]
        val_last = flags.semantic_stack[-1]
        second_last = flags.semantic_type[-2]
        val_second_last = flags.semantic_stack[-2]
        
        flags.semantic_stack.append(val_second_last)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])         
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
        flags.semantic_stack.append(val_last)
        flags.print_semantic_stack.append(flags.semantic_stack[-1]) 
                                                                                    
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        poplist(3)                                  
        flags.boolean_count = flags.boolean_count + 1
        string = 'B$' + str(flags.boolean_count)                                  
        flags.semantic_stack.append(string)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('B$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ string + "," + "AND" + "," + val_second_last  + "," + val_last + ")"
            print str(prntstr) 
        

    if red_no == 88:
        last = flags.semantic_type[-1]
        val_last = flags.semantic_stack[-1]
        second_last = flags.semantic_type[-2]
        val_second_last = flags.semantic_stack[-2]
        
        flags.semantic_stack.append(val_second_last)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])         
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])                                           
        flags.semantic_stack.append(val_last)
        flags.print_semantic_stack.append(flags.semantic_stack[-1]) 
                                                                                    
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        poplist(3)                                  
        flags.boolean_count = flags.boolean_count + 1
        string = 'B$' + str(flags.boolean_count)                                  
        flags.semantic_stack.append(string)
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('B$')

        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)                
        
        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ string + "," + "OR" + "," + val_second_last  + "," + val_last + ")"
            print str(prntstr) 



    if red_no == 84:

        skipflag = 0
        var = 0
        temp = 0
        axpr = flags.semantic_stack[-1]

            
        if (flags.semantic_type[-1] == 'NI' or flags.semantic_type[-1] == 'NR' or flags.semantic_type[-1] == 'A' ):
  
            skipflag = 1

        if skipflag == 0:
            if(axpr[0] == 'R'):
                type1='REAL'
            elif (axpr[0] == 'I'):
                type1='INTEGER'

            k = len(flags.total_list)-1
            while k>=0:
                if flags.total_list[k] == '<-':               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
                   break
                else:
                    k = k - 1
            k = k -1
            k1 = len(flags.original_identifier)-1
            while k1>=0:
                if flags.original_identifier[k1] == flags.total_list[k] :                                                                                                #right of it
                   break
                else:
                    k1 = k1 - 1
            var = flags.original_identifier[k1]
            var_index = k1
            flags.semantic_stack.append(var_index)                                          # Var
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            flags.semantic_stack.append('-')                                          # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[var_index])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    colST = flags.local_symbol_table[index][4]
                    name1 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[var_index])
                    typeval = flags.global_symbol_table[index][1]
                    colST = flags.global_symbol_table[index][4]
                    name1 = flags.global_symbol_table[index][0]                
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name1 = flags.global_symbol_table[index][0]
            
            if(typeval == 'REAL' and typeval != type1):
                flags.real_count = flags.real_count + 1
                value = 'R$' + str(flags.real_count)
                name = axpr
                name2 = value
                flags.semantic_stack.append(value)                                          # Var
                flags.print_semantic_stack.append(flags.semantic_stack[-1])
                
                if flags.flag[13]:
                    prntstr= "                                       Tuple is  ("+ value + "," + "CONVERTIR" + "," +  name  + "," + "-" +  ")"
                    print str(prntstr)  
                    temp_tuples = []
                    temp_tuples.append(value)
                    temp_tuples.append("CONVERTIR")
                    temp_tuples.append(name)
                    temp_tuples.append("-")
                    temp_tuples.append("REAL")
                    flags.tuples.append(temp_tuples)
                    localvar = 0
                    pragmatic(temp_tuples, localvar)        

                    if flags.flag[20]:
                        prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                        print str(prntstr)
                        temp_tuples = []

                        temp_tuples.append("20")

                        temp_tuples.append("FLAG")

                        temp_tuples.append("-")

                        temp_tuples.append("-")

                        temp_tuples.append("-") 
                        localvar = 0

                        pragmatic(temp_tuples, localvar)
      	    
            if(typeval == 'INTEGER' and typeval != type1):
                flags.integer_count = flags.integer_count + 1
                value = 'I$' + str(flags.integer_count)
                name = axpr
                name2 = value
                flags.semantic_stack.append(value)                                          # Var
                flags.print_semantic_stack.append(flags.semantic_stack[-1])

                if flags.flag[13]:
                    prntstr= "                                       Tuple is  ("+ value + "," + "CONVERTRI" + "," +  name  + "," + "-" +  ")"
                    print str(prntstr)
                    
                    temp_tuples = []
                    temp_tuples.append(value)
                    temp_tuples.append("CONVERTRI")
                    temp_tuples.append(name)
                    temp_tuples.append("-")
                    temp_tuples.append("INTEGER")
                    localvar = 0
                    pragmatic(temp_tuples, localvar)
                    flags.tuples.append(temp_tuples)

                    if flags.flag[20]:
                        prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                        print str(prntstr)
                        temp_tuples = []

                        temp_tuples.append("20")

                        temp_tuples.append("FLAG")

                        temp_tuples.append("-")

                        temp_tuples.append("-")

                        temp_tuples.append("-") 
                        localvar = 0

                        pragmatic(temp_tuples, localvar)
                
            if(typeval == type1):
                name2 = axpr
                flags.semantic_stack.append(axpr)
                flags.print_semantic_stack.append(flags.semantic_stack[-1])

            if flags.flag[13]:
                prntstr= "                                           Tuple is  ("+ var + "," + "STORE" + "," + name2  + ","+ "- "+ ")"
                print str(prntstr)
                
                temp_tuples = []
                temp_tuples.append(var)
                temp_tuples.append("STORE")
                temp_tuples.append(name2)
                temp_tuples.append("-")
                temp_tuples.append(typeval) 
                localvar = 0
                pragmatic(temp_tuples, localvar)
                flags.tuples.append(temp_tuples)
                
                if flags.flag[20]:
                    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                    print str(prntstr)
                    temp_tuples = []

                    temp_tuples.append("20")

                    temp_tuples.append("FLAG")

                    temp_tuples.append("-")

                    temp_tuples.append("-")

                    temp_tuples.append("-") 
                    localvar = 0

                    pragmatic(temp_tuples, localvar)
      	    
            if flags.flag[12]:
                print "Semantic stack before reduction:"
                printlist(flags.print_semantic_stack)
                
            poplist(3)           
            flags.semantic_stack.append(name2)    
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            flags.semantic_type.append('I$')
        else:

            k = len(flags.total_list)-1
            while k>=0:
                if flags.total_list[k] == '<-':               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
                   break
                else:
                    k = k - 1
            k = k -1 
            countb=0
            while k>=0:
                if flags.total_list[k] == ']':               #searching for last identifier in total list so that we can check what is to tbe
                    countb=countb+1
                if flags.total_list[k] == '[':
                    countb=countb-1
                if countb == 0:
                    break
                
                k = k - 1       

            k=k-1
            
          
            k1 = len(flags.original_identifier)-1
            while k1>=0:
                if flags.original_identifier[k1] == flags.total_list[k] :                                                                                                #right of it
                   break
                else:
                    k1 = k1 - 1      
            var = flags.original_identifier[k1]
            var_index = k1
            flags.semantic_stack.append(flags.semantic_stack[-1])
            
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[var_index])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                 #   colST = flags.local_symbol_table[index][4]
                  #  name1 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[var_index])
                    typeval = flags.global_symbol_table[index][1]
                   # colST = flags.global_symbol_table[index][4]
                    #name1 = flags.global_symbol_table[index][0]                
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
               # colST = flags.global_symbol_table[index][4]
                #name1 = flags.global_symbol_table[index][0]
                
            if (flags.semantic_type[-1] == 'A' ):
                name = flags.original_identifier[flags.semantic_stack[-1]]
                flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
                flags.semantic_type.append('A')
            elif flags.semantic_type[-1] == 'NI':
                name = flags.original_integer[flags.semantic_stack[-1]]
                flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
                flags.semantic_type.append('NI')
            else:
                name = flags.original_real[flags.semantic_stack[-1]]
                flags.print_semantic_stack.append(flags.original_real[flags.semantic_stack[-1]])
                flags.semantic_type.append('NR')                
            
            if flags.flag[13]:
                prntstr= "                                           Tuple is  ("+ var + "," + "STORE" + "," + name  + ","+ "- "+ ")"
                print str(prntstr)
                
                temp_tuples = []
                temp_tuples.append(var)
                temp_tuples.append("STORE")
                temp_tuples.append(name)
                temp_tuples.append("-")
                temp_tuples.append(typeval) 
                flags.tuples.append(temp_tuples)
                localvar = 0
                pragmatic(temp_tuples, localvar)
                if flags.flag[20]:
                    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                    print str(prntstr)
                    temp_tuples = []

                    temp_tuples.append("20")

                    temp_tuples.append("FLAG")

                    temp_tuples.append("-")

                    temp_tuples.append("-")

                    temp_tuples.append("-") 
                    localvar = 0

                    pragmatic(temp_tuples, localvar)
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)

                
        


    if red_no == 85:

        skipflag = 0
        var = 0
        temp = 0
        axpr = flags.semantic_stack[-1]
      #  vectorsize = flags.semantic_stack[-3]

        if (flags.semantic_type[-1] == 'NI' or flags.semantic_type[-1] == 'NR' or flags.semantic_type[-1] == 'A' ):
            skipflag = 1
            
        if skipflag == 0:   
            if(axpr[0] == 'R'):
                type1='REAL'
            else:
                type1='INTEGER'

            k = len(flags.total_list)-1
            while k>=0:
                if flags.total_list[k] == '<-':               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
                   break
                else:
                    k = k - 1
            k = k -1 
            countb=0
            while k>=0:
                if flags.total_list[k] == ']':               #searching for last identifier in total list so that we can check what is to tbe
                    countb=countb+1
                if flags.total_list[k] == '[':
                    countb=countb-1
                if countb == 0:
                    break
                
                k = k - 1       

            k=k-1
            
          
            k1 = len(flags.original_identifier)-1
            while k1>=0:
                if flags.original_identifier[k1] == flags.total_list[k] :                                                                                                #right of it
                   break
                else:
                    k1 = k1 - 1
            varold = flags.original_identifier[k1-1]        
            var = flags.original_identifier[k1]
            var1 = flags.original_identifier[k1+1]
            
            var_index = k1


            flags.semantic_stack.append(var_index)                                          # Var
            flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
            flags.semantic_stack.append('-')                                          # '-'
            flags.print_semantic_stack.append(flags.semantic_stack[-1])       

            
            if(flags.total_list[k+1]=='[' and flags.total_list[k+3]==']'):
                var = flags.original_identifier[k1]
                var1 = flags.original_identifier[k1+1]

                flags.semantic_stack.append(k1+1)
                vectorsize = flags.original_identifier[flags.semantic_stack[-1]]

                                                                  
                flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
            else:
                flags.semantic_stack.append(vectorsize)


                flags.print_semantic_stack.append(flags.semantic_stack[-1])

                             

            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])

            flags.semantic_stack.append('-')
            flags.print_semantic_stack.append(flags.semantic_stack[-1])

            
                                                                        
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[var_index])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                    colST = flags.local_symbol_table[index][4]
                    name1 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[var_index])
                    typeval = flags.global_symbol_table[index][1]
                    colST = flags.global_symbol_table[index][4]
                    name1 = flags.global_symbol_table[index][0]                
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name1 = flags.global_symbol_table[index][0]

                                                     


            
            if(typeval == 'REAL' and typeval != type1):

                flags.real_count = flags.real_count + 1
                value = 'R$' + str(flags.real_count)
                name = axpr
                name2 = value
                flags.semantic_stack.append(value)                                          # Var
                flags.print_semantic_stack.append(flags.semantic_stack[-1])
                if flags.flag[13]:
                    prntstr= "                                       Tuple is  ("+ value + "," + "CONVERTIR" + "," +  name  + "," + "-" +  ")"
                    print str(prntstr)
                    
                    temp_tuples = []
                    temp_tuples.append(value)
                    temp_tuples.append("CONVERTIR")
                    temp_tuples.append(name)
                    temp_tuples.append("-")
                    temp_tuples.append("REAL")
                    localvar = 0
                    pragmatic(temp_tuples, localvar)                 
                    flags.tuples.append(temp_tuples)                    
                    if flags.flag[20]:
                        prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                        print str(prntstr)
                        temp_tuples = []

                        temp_tuples.append("20")

                        temp_tuples.append("FLAG")

                        temp_tuples.append("-")

                        temp_tuples.append("-")

                        temp_tuples.append("-") 
                        localvar = 0

                        pragmatic(temp_tuples, localvar)
      	    
            if(typeval == 'INTEGER' and typeval != type1):

                flags.integer_count = flags.integer_count + 1
                value = 'I$' + str(flags.integer_count)
                name = axpr
                name2 = value
                flags.semantic_stack.append(value)                                          # Var
                flags.print_semantic_stack.append(flags.semantic_stack[-1])
                if flags.flag[13]:
                    prntstr= "                                         Tuple is  ("+ value + "," + "CONVERTRI" + "," +  name  + "," + "-" +  ")"
                    print str(prntstr)
                    
                    temp_tuples = []
                    temp_tuples.append(value)
                    temp_tuples.append("CONVERTRI")
                    temp_tuples.append(name)
                    temp_tuples.append("-")
                    temp_tuples.append("INTEGER")
                    localvar = 0
                    pragmatic(temp_tuples, localvar)                  
                    flags.tuples.append(temp_tuples)
                    if flags.flag[20]:
                        prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                        print str(prntstr)
                        temp_tuples = []

                        temp_tuples.append("20")

                        temp_tuples.append("FLAG")

                        temp_tuples.append("-")

                        temp_tuples.append("-")

                        temp_tuples.append("-") 
                        localvar = 0

                        pragmatic(temp_tuples, localvar)
      	    
            if(typeval == type1):

                name2 = axpr
                flags.semantic_stack.append(axpr)
                flags.print_semantic_stack.append(flags.semantic_stack[-1])
            

  #          if flags.flag[13]:
   #             prntstr= "                                           Tuple is  ("+ var + "," + "SUBSTORE" + "," + name2  + ","+ str(vectorsize) + ")"
    #            print str(prntstr)                                             

            if flags.flag[13]:
                prntstr= "                                           Tuple is  ("+ var + "," + "SUBSTORE" + "," + name2  + ","+ str(flags.total_list[k+2]) + ")"
                print str(prntstr)
                
                temp_tuples = []
                temp_tuples.append(var)
                temp_tuples.append("SUBSTORE")
                temp_tuples.append(name2)
                temp_tuples.append(str(flags.total_list[k+2]))
                temp_tuples.append(typeval)
                localvar = 0
                pragmatic(temp_tuples, localvar)                        
                flags.tuples.append(temp_tuples)                
                if flags.flag[20]:
                    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                    print str(prntstr)
                    temp_tuples = []

                    temp_tuples.append("20")

                    temp_tuples.append("FLAG")

                    temp_tuples.append("-")

                    temp_tuples.append("-")

                    temp_tuples.append("-") 
                    localvar = 0

                    pragmatic(temp_tuples, localvar)

            if flags.flag[12]:
                print "Semantic stack before reduction:"
                printlist(flags.print_semantic_stack)
                
            flags.semantic_stack.append(name2)    
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            flags.semantic_type.append('I$')
            
            poplist(6)

        else:

            k = len(flags.total_list)-1
            while k>=0:
                if flags.total_list[k] == '<-':               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
                   break
                else:
                    k = k - 1
            k = k -1 
            countb=0
            while k>=0:
                if flags.total_list[k] == ']':               #searching for last identifier in total list so that we can check what is to tbe
                    countb=countb+1
                if flags.total_list[k] == '[':
                    countb=countb-1
                if countb == 0:
                    break
                
                k = k - 1       

            k=k-1
            
          
            k1 = len(flags.original_identifier)-1
            while k1>=0:
                if flags.original_identifier[k1] == flags.total_list[k] :                                                                                                #right of it
                   break
                else:
                    k1 = k1 - 1      
            var = flags.original_identifier[k1]
            vecsize = flags.total_list[k+2]
            var_index = k1
                                       
            if flags.procedure_start == 1:
                index = indexlocal(flags.original_identifier[var_index])
                if index >=0:
                    typeval = flags.local_symbol_table[index][1]
                   # colST = flags.local_symbol_table[index][4]
                    #name1 = flags.local_symbol_table[index][0]
                else:
                    index = indexglobal(flags.original_identifier[var_index])
                    typeval = flags.global_symbol_table[index][1]
                   # colST = flags.global_symbol_table[index][4]
                   # name1 = flags.global_symbol_table[index][0]                
            else:
                    index = indexglobal(flags.original_identifier[var_index])
                    typeval = flags.global_symbol_table[index][1]
                    #colST = flags.global_symbol_table[index][4]
                    #name1 = flags.global_symbol_table[index][0]


            flags.semantic_stack.append(flags.semantic_stack[-1])
            if (flags.semantic_type[-1] == 'A' ):
                name = flags.original_identifier[flags.semantic_stack[-1]]
                flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])
                flags.semantic_type.append('A') 
            else:
                name = flags.original_integer[flags.semantic_stack[-1]]
                flags.print_semantic_stack.append(flags.original_integer[flags.semantic_stack[-1]])
                flags.semantic_type.append('NI')           

            if flags.flag[13]:
                prntstr= "                                           Tuple is  ("+ var + "," + "SUBSTORE" + "," + name + ","+ str(vecsize) + ")"
                print str(prntstr)
                
                temp_tuples = []
                temp_tuples.append(var)
                temp_tuples.append("SUBSTORE")
                temp_tuples.append(name)
                temp_tuples.append(str(vecsize))
                temp_tuples.append(typeval)
                localvar = 0
                pragmatic(temp_tuples, localvar)                        
                flags.tuples.append(temp_tuples)
                if flags.flag[20]:
                    prntstr= "                                           Tuple is (" + "20" + "," + "FLAG" + "," + "-" + ","+ "-" + ")"

                    print str(prntstr)
                    temp_tuples = []

                    temp_tuples.append("20")

                    temp_tuples.append("FLAG")

                    temp_tuples.append("-")

                    temp_tuples.append("-")

                    temp_tuples.append("-") 
                    localvar = 0

                    pragmatic(temp_tuples, localvar)
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)


      


    if red_no == 86:
        var = 0
        temp = 0
        axpr = flags.semantic_stack[-1]

        if(axpr[0] == 'R'):
            type1='REAL'
        else:
            type1='INTEGER'

        k = len(flags.total_list)-1
        while k>=0:
            if flags.total_list[k] == '<-':               #searching for last identifier in total list so that we can check what is to tbe                                                                                 #right of it
               break
            else:
                k = k - 1                
        k = k-1
        countb=0
        while k>=0:
            if flags.total_list[k] == ']':               #searching for last identifier in total list so that we can check what is to tbe
                countb=countb+1
            if flags.total_list[k] == '[':
                countb=countb-1
            if countb == 0:
                break
            
            k = k - 1       

        k=k-1
        k1 = len(flags.original_identifier)-1
        while k1>=0:
            if flags.original_identifier[k1] == flags.total_list[k] :                                                                                                #right of it
               break
            else:
                k1 = k1 - 1
        var = flags.original_identifier[k1]
        var_index = k1
        var = flags.original_identifier[k1]
        var1 = flags.original_identifier[k1+1]
        
        flags.semantic_stack.append(var_index)                                          # Var
        flags.print_semantic_stack.append(flags.original_identifier[flags.semantic_stack[-1]])          
        flags.semantic_stack.append('-')                                          # '-'
        flags.print_semantic_stack.append(flags.semantic_stack[-1])       
        flags.semantic_stack.append(flags.total_list[k+2])
        rows = flags.total_list[k+2]                                  
        flags.print_semantic_stack.append(flags.total_list[k+2])                                         
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])                                         
        flags.semantic_stack.append(flags.total_list[k+4])
        flags.print_semantic_stack.append(flags.total_list[k+4])                                             
        cols = flags.total_list[k+4]                                                     
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_stack.append('-')
        flags.print_semantic_stack.append(flags.semantic_stack[-1])


        if flags.procedure_start == 1:
            index_last = indexlocal(flags.total_list[k+2])
            index_second_last = indexlocal(flags.total_list[k+4])            
            if index_last >=0:
                typelast = flags.local_symbol_table[index_last][1]
                shapelast = flags.local_symbol_table[index_last][2]
            else:
                typelast = flags.global_symbol_table[index_last][1]               
                shapelast = flags.global_symbol_table[index_last][2] 
            if index_second_last >=0:
                typeseclast = flags.local_symbol_table[index_second_last][1]
                shapeseclast = flags.local_symbol_table[index_second_last][2]
            else:
                typeseclast = flags.global_symbol_table[index_second_last][1]
                shapeseclast = flags.global_symbol_table[index_second_last][2]
        else:
            index_last = indexglobal(flags.total_list[k+2])
            index_second_last = indexglobal(flags.total_list[k+4])

            typelast = flags.global_symbol_table[index_last][1]
            typeseclast = flags.global_symbol_table[index_second_last][1]
            shapelast = flags.global_symbol_table[index_last][2]
            shapeseclast = flags.global_symbol_table[index_second_last][2]

            
        if typelast == 'REAL': 
            print '                                              ERROR Subscript ' + flags.total_list[k+2] + ' is of type REAL' 
        if typeseclast == 'REAL': 
            print '                                              ERROR Subscript ' + flags.total_list[k+4] + ' is of type REAL'             
        #if shapelast == 'MATRIX': 
            #print '                                              ERROR Subscript ' + flags.total_list[k+2] + ' is of shape MATRIX'
        #if shapeseclast == 'MATRIX': 
            #print '                                              ERROR Subscript ' + flags.total_list[k+4] + ' is of shape MATRIX'
        #if shapelast == 'VECTOR': 
            #print '                                              ERROR Subscript ' + flags.total_list[k+2] + ' is of shape VECTOR'
        #if shapeseclast == 'VECTOR': 
            #print '                                              ERROR Subscript ' + flags.total_list[k+4] + ' is of shape VECTOR'


        if flags.procedure_start == 1:
            index = indexlocal(flags.original_identifier[var_index])
            if index >=0:
                typeval = flags.local_symbol_table[index][1]
                colST = flags.local_symbol_table[index][4]
                name1 = flags.local_symbol_table[index][0]
            else:
                index = indexglobal(flags.original_identifier[var_index])
                typeval = flags.global_symbol_table[index][1]
                colST = flags.global_symbol_table[index][4]
                name1 = flags.global_symbol_table[index][0]                
        else:
            index = indexglobal(flags.original_identifier[var_index])
            typeval = flags.global_symbol_table[index][1]
            colST = flags.global_symbol_table[index][4]
            name1 = flags.global_symbol_table[index][0]
        
        if(typeval == 'REAL' and typeval != type1):
            flags.real_count = flags.real_count + 1
            value = 'R$' + str(flags.real_count)
            name = axpr
            name2 = value
            flags.semantic_stack.append(value)                                          # Var
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
        
            if flags.flag[13]:
                prntstr= "                                       Tuple is  ("+ value + "," + "CONVERTIR" + "," +  name  + "," + "-" +  ")"
                print str(prntstr)
                
                temp_tuples = []
                temp_tuples.append(value)
                temp_tuples.append("CONVERTIR")
                temp_tuples.append(name)
                temp_tuples.append("-")                
                flags.tuples.append(temp_tuples)
                
        if(typeval == 'INTEGER' and typeval != type1):
            flags.integer_count = flags.integer_count + 1
            value = 'I$' + str(flags.integer_count)
            name = axpr
            name2 = value
            flags.semantic_stack.append(value)                                          # Var
            flags.print_semantic_stack.append(flags.semantic_stack[-1])
            if flags.flag[13]:
                prntstr= "                                       Tuple is  ("+ value + "," + "CONVERTRI" + "," +  name  + "," + "-" +  ")"
                print str(prntstr)
                
                temp_tuples = []
                temp_tuples.append(value)
                temp_tuples.append("CONVERTRI")
                temp_tuples.append(name)
                temp_tuples.append("-")                
                flags.tuples.append(temp_tuples)
                
        if(typeval == type1):
            name2 = axpr
            flags.semantic_stack.append(axpr)
            flags.print_semantic_stack.append(flags.semantic_stack[-1])        
     
        flags.integer_count = flags.integer_count + 1
        
        if flags.flag[13]:                                          
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IMULT" + "," + rows + ","+ colST + ")"
            print str(prntstr)
            
            temp_tuples = []
            temp_tuples.append("I$" + str(flags.integer_count))
            temp_tuples.append("IMULT")
            temp_tuples.append(rows)
            temp_tuples.append(colST)                
            flags.tuples.append(temp_tuples)
                
        flags.integer_count = flags.integer_count + 1
        temp_count = flags.integer_count
        if flags.flag[13]:        
            prntstr= "                                           Tuple is  ("+ "I$" + str(flags.integer_count) + "," + "IADD" + "," +  "I$" + str(flags.integer_count-1)  + ","+ cols + ")"
            print str(prntstr)
            
            temp_tuples = []
            temp_tuples.append("I$" + str(flags.integer_count))
            temp_tuples.append("IADD")
            temp_tuples.append(  "I$" + str(flags.integer_count-1))
            temp_tuples.append(cols)                
            flags.tuples.append(temp_tuples)            

        if flags.flag[13]:
            prntstr= "                                           Tuple is  ("+ var + "," + "SUBSTORE" + "," + name2  + ","+ "I$" + str(flags.integer_count) + ")"
            print str(prntstr)
            
            temp_tuples = []
            temp_tuples.append(var)
            temp_tuples.append("SUBSTORE" )
            temp_tuples.append(name2)
            temp_tuples.append("I$" + str(flags.integer_count))                
            flags.tuples.append(temp_tuples)
            
        if flags.flag[12]:
            print "Semantic stack before reduction:"
            printlist(flags.print_semantic_stack)
        poplist(8)           
        flags.semantic_stack.append(name2)    
        flags.print_semantic_stack.append(flags.semantic_stack[-1])
        flags.semantic_type.append('I$')
        
        if flags.flag[12]:
            print "Semantic stack after reduction:"
            printlist(flags.print_semantic_stack)        


        
          
              
        
        
             
        

    
    

