class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
            
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
       
        # defining a blank res variable
        res = ""
         
        # initializing ptr to head
        ptr = self.head
         
       # traversing and adding it to res
        while ptr:
            res += str(ptr.val) + "-> "
            ptr = ptr.next
 
       # removing trailing commas
        res = res.strip("-> ")
         
        # chen checking if 
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"
    
    def append(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node
    
    def insertAtBegin(self, data):
        new_node = ListNode(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

def reverseList(head):
    new_list = None
    current = head
    
    while current:
        next_node = current.next
        current.next = new_list
        new_list = current
        current = next_node
    return new_list


linked_list = LinkedList()
linked_list.insertAtBegin(3)
linked_list.insertAtBegin(2)
linked_list.insertAtBegin(1)
print(str(linked_list))

new_list = LinkedList()
new_list_head = reverseList(linked_list.head)
while new_list_head:
    new_list.append(new_list_head.val)
    new_list_head = new_list_head.next

print(str(new_list))





