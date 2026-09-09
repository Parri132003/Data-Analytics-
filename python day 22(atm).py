'''
DAY 22(8/09/26)

Building the project: ATM

madhu_details_ICICI = {
    "Name" : 'madhu',
    'Adr' : '1234567890',
    'pan' : 'GPCBU2073T',
    'ATMPIN' : '6600',
    'Balance' : 10000,
    'MINI State':[]
}
All_attmps = 3
while All_attmps > 0:
    user_pin = input('Enter a 4 digit pin: ')
    if user_pin in madhu_details_ICICI['ATMPIN'] and len(user_pin) ==4:
       print('Welcome ICICI ATM')
       choice_ = int(input('Enter \n1.Withdraw\n2.Deposite\n3.Check Balance '))
       if choice_ == 1:
            with_m = int(input('Enter amount to withdraw: '))
            if with_m <= madhu_details_ICICI['Balance'] and with_m % 100 ==0:
              madhu_details_ICICI['Balance'] -= with_m
              print(f'Take your cash and the balance is {madhu_details_ICICI["Balance"]}')
              madhu_details_ICICI['MINI State'].append(f' withdraw: {with_m}')
              print(f"{madhu_details_ICICI['mini State']}")
              user_opt = int(input('Enter\n1.Home Page \n.2 exist: '))
              if user_opt ==1:
                  print('Taking to Home Page')
              elif  user_opt ==2:
                  print('Thanks for Visiting')
                  break
            else:
                  print('insufficient balance or This ATM can not provide change')
                  break
       elif choice_ == 2:
            depo_m = int(input('Enter amount to deposit: '))
            if depo_m % 100 ==0:
                madhu_details_ICICI['Balance'] += depo_m
                print(f' amount to deposit and total amount in your balance is{madhu_details_ICICI["Balance"]}')
                madhu_details_ICICI['MINI State'].append(f'deposit:{depo_m}')
                print(f"{madhu_details_ICICI['MINI State']}")
                user_opt = int(input('Enter\n1.Home Page \n.2 exist: '))
            if user_opt == 1: 
                  print('Taking to Home Page')
            elif  user_opt ==2:
                  print('Thanks for Visiting')
                  break
            else:
                print('This ATM is not accepts change')
       elif choice_ ==3:
                print(f' your balance is {madhu_details_ICICI["Balance"]}')
       else:
            All_attmps -= 1
            if All_attmps > 0:
                print(f'Incorrect pin entered and you have {All_attmps} left')
            else:
                print('Your card is blocked..')

'''
madhu_details_ICICI = {
    "Name" : 'madhu',
    'Adr' : '1234567890',
    'pan' : 'GPCBU2073T',
    'ATMPIN' : '6600',
    'Balance' : 10000,
    'MINI State':[]
}
All_attmps = 3
while All_attmps > 0:
    user_pin = input('Enter a 4 digit pin: ')
    if user_pin in madhu_details_ICICI['ATMPIN'] and len(user_pin) ==4:
       print('Welcome ICICI ATM')
       choice_ = int(input('Enter \n1.Withdraw\n2.Deposite\n3.Check Balance '))
       if choice_ == 1:
            with_m = int(input('Enter amount to withdraw: '))
            if with_m <= madhu_details_ICICI['Balance'] and with_m % 100 ==0:
              madhu_details_ICICI['Balance'] -= with_m
              print(f'Take your cash and the balance is {madhu_details_ICICI["Balance"]}')
              madhu_details_ICICI['MINI State'].append(f' withdraw: {with_m}')
              print(f"{madhu_details_ICICI['mini State']}")
              user_opt = int(input('Enter\n1.Home Page \n.2 exist: '))
              if user_opt ==1:
                  print('Taking to Home Page')
              elif  user_opt ==2:
                  print('Thanks for Visiting')
                  break
            else:
                  print('insufficient balance or This ATM can not provide change')
                  break
       elif choice_ == 2:
            depo_m = int(input('Enter amount to deposit: '))
            if depo_m % 100 ==0:
                madhu_details_ICICI['Balance'] += depo_m
                print(f' amount to deposit and total amount in your balance is{madhu_details_ICICI["Balance"]}')
                madhu_details_ICICI['MINI State'].append(f'deposit:{depo_m}')
                print(f"{madhu_details_ICICI['MINI State']}")
                user_opt = int(input('Enter\n1.Home Page \n.2 exist: '))
            if user_opt == 1: 
                  print('Taking to Home Page')
            elif  user_opt ==2:
                  print('Thanks for Visiting')
                  break
            else:
                print('This ATM is not accepts change')
       elif choice_ ==3:
                print(f' your balance is {madhu_details_ICICI["Balance"]}')
       else:
            All_attmps -= 1
            if All_attmps > 0:
                print(f'Incorrect pin entered and you have {All_attmps} left')
            else:
                print('Your card is blocked..')





























