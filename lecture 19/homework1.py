
class Node:
    def __init__(self, data=None):  # ვქმნით კვანძს რომელიც შეინახავს დატას და ლინკს, რომელიც დაუკავშირდება შემდეგ კვანძს
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # ინიციალიზაცია თავის სადაც მოთავსებული იქნება პირველი კვანძი

    def append(self, data):
        new_node = Node(data)

        if self.head is None:  # თუ ცარიელია სია ვქმნით თავს 
            self.head = new_node
            return

        last_node = self.head  # ლუპს ვიწყებთ პირველი კვანძიდან

        while last_node.next:   
            last_node = last_node.next  # ჩავდივართ ბოლო კვანძამდე

        last_node.next = new_node  # ვამატებთ ახალ კვანძს

    def remove_index(self, index):
        if index < 0 or self.head is None:  # return თუ რიცხვი უარყოფითია ან თავი არ არის შექმნილი 
            return

        if index == 0:  # თუ შეყვანილი ინდექსი პირველი კვანძია გადავაწერთ მომდევნო კვანძს
            self.head = self.head.next
            return

        current_node = self.head  # ძებნას ვიწყებთ პირველი კვანძიდან
        current_position = 0

        while current_node.next and current_position < index - 1:  # ვპოულობთ წასაშლელი კვანძის წინა კვანძს
            current_node = current_node.next
            current_position += 1

        if current_node.next:  # წაშლილისთვის კვანძის ადგილს იკავებს მისი შემდეგი კვანძი
            current_node.next = current_node.next.next

    def display(self):
        current_node = self.head  # ლუპს ვიწყებთ პირველი კვანძიდან

        while current_node is not None: 
            print(current_node.data, end=" -> ")  # ვპრინტავთ კვანძის დატას
            current_node = current_node.next  # გადავდივართ შემდეგ კვანძზე



class Stack:
    def __init__(self):  # ვქმნით კვანძს რომელიც შეინახავს დატას და ლინკს, რომელიც დაუკავშირდება შემდეგ კვანძს
        self.top_node = None
        self.length = 0

    def empty(self):  # ვამოწმებთ ცარიელია თუ არა სტაკი
        return self.length == 0   

    def size(self):  # ვაბრუნებთ სტაკის სიგრძეს
        return self.length  

    def push(self, data):  # ვამატებთ კვანძს 
        new_node = Node(data)  # ვქმნით Node ინსტანციას და ვაწოდებთ დატას
        new_node.next = self.top_node  # ახალ კვანძის ლინკს ვაკავშირებთ ტოპ კვანძთან
        self.top_node = new_node  # ვქმნით ტოპ კვანძს
        self.length += 1  # სტაკის სიგრძის გაზრდა

    def top(self):
        if not self.empty(): # თუ სტაკი ცაიელი არ არის ვაბრუნებთ ბოლო კვანძს
            return self.top_node.data 
        else:
            raise IndexError("Stack Is Empty")  # ერორი თუ კვანძი ცარიელია

    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data  # თუ სტაკი ცარიელი არ არის ტოპ კვანძის დატას ვინახავთ ცვლადში
            self.top_node = self.top_node.next  # წაშლისთვის ტოპ კვანძს გადავაწერთ
            self.length -= 1  # სტაკს სიგრძეს ვაკლებთ
            return popped_item
        else:
            raise IndexError("Stack Is Empty")


