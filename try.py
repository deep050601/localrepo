class deep:
    name = "deep"
    occupation = "aws"
    income = 0

    def info(self):
        print(f"{self.name} is an {self.occupation}")


a = deep()
b = deep()

b.name = "vidhi"
b.occupation = "frontend dev"

a.info()
b.info()
