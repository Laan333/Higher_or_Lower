from data.game_data import *
from img.ascii_imgs import *
from random import choice
score = 0
print(logo)
def random_name():
    first_person=choice(data)
    return first_person
def send_info(people_dict:dict):
    for i in range(len(people_dict)):
        print(f" {people_dict['name']}, {people_dict['description']}, from {people_dict['country']}")
        return people_dict['follower_count']
def into_dict(person_points:list):
    dict_person = {}
    pers_name = ("A","B")
    for i in range(len(pers_name)):
        dict_person.update({pers_name[i]:person_points[i]})
    return dict_person
def check_answer(list_points,user_answer):
    global score
    dict_all_persons = into_dict(list_points)
    my_keys = list(dict_all_persons.keys())
    if user_answer == my_keys[0] and dict_all_persons[my_keys[0]] > dict_all_persons[my_keys[1]]:
        score += 1
        return True
    elif user_answer == my_keys[1] and dict_all_persons[my_keys[1]] > dict_all_persons[my_keys[0]]:
        score += 1
        return True
    else:
        print(f"You lose, your score is: {score}")
        return False
def versus():
    list_points = []
    a = random_name()
    b = random_name()
    points = send_info(a)
    print(vs)
    points_second = send_info(b)
    list_points.append(points_second)
    list_points.append(points)
    user_answer = input("Who has more followers? A/B: ")
    if check_answer(list_points, user_answer) is True:
        print("Youre right!\nLets continue...\n")
        versus()
    else:
        exit()

if __name__ == '__main__':
    versus()
