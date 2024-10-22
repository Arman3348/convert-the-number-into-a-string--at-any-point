def calculate_difference(n):
    odd_sum = 0
    even_sum = 0
    position = 1
    while n > 0:
        digit = n % 10
        if position % 2 == 1:
            odd_sum += digit
        else: 
            even_sum += digit
        n //= 10  
        position += 1 
    difference = odd_sum - even_sum
    return difference
number = int(input("Enter a positive integer: "))
result = calculate_difference(number)
print("The difference between the sum of digits at odd positions and even positions is:", result)
