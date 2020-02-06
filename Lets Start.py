
def master_function_of_exercise():
    def exercise_one():
        name= input('What is your name? ')
        favorite_color =input('What is your favourite color? ')
        print(name+ ' likes ' +favorite_color)


        birth_year= input('Your Birth Year: ')
        age= 2020-int(birth_year)
        print(age)

        weight= input('What is your Weight in pound: ')
        kilogram= 0.45* float(weight)
        print('your weight is',kilogram,'kg')


        name= '''Hi,
        its me Rakib Hasan 
        am learning Pythyon'''
        print(name)


        start_end_string = 'I love Mushu, My Wife.'
        print(start_end_string[5:-5])


        first= 'Rakib'
        last='Hasan'
        message= f'{first} {last} is a coder'
        print(message)

        price= input('What is the price of onion: ')
        informer= input('What is your name: ')
        msg=f'{informer} has said the price of onion is {price} taka'
        print(msg)
    exercise_one()


    def exercise_two():
        counting_string='I love You Mushu'
        print(len(counting_string))


        learning_method= 'Alhamdulillah'
        print(learning_method.upper())

        #there are lots of method,some of them are Upper,Lower,capitalize,find and so on..
        repl= 'Murshida Akter'
        print(repl.replace('Murshida Akter','I love You'))


        asking_by_in_function= 'I love You Mushu'
        print("I love You" in asking_by_in_function)
    exercise_two()


    def arithmatic_operation():

        x=10
        x**=3
        print(x)

    arithmatic_operation()

    def operation_precendence():
    #ODMAS Brackets ((),{},[]) ,Orders(),Division,Multiplication,Addition,Substraction
        x= (3+4)*39/3
        print(x)
    operation_precendence()

    def math_functions():
        x=2.9
        print(round(x))

        x=2.55
        print(abs(-x))

        x=-43
        print(abs(x))

        import math 
        print(math.ceil(2.9))
        print(math.floor(2.9))
    math_functions()


    def if_statement():

        its_a_hot_day=False
        its_a_cold_day=True
        if its_a_hot_day:
            print('''Its hot day
        Drink plenty of water..''')

        elif its_a_cold_day:
            print('''Its a cold day
        Wear Warm clothes) 
        else:
        print('its a lovely day...''')                       
    if_statement()

    def if_function_exercise():

        price_of_house= 1000000
        good_credit=False
        if good_credit:
            put_down= (1000000*10)/100
            print("Your Down payment is $",put_down)
        else:
            put_down= (1000000*20)/100
            print("Your Down Payment is $",put_down)
            print('Thank You')
    if_function_exercise()


    def another_way():
        price= 1000000
        has_good_credit= False
        if has_good_credit:
            down_payment= 0.1*1000000
        else:
            down_payment= 0.2*1000000
        print(f"Your Down Payment is: ${down_payment}")
    another_way()


    def operatin_operator():

        name= input("Your name: " )

        if len(name) <3:
            print("Name must be at least 3 characters")
            print("name can be a maximum od 50 characters")
        else:
            print('name looks good!')
    operatin_operator()


    def weight_convert_exercise():

        weight=int(input('Weight: ' ))
        what_to_convert= input('(L)bs or (K)g: ')

        if  what_to_convert.upper()== "L":
            convert= weight*0.45 
            print(f'Your weight is {convert} kilos')
        else:
            convert= weight/0.45
            print(f'Your weight is {convert} pounds')


        has_high_income= True
        good_credit= True

        if has_high_income and good_credit:
            print('Eligible for loan')
        else:
            print('Not Eligible for loan...')    


        has_high_income=False
        good_credit= True
        if has_high_income or good_credit:
            print('Eligible for loan')
        else:
            print('not eligible for loan')


        has_good_credit= True
        criminal_record= False
        if has_good_credit and not criminal_record:
            print('eligible for loan')
        else:
            print('not eligible for loan...')
    weight_convert_exercise()

    def tempareture_exercise():
        tempareture= int(input('Tempareture today in Celcius: '))
        if tempareture>30 :
            print('Its a hot day...')
        elif tempareture<10:
            print('its a cold day')
        else:
            print('Its neither hot nor cold.....')

        def length():
            name= len(input('Your Name: '))
            if name<3:
                print('Must be greater than 3 Character')
            elif name>50:
                print("Must be less than 50 character")
            else:
                print('Sounds ok!!!')
        length()


        def creating_design():
            i=0
            while i<3:
                print(i)
                i+=1

            star_mark_start= 0
            while star_mark_start<10:
                print("*"*star_mark_start)
                star_mark_start+= 1
        creating_design()

        def secret_number_guess():
            secret_number=15
            guess_chance=1

            while guess_chance<=3:
                guess= int(input("Guess a Number Between 1 to 15: "))
                guess_chance+= 1
                if secret_number== guess:
                    print('You Win!!!')
                    break
            else:
                    print('You Loss!!!')
        secret_number_guess()
    tempareture_exercise()


    def car_game_interface():

        inputed=0

        while inputed<100:
            command= input('>')
            inputed+=1

            if command.upper()== 'HELP':
                print('''Start- to start the car
        Stop- to stop the car 
        Quit- to exit''')
            elif command.upper()== 'START':
                print('car started... Ready to go')
            elif command.upper()== 'STOP':
                print('car stopped!!')
            elif command.upper()== 'QUIT':
                print('')
                break
            else:
                print('I dont understand that...')


        is_not_started= True
        if command== 'help':
                print('''
        Start- to start the car
        Stop-to stop the car
        Quit-to exit''')
        elif command== 'start':
                print('car has started...')
        elif command== 'stop':
                print('Car has stopped')
        else:
            print()
    car_game_interface()

    def for_loop():

        command= ''
        started= False
            
        if command== 'start':
            if started:
                print('car is already started...')
            else:
            
                print('Car Started')
        elif command=="stop":
            if not started:
                    
                print('Car is already stopped')
            else:
                print('car topped')    
        elif command== 'help':
            print('''Start- to Start
        Stop-to Stop
        Quit- to Quit''')

        else:
            print('I dont understand that...')
    for_loop()





    def more_for_loops():

        for rakib in 'Hridoy':
            print(rakib)
        
        for learning in 'Python':
            print(learning)

        for item in range(20,30,2):
            print(item)


        prices=[10,20,30]
        total=0
        for anything in prices:
        
            print(f'Total: {total}')
    more_for_loops()

    def nested_for_loops():
        for x in range(4):
            for y in range(4):
                print(f'({x}),({y})')



        number=[5,2,5,2,2]
        for x_count in number:
            print('x'* x_count)

        numbers= [2,2,2,2,5]
        for x_count in numbers:
            print('x'*x_count)


        names= ["john",'bob','Mosh',"sarah","mary"]
        print(names[2:3])
        print(names)

        numbers=[12,14,23,76,44]
        max=numbers[0]
        for number in numbers:
            if number>max:
                max=number
            print(max)


    nested_for_loops()

    def list(): 
        lists=['rakib','murshida','mushhrid','hasan']
        print(lists)
        lists[0]= 'Rakib Hasan'
        lists[2]= 'Akter'
        lists[3]= 'Moushumi'
        print(lists)
    list()


    def find_the_largest_number():

        numbers=[45,32,43,55]
        max=numbers[0]
        for number in numbers:
            if number>max:
                max=number
        print(max)
    find_the_largest_number()


    def two_dimension_list():

        def replacing_matrix_values():

            matrix= [
            [1,2,2],
            [2,5,4],
            [8,10,9]
            ]

            matrix[0][0]= 23
            print(matrix)
        replacing_matrix_values()


        numbers= [521,23,12,22,45,22,12,2333]
        numbers.append(123)
        numbers.insert(2,63562)
        numbers.remove(23)
        numbers.clear()
        numbers.pop()
        numbers.reverse()
        copied_numbers= numbers.copy()
        print(numbers)
        print(copied_numbers)
        copied_numbers.insert(3,125)
        print(copied_numbers)
    two_dimension_list()


    #fix it later 

    def first_function():
        email_address= input('Enter Your Email: ')
        my_all_email_address={
            'email1': 'rakibhroidooy63@gmail.com',
            'email2': 'rakibhhridoy2670@gmail.com',
            'email3': 'rakibhhridoy@yahoo.com',
            'email4': 'hasanrakib33487@gmail.com'
        }
        if email_address== my_all_email_address:
            print('You enter a correct email Address')
        else:
            print('You entred a wrong email')



        print('lets show a message')
    first_function()

    def tuples():
    #it is used instead of lists because it cant be changed.. Toples are never can be changed....

        lists= [323,121244,4,4,12,4,24,12421,4124124254]
        lists.insert(3,353)
        print(lists)

        def removing_Duplicates_from_lists():

            dupl= [123,434,233,22,23,22,22,223,233,21]
            store= []
            for storing in dupl:
                if storing not in store:
                    store.append(storing)
                print(store)   
        removing_Duplicates_from_lists()    

        def putting_data_into_lists():

        
            customer_info={
            'age': 21,
            'name': 'Rakib Hasan',
            'Future Plan' : 'Data Scientist'
            }

            customer_info['birthyear']= input('Enter Your BirthYear: ')
            print(customer_info['birthyear'])
        putting_data_into_lists()

        

        def storing_by_input_in_lists_form(): 

            def putting_data_lists():

                customer_info={
                    'name': input("Enter Your Name: "),
                    'birthyear': input('Enter Your Birthyear: '),
                    'fav': input('Your Fav. game: ')
                }

                print(customer_info['name'])

            putting_data_lists()

        
    tuples()
        
    def lists_function():
        lists_by_paranthesis1={
            'firstname':input("your first name: "),
            'lastname': input('your last name: '),
            "age": int(input("enter your age: ")),
            "department": input('Enter Your Department: '),
            'aim': input('Enter Your aim: ')
        }
        print(lists_by_paranthesis1['age'])

    print("Hey,input your information that we have asked")
    lists_function()



    def classes():
        class point:
            def move(self):
                print('move')
            def draw(self):
                print('draw')


        point1=point()
        point1.y= 20
        point1.draw()
        print(point1.y)
    classes()

    def fixing_error():
        try:
            print(point1.x)
        except InvalidSyntax:
            print("Invalid syntex...")
    fixing_error()  
        

    def exercise_three():
        customer={
            'name': input("Enter Your Name"),
            "age": int(input('Enter your age: '))  
        }     

        print(customer['name'])
        print(customer.get('birthday'))
        print(customer.get('birthday',"2nd January 1999"))
        print(customer['birthday'])
        '''

        '''
        x= 'rakib'
        print('rakib' in x)

        def welcoming_new_student():
            name=input('Your Name: ')
            department=input('Your Department: ')
            merit=input('Your Merit: ')
            print(f'Assalamu Alaikum {name}, We feel honour to have such a talent guy and We welcome you in Department of {department} University of Dhaka securing {merit} Merit position')

        welcoming_new_student()
        print('Done Successfully..')
    exercise_three()


    def exercise_last():
        variables=["I love you Mushu"]

        for variable in variables:

            def proposing(variable):
                return variable*1000
                print(proposing("I love You Mushu"))

            proposing()

        def rakib_loves_Mushu(word):
            return word*1000
        print(rakib_loves_Mushu('I love You Mushu\n Do you love me??\n '))

        def irritate(z):
            return z*10000000
        print(irritate(' বাচ্চারা কেমন আছো?? \n \n'))


        first_message= "Hey,Its Rakib Telling you a joke.."
        print(first_message)
        first_message= 'lets change the title..'
        print(first_message)
    exercise_last()

    def exercise():
        def first_name():
            first_n= input('Your First Name: ')
            uppercasing= first_n.upper()
            print(uppercasing)
        first_name()

        def last_name():
            last_n= input('Your Last Name: ')
            title= last_n.title()
            print(title)
            def final_result():
                print(f'Thank you,\n\t Mr. {title}')
            final_result()
        last_name()

        stripping_white_space= '  I love to write code in python,because its very energetic and efficient..  '
        print(stripping_white_space.rstrip())
    exercise()
