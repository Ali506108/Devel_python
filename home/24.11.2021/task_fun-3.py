def calc_average(wan , two , there , four , five):
    average_score = (wan + two + there + four + five) / 5
    print(average_score)

calc_average(int(input('введите вашу оценку: ')) , int(input('введите вашу оценку: ')) , int(input('введите вашу оценку: ')) , int(input('введите вашу оценку: ')) , 
int(input('введите вашу оценку: ')) )

def determine_grade(ai , c , v , d , f):
    a = (ai + c + v + d + f) / 5
    if a < 60 and a > 0:
        print('F')
    elif a < 69 and a > 60:
        print('D')
    elif a < 79 and a > 70:
        print('C')
    elif a < 89 and a > 80:
        print('B')
    elif a < 100 and a > 89:
        print('A')

determine_grade(int(input('введите вашу оценку: ')) , int(input('введите вашу оценку: ')) , int(input('введите вашу оценку: ')) , int(input('введите вашу оценку: ')) , 
int(input('введите вашу оценку: ')) )