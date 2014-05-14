import re
import dict
import sys
from dict import*
import datetime
from Parse import*
import flags


print "Pragmatics Output".rjust(50)
print""
print "Name : Parag Acharya,Ravi Mandliya "
print "Email: pachary@clemson.edu,rmandli@clemson.edu"
print "Time stamp: ",datetime.datetime.now()
print ""
print""


flagx = 0       #Flag set when data found before ..../* in multiline comments
flagy = 0       #Flag set when data found after  */..... in multiline comments
flagz = 0       #Flag set when  .../*.....*/..... found in a single line 
fin_out_mul = ""

     

for x in range(0,33):
    flags.flag.append(0)
    
flags.flag[1] = 1   #Print source lines
flags.flag[2] = 0   #Print the lexical token and the code
input_token = []


def reserve(token):                      #Validating if the reserve word is within the specified reserve words
    expr = re.compile("END|PROGRAM|DECLARE|SCALAR|VECTOR|MATRIX|REAL|INTEGER|PROCEDURE|VALUE|REFERENCE|EXECUTE|STDIN|STOUT|CALL|ELSE|IF|THEN|FOR|BY|UNTIL|DO")
    out = expr.match(token)
    if flags.flag[2]:
        if out:
            data = "TOKEN : " + str(token) +" CODE : " + str(reservedt[token])
            
            print data.rjust(50)

        else  :
            data= "Invalid Reserved Word : " + str(token)
            print data.rjust(50)
    if out:
        flags.original_reserve.append(token)
        flags.total_list.append(token)
        parse_fun(reservedt[token])


def identifier(token):                   #Validating if the identifier is less than 16
    expr = re.compile("""start|
           prog|
           body|
       declpart|
       decllist|
      decllist-|
       declstat|
      declstat-|
           type|
       procpart|
       proclist|
           proc|
       prochead|
       procname|
      null-list|
      fparmlist|
     fparmlist-|
         callby|
       execpart|
       exechead|
       statlist|
      statlist-|
           stat|
         instat|
        instat-|
       instathd|
        outstat|
       outstat-|
      outstathd|
       callstat|
       callname|
      aparmlist|
     aparmlist-|
         ifstat|
         ifthen|
         ifhead|
        forinit|
          forby|
          forto|
        forstat|
     assignstat|
         astat-|
          bexpr|
         orexpr|
        andexpr|
       andexpr-|
        notexpr|
        relexpr|
          aexpr|
         aexpr-|
           term|
          term-|
        primary|
       constant|
       real
""",re.VERBOSE)
    out = expr.match(token)
    count=len(token)
    if flags.flag[2]:
        if count>16:
            data ="Invalid identifier : "+ str(token)
            print data.rjust(50)
            print "Identifiers should be at most 16 characters of the form ([a-z][\w_]*)".rjust(50)
       
        else:
              if out:
                     data = "TOKEN : " + str(token) + " CODE : " + str(reservedt[token])
                     print data.rjust(50)   
              else:
                    tokenid = 'var'
                    data = "TOKEN : " + str(token) + " CODE : " + str(reservedt[tokenid])
                    print data.rjust(50)
    if count<17 and out:
        flags.original_identifier.append(token)
        flags.total_list.append(token)
        parse_fun(reservedt[token])
    if count<17:
        tokenid = 'var'
        flags.original_identifier.append(token)
        flags.total_list.append(token)        
        parse_fun(reservedt[tokenid])
         
             
   
def int_fun(token):                        #Validating if the number is integer is <= 9  
    tokenid_int = 'integer'
    count = len(token)

    if flags.flag[2]:
 
         if  count < 10:
               data = "TOKEN : "+ str(token) + " CODE : " + str(reservedt[tokenid_int])
               print data.rjust(50)
         else:
               data = "Invalid Integer Number : " + str(token)
               print data.rjust(50)
               print "The number has more than 9 significant digits".rjust(50)
    if count<10:
        flags.original_integer.append(token)
        flags.total_list.append(token)      
        parse_fun(reservedt[tokenid_int])
        
            
        
def real(token):                        #Validating if the real value is <= 7   
    tokenid_real= 'real'
    count = len(token)

    if flags.flag[2]:

         if  count < 8:
               data = "TOKEN : "+ str(token) + " CODE : " + str(reservedt[tokenid_real])
               print data.rjust(50)

         else:
               data = "Invalid Real Number : " + str(token)
               print data.rjust(50)
               print "The number has more than 7 significant digits".rjust(50)
    if count < 8:
        flags.original_real.append(token)
        flags.total_list.append(token)   
        parse_fun(reservedt[tokenid_real])
        
     

def string(token):                               #String within "..."
    tokenid_str = 'string'

    if flags.flag[2]:
        data = "TOKEN : " + str(token) + " CODE :" + str(reservedt[tokenid_str])
        print data.rjust(50)
    flags.total_list.append(token)  
    parse_fun(reservedt[tokenid_str])


