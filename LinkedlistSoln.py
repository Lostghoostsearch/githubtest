class Element:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,head_node=None):
        self.head = head_node

    def append(self,data):
        New_node = data

        if self.head is None:
            self.head = New_node
            return

        Movingtolast = self.head

        while Movingtolast.next!=None:
            Movingtolast = Movingtolast.next

        Movingtolast.next = New_node

    def insert(self,data,position):
        fn_position = 1
        New_node = data

        Movingthrough = self.head

        while Movingthrough.next:
            if fn_position == position - 1:
                New_node.next =Movingthrough.next
                Movingthrough.next = New_node
                break
            else:
                fn_position +=1
                Movingthrough = Movingthrough.next
                continue
                

    def get_position(self,value):
        fn_position = 1
        Movingthrough = self.head
        while Movingthrough.next:
            if fn_position == value:
                break
            else:
                Movingthrough = Movingthrough.next
                fn_position +=1
        return Movingthrough

    def Display(self):
        b=[]
        Movingthrough = self.head
        while Movingthrough.next!=None:
            b.append(Movingthrough.value)
            Movingthrough=Movingthrough.next
        b.append(Movingthrough.value)
        print(b)
        
    def delete(self,data):
        delete_node = self.head
        p=1
        fn_position=1
        while delete_node.next:
            if delete_node.value == data:
                a=p
                savedata = delete_node.next
                break
            else:
                delete_node = delete_node.next
                p+=1
                continue
            
        Movingthrough = self.head
        if a-1==0:
            self.head = Movingthrough.next
        else:
            while Movingthrough.next:
                if fn_position == a - 1:
                    Movingthrough.next = savedata
                    break
                else:
                    fn_position +=1
                    Movingthrough = Movingthrough.next
                    continue   
        
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)       

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.Display()
print (ll.head.next.next.value)
print (ll.get_position(3).value)
ll.insert(e4,3)
ll.Display()
print (ll.get_position(3).value)
ll.delete(1)
ll.Display()
print (ll.get_position(1).value)
print (ll.get_position(2).value)
print (ll.get_position(3).value)
