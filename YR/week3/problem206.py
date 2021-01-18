# problem 206




def grade(score):
    if 100 >= score >= 90:
        print('A')
    elif 90 > score >= 80:
        print('B')
    else:
        print('C')


if __name__ == "__main__":
    grade_in = int(input('enter you score'))
    grade(grade_in)