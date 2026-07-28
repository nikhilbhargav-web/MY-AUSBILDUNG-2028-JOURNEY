print("=========================================")
print("       TABLE GENERATOR - DAY 4"     )
print("=========================================")


num = int(input("table kis number ka chaiya? daalo :"))

print(f"\n----- {num} ka table -----")

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

print("---------------------------------")
print("DAY 4 COMPLETE")
