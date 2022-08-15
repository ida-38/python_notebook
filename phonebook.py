## first we need to import the classes we need
from phonebookc import person
from phonebookc import address
def welcome():
##    a function for control the main menu senteces and asking for entrance
    entry=int(input("""                      -------------------
                      |    *MAIN MENU*    |
                      |1.Add a new contact|
                      |2.Delete contact   |
                      |3.Contacts list    |
                      |4.Exit             |
                       -------------------
Enter your entry here:\n"""))
    return entry
##  main function for doing orders and playing program
def phonebook():
##    dict for making a neat contact list
    contacts={}

    while True:
##  showing menu and ask for an entry to start the program
        entry=welcome()
##    start getting informations for adding a new contact
        if entry==1:
            name=input("Enter frist name:\n")
            lname=input("Enter sur name:\n")
            age=int(input("Enter your age :\n"))
            phone_number=int(input("Enter phone number :\n"))
            city=input("Enter city name:\n")
            street=input("Enter street name:\n")
            allay=input("Enter allay name :\n")
            zipcode=int(input("Enter zipcode number :\n"))
            a1=person(name,lname,age,phone_number)
            a2=address(city,street,allay,zipcode)
##
#             changing a1 and a2 type into str so we can use Conditions  
            b1=str(a1)
            b2=str(a2)
##    using if to make sure there's no repetitious and add objects into dict
            if b1 not in contacts.items():
                contacts.update({b1:b2})
                print('contact successfully saved')
                print('Your updated phonebook is shown below: ')
##        then making a loop to make sure and see that informs are saved
                for k, v in contacts.items():
                    print('*******************')
                    print(k, ":" ,v)
            else:
                print('that contact already exits')
##         asking for a name that should be deleted       
        elif entry==2:
            x=input("Enter the name of contact you wish to delete: \n")
##           then use a if to check if that name exsits or not
            for k in contacts.keys():
                if x in k :
    ##                if exsits that show the whole information and ask for a confirmation
                    print('Contact information:')
                    print(k)
                
                    confrim=input('Are you sure you want to delet this contact? yes/no \n')
        ##            if answer is yes then delete the objects and show dict
                    if confrim=="yes":
                        contacts.pop(k,v)
                        print('contact successfully deleted! return in main menu.')
                        break
                            
                    else:
                        print('Return in main menu')
                        break
                else:
                    continue

        elif entry==3:
##            making a loop to see the phonebook
            for k, v in contacts.items():
                print('*******************')
                print(k, ":" ,v)
        elif entry==4:
##            and for exit the program should use the exit func
            print('thanks for using this phonebook BYE!')
            exit()
        else:
##            if numbers were wrong the loop must continue and ask again
            print('incorect entry!')
            continue
if __name__=="__main__":
##    start the program
    phonebook()