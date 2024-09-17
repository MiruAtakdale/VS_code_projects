import os
# obrazky.py
# texty.py
# gify.py
jmena_slozek = ("obrazky","texty", "gify")

for jmeno in jmena_slozek:
   
    if os.path.exists(jmeno) and os.path.isdir(jmeno):
        print('Složka již existuje!') 
    
    else: 
        print('Tvořím novou složku:',jmeno)
        os.mkdir(jmeno)
 
print ('Všechny složky existují')