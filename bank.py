class Bank:
    acbal=10000

    def confirm(self):
        print("1. Contiue ")
        print("0. Exit")
        option=int(input("Choose your option :"))
        if option==1:
            obj.viewOptions()

    def withdraw(self):
        amount=int(input("Enter withdraw amount"))
        if amount%100==0:
            if amount<=20000:
                if amount<=self.acbal:
                    self.acbal=self.acbal-amount
                    print("Available bal is: ",self.acbal)


                else:
                    print("Insufficent fund")

            else:
                print("transaction limit it 20K only")

        else:
            print("Please enter multiples of 100")

        
    def deposite(self):
        amount=int(input("Enter deposit amount"))
        if amount%100==0:
            if amount<=50000:
                self.acbal=self.acbal+amount
            else:
                print("Deposit limit is 50K only")
        else:
            print("Please enter multiples of 100 only")
        print("Available bal is: ",self.acbal)

    def viewOptions(self):
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Bal Enquiry")
            print("0. Exit")
            option=int(input("choose your option"))
            if option==1:
                obj.deposite()
                obj.confirm()

            elif option==2:
                obj.withdraw()
                obj.confirm()
        
    def validate(self):
        pin = 1234
        print("Welcome to RKCE bank")
        upin=int(input("Enter your pin : "))

        if upin==pin:
            obj.viewOptions()
                       
        else:
            print("Invalid pin")
obj=Bank()
obj.validate()
