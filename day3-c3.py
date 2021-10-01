name1 = input("Please enter your name\n")
name2 = input("Please enter second name\n")

truec = 0
lovec = 0

t_count = name1.count("t")
r_count = name1.count("r")
u_count = name1.count("u")
e_count = name1.count("e")

truec =  truec + t_count + r_count + u_count + e_count



l_count = name1.count("l")
o_count = name1.count("o")
v_count = name1.count("v")
e_count = name1.count("e")

lovec = lovec +  l_count + o_count + v_count + e_count

t_count = name2.count("t")
r_count = name2.count("r")
u_count = name2.count("u")
e_count = name2.count("e")

truec =  truec + t_count + r_count + u_count + e_count


l_count = name2.count("l")
o_count = name2.count("o")
v_count = name2.count("v")
e_count = name2.count("e")

lovec = lovec +  l_count + o_count + v_count + e_count


print(truec)
