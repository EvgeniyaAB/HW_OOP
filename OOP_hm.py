class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        all_rate = []
        for value in self.grades.values():
            all_rate.extend(value)
            average = sum(all_rate) / len(all_rate)
            return round(average, 2)


    def __lt__(self, other):
        if not isinstance(other, Student):
           print('not a class Student')
           return
        return self.average_rate() < other.average_rate()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_rate()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate(self):
        all_rate = []
        for value in self.grades.values():
            all_rate.extend(value)
            average = sum(all_rate) / len(all_rate)
            return round(average, 2)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
           print('not a class Lecturer')
           return
        return self.average_rate() < other.average_rate()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rate()}'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['GIT']
some_student.finished_courses += ['Введение в программирование']

one_student = Student('Ivan', 'Ivanov', 'your_gender')
one_student.courses_in_progress += ['Python']
one_student.courses_in_progress += ['GIT']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['GIT']

some_lecturer = Lecturer('Bob', 'Marley')
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['GIT']

one_lecturer = Lecturer('Best', 'Bob')
one_lecturer.courses_attached += ['Python']
one_lecturer.courses_attached += ['GIT']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 7)
some_reviewer.rate_hw(some_student, 'GIT', 5)
some_reviewer.rate_hw(some_student, 'GIT', 9)

some_reviewer.rate_hw(one_student, 'Python', 2)
some_reviewer.rate_hw(one_student, 'Python', 5)
some_reviewer.rate_hw(one_student, 'Python', 10)
some_reviewer.rate_hw(one_student, 'GIT', 2)
some_reviewer.rate_hw(one_student, 'GIT', 10)

some_student.rate_lect(some_lecturer, 'Python', 5)
some_student.rate_lect(some_lecturer, 'Python', 8)
one_student.rate_lect(some_lecturer, 'GIT', 10)
one_student.rate_lect(some_lecturer, 'GIT', 10)

some_student.rate_lect(one_lecturer, 'Python', 9)
some_student.rate_lect(one_lecturer, 'Python', 10)
one_student.rate_lect(one_lecturer, 'GIT', 7)
one_student.rate_lect(one_lecturer, 'GIT', 8)

students_list = []
students_list.append(some_student.grades)
students_list.append(one_student.grades)

lecturers_list = []
lecturers_list.append(some_lecturer.grades)
lecturers_list.append(one_lecturer.grades)


def get_avg_grade_st(list, course):
    sum_grade = 0
    count = 0
    for s_list in list:
        if course in s_list:
            for grade in s_list[course]:
                sum_grade += grade
                count += 1

    result = round(sum_grade / count, 2)
    return f"Средний балл по курсу {course} всех студентов: {result}"

def get_avg_grade_lect(list, course):
    sum_grade = 0
    count = 0
    for s_list in list:
        if course in s_list:
            for grade in s_list[course]:
                sum_grade += grade
                count += 1

    result = round(sum_grade / count, 2)
    return f"Средний балл по курсу {course} всех преподавателей: {result}"


print(some_student.grades)
print(one_student.grades)
print(some_lecturer.grades)
print(one_lecturer.grades)
print('------------------')
print(some_student < one_student)
print(some_lecturer < one_lecturer)
print('------------------')
print(some_student.__str__())
print('------------------')
print(some_reviewer.__str__())
print('------------------')
print(some_lecturer.__str__())
print('------------------')
print(get_avg_grade_st(students_list, 'GIT'))
print(get_avg_grade_st(students_list, 'Python'))
print('------------------')
print(get_avg_grade_lect(lecturers_list, 'GIT'))
print(get_avg_grade_lect(lecturers_list, 'Python'))