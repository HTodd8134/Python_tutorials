class Worker:
    def __init__(self, name, job, salary, costs, personality, should_keep):
        self.name = name
        self.job = job
        self.salary = salary
        self.costs = costs
        self.personality = personality
        self.should_keep = should_keep

    def check_employee(self):
        if self.costs <= self.salary:
            print(f"keep {self.name}")
            self.should_keep = True
        elif ((self.costs - self.salary) < 50) and (self.personality != "mean"):
            print(f"keep {self.name}")
            self.should_keep = True
        else:
            print(f"fire {self.name}")
            self.should_keep = False


one = Worker("Jill", "HR", 200, 20, "nice", "")
two = Worker("Bob", "Garbage", 50, 60, "mean", "")
three = Worker("Matt", "Accounts", 100, 120, "nice", "")
four = Worker("martha", "Lunchlady", 200, 220, "nice", "")

one.check_employee()
two.check_employee()
three.check_employee()
four.check_employee()