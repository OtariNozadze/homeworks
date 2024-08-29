class Functor:
    def __init__(self, value=int):
        self.value = value
    def __call__(self):
        if self.value < 0:
            raise ValueError("The Number Must Be Positive")
        print(self.value)
        return self.value

positive_num = Functor(6)
positive_num()
neg_num = Functor(-10)
neg_num()


        
