
mu_list = "This is a test string".split()
print(mu_list)

#改变比较规则, 传入比较规则的函数
print(sorted(mu_list, key=str.lower))

def change_lower(str_name):
     return str_name.lower()

print(sorted(mu_list, key=change_lower))

print("-"*50)


student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('dave', 'B', 10),
]



print(sorted(student_tuples, key = lambda x:x[2]))

#排字典,

mydict = {
     'Li' : ['M',7],
     'Zhang': ['E',2],
     'Wang' : ['P',3],
     'Du' : ['C',2],
     'Ma' : ['C',9],
     'Zhe' : ['H',7]
}

#注意不要漏了.item()
print(sorted(mydict.items(), key = lambda x:(x[1][1],x[1][0])))
#key填的是一个元组, 元组也是可以比较的, 先比前面后比后面