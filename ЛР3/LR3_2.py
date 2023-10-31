def find_common_participants(first_group,second_group, razd=","):
    group_1 = set(first_group.split(razd))
    group_2 = set(second_group.split(razd))
    obshie = group_1.intersection(group_2)
    list_obsh = list(obshie)
    list_obsh.sort()
    return list_obsh


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group,participants_second_group,"|"))
