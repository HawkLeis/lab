def find_common_participants(first_group, second_group, separator = ','):
    participants_first_group = first_group.split(separator)
    participants_second_group = second_group.split(separator)

    set_first_group = set(participants_first_group)
    set_second_group = set(participants_second_group)
    common_participants = set_first_group.intersection(set_second_group)
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, '|')
print("Общие участники:", common_participants)
