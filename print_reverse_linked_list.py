'''
'''

class linked_list:
    def __init__(self):
        self.node_values = { 'a' : '1',
                    'b' : '2',
                    'c' : '3' }
        self.ll = ['a','b','c','']
        pass

    def next_node(self,node):
        current_node_index = self.ll.index(node)
        next_node_index = current_node_index + 1
        return self.ll[next_node_index]
    
    def value(self,node):
        return self.node_values[node]

    def recursively_print_backwards(self,node):
        if node == '':
            return node
        else:
            self.recursively_print_backwards(self.next_node(node))
            print self.value(node)
            return node
def main():
    ll = linked_list()
    node = 'a'
    ll.recursively_print_backwards(node)

    #while node != '':
    #    node = ll.next_node(node)
    #    print node

if __name__ == '__main__':
    main()
