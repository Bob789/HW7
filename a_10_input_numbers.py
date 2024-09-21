numbers: int = 0
counter: int = 0
positive_number: int = 0
negative_number: int = 0
zero_number: int = 0
numbers_divided_by_7: int = 0
last_positive_number: int = 0  # if dont print None
last_negative_number: int = 0  # if dont print None
while 10 > counter:
    number: int = int(input("Enter 10 numbers :"))
    if number == -9999:
        break
    else:
        if -1000 <= number <= 1000:
            counter += 1

            if 0 < number:
                positive_number += 1
                last_positive_number = number
            if 0 > number:
                negative_number += 1
                last_negative_number = number
            if 0 == number:
                zero_number += 1
            else:
                if 0 == number % 7:
                    numbers_divided_by_7 += 1

        else:
            continue
else:
    print("statistics :")
    print(
        f"positive_number :{positive_number} negative_number :{negative_number} zero_number :{zero_number} numbers_divided_by_7 : {numbers_divided_by_7}")
    print(f"last_positive_number : {last_positive_number if last_positive_number > 0 else 'None'}")
    print(f"last_negative_number : {last_negative_number if last_negative_number < 0 else 'None'}")
