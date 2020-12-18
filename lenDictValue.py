dict =  {
2	   'Alex': ['subj1', 'subj2', 'subj3'], 
3	   'David': ['subj1', 'subj2']}
4	count=0
5	for key in dict:
6	    for value in dict[key]:
7	        count=count+1
8	print(count)