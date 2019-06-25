u = ['a','a','b','a','c','b']
a = 0
b = 0
c = 0
for x in u:
	if x == 'a':
		a = a + 1	
		
	elif x == 'b':
		b = b + 1
		
	elif x == 'c':
		c = c + 1
		
d = {'a':a,'b':b,'c':c}
print(d)

str_list = ['a', 'a', 'b', 'a', 'b', 'c']
s = set(str_list)
d = dict.fromkeys(s, 0)
for i in s:
    d[i] = str_list.count(i)
print(d)