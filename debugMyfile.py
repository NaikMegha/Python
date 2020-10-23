class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next =next

class LinkedList():
    def __init__(self):
        self.head = None

    def insert_element_begining(self,data):
        node = Node(data,self.head)
        self.head = node

    def print(self):
        if self.head == None:
            print("No elements")
            return
        itr = self.head
        liststr =''
        while itr:
            liststr += str(itr.data)+"--->"
            itr = itr.next
        print(liststr)

    def insert_at_end(self,data):
        temp = self.head
        node = Node(data, None)
        if temp == None:
            self.head = node
            return
        while temp.next:
            temp = temp.next
        temp.next = node

    def insert_values(self,data_list):
        self.head=None;
        for data in data_list:
            self.insert_at_end(data)

    def get_length_list(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count +=1
        return count

    def remove_at_index(self, index):
        if index < 0 or index > self.get_length_list():
            raise Exception("Cannot delete item")
        if index == 0:
            self.head = self.head.next
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_at_index(self, index, data):
        length_list = self.get_length_list()
        if index < 0 or index > length_list:
            raise Exception("Invalid index")

        if index == 0:
            self.insert_element_begining(data)
            return
        if index == length_list:
            self.insert_at_end( data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index-1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1

    def add_after_value(self,data,value):
        if self.head == None:
            print("No item! Adding the data as first item")
            node = Node(data,self.head)
            self.head = node
            return
        itr = self.head
        found = False
        while itr:
            if str(itr.data) == value:
                node = Node(data, itr.next)
                itr.next = node
                found =True
                break
            itr = itr.next
        if not found:
            print("'{}' not found in the existing list".format(value))

    def remove_by_value(self,value):
        if self.head == None:
            return
        itr = self.head
        if itr.data == value:
            self.head = itr.next
            return

        found = False
        while itr.next:
            if str(itr.next.data) == value:
                found = True
                itr.next = itr.next.next
                break
            itr = itr.next
        if not found:
            print("'{}' not found".format(value))

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.add_after_value("apple", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
