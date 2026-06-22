class Employee:
    def __init__(self, ):
        self.id = 123
        self.salary = 50_000
        self.designation = "SDE"

    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")

sam = Employee()
print(sam.salary)
sam.travel("Kerala")