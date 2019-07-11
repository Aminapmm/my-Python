numbers_dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty',90:'ninety'}

#single_digit_num = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'hundred', 'thousand']

#two_digit_num = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
#'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
#'ninety']

entry_number = int(input("Write an integer number between 0 & 9999 "))
entry = str(entry_number)
toole_adad = len(entry)
#get_string = NUMBERS_IN_STRING.get(entry_number)

#print(get_string)

#for char in range(len(entry)):
if type(entry_number / 10) == float and toole_adad == 2 :

    first_digit = numbers_dict.get(int(entry[0]))

    string = numbers_dict.get(first_digit)

    second_digit_str = numbers_dict.get(int(entry[1]))


    print(string,second_digit_str)

elif entry_number >= 10 and entry_number<=20 :

    string = numbers_dict.get(entry_number)

    print(string)

elif type(entry_number / 10) == float and toole_adad == 3:

    first_digit = numbers_dict.get(int(entry[0]))

    new_entry = int(entry_number % 100)

    other_digits = numbers_dict.get(new_entry)

    print ( first_digit , 'hundred' , other_digits )

    if other_digits == None:
        new_entry =str(new_entry)

        second_digit = int(new_entry[0])*10

        _string_ = numbers_dict.get(second_digit)

        new_entry = str(new_entry)

        other_digits = numbers_dict.get(int(new_entry[1]))

        print(first_digit,'hundred',_string_,other_digits)

elif type(entry_number / 10) == float and toole_adad == 4:

    first_digit = numbers_dict.get(int(entry[0]))

    entry_1 = str(entry_number % 1000)

    second_digit = numbers_dict.get(int(entry_1[0]))

    entry_2 = str(entry_number % 100)

    other_digits = numbers_dict.get(int(entry_2))

    if other_digits == None :

        _first_digit = int(entry[0]) * 10

        string = numbers_dict.get(_first_digit)

        second_digit_str = numbers_dict.get(int(entry[1]))

        print(first_digit,"thousand",second_digit,"hundred",string,second_digit_str)

    elif entry[1] == 0  and other_digits != None:

        first_digit = numbers_dict.get ( int ( entry[ 0 ] ) )

        string = numbers_dict.get ( first_digit )

        entry_0 = int(entry_number % 1000)

        bakhsh_pazir = numbers_dict.get(entry_0)

        if bakhsh_pazir == None :

            adad_1 = int(entry_0/10) * 10

            digit_3 = numbers_dict.get(adad_1)

            digit_4 = numbers_dict.get(int(entry[3]))

            print(string,"thousand",digit_3,digit_4)

        else:
            print(string,"thousand",bakhsh_pazir)

    else:
        print ( first_digit , "thousand" , second_digit , "hundred" , other_digits )
