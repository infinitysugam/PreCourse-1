# Time complexity = O(n)
# Space Complexity = O(n)
class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        new_node = ListNode(data)
        if not self.head:
            self.head=new_node
            return 

        current = self.head
        while current.next is not None:
            current=current.next
        current.next = new_node


        
    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """

        current = self.head
        while current:
            if current.data == key:
                return current
            current=current.next
        return None


        
    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        current=self.head
        prev = None

        if current and current.data == key:
            self.head = self.head.next
            return

        while current and current.data != key:
                prev=current
                current = current.next
        if current:
            prev.next=current.next

        
        return None
