class Calculator:
    count = 0

    @staticmethod
    def add(a, b, ):
        Calculator.count += 1
        return a + b


print("Sum:", Calculator.add(34, 58,))
print("Add method  that is called:", Calculator.count, "times")
