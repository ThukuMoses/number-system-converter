# Number system converter Logic

def convert_n(num_str, from_base, to_base):

    #  Step 1: Convert input to decimal system
    if "." in num_str:
        integer_part, fraction_part = num_str.split(".")
    else:
        integer_part, fraction_part = num_str, ""

    # integer part to decimal
    decimal_int = int(integer_part, from_base)

    # fraction part to decimal
    decimal_frac = 0
    for i, digit in enumerate(fraction_part, start=1):
        decimal_frac += int(digit, from_base) * (from_base ** -i)

    decimal_value = decimal_int + decimal_frac

    #  Step 2: Convert decimal to target base 

    # convert the integer part
    int_part = int(decimal_value)
    digits = []#stores integer part digits in target base
    if int_part == 0:
        digits.append("0")
    else:
        while int_part > 0:#keep extracting digits until number is fully converted

            #Take remainder of int_part % to_base as index to get corresponding character (0–F) and append to digits
            digits.append("0123456789ABCDEF"[int_part % to_base])

            #Divide int_part by base, keep only integer part, continue conversion.
            int_part //= to_base
    int_converted = "".join(reversed(digits))#digits were collected in reverse order, reverse and join to get final int string

    # convert the fractional part
    frac_part = decimal_value - int(decimal_value)
    frac_digits = []#empty list for fractions


    for _ in range(10):  #prevent endless loop(limit fractional digits to 10 for precision)

        frac_part *= to_base
        digit = int(frac_part)#take integer part frac_part and store it in digit
        frac_digits.append("0123456789ABCDEF"[digit])#look up for the digit in digits that matches the index(digit)
        frac_part -= digit#Remove the integer part, keep the remaining fraction for next iteration

        if frac_part == 0:#break early 
            break

    if frac_digits:
        return int_converted + "." + "".join(frac_digits)#join the whole number with fraction part and return the whole string
    
    else:
        return int_converted

print(convert_n("101.10", 2, 10))