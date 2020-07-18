class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class linked_list:
    
    def __init__(self):
        self.head = None
    
    def insert_last(self,data):
        
        if(self.head == None):
            node1 = node(data)
            self.head = node1
            print("first node has been inserted")
        else:
            node1 = node(data)
            temp = self.head
            
            while(temp.next != None):
                temp = temp.next
                
            temp.next = node1
            print("last node has been inserted")
            
    def delete_all_nodes(self):
        temp = self.head
        if(temp is None):
            print("not possible to delete empty list")
        else:
            while temp:

                self.head = temp.next
                temp = None
                temp = self.head
                
            print("value has been deleted")

    def delete_first_node(self):
        if(self.head == None):
            return print( "not possible to delete empty list")
        temp = self.head.data
        self.head = self.head.next
        
        print("value "+str(temp)+"has been deleted")
        del temp
        print("value has been deleted")


    def delete_last_node(self):
        if(self.head == None):
            return print( "not possible to delete empty list")
        temp = self.head
        previous_temp = temp
        while temp.next != None:
            previous_temp = temp

            temp = temp.next

        previous_temp.next = None
        val = temp.data
        temp = None
        del temp
        print("value "+str(val)+"has been deleted")

    def delete_desirable_node(self,p):
        if(self.head == None):
            return print("not possible to delete empty list")
        count = p-1
        temp = self.head
        previous_temp = temp
     

        while(count):
            previous_temp = temp

            temp = temp.next
            

            count = count -1

        previous_temp.next = temp.next
        val = temp.data
        temp = None
        del temp

        print("value "+str(val)+"has been deleted")




        



            
            
            
                
            
    def show_first_node(self):
        if(self.head == None):
            x = '''
             _______
            [_______]
                '''
            print(x)
            print("list is empty")
            
        else:
            temp = self.head
            
            while(temp.next != None):
                print(temp.data)
                temp = temp.next

            print(temp.data)
                
            temp = self.head
            
                  
            x = '''
            _______
           [_______]
               |
               '''
            
            while(temp.next != None):
                print(x,end=" ")
                temp = temp.next

          
            del temp
          
                
                
                
                
                
            
        


if __name__ == '__main__':
    
    
    
    l1 = linked_list()
    x =  c= True
    position = 0
    usr_int = 0
    while(x):
        x = """
        +++++++++++++++++++++++
        + 1:- To Insert value +
        + 2:- Show all value  +
        + 3:- Delete node value+
        + Q:- Quit            +
        +++++++++++++++++++++++    
        """

        print(x)

        user_inp = input("Enter your choise:- ")

        if(user_inp == '1'):
            value = input("Enter the value ")

            l1.insert_last(value)

        elif(user_inp == '2'):
            l1.show_first_node()

        elif(user_inp == '3'):

            c = True
            


        
            while(c):
                
                o = """
                    +++++++++++++++++++++++++++++
                    + 1:- Delete first node     +
                    + 2:- Delete Last node      +
                    + 3:- Delete all nodes      +
                    + 4:- Delete desirable node +
                    + Q:- Quit                  +
                    +++++++++++++++++++++++++++++


                """
                print(o)

                usr_int = input("Enter your choice")

                if(usr_int == "1"):
                    l1.delete_first_node()
                    
                elif(usr_int == "2"):
                    l1.delete_last_node()

                    
                elif(usr_int == "3"):
                    l1.delete_all_nodes()

                elif(usr_int == "4"):
                    position = int(input("Enter the position of node which you want to delete"))
                    l1.delete_desirable_node(position)
                    
                elif(usr_int == "Q" or usr_int == "q"):
                    c = False
                    print("exiting")

                    
                else:
                    Print("invalid input!")


                

        elif(user_inp == 'Q' or user_inp == 'q'):
            x = False
        else:
            print("invalid input")
            