#master_function_of_exercise()

#  Python Crash Course
#Introducing Lists

def lists_new_ideas():
    name= input('Input your name: ').title()
    age=int(input("Input Your Age: "))
    id_number= int(input('Input Your id Number: '))
    storing_in_list= [name,age,id_number]
    print(storing_in_list)
    print(storing_in_list[2])
    if storing_in_list[1]== 21:
        print('So your 21')
    else:
        print('So you are not 21')

#lists_new_ideas()

def exercise_in_toples():
    def userform():
        client_name= input('Enter Your Name: ').title()
        client_age= int(input('Enter Your Age: '))
        client_country= input('Enter Your Country: ')
        purchase_price= float(input("Enter Your Purchasing Amount:$ "))
        client_info=(client_name,client_age,client_country,purchase_price)
        restricted_age= 18
        if client_info[1] < restricted_age :
            print('So Your Not Adult. You are not allowed to visit the page.')
        else:
            print('Your Allowed to go next page. Thank you.. Have a good day..')
        if client_info[3] >100:
            print("you have no discount.")
        else:
            print('You can have a discount about 20% off. Have a good day..')
        print(f'Thank You {client_info[0]}, I hope you love your country, {client_info[2]}.\n\t Have a nice day buddy!!')
    userform()
#exercise_in_toples()

