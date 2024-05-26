class People:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age

    def sleep(self):
        print(f"{self.name} is sleeping...")   

class Student(People):
    def __init__(self, name, age,student_id):
        super().__init__(self,student_id)
        self.student_id =student_id


student_one = Student("ethan",39,1)
student_two = Student("zora",33,2)
                