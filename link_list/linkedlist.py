class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.start = None

    def insert_last(self,value):
        newNode = node(value)
        if(self.start == None):
            self.start = newNode
            print("value has been inserted")
        else:
            temp = self.start
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
            print("value has been inserted")

    #------- traversing value--------#
    def traversing(self):
        if(self.start == None):
            print("list is empty")
        else:
            temp = self.start
            while temp.next != None:
                print(temp.data)
                temp = temp.next
            print(temp.data)

    def size(self):
        if(self.start == None):
            return 0
        else:
            temp = self.start
            n = 0
            flag = 0
            while temp.next != None:
                flag = 1
                n += 1
                temp = temp.next

            if(flag == 0):
                return 1
            else:
                return n+1
    def delete_first(self):
        if(self.start == None):
            print("list is empty,  nothing to delete")
        else:
            self.start = self.start.next
            print("first node has been deleted")

                
                

            

node1 = linked_list()
node1.insert_last(20)
node1.insert_last(30)
node1.traversing()
print(node1.size())
node1.delete_first()
node1.insert_last(20)
node1.insert_last(30)
node1.traversing()
print(node1.size())




