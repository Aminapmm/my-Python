import random
def  compare_digits(random,guess):
    random_number = str ( random.randint( 1000 , 10000 ) )

    print ( random_number )

    digit_tuple = (random_number[ 0 ] , random_number[ 1 ] , random_number[ 2 ] , random_number[ 3 ])

    usr_num = str(1035)

    guess_tuple = (usr_num[ 0 ] , usr_num[ 1 ] , usr_num[ 2 ] , usr_num[ 3 ])

    cows_bulls = [ 0 , 0 ]

    for every_digit in digit_tuple :

        digit_position = digit_tuple.index(every_digit)

        for guess_digit in guess_tuple :

            guess_position = guess_tuple.index(guess_digit)

            while cows_bulls[ 0 ] < 5 :

                if every_digit == guess_digit and digit_position == guess_position :

                    cows_bulls[ 0 ] += 1

                    print ( 'well done you had  nice guess keep going you have' , cows_bulls[ 0 ] , 'cow' )

                elif every_digit == guess_digit and digit_position != guess_position :

                    cows_bulls[ 1 ] += 1
                    print ( "Not so bad but Think more you have" , cows_bulls[ 1 ] , "bull" )












