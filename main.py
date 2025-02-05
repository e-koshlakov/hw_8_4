# Модуль 8-4 классы
# Кошлаков Евгений Python 320-2
# У вас есть класс Teacher и класс DisciplineTeacher.
# Примените к ним те методы которые о которых вы узнали на
# уроке. А также попробуйте создать собственный.

class Teacher:
    """Класс учителя"""
    employers_list = []

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        self.employers_list.append(self)

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, experience):
        self.__experience = experience
        return self.__experience

    def get_teacher_data(self):
        return f'{self.get_name()}, образование {self.get_education()}, опыт работы {self.get_experience()} года.'

    def add_mark(self, student_name, mark):
        return f'{self.get_name()} поставил оценку {mark} студенту {student_name}.'

    def remove_mark(self, student_name, mark):
        return f'{self.get_name()} удалил оценку {mark} студенту {student_name}.'

    def give_a_consultation(self, class_name):
        return f'{self.get_name()} провел консультацию в классе {class_name}.'

    def fire_employer(self):
        if self in self.employers_list:
            self.employers_list.remove(self)
            return f"Сотрудник {self.get_teacher_data()} был уволен."
        else:
            return f"Сотрудника {self.get_teacher_data()} уже уволили."


teacher_1 = Teacher('Иван Петров', 'БГПУ', 4)
# print(teacher_1.get_teacher_data())
# print(teacher_1.add_mark('Петр Сидоров', 4))
# print(teacher_1.remove_mark('Петр Сидоров', 3))
# print(teacher_1.give_a_consultation('9Б'))
# print()
print(hasattr(teacher_1, 'employers_list'))
print(teacher_1.__dict__)


class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title
        return self.__job_title

    def get_teacher_data(self):
        return (f'{self.get_name()}, образование {self.get_education()}, опыт работы {self.get_experience()} года.\n'
                f'Предмет {self.get_discipline()}, должность {self.get_job_title()}')

    def add_mark(self, student_name, mark, discipline):
        return (f'{self.get_name()} поставил оценку {mark} студенту {student_name}.\n'
                f'Предмет: {self.get_discipline()}')

    def remove_mark(self, student_name, mark):
        return (f'{self.get_name()} удалил оценку {mark} студенту {student_name}.\n'
                f'Предмет: {self.get_discipline()}')

    def give_a_consultation(self, class_name):
        return (f'{self.get_name()} провел консультацию в классе {class_name}.\n'
                f'По предмету {self.get_discipline()} как {self.get_job_title()}')


discipline_teacher = DisciplineTeacher('Иван Петров', 'БГПУ', 4, 'Химия',
                                       'Директор')
discipline_teacher_2 = DisciplineTeacher('Сидор Иванов', 'БГПУ', 2, 'Биология',
                                         'Завуч')
# print(discipline_teacher.get_teacher_data())
# print()
# print(discipline_teacher.add_mark('Николай Иванов', 4, 'Химия'))
# print()
# print(discipline_teacher.remove_mark('Дмитрий Сидоров', 3))
# print()
# print(discipline_teacher.give_a_consultation('10Б'))
# print()
# print('Список перед увольнением:')
# [print(teacher.get_teacher_data()) for teacher in Teacher.employers_list]
# print()
# print(discipline_teacher.fire_employer())
# print()
# print('Список после увольнения:')
# [print(teacher.get_teacher_data()) for teacher in Teacher.employers_list]
print(Teacher.__dict__)
print(discipline_teacher.__dict__)
print(discipline_teacher_2.__dict__)
print(hasattr(discipline_teacher, 'student_name'))
print(Teacher.__doc__)
print(DisciplineTeacher.__name__)
print(type(discipline_teacher).__name__)
print(Teacher.__module__)
print(DisciplineTeacher.__bases__)
print(getattr(Teacher, 'get_name'))
