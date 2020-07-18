
# Python program to demonstrate  
# circular linked list traversal  
  
# Structure for a Node 
class Node: 
      
    # Constructor to create  a new node 
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class CircularLinkedList: 
      
    # Constructor to create a empty circular linked list 
    def __init__(self): 
        self.head = None
  
    # Function to insert a node at the beginning of a 
    # circular linked list 
    def push(self, data): 
        ptr1 = Node(data) 
        temp = self.head 
          
        ptr1.next = self.head 
  
        # If linked list is not None then set the next of 
        # last node 
        if self.head is not None: 
            while(temp.next != self.head): 
                temp = temp.next 
            temp.next = ptr1 
  
        else: 
            ptr1.next = ptr1 # For the first node 
  
        self.head = ptr1

    def insert_position(self,data,p):
        ptr1 = Node(data)
        temp = self.head
        p = p-1


        if(temp.next == None):
            print("list is empty")
        else:
            previous_node = temp
            while(p):

                previous_node = temp
                temp = temp.next
                p -= 1

            ptr1.next = previous_node.next
            previous_node.next = ptr1
            del temp,previous_node
           

           
            print("value has been inserted")
     
  
    # Function to print nodes in a given circular linked list 
    def printList(self): 
        temp = self.head 
        if self.head is not None: 
            while(True): 
                print(temp.data) 
                temp = temp.next
                if (temp == self.head): 
                    break

        else:
            print("list is empty") 

    def delete_first_node(self):
        temp = self.head
        if(temp == None):
            print("can't possible to delete an empty list")
            return 0
        else:
            t = temp
            self.head = temp.next

            while(True):

                t = t.next
                if(t.next == temp):
                    break

            t.next = self.head
            temp.next = None
            print("value has been deleted"+str(temp.data))
            del temp
            print("value has been deleted")

    def delete_last_node(self):
        temp = self.head
        if(temp == None):
            print("can't possible to delete an empty list")
        else:
            previous_node = temp

            while(True):
                previous_node = temp
                temp = temp.next
                if(temp.next == self.head):
                    break 
            

            previous_node.next = self.head

            temp.next = None
            del temp
            print("last node has been deleted")  
                


                



  
  
# Driver program to test above function 
  
# Initialize list as empty 
cllist = CircularLinkedList() 
  
# Created linked list will be 11->2->56->12 
cllist.push(12) 
cllist.push(56) 
cllist.push(2) 
cllist.push(11)
cllist.insert_position(41,3) 
cllist.printList()

cllist.delete_first_node()
cllist.delete_last_node()
  
print( "Contents of circular Linked List")
cllist.printList() 
            
# This code is contributed by  
# Nikhil Kumar Singh(nickzuck_007) 
