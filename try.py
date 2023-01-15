class Students:
    __data = {}

    @classmethod
    def get_global_data(cls) -> dict:
        return Students.__data

    @classmethod
    def expelled(cls, name, group):
        student_expelled = {name: group}
        if student_expelled in Students.__data:
            print(f"Студент {name} отчислен из группы {group}")
            Students.__data.remove(student_expelled)
        else:
            print("Такого студента нет")

    def __init__(self, name, group):
        self.__name = name
        self.__group = group
        if group not in Students.__data:
            Students.__data[group] = [name]
        else:
            Students.__data[group].append(name)

    def get_name_student(self) -> str:
        return self.__name

    def set_new_name_student(self, value: str):
        if isinstance(value, str):
            index = Students.__data.index({self.__name: self.__group})
            self.__name = value
            Students.__data[index] = {self.__name: self.__group}
            self.__name = value
        else:
            raise ValueError("Недопустимый формат")

    name = property(get_name_student, set_new_name_student)


ilya = Students("Ilya", "PMI-119")
kirill = Students("Kirill", "PMI-119")
print(Students.get_global_data())
