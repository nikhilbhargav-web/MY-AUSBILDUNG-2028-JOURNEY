# IGL Day 3 - Task 1
print("=== IGL GERMANY VISA CHECKER ===")

name = input("Tera naam: ")
age = int(input("Teri age: "))
salary = int(input("Teri salary EUR/month: "))

yearly = salary * 12
print("Yearly Salary:", yearly, "EUR")

if age >= 18 and yearly >= 58000:
    print("Result: Bhai tu Germany ja sakta 🇩🇪")
    print("EU Blue Card Approved ✅")
else:
    print("Result: Abhi ruk ja IGL")
    print("Reason: Age 18+ aur 58k EUR/year chahiye")

print("Day 3 Task 1 Done")
