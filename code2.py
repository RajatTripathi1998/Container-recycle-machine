list=[]
class Container_Recycling_Machine:
    #constructor for initializing_______________________________________
    def __init__(self,item,option,bal,can,bottle,box,n_item,money):
        self.item=item
        self.option=option
        self.bal=bal
        self.can=can
        self.bottle=bottle
        self.box=box
        self.n_item=n_item
        self.money=money
        
        
#this function select the product____________________________________

    def select_product(self):
        if(self.option=="stop"):
            exit()
        elif self.option=="can" or "bottle" or "box":
            self.item+=self.option
            
           
            self.n_item=int(input("How many {n_option} do you have? : ".format(n_option=self.option)))
           
            if (self.n_item<=0):
                print("Please Enter Valid input and Try again")
                input('Press Any key to Continue!!!!!')
                Container_Recycling_Machine.accept_product(self)
                
        
            if (self.n_item<=50):
                print("Please place {n_item} {n_option} into machine.".format(n_item=self.n_item,n_option=self.option))
                for i in range(self.n_item):
                    print("{n_option} accepted".format(n_option=self.option))
            else:
                print("Machine is full!!!!"+"Can't accept the item more than 50")
                input('Press Any key to Continue!!!!!')
                Container_Recycling_Machine.accept_product(self)
        
        if(self.option=="can" or self.option=="Can" or self.option=="CAN"):
            print("You added {n_item} {n_option}(s) for".format(n_item=self.n_item,n_option=self.option),"$",0.20)
            self.money=0.20*self.n_item
            self.item+=" "+str(self.n_item)+" "+str(self.money)+" "
            #list.append(self.item)
            can="can"
            list.append(can)
            list.append(self.money)
            

        elif(self.option=="bottle" or self.option=="Bottle" or self.option=="BOTTLE"):
            print("You added {n_item} {n_option}(s) for".format(n_item=self.n_item,n_option=self.option),"$",0.50)
            self.money=0.50*self.n_item
            self.item+=" "+str(self.n_item)+" "+str(self.money)+" "
            #list.append(self.item)
            bottle="bottle"
            list.append(bottle)
            list.append(self.money)
      
            
        elif(self.option=="box"):
            print("You added {n_item} {n_option}(s) for ".format(n_item=self.n_item,n_option=self.option),"$",0.80)
            self.money=0.80*self.n_item
            self.item+=" "+str(self.n_item)+" "+str(self.money)+" "
            #list.append(self.item)
            box="box"
            list.append(box)
            list.append(self.money)
            
      
        

        print("You now have $  "+"{:.1f}".format(self.money))
        self.bal+=self.money
        print("Total Balance is  "+"{:.1f}".format(self.bal))
        Container_Recycling_Machine.accept_product(self)
    
    # this function accepts the product______________________________________
    def accept_product(self):
        print("\n")
        print("Balance: $"+"{:.2f}".format(self.bal)+ "  Please select a product: (Can,Bottle,Box,Stop): ")
        self.option=input("")
        
        a=["can","bottle","box","CAN","BOTTLE","BOX","Can","Bottle","Box"]
        if self.option in a:
            self.option=str(self.option)
            Container_Recycling_Machine.select_product(self)
        elif self.option=='stop' or self.option=='Stop' or self.option=='STOP':
            Container_Recycling_Machine.print_recipt(self)

            
        else:
            print("Invalid input please choose from the product")
            Container_Recycling_Machine.accept_product(self)
        Container_Recycling_Machine.payout(self)
            

    

    #function used to print the recipt__________________________ 
    def print_recipt(self):
        print("\n---------Final Recipt--------\n")
        l=self.item.split(" ")
        
        try:
            for i in range(5):
                if list[i]=="can":
                    print("can             "+"{:.2f}".format(list[i+1]))
                elif list[i]=="bottle":
                    print("bottle        "+"{:.2f}".format(list[i+1]))
                elif list[i]=="box":
                    print("box            "+"{:.2f}".format(list[i+1]))
            print("\n")
            print("Number of containers:                ",self.n_item+1)
            print("Amount paid:                      ",self.bal)
        except:
                print("\n")
                print("Number of containers:        ",self.n_item)
                print("Amount paid:                      "+"{:.2f}".format(self.bal))
                print("\n")
                
                    


        #print("Total Balance is",self.bal)
        print("Thank you for recycling at FedUni!")
        self.item=" "
        


    def payout(self):
        
        self.l=input("(N)ext or (Q)uit? ")
        if self.l=='n' or self.l=='N' or self.l=='next' or self.l== 'Next':
            Container_Recycling_Machine.accept_product(self)
            #object.select_product()

        elif self.l=='q' or self.l=='Q' or self.l=='quit' or self.l=='Quit':
            quit()
        else:
            print("Something went wrong")
        

    

    
    



            
            
