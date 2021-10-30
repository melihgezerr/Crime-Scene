f = open("crime_scene.txt")
sol1 = open("solution_part1.txt", "w")
sol2 = open("solution_part2.txt", "w")
sol3 = open("solution_part3.txt", "w")
list_of_lines = f.read().splitlines()
w_limit = int(list_of_lines[0].split()[0])
t_limit = int(list_of_lines[0].split()[1])
number_of_evi = int(list_of_lines[1])
dict_of_evi = {}                    ## ID ===  WEİGHT  ,  TİME  ,  VALUE.
psble_evi_vals = []                 ## VALUEsum   WEİGHTsum  ,  TİMEsum  ,  ID-list
def creating_initial_dict(dicttt, num=0):
    if num == number_of_evi:
        return dicttt
    list_for_append = []
    list_for_append.append((int((list_of_lines[num+2]).split()[1])))
    list_for_append.append((int((list_of_lines[num+2]).split()[2])))
    list_for_append.append((int((list_of_lines[num+2]).split()[3])))
    dicttt[int(list_of_lines[num+2].split()[0])] = list_for_append
    creating_initial_dict(dicttt, num+1)
creating_initial_dict(dict_of_evi, 0)
id_list = list(dict_of_evi)
id_subsets = []

def sorttt(l):
    asd = 0
    while asd < len(l):
        abc = asd+1
        while abc < len(l):
            if l[asd] < l[abc]:
                l[asd], l[abc] = l[abc], l[asd]
            abc = abc +1
        asd = asd +1

def sortt_3d(l):
    asd = 0
    while asd < len(l):
        abc = asd+1
        while abc < len(l):
            if l[asd][0] < l[abc][0]:
                l[asd], l[abc] = l[abc], l[asd]
            abc = abc +1
        asd = asd +1

def list_of_subsets(listt , emp_list):
    if len(listt) == 0:
        return
    if listt not in emp_list:
        emp_list.append(listt)
    ids = 0
    while ids < len(listt):
        list_of_subsets(listt[:ids]+listt[ids+1:], emp_list)
        ids += 1
list_of_subsets(id_list, id_subsets)

def list_parts(sublist):
    sorttt(sublist)
    sublist.reverse()
    sublstt = []
    sum_weigh = 0
    sum_time = 0
    sum_value = 0
    x = 0
    while x < len(sublist):
        sum_weigh = sum_weigh + dict_of_evi[sublist[x]][0]
        sum_time = sum_time + dict_of_evi[sublist[x]][1]
        sum_value = sum_value + dict_of_evi[sublist[x]][2]
        x = x+1
    sublstt = [sum_value ,sum_weigh, sum_time, sublist]
    return sublstt

iter = len(id_subsets) - 1
def arranging(subsets, iteration, last_list):
    if iteration == -1:
        return
    last_list.append(list_parts(subsets[iteration]))
    arranging(subsets, iteration-1, last_list)
arranging(id_subsets, iter, psble_evi_vals)


my_evi_val_list = []
x = 0
while x < len(psble_evi_vals):
    my_evi_val_list.append(psble_evi_vals[x][0])
    x += 1

sorttt(my_evi_val_list)
sortt_3d(psble_evi_vals)

def sol_1(psbl_dict):
    iter = 0
    while iter < len(psbl_dict):
        if psbl_dict[iter][1] <= w_limit:
            sol1.write(str(psbl_dict[iter][0])+"\n")
            x = 0
            while x < len(psbl_dict[iter][3]):
                if x != len(psbl_dict[iter][3]) - 1:
                    sol1.write(str(psbl_dict[iter][3][x])+ " ")
                else:
                    sol1.write(str(psbl_dict[iter][3][x]))
                x = x+1
            return
        iter +=1
sol_1( psble_evi_vals )

def sol_2(psbl_dict):
    iter = 0
    while iter < len(psbl_dict):
        if psbl_dict[iter][2] <= t_limit:
            sol2.write(str(psbl_dict[iter][0])+"\n")
            x = 0
            while x < len(psbl_dict[iter][3]):
                if x != len(psbl_dict[iter][3]) - 1:
                    sol2.write(str(psbl_dict[iter][3][x])+ " ")
                else:
                    sol2.write(str(psbl_dict[iter][3][x]))
                x = x+1
            return
        iter +=1
sol_2( psble_evi_vals )

def sol_3(psbl_dict):
    iter = 0
    while iter < len(psbl_dict):
        if psbl_dict[iter][2] <= t_limit and psbl_dict[iter][1] <= w_limit :
            sol3.write(str(psbl_dict[iter][0])+"\n")
            x = 0
            while x < len(psbl_dict[iter][3]):
                if x != len(psbl_dict[iter][3]) - 1:
                    sol3.write(str(psbl_dict[iter][3][x])+ " ")
                else:
                    sol3.write(str(psbl_dict[iter][3][x]))
                x = x+1
            return
        iter +=1
sol_3( psble_evi_vals )


f.close()
sol1.close()
sol2.close()
sol3.close()