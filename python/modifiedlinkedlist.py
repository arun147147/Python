class Node:
    def __init__(self,data):
        self.data=data
        self.link=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.last_node=None

    def insert_end(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head

        else:
            self.last_node.link=Node(data)
            self.last_node=self.last_node.link

    def insert_front(self,data):
        if self.last_node is None:
            self.head=Node(data)
            self.last_node=self.head

        else:
            self.new_node=Node(data)
            self.new_node.link=self.head
            self.head=self.new_node


    def delete_front(self):
        if self.last_node is None:
            print("there is no elements to delete from linked list")
        else:
            curr=self.head
            self.head=self.head.link
            print("first element is deleted")
            curr.link=None

    def delete_end(self):
        if self.last_node is None:
            print("There is mo elements to delete from linked list")
        else:
            curr=self.head
            prev=self.head
            while curr.link is not None:
                prev=curr
                curr=curr.link

            print("last element is deleted")
            prev.link=None

    def insert_middle(self,pos,data):
        if self.last_node is None:
            print("there is no elements to insert at particular position")
        else:
            curr=self.head
            while curr.data!=pos :
                curr=curr.link

            new_node=Node(data)
            new_node.link=curr.link
            curr.link=new_node


    def find_pos(self,value):
        if self.last_node is None:
            print("There is no lements to search position")
        else:
            curr=self.head
            pos=0
            while curr.data!=value :
                pos=pos+1
                curr=curr.link
            print("element is found at %pos position")
            print(pos)
    def display(self):
        curr=self.head
        while curr is not None:
            print(curr.data)
            curr=curr.link

list=LinkedList()
n=int(input("enter how many elements you want to insert : "))
for i in range(n):
    data=int(input("enter element : "))
    list.insert_front(data)
    #list.insert_end(data)
list.display()
#list.delete_end()
list.delete_front()
list.display()
print("insertion at middle : ")
list.insert_middle(30,100)
list.display()
n=int(input("enter element to find position"))
list.find_pos(n)
