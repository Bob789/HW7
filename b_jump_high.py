counter: int = 0
sum: float = float(0)
best_jumping: float = float(0)
best_name_record: str = ""
best_record_score: float = float(0)#if the record broken more then 1 time
for x in range(7):
    number: float = float(input("Enter 7 resualt jumping score :"))
    print()
    if 5.8 > number:
        continue
    else:
        counter += 1
        sum += number
        if best_jumping < number:
            best_jumping = number

        # A new record was broken
        if 6.23 < number:
            if best_record_score < number:
                best_record_score = number
                best_name_record = str(input("Enter name"))

print(f"Player which get score more then 5.8 are:{counter} The Average : {sum / counter}")
print(f"The best score are : {best_jumping}")
if best_name_record != "":
    print(f"A new record was broken by:{best_name_record} The score : {best_jumping}")
else:
    print("None")