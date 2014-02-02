class stack:
    '''
    first in / last out
    '''
    def __init__(self,array=[]):
        self.s = array
        pass

    def get_element(self):
        first_item =  self.s[0]
        self.s.pop(0)
        return first_item

    def add_element(self,element):
        self.s.append(element)

    def unload_stack(self):
        while len(self.s) !=0:
            print self.get_element()

class queue:
    """
    last in / first out
    """
    def __init__(self,array=[]):
        self.stack = stack(array)
        self.reversed_stack_aka_queue = []
        self._unload_queue()
        self.queue = stack(self.reversed_stack_aka_queue)


    def unload_queue(self, stack):
        if len(stack.s) == 1:
            el= stack.get_element()
            print el
            return el
        else:
            el = stack.get_element()
            self.unload_queue(stack)
            print el
            return el

    def _unload_queue(self):
        if len(self.stack.s) == 1:
            el= self.stack.get_element()
            self.reversed_stack_aka_queue.append(el)
            return el
        else:
            el = self.stack.get_element()
            self._unload_queue()
            self.reversed_stack_aka_queue.append(el)
            return el

    def get_element(self):
        return self.queue.get_element()
        

    def add_element(self,element):
#        #reverse
#        self.stack = stack(self.queue.s)
#        self.reversed_stack_aka_queue = []
#        self._unload_queue()
#        temp_stack = stack(self.reversed_stack_aka_queue)
#        #add element
#        temp_stack.add_element(element)
#        print temp_stack.s
#        #reverse back
#        self.stack = stack(temp_stack.s)
#        self.reversed_stack_aka_queue = []
#        self._unload_queue()
#        self.queue = stack(self.reversed_stack_aka_queue)
        self.queue.add_element(element)

def main():

    print 'stack'
    stack_obj = stack([1,2,3,4,5,6])
    stack_obj.unload_stack()
    print 'queue menthod 1'
    #stack_obj = stack([1,2,3,4,5,6])
    #queue_obj = queue()
    #queue_obj.unload_queue(stack_obj)
    print 'queue method 2'
    queue_obj = queue([1,2,3,4,5,6])
    print queue_obj.get_element()
    queue_obj.add_element(0)
    print queue_obj.get_element()
    



    

if __name__ == "__main__":
    main()
