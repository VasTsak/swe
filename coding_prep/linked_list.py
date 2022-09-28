class Node:

    def __init__(self, data: str):
        self.next = None
        self.data = data

    def __repr__(self):
        return self.data

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return " -> ".join(nodes)
    
    def prepend(self, node: Node):

        node.next = self.head
        self.head = node
        
    def append(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            prev_node = self.tail
            prev_node.next = node
            self.tail = node
    
    def append_no_tail(self, node: Node):
        next_node = self.head
        for node in self:
            new_node.next = node.next
            


def main():

    
    llist = LinkedList()
    llist.append(Node("1"))
    llist.append(Node("2"))
    llist.append(Node("3"))
    llist.prepend(Node("0"))
    print(llist)
            

if __name__ == "__main__":
    print((((5*60)+24)*26)/60)
    main()