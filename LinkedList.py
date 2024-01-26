'''
The basic operations on a linkedlist which include-->
append: appends element to end of the list.
insert: inserts element to the beginning if the list.
insertpos: insert element to the preferred position(nodes are indexed from 1).
delete: searches for preferred element and deletes it.  
display: prints the linkedlist
'''
class Node:
    def __init__(self, v=None):
        self.value = v
        self.next = None
        return
    
    def isempty(self):
        if self.value == None:
            return(True)
        else:
            return(False)
    
    def append(self, v):
        if self.isempty():
            self.value = v
            return
        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = Node(v)
        return
    
    def insert(self, v):
        if self.isempty():
            self.value = v
            return
        newnode = Node(v)
        (self.value,newnode.value) = (newnode.value, self.value)
        (self.next, newnode.next) = (newnode, self.next)
        return
    
    def insertpos(self,v,pos):
        if self.isempty():
            return
        temp = self
        for i in range(pos-2):
            if temp.next != None:
                temp = temp.next
            else:
                print(f"Length of list exceeded., no node at positon {pos}")
                return
        newnode = Node(v)
        (newnode.next,temp.next) = (temp.next,newnode) 
        print(f"{v} is inserted at node-{pos}\n")
        return
    
    def delete(self, v):
        if self.isempty():
            return
        
        if self.value == v:
            self.value = None
            print(f"{v} is deleted")
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
            return 
        else:
            if self.value != None and self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
            else:
                print("Value not in list")
                return
        return
    
    def display(self):
        if self.isempty():
            return
        temp = self
        while temp != None:
            print(f"{temp.value}--", end='')
            temp = temp.next
        print("\n")

LL = Node()
while True:  
  choice = int(input("Select operation---\n1.Append, 2.Insert at beginning, 3.Insert at position, 4.Delete element, 5.Display, 6.Exit: "))
  match choice:
      case 1:
          value = int(input("Enter value to append: "))
          LL.append(value)
          print(f"{value} is appended\n")

      case 2:
          value = int(input("Enter value to insert: "))
          LL.insert(value)
          print(f"{value} is inserted\n")
      
      case 3:
          value = int(input("Enter value to insert: "))
          position = int(input("Enter position: "))
          LL.insertpos(value,position)
          
        
      case 4:
          value = int(input("Enter value to delete: "))
          LL.delete(value)
          
      case 5:
          print("The Linked-List: ")
          LL.display()
    
      case 6:
          break

      case default:
          print("Invalid input")


    