def for_loops_in_list():
    def fisrt_input_all_info():
        university= input('Enter Your University name in Short Case: ').upper()
        department=input('Input Your Department: ').title()
        batch= int(input('Enter Your Batch: '))
        id= int(input('Enter Your Id: '))
        quantiity_of_books= int(input("Number of books you want to borrow: "))
        asking_purchase= input("Do you want to purchase any book: ").upper()

        store_of_information=[university,department,batch,id,quantiity_of_books,asking_purchase]

        def testing_store_info():
            for info in store_of_information:
                print(info)
        testing_store_info()
        def processing_info():
            if store_of_information[0] == "DU":
                if store_of_information[1]== "Soil, Water And Environment":
                    if store_of_information[2]==69:
                        print("hey buddy!! Its Rakib,Your Friend. Your Code for All the books for Soil, Water And Environment is above 700. It startes from 700 globally. Thank you,Have A Good Day")
                    else:
                        print('This Section is only for batch 69 of Department Of Soil, Water And Environment. Thank you for your time. Have A Good Day.') 
                else:
                    print('This Section is only for batch 69 of Department of Soil, Water And Environment. Thank you.')
            else:
                print('You are not Allowed to have access this service. Its only for Dhaka University Students.') 

            if store_of_information[3]== 18:
                print('Your Wife is waiting for your message Mr. Rakib Hasan. Go and spend with your wife some time.')
            else:
                print('Hey,\nBuddy!!\n Its Rakib H. Hridoy,Your Classmate developed this system.')
            if store_of_information[4]>2:
                print('You can borrow not greater than 2 books. Thank You.')
            else:
                print('You are allowed to borrow books that you want. Thank You.')
            if store_of_information[5]== 'YES':
                name_of_the_book= input('Enter The Name of the book You Want to purchase: ')
                want_to_spend= float(input("Enter The Amount You Want To Spend: $ "))
                if want_to_spend> 50:
                    print('You can have 20% off/discount. Hope You will be happy. Be smiling.') 
                else:
                    print("You can't have off/discount.")
                print(f'So,You Want to purchase {name_of_the_book}. We are preparing the process. Please wait for while. Thank for Your Time..')
            else:
                print("Its Better To Purchase Than Borrow.")

        processing_info()
    fisrt_input_all_info()
