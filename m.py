class GradeCalculator:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def show(self):
        print("Student:", self.name)
        print("Grades:", self.grades)
        print("Average:", self.average())


def main():
    g = GradeCalculator("Jahongir")

    g.add_grade(80)
    g.add_grade(90)
    g.add_grade(70)

    g.show()


main()
