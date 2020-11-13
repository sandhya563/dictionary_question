# while useing pop method
Dic= {
        1: 'NAVGURUKUL',
        2: 'IN',  
  	    3: {    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'
            }
        }
add=Dic.get(3)
add.pop('A')
Dic[3]=add
print(Dic)


# while useing del method
Dic= {
        1: 'NAVGURUKUL',
        2: 'IN',  
  	    3: {    
             'A' : 'WELCOME',
             'B' : 'To',
             'C' : 'DHARAMSALA'
            }
        }
del Dic [3]['A']
print(Dic)