#for_loops_in_list()

def adding_changing_removing():
    def adding():
        my_list= []
        my_list.append(input('Enter Your Name: '))
        my_list.append(int(input('Enter Your Age: ')))
        my_list.append(input('Enter Your Password: '))
        print(my_list)
    adding()
    def poping():
        my_list=[]
        my_list.append(input('Enter Your Name: '))
        my_list.append(int(input('Enter Your Roll: ')))
        print(my_list)
        my_list.pop(-1)
        print(my_list)
    poping()
    def removing_by_del():
        user_list= []
        user_list.append(input('Enter Your University Name: '))
        user_list.append(input('Enter Your Department Name: '))
        print(user_list)
        del user_list[-1]
        print(user_list)
        del user_list[0]
        print(user_list)
    removing_by_del()
    def removing_by_remove():
        user_info=[]
        user_info.append(input('Which country are you from: '))
        user_info.append(int(input('Enter Your Favorite Number: ')))
        user_info.append(int(input('Enter Your position in your undergraduate exam: ')))
        print(user_info)
        removing= user_info[-1]
        user_info.remove(removing)
        print(user_info)
        print(removing)
    removing_by_remove()
#adding_changing_removing()
        

def organizing_a_list():
# Uppercase will be sorted first,then lowercase.. Integer and String Value cant be sort or sorted in python    
    def sorting():
        user_information= []
        user_information.append(input('Result of your undergraduate exam: '))
        user_information.append((input('Enter your position: ')))
        user_information.append(input('Enter your favorite color: '))
        print(user_information)
        user_information.sort()
        print(user_information)
    sorting()
    def sorting_by_sorted():
        user_define=[]
        user_define.append(input('Hey,Are a user: '))
        user_define.append(input('Enter Your skill: '))
        user_define.append(input('Enter Your Favorite brand: '))
        print(user_define)
        print(sorted(user_define))
    sorting_by_sorted()    
    def reverse_sorting():
        user=[]
        user.append(input('The name of book: '))
        user.append(input('Topic: '))
        user.append(input('Learned From this topic: '))
        for user_formated in user:
            print(user_formated)
        print(sorted(user))
        user.sort()
        print(user)
        user.sort(reverse=True)
        print(user)
    reverse_sorting()
    def reversing_by_reverse():
        customer=[]
        customer.append(input('Enter Your Catagory: ').title())
        customer.append(input('Name of your service: ').title())
        customer.append(input('Whats Your Name: ').title())
        print(customer)
        for info in customer:
            print(info)
        customer.reverse()
        print(customer)
        customer.reverse()
        print(customer)
    reversing_by_reverse()

