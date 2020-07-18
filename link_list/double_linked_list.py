class node :
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


class double_linked_list:
    def __init__(self,):
        self.head = None

    def insert_first_node(self,data):

        node1 = node(data)
        if(self.head  == None):
            self.head = node1
            print("value has been inserted")
        
        else:

            temp = self.head

            while temp.next != None:

                temp = temp.next
                
            temp.next = node1
            node1.prev = temp
            del temp
            print("value has been inserted")

    def traversing(self):
        if(self.head == None):
            print("node is empty")

        else:
            temp = self.head

            while temp.next != None:
                print(temp.data)
                temp = temp.next

            print(temp.data)


l1 = double_linked_list()
l1.insert_first_node(10)
l1.insert_first_node(50)
l1.traversing()