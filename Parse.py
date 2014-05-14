import re
from dict import*
import flags
import copy
from semantic import*

stack = []

spf = open("spfile.txt","r")

handle = []
panic_flag = []
temp_data = []
ignore_data = []

found = 0
found1 = 0
index_j = 0
reduction_found = False

list1 = []
list2 = []
list3 = []

list3_regex = re.compile(r'(\d)');

line = spf.readline()

line = spf.readline()

while line:
      global found1
      global found 

   
      if "00000" in line: found1 = 1

     
      if found!=1:
           list1.append(line) 

      
      if "real" in line:     
           line = spf.readline()
           found = 1
    

      if found and found1!=1:
           column = line.split()
           list2.append(column)


      if found1:     
           outline = list3_regex.findall(line)             
           if outline:             
                 list3.append(outline)
                  
              
           
      line = spf.readline()

spf.close()

def parse_fun(input_token):
      

    global list1
    global list2
    global list3
    global stack
    global index_j
    global handle
    global panic_flag
    global temp_data
    global ignore_data   
    handle = []
 
    if not stack:       
          stack.append(int(input_token))                   
    else:
          if panic_flag == True:
                if input_token == 59:
                      set1= set(stack)
                      set2 = set(temp_data)
                      unmatched = set1.symmetric_difference(set2)
                      unmatched_list = list(unmatched)
                      print "Symbols popped from stack ",get_list(reservedt,unmatched_list)
                      stack = []
                      stack = copy.deepcopy(temp_data)
                      ignore_data.append(input_token)
                      panic_flag = False
                      print "Symbols ignored",get_list(reservedt,ignore_data)
                      ignore_data = []
                else:
                      ignore_data.append(input_token)
  
          else:
                
                lastelement = stack[-1]
                lastelement = int(lastelement)
                relation1 = list3[lastelement-1][int(input_token)-1]

              
                if relation1 == '0':
                      print "Character Pair Error between ",get_value(reservedt,lastelement)," and ",get_value(reservedt,input_token)
                      ignore_data.append(input_token)
                      panic_flag = True

                      
                if flags.flag[9] == 1:
                      print"Top of the stack: ",get_value(reservedt,int(stack[-1]))
                      print"Input Symbol: ",get_value(reservedt,input_token)
                      print"Relation: ",get_value(relation_dict,int(relation1))

            
                if(int(list3[lastelement-1][int(input_token)-1]) == 1 or int(list3[lastelement-1][int(input_token)-1]) == 3):     #less than | Equal
                      stack.append(int(input_token))

                
                elif(int(list3[lastelement-1][int(input_token)-1]) == 2):                                              #Greater than
                      if flags.flag[8]==1:
                            print "Stack before Reduction:",get_list(reservedt,stack)
                      handle.insert(0,stack[-1])
                      stack.pop()

                      
                      if stack:
                            relation = list3[int(stack[-1])-1][int(handle[0])-1]
                            if relation == '0':
                                  print "Character Pair Error between ",get_value(reservedt,stack[-1])," and ",get_value(reservedt,handle[0])
                                  panic_flag = True                      
                      else:
                            relation = '2'  #error

                      
                      while relation == '1':
                            handle.insert(0,stack[-1])
                            stack.pop()
                            if stack:
                                  relation = list3[int(stack[-1])-1][int(handle[0])-1]
                                  if relation == '0':
                                        print "Character Pair Error between ",get_value(reservedt,stack[-1])," and ",get_value(reservedt,handle[0])
                                        panic_flag = True
                            else:
                                  relation = '2'

                         
                      redlist_index = 0      
                      for redlist in list2:
                            redlist_index = redlist_index + 1

                            if   int(redlist[0]) == len(handle) :                             #Check if entire string is getting reduced
                                  redlist = map(int,redlist)


                                  if handle == redlist[1:-1]:
                                        if flags.flag[10] == 1:
                                              print "Matched handle: ",get_list(reservedt,handle)            
                                        global reduction_found
                                        reduction_no = redlist_index
                                        
                                        for m in range(0,len(flags.valid_reduction)):
                                              if reduction_no == flags.valid_reduction[m]:
                                                    flags.semantic_flag = 1
                                                    break
                                        if flags.semantic_flag == 1:
                                               for k in range(1,len(redlist)-1):
                                                       flags.syntax_stack.append(redlist[k])
         
                                        semantic_fun(reduction_no)        
      
                                        if flags.semantic_flag == 1:
                                               flags.semantic_flag = 0
                                               itr = 1
                                               while itr<=redlist[0]:
                                                      flags.syntax_stack.pop()
                                                      itr = itr+1
                                               flags.syntax_stack.append(redlist[-1])
                                               
                                        stack.append(redlist[-1])                      
                                        string =  "Reduction #" + str(reduction_no) + ": " + get_value(reservedt,int(redlist[-1])) + " --> "
                                        for k in range(1,len(redlist)-1):
                                              string = string + " " +  get_value(reservedt,int(redlist[k]))
                                        if flags.flag[7] == 1:
                                              print string
                                        if flags.flag[8] == 1:
                                              print "Stack after Reduction:",get_list(reservedt,stack)
                                        if int(stack[-1]) == 6:
                                              temp_data = []
                                              temp_data = copy.deepcopy(stack)
                                        if int(stack[-1]) == 23:
                                              temp_data = []
                                              temp_data = copy.deepcopy(stack)
                                        handle = []
                                        reduction_found = True
                                       
                      if reduction_found == True:
                            parse_fun(input_token)
                                  


