flag = []
procedure_start = 0
syntax_stack = []
semantic_stack = []
original_identifier = []
original_integer = []
original_real = []
original_reserve = []
global_symbol_table = []
local_symbol_table = []
print_reg = 12
print_reg1 = 12
valid_reduction = [1,2,10,11,12,13,14,15,19,20,23,26,27,28,29,30,31,32,33,46,47,48,49,50,51,52,55,56,57,58,59,60,61,62,63,64,66,
                   67,68,69,70,71,74,76,84,85,86,88,91,93,95,96,97,98,99,100,117,116,115,114,113,111,109,108,105,104,103]
semantic_flag = 0
print_semantic_stack = []
total_list = []
integer_count = 0
real_count = 0
boolean_count = 0
semantic_type = []        # NI - integer number,NR-real number,A - identifier, D- dash,LST-local symbol table,GST-global symbot table , V - reserved words REAL,INTEGER,
                          # VALUE,REFERENCE,STRNG - String , I$ - Intermediate result , EXPR - expression , B$ - boolean expr , INTIND - int index , RELIND - real index
                          # AIND - identifier used as an index

used_flag = 0
used_list = []
label_counter = 0
for_loop = 0
tuples = []
global_list = []
local_list = []
var_reg = {}
printf_flag = 0
localintegers = []
globalintegers = []
condition = ''
print_counter = 0
datasection = []
print_register = 0
printregcontent = []
globalreal = []
realnos = []
