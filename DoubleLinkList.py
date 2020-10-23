class Node:
    def __init__(self,data,next,prev):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self,data):
        if self.head == None :
            node = Node(data,self.head,self.head)
            self.head = node
            return
        node = Node(data,self.head,None)
        self.head.prev = node
        self.head = node
        return

    def print_forward(self):
        if self.head == None:
            print("No element")
            return
        itr = self.head
        liststr = ''
        while itr:
            liststr += str(itr.data)+"--->"
            itr = itr.next

        print(liststr)

    def get_length(self):
        count = 0
        if self.head == None:
            return count
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def print_backward(self):
        if self.head == None:
            print("No element")
            return
        itr = self.head
        liststr = ''
        while itr.next:
            itr = itr.next
        while itr:
            liststr += str(itr.data)+"--->"
            itr = itr.prev
        print(liststr)

    def insert_elemnt(self,list):
        for listitem in list:
            self.insert_begining(listitem)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_elemnt([12,13,14,15,46])
    ll.print_backward()
    ll.print_forward()