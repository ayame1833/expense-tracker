import exchange
print('Welcome to Expense-tracker!')
##This tracker is recorded in JPY.If you would like to record other currencies, please change below <add> command.

#input participant
name1=input('Participant A: ').capitalize()
name2=input('Participant B: ').capitalize()
print(f'Participants set\n{'-'*17}')
payment_list_AB=[]
payer_totals = {
            name1.capitalize(): 0.0,
            name2.capitalize(): 0.0,
          }

pro_run=True
while pro_run :
  
  print('Please select an action: ')
  command=input('Add, Transfer, List, Status, Delete, Exit: ').upper()
  if command =='EXIT':
    #Exit - to exit from this app!
      print('See you!')
      pro_run=False
      break

  elif command=='ADD':
    #Add - Add [Payer,Pay-Date,Usage, Amount:exchanged] in list.
    #Each Amounts[AUD, USD, EUR, CNY, INR] are exchanged and registered as JPY in the tracker for Transfer.
      payer=input('Payer: ').capitalize()
      if payer not in (name1.capitalize(), name2.capitalize()) :
         print(f'Input {name1.capitalize()} or {name2.capitalize()}!')
         print()
      else:
        date=input('Date(e.g. 2025-04-22): ')
        usage=input('Enter usage[Food, Rent, Else]: ').capitalize()
        if usage not in ('Food','Rent','Else') :
             print('Invalid usage. Please input accurate.')
        else:
             currency = input('Enter currency to exchange from [AUD, USD, EUR, CNY, INR, JPY]: ').upper()
             currencies={"USD": 142.79,"EUR": 162.01, "CNY": 19.53, "INR":1.68, "AUD":90.16, "JPY":1 }
              
             if currency in currencies:
                rate=currencies[currency]
                         
                try:
                   amount = float(input('Amount: '))
                   break  
                except ValueError:
                   print('Please enter a valid number.')
                   print()
                   continue

                exchanged=round(exchange.get_exchange_amount(amount, rate),2)
                print(f'Success! {currency} {amount}→ JPY {exchanged} !') 
                item={
                 'Payer':payer,
                 'Date':date,
                 'Usage':usage,
                 'Amount':exchanged
                }
                payment_list_AB.append(item)       
                print(f'< Added :{date}*{payer.capitalize()}*{usage}* JPY: {exchanged} >')   
                print()       
             else :
                print('Cannot exchange that!')
                print()

  elif command=='LIST':
    #List - Show the current list and sum total in each items[food,rent,transger,else]
       usage_totals = {
            'Food': 0.0,
            'Rent': 0.0,
            'Transfer':0.0,
            'Else': 0.0
       }
       for i, item in enumerate(payment_list_AB):
         print(f'{i}:{item}')
         
       for index, item in enumerate(payment_list_AB):
           usage_totals[item['Usage']]+=item['Amount']
       print(f'{'-'*5}Totals{'-'*5}')
       for usage, total in usage_totals.items():
          print(f'{usage}:{total:.2f}')
       print(f"{'-'*16}")  

  

  elif command=='TRANSFER':
       #Transfer - Pay amount to another person and update Status & List.
       answer=input(f"1. from {name1} to {name2} or 2. from {name2} to {name1} [1 or 2]: ")
       
       if answer == '1':
         payer = name1
         receiver = name2
       elif answer == '2':
          payer = name2
          receiver = name1
       else:
           print('Invalid selection')
           print()
           continue

       
       date=input('Date(e.g. 2025-04-22): ')
       try:
            amount1 = float(input('Amount(JPY): '))
            break  
       except ValueError:
            print('Please enter a valid number.')
            print()
            continue
       
       item2={
             'Payer':receiver,
             'Date':date,
             'Usage':'Transfer',
             'Amount':-amount1
                }

       print(f'{payer} tranfered JPY{amount1} to {receiver}')
       print()
       
       payment_list_AB.append(item2)
          
 
  elif command =='DELETE':
       #Delete- We can delete lines when you mistake your registration.
        answer2 = input('Are you sure to delete?[Yes:No]: ').upper()
        if answer2=='YES':
          print('OK!, this is a current list.')
          for i, item in enumerate(payment_list_AB):
            print(f'{i}:{item}')
          delete = int(input('Which lines would you like to delete?[e.g 1]:' ))
          if delete < len(payment_list_AB):
                 d_item=payment_list_AB[delete]
                 print('Please check your delete list again.')
                 print(d_item)
                 answer4 = input('Can I delete?[Yes,No]: ').upper()
          
                 if answer4 == 'YES':
                    delete_list = payment_list_AB.pop(delete)  
                    usage = delete_list['Usage']
                    amount = delete_list['Amount']
                    if usage in usage_totals:
                      usage_totals[usage] -= amount
                    print('Delete success!')
                    print()
                 else :
                     print('All right! See you!')
                     print()
          else :
                  print(f'Please input 0 to {len(payment_list_AB)}')    
                  print()  
        
        elif answer2 == 'NO' :
            print('Alright! See you!')
            print()
        else:
            print('Invalid input!')
            print()

  elif command=='STATUS':
      #Status - Check which person need to pay to another.
      payer_totals = {
            name1: 0.0,
            name2: 0.0,
          }
      for index, item in enumerate(payment_list_AB):
           payer_totals[item['Payer']]+=item['Amount']
      
      balance = payer_totals[name1]-payer_totals[name2]
      
      print(f'{'-'*8}Status{'-'*8}')
       
      if balance>0.00 :
           print(f'{name2} should pay {name1} JPY {balance:.2f}')
      elif balance<0.00:
          print(f'{name1} should pay {name2} JPY {abs(balance):.2f}')
      else :
          print('No balance remaining!')

      print(f"{'-'*22}")
      
  else:
        print('Invalid input! Try again!')
        print()
           
            
        