def parse_last():

    global list1
    global list2
    global list3
    global stack
    global index_j
    global handle
    
    handle.insert(0,stack.pop())

    if not stack:
          relation = '2' 
    
          
    else:
          if flags.flag[8] == 1:
                print "Stack before Reduction:",get_list(reservedt,stack)

          lastelement = stack[-1]
          lastelement = int(lastelement)          
          relation = list3[lastelement-1][int(handle[0])-1]

          while relation == '1':
                handle.insert(0,stack[-1])
                stack.pop()
                if stack:
                      relation = list3[int(stack[-1])-1][int(handle[0])-1]                         
                else:
                      relation = '2'
 
          redlist_index = 0            
          for redlist in list2:
                redlist_index = redlist_index + 1
                        
                if   int(redlist[0]) == len(handle) :                             #Check if entire string is getting reduced 
                      redlist = map(int,redlist)

                      if handle == redlist[1:-1]:
                            if flags.flag[10] == 1:
                                  print "Matched handle: ",get_list(reservedt,handle)
        
                            stack.append(redlist[-1])
               
                            reduction_no = redlist_index
                            for m in range(0,len(flags.valid_reduction)):
                                  if reduction_no == flags.valid_reduction[m]:
                                        flags.semantic_flag = 1
                                        break
                            if flags.semantic_flag == 1:
                                  for k in range(1,len(redlist)-1):
                                        flags.syntax_stack.append(redlist[k])                            
                            semantic_fun(reduction_no)
                            if flags.semantic_flag == 1:
                                  flags.semantic_flag = 0
                                  itr = 1
                                  while itr<=redlist[0]:
                                        flags.syntax_stack.pop()
                                        itr = itr+1
                            flags.syntax_stack.append(redlist[-1])

                                           
                            string =  "Reduction #" + str(reduction_no) + ": " + get_value(reservedt,int(redlist[-1])) + "-->"
                            for k in range(1,len(redlist)-1):
                                    string = string + " " + get_value(reservedt,int(redlist[k]))
                            if flags.flag[7] == 1:        
                                  print string                                                      
                            if flags.flag[8] == 1:
                                  print "Stack after Reduction:",get_list(reservedt,stack)
                            handle = []
                            
                           # for k in range(0,len(flags.tuples)):
                            #         print ("( " + flags.tuples[k][0] + "," + flags.tuples[k][1] +
                             #              "," + flags.tuples[k][2] + "," + flags.tuples[k][3]+"," + flags.tuples[k][4] + ")")      






                                 