#organizing_a_list()


def length_by_len():
    customer_information=[]
    customer_information.append(input('Enter Your Name: ').title())
    customer_information.append(int(input('Enter Your Roll Number: ')))
    customer_information.append(input('Enter Your Bio: ').title())
    print(customer_information)
    print(len(customer_information))
    if len(customer_information[0])>20:
        print('You Cant Enter More Than 20 Character!!')
    else:
        print('Inputted Successfully..')
#length_by_len()

def working_with_the_list():
    def by_for_loop():
        soil_particles=[]
        soil_particles.append(input('Enter Your Name: ').title())
        soil_particles.append(input('Enter Your Name: ').title())
        soil_particles.append(input('Enter Your Name: ').title())
        for soil_particle in soil_particles:
            print(soil_particle)
    by_for_loop()

    def doing_more_with_for_loop():
        books=[]
        books.append(input('Enter the name of Course 100 Book: ').title())
        books.append(input('Enter the name of Course 101 Book: ').title())
        books.append(input('Enter the name of Course 102 Book: ').title())
        for book in books:
            print(f'I cant wait to read {book}!!')
    doing_more_with_for_loop()

    def using_range_function():
        for value in range(1,6):
            print(value)
        values= list(range(1,6))
        print(values)
    using_range_function()
    def  making_a_list():
        squares=[]
        for value in range(1,11):
            square=value**2
            squares.append(square)
            for squar in squares:
                print(squar)
    making_a_list()
    def easy_way():
        squares=[]
        for value in range(1,11):
            squares.append(value**2)
            print(squares)
    easy_way()
    def simple_statistics_with_a_list():
        lists_of_even= list(range(2,20,2))
        print(lists_of_even)
        print(max(lists_of_even))
        print(min(lists_of_even))
        print(sum(lists_of_even))
        numbers= list(range(1,1000001))
        print(numbers)
        print(sum(numbers))
    simple_statistics_with_a_list()
    def making_a_list_more_easy_way():
        a_list=[value for value in range(2,99,3)]
        another_list=[value for value in range(1,11)]
        print(another_list)
        print(a_list)
        storing_the_list=[value**2 for value in range(1,11)]
        print(storing_the_list)
    making_a_list_more_easy_way()

    def working_with_part_of_a_list():
        def exercise1():

            universities= []
            universities.append(input('Enter University Name: ').title())
            universities.append(int(input('Enter Position in Bangladesh: ')))
            for university_info in universities:
                print(university_info)
            for taking_data_from_list in universities[:1]:
                print(taking_data_from_list)
        exercise1()
        def using_slice():
            numbers_list= [value for value in range(1,11)]
            print(sum(numbers_list[:6]))
            print(max(numbers_list[:-2]))
            print(min(numbers_list[1:7]))
            print(sum(numbers_list[:]))
        using_slice()

        def copying_using_slice():
            lists=[x for x in range(1,13,1)]
            lists_copied= lists[:]
            lists.append(int(input('Enter a random number: ')))
            print(lists)
            print(lists_copied[1:10:2])
            print(lists_copied)
        copying_using_slice()

        def writing_over_a_tuple():
            lists_of_number= [x for x in range(1,16)]
            print(lists_of_number)
            lists_of_number[0]= 12
            print(lists_of_number)
            dimensions= (100,250)
            for dimension in dimensions:
                print(dimension)

            dimensions= (230,160)
            for dimension in dimensions:
                print(dimension)


        writing_over_a_tuple()

    working_with_part_of_a_list()
    
