class Students:
    __data = {}

    @classmethod
    def get_global_data(cls) -> dict:
        return Students.__data

    @classmethod
    def expelled(cls, name, group):
        if name in Students.__data[group]:
            index = Students.__data[group].index(name)
            Students.__data[group].pop(index)
        else:
            raise ValueError("Такой студент не найден")

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
            if self.__name in Students.__data[self.__group]:
                index = Students.__data[self.__group].index(self.__name)
                Students.__data[self.__group][index] = value
                self.__name = value
            else:
                raise ValueError("Такой студент не найден")
        else:
            raise ValueError("Недопустимый формат")

    def transfer_group(self, new_group):
        if new_group in Students.__data:
            Students.__data[self.__group].remove(self.__name)
            Students.__data[new_group].append(self.__name)
            self.__group = new_group
        else:
            raise ValueError("Такой группы не существует")

    name = property(get_name_student, set_new_name_student)