def ascii(token):                                 #Multiple ascii characters
    if flags.flag[2]:
        data = "TOKEN : " + str(token) + " CODE : " + str(reservedt[token])
        print data.rjust(50)
    flags.total_list.append(token)
    parse_fun(reservedt[token])


def singleline(sinline):                          #Extract data  .....//  from  single line comments
    
    singlec = sc.match(sinline)
    out_sin = ""
    if singlec:
         out_sin = sc.sub(singlec.group(2),sinline)
    else : out_sin = sinline     
    return out_sin

def multiline(sinline):                           #Extract data ...../*  or */....... from multi line commentts
    multic = mc.match(sinline)
      
    global flagx
    global flagy
    global fin_out_mul

    if  multic:
        
        if multic.lastindex==1:
         
            
            flagx = 1
                  
            fin_out_mul = mc.sub(multic.group(2),sinline)
     
    
        
        if multic.lastindex==3:
      
            
             flagy = 1
             flagx = 0
       
             fin_out_mul = fin_out_mul +" " + mc.sub(multic.group(4),sinline)
     
                 
    else: fin_out_mul = sinline
           
    return fin_out_mul
    

def nomatch(token):                            #None of the regular expressions matched              
    ascii_value = ord(token)
    if flags.flag[2]:
        data = "Invalid ASCII character : "+str(token)+" ASCII value is : " + str(ascii_value)
        print data.rjust(50)
    

def flagfun(token,line):                            #Turning on corressponding flag for '+' and turning it off for '-'
    
  
    reg1 = re.compile('([\+\-])([0-9]+)')
    iterator = re.finditer(reg1,line)
    for match in iterator:
        if match.group(1) == '+':
            flags.flag[int(match.group(2))] = 1
        else:
            flags.flag[int(match.group(2))] = 0
                
    return None



       

sc = re.compile(r'((.*)//.*$)')                  #......//....... 

mc = re.compile(r"""                             
                ((.*)/\*.*)                      #1 ..../*   
                |(.*\*/(.*))                     #2 */....
                """,re.VERBOSE)

mc2 = re.compile(r'((.*?)/\*.*?\*/(.*))')        #..../*.....*/....

strre = re.compile(r'(.*\".*/\*.*\*/(.*)\".*)')  # ...."...../*....*/...."....

 

intoken = re.compile(r"""
    ([A-Z]+)                                                                                                    # 1. Reserve Words
    |([a-z][\w_]*)                                                                                              # 2. Identifiers
    |([0-9]+[\.][0-9]+)                                                                                                  # 3. Real Number
    |([0-9]+)                                                                                                     # 4. Integers
    |(\".*?\")                                                                                                  # 5. String
    |(\s+)                                                                                                      # 6. whitespace
    |([\=]{2} | [\!][\=]{0,1} | [\<][\=\-]{0,1} | [\>][\=]{0,1} | [\:]{1,2} | [\;\,\[\]\(\)\+\*\/\{\}\&\|\-] )  # 7. Multiple Ascii characters
    |(\s*?[\#]{2}[\+\-]\d*[\+\-]?\d*?.*?[\#]{2})                                                                 # 8. Flag     
    |(.)                                                                                                        # 9. No match
    
    """, re.VERBOSE)    


flagfind = re.compile(r'(^\s*?[\#]{2}[\+\-]\d*[\+\-]?\d*?.*?[\#]{2})')       


f = open('static.txt',"r")

sinline = f.readline()



while sinline:

    if flagz==1:
            flagy = 0
        

    outflag = flagfind.match(sinline)
    if outflag:
            flagfun(outflag.group(0),sinline)
   

    if flags.flag[1]:
        print " "
        print"INPUT LINE: ",sinline
      
   
    output_sc= singleline(sinline)
    output_mc = multiline(output_sc)
    output_mc2 = mc2.match(sinline)
    output_str = strre.match(sinline)

    if output_mc2:
         while output_mc2:
                
                output_mc = output_mc2.group(2) + " " + output_mc2.group(3)
                output_mc2 = mc2.match(output_mc)
                    
                flagx = 0
                flagz = 1
       
    while flagx and flagy==0:
     
         sinline = f.readline()
         output_mc = multiline(sinline)
         if flags.flag[1]:
             print " "
             print "INPUT LINE: ",sinline
             
         
  
    if output_str:     
        output_mc = output_str.group(0)
        
    
  
    scan = intoken.scanner(output_mc)
            
 
    while 1:
         m = scan.match()
   
         if not m:
             break
     
         if m.lastindex==8:
            flagfun(m.group(m.lastindex),output_mc)
         
            
         if m.lastindex==1:
            reserve(m.group(m.lastindex))
         if m.lastindex==2:
            identifier(m.group(m.lastindex))
         if m.lastindex==4:
            int_fun(m.group(m.lastindex))
         if m.lastindex==5:
            string(m.group(m.lastindex))
         if m.lastindex==7:
            ascii(m.group(m.lastindex))   
         if m.lastindex==9:
            nomatch(m.group(m.lastindex))
         if m.lastindex==3:
            real(m.group(m.lastindex))   
   
    sinline = f.readline()
   
       
f.close()
parse_last()