#working_with_the_list()


def if_statement():
    def conditional_tests():
        def using_flag():

            prompt = '\nTell me something,and I will repeat it back to you: '
            prompt += "Enter 'quit' to end the program: "
            active = True
            while active:
                message= input(prompt)
                if message in 'quit':
                    active = False
                else:
                    print(message)
        using_flag()

        def checking_that_list_not_empty():
            lists = []
            lists.append(input('Enter Your favorite need: ')) 

            if lists:
                for list in lists:
                    print(f'Adding {list}.')
                print('\nFinished making Your Pizza.')
            
            else:
                answer = input('Do You Want a plain pizza?? ')
                if answer in 'yes':
                    print('Okh,We are making Your Pizza')
                else:
                    lists.append(input('Enter What you Want: '))
        checking_that_list_not_empty()

        def using_multiple_lists():
            x= ['mushroom','pipes','cheese','mango']
            y= []
            y.append(input('What you like to have with your lunch: ').lower())

            for y_element in y:
                if y_element in x:
                    print('The Item is in the x list.')
                else:
                    print('Sorry,that is not in the x list..')
        using_multiple_lists()

    conditional_tests()

#if_statement()


def dictionaries():
    def working_with_Dictionaries():
        def accessing_values_in_a_dictionary():

            our_first_dictionary= {
                'color': input('Enter Your favorite color: ').upper(),
                'name': input("Enter Your Name: ").title()
            }
            
            print(f"{our_first_dictionary['name']}'s favorite color is {our_first_dictionary['color']}")

        accessing_values_in_a_dictionary()

        def modifying_values_in_a_dictionary():

            content_0 = {'x_position': 0,'y_position': 25,'speed': input('How Fast You Want to go? ').lower()}

            print(f"Original position is {content_0['x_position']}.")
            if content_0['speed'] == 'medium':
                x_increment= 5
            elif content_0['speed'] == 'slow':
                x_increment=10
            else:
                x_increment=20
            x_increment += content_0['x_position']
            print(f'New position will be at {x_increment}.')
        
        modifying_values_in_a_dictionary()

        def removing_key_value_pairs():
            lists= {
                'name': input('Enter Your Name: ').title(),
                'school': input('Enter Your school name: ').title(),
                'graduated': input('Are you graduated: ').lower()
            }

            if lists['graduated'] == 'yes':
                del lists['school']
                print('Look for job my boy.')
                print(lists)
            else:
                print('To be admit in a reputed university you have to work hard.')
                print(lists)

        removing_key_value_pairs()
        
        def using_get_to_access_values():
            list= {
                'name': input('Enter your name: '),
                'age': int(input("Enter Your Age: ")),
                'color': input('Enter Your Favorite Color: ')


            }
            print(list.get('age','age value has not assingned.'))
        using_get_to_access_values()

        def looping_through_a_dictionary():
            our_exercise_list={
                'name': input('Enter Your Name: ').title(),
                'age': int(input('Enter Your Age: ')),
                'married': input('Are You Married: ').lower()
            }
            favorite_language={
                'rakib': input('Enter Your Favorite programming language: '),
                'murshida': input('Enter Your Favorite Programming Language: '),
                'mushhrid': input('enter your favorite programming language: ')
            }

            for k,v in favorite_language.items():
                print(f"{k.title()}'s Favorite Programming Language is {v.upper()}.")
            print("We've got our value and their keyword successfully.")

            for keyword,value in our_exercise_list.items():
                print(f'Keyword: {keyword}\nValue: {value}\n')
            print("We've got our list keyword and their value.")

        looping_through_a_dictionary()

        def looping_through_all_keys_in_dictionary():
            a= {
                'rakib': 'is a python programmer',
                'murshida': 'is wife of rakib hasan',
                'mushhrid': 'is nickname of rakib hasan and murshida akter'
            }

            for x in a.keys():
                print(f'It is me {x.title()}.')

            a_lists={
                'phil': 'c',
                'sarah': 'kotlin',
                'rakib': 'python'
            }

            friends= []

            friends.append(input('Enter Your Name: '))
            friends.append(input('Enter Your Name: '))

            for name in a_lists.keys():
                print(f'Hi, {name.title()}')

                if name in friends:
                    language= a_lists[name].title()
                    print(f'\t{name.title()}, I see you love {language}')

            favorite_language={
                'rakib': 'python',
                'murshida': 'c#',
                'mushhrid': 'java'
            }
            if 'sarah' not in favorite_language.keys():
                print('Hey Sarah, You did not take the poll. Go to the poll and get finished.')

        looping_through_all_keys_in_dictionary()

        def looping_through_dictionarys_keys_particular_order():
            list={
                'rakib': 'python',
                'murshida': 'c#',
                'mushhrid': 'java'
            }

            for list_keyname in sorted(list.keys()):

                print(f'{list_keyname.title()}, thank you for taking the pool')

            creating_list={
            input('enter your name: ') : input('enter your favorite language: '),
            input('Enter Your Name: ') : int(input('Enter Your Age: '))
            }

            print(creating_list)
            for value in creating_list.values():
                print('The Value are:')
                print(f'{value}')

        looping_through_dictionarys_keys_particular_order()


    working_with_Dictionaries()

    def nesting():
        i=0
        our_list= {
            'name': input('Enter Your name: ').title(),
            'favorite_language': []
        }
        while len(our_list['favorite_language'])<3:
            our_list['favorite_language'].append(input('Enter Your Favorite Language: '))
