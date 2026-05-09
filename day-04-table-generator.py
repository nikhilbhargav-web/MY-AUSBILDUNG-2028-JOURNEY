# DAY 4: TABLE GENERATOR BY NIKHIL BHARGAV
# GOAL : GERMANY IT AUSBILDUNG 2028

print("=========================================")
print("       IGL TABLE GENERATOR - DAY 4"     )
print("=========================================")

# USER SE NUMBER INPUT LO
num = int(input("table kis number ka chaiya? daalo :"))

print(f"\n----- {num} ka table -----")
# For loop: 1 se 10tak chalao
for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

print("---------------------------------")
print("IGL DAY 4 COMPLETE")
