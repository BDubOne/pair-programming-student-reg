class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade

    def __str__(self):
        return f"{self._name} | {self._age} | {self._grade}"

    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        if (not isinstance(new_name, str)) or new_name.isalpha() == False or len(new_name) < 3:
            return f"{new_name} is not a valid name"
        
        else:
            self._name = new_name.title()

    
    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def set_age(self, new_age):
        if type(new_age) == int and 11 < new_age < 18:
            self._age = new_age

        else:
            print("Age must be a number between 11 and 18")

    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
       
        if new_grade in ["9th", "10th", "11th", "12th"]:
            self._grade = new_grade
        
        else:
            print("Enter a valid grade")

    def advance(self): 
        grade_list = ["9th", "10th", "11th", "12th"]
        if self._grade == "12th":
            print("Good luck on your next chapter!")
        else:
            new_grade_index = grade_list.index(self._grade) + 1
            self._grade = grade_list[new_grade_index]

        return
    
    def study(self):
        print(f"{self._name} is studying")

        return
    
chad = Student("chad", 15, "10th")
bryan = Student("bryan", 14, "9th")
shengan = Student("shengan", 17, "12th")

print(chad)
bryan.study()
chad.advance()
print(chad)

bryan.set_name = "Bryan"

print(bryan)