#            I am missing something here.. 

        print(our_list)    
    nesting()
    def a_list_in_a_dictionary():
        def page_108():
            our_exercise_list= {
            'name': input('Enter Your Name: ').title(),
            'favorite_dishes': ['murgir polaw','kacchi','chatni','lacchi']
            }
            print(our_exercise_list['favorite_dishes'[:]])
            our_exercise_list['favorite_dishes'].append(input('Enter Your favorite food else all these: '))

            print(f"{our_exercise_list['name']} Want These: ")
            for fav in our_exercise_list['favorite_dishes']:
                print(f'\t{fav.upper()}')
        page_108()

        def page_109():
            lists={
                input('Enter Your Name: ').title(): {
                    'fav_1': input('Enter Your 3 Favorite language using comma(,): ')
                },
                input('Enter Your Name: ').title(): {
                     'fav_1': input('Enter Your 3 Favorite language using comma(,): ')
                }
                
            }

            for list in lists:
                list[:] = name 
                for element in name:
                    print(element['fav_1'])

        page_109()

        def a_dictionary_in_a_dictionary():
            user={
                'aeinstein':{
                    'first_name' : 'albert',
                    'last_name' : 'einstein',
                    'location' : 'princeton'
                },

                'mcurie': {
                    'first_name' : 'marie',
                    'last_name' : 'curie',
                    'location' : 'paris'
                }
                }
            
            for username,user_info in user.items():
                print(f'Username: {username.title()}')
                full_name_we_get= f"{user_info['first_name']} {user_info['last_name']}"
                print(f'\tFull name: {full_name_we_get.title()}')
                print(f"\tLocation: {user_info['location'].upper()}")
            
        a_dictionary_in_a_dictionary()
    a_list_in_a_dictionary()
#dictionaries()


def user_input_and_while_loops():
    def Introducing_while_loops():

        initial= 0
        while initial <= 100:
            print('Yes \nI love you toooooooooooooooooooooooooooooo Hriddu..')
            initial += 1

    Introducing_while_loops()
user_input_and_while_loops()

