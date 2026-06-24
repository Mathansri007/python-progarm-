# Program to calculate the electricity bill using control structures

n = int(input("Enter the number of users: "))
for i in range(0, n):
    f_name = (input("\nEnter the Consumer's First Name: \n"))
    l_name = (input("Enter the Consumer's Last Name: \n"))
    consumer_name=f_name+" "+l_name
    book_no = int(input("\nEnter the Consumer book number: CNEB"))
    if len(str(book_no))==5:
      pass
    else:
      print("\nPlease, enter a valid Book Number containing 5 digit.")
      break
    mobile_no = int(input("\nEnter the Mobile Number: \n"))
    prev_reading = int(input("\nEnter the Previous Month Reading: \n"))
    #curr_reading =
    units = int(input("\nEnter the no.of units consumed this month: \n"))
    print("\n Type of Connection:\n")
    print("1 - Domestic ")
    print("2 - Commercial \n")
    typeCon = int(input("\nEnter the type of EB connection: "))

    print("\nConsumer Name: ",consumer_name)
    print("Consumer Book No: CNEB", book_no)
    print("Mobile Number: ", mobile_no)
    print("Previous Month Reading: ", prev_reading)
    print("Current Month Reading: ", units)

    if (typeCon==1):

      if (units <= 100):
        bill = (units * 1)

      elif (units <= 200):
        bill = ((100 * 1) +
                (units - 100) * 2.5)

      elif (units <= 300):
        bill = ((100 * 1) +
                (100 * 2.5) +
                (units - 200) * 4)

      elif (units > 300):
        bill = ((100 * 1) +
                (100 * 2.5) +
                (100 * 4) +
                (units - 300) * 6);

      print("Type of EB Connection: Domestic")
      print("\nThe Bill amount is ",bill)

    elif (typeCon==2):

      if (units <= 100):
        bill = (units * 2)

      elif (units <= 200):
        bill = ((100 * 2) +
                (units - 100) * 4.5)

      elif (units <= 300):
        bill = ((100 * 2) +
                (100 * 4.5) +
                (units - 200) * 6)

      elif (units > 300):
        bill = ((100 * 2) +
                (100 * 4.5) +
                (100 * 6) +
                (units - 300) * 7)


      print("Type of EB Connection: Commercial")
      print("\nThe Bill amount is ",bill)

    else:
      print("\nType of EB connection is Invalid")