class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class stack:
    def __init__(self):
        self.top=None
    
    def isempty(self):
        return self.top is None
    
    
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node
    
    def pop(self):
        if self.isempty():
            print("Stack Empty")
        else:
            temp=self.top
            print("Poped Element: ",temp.data)
            self.top=self.top.next
            temp=None
    
    # def reverse(self):
    #     temp=self.top
    #     while temp:
    #         st1.push(Node(temp.data))
    #         temp=temp.next

       
    def print(self):
        temp=self.top
        while temp:
            print(temp.data)
            temp=temp.next
class Queue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node
    def dequeue(self):
        if self.front:
            temp=self.front
            dequed_data=temp.data
            self.front=self.front.next
            if self.front==None:
                self.rear==None
                print("Now Queue is Empty")

            temp=None
            return dequed_data
        else:
            print("Queue is Empty")
    
    def is_empty(self):
        return self.front is None
   
    def print(self):
        temp=self.front

        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()
    
def reverse_queue(q1):
    st1=stack()
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))

    st1.print()
def reverse_stack(s1):
    q1=Queue()
    while not s1.isempty():
        q1.enqueue(Node(s1.pop()))
    q1.print()


lq=Queue()
lq.enqueue(Node(15))
lq.enqueue(Node(24))
lq.enqueue(Node(33))
lq.enqueue(Node(42))
lq.enqueue(Node(51))
lq.enqueue(Node(60))
lq.print()
reverse_queue(lq)
# lq.dequeue()
# lq.dequeue()
# lq.dequeue()
# lq.print()
# lq.enqueue(Node(69))
# lq.enqueue(Node(87))
# lq.print()

# st=stack()
st=stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.print()
reverse_stack(st)
# st.pop()
# #st.print()
# st.reverse()
# st1.print()