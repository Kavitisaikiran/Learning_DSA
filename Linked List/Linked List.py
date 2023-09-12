First we create a class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# Insertipon of element at begining at linked list 
# Create new node for new data 
  
    def insertionatbegining( self, data):
    # create new node for the new data insertion 
        new_node = Node(data)
        new_node.next = self.head # here it says inserting the data at first of LL
        self.head = new_node


# Insertion at the end of the LL:

def insertionatend(self, data):
  temp = self.head
  new_node = Node(data)
  if self.head is None: #when theLL is empty
    self.head = new_node
    return
  while temp.next :
    temp = temp.next
  temp.next = new_node
  

  # Insertion at mid/any place
  def insertatany(self, data):
    if prev_node is None:
      print(no node available)
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node
    
#Priniting the linked list 
  def linkedlist(self):
    current = self.head
    while current:
      print(str(current.data))  # converts the integer data type to string before printing 
      current = current.next
