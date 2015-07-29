import time
import numpy as np
from linkedlist import LinkedList
from Trees import BST,AVL
from matplotlib import pyplot as plt
from WordList import create_word_list


def iterative_search(linkedlist, data):
    current = linkedlist.head
    while current is not None:
        if current.data == data:
            return current
        current = current.next
    raise ValueError(str(data) + " is not in the list.")

def recursive_search(linkedlist, data):
    def _search(node, data):
        while node is not None:
            if node.data == data:
                return data
            else:
                return _search(node.next, data)
        raise ValueError(str(data) + " is not in the list.")
    current = linkedlist.head
    return _search(current, data)

def timings():
    ll = LinkedList()
    bst = BST()
    avl = AVL()

    ll_add = []
    bst_add = []
    avl_add = []

    ll_search = []
    bst_search = []
    avl_search = []

    for items in range(500,5500,500):
        wordlist = create_word_list(items)
        
        ll = LinkedList()
        before = time.time()
        for i in xrange(items):
            ll.add_node(wordlist[i])
        after = time.time()
        ll_add.append(after - before)
    
        random_indices = np.random.random_integers(0,items,5)
        temp = []
        for i in xrange(len(random_indices)):
            before = time.time()
            iterative_search(ll, wordlist[random_indices[i]]) 
            after = time.time()
            temp.append(after - before)
        ll_search.append(sum(temp)/len(temp))
    
        bst = BST()
        before = time.time()
        for i in xrange(items):
            bst.insert(wordlist[i])
        after = time.time()
        bst_add.append(after - before)

        temp = []
        for i in xrange(len(random_indices)):
            before = time.time()
            bst.find(wordlist[random_indices[i]])
            after = time.time()
            temp.append(after - before)
        bst_search.append(sum(temp)/len(temp))

        avl = AVL()
        before = time.time()
        for i in xrange(items):
            avl.insert(wordlist[i])
        after = time.time()
        avl_add.append(after - before)
        
        temp = []
        for i in xrange(len(random_indices)):
            before = time.time()
            avl.find(wordlist[random_indices[i]])
            after = time.time()
            temp.append(after - before)
        avl_search.append(sum(temp)/len(temp))
    
    plt.subplot(1,2,1)
    plt.plot(ll_add, "r")
    plt.plot(bst_add, "g")
    plt.plot(avl_add, "b")
    plt.subplot(1,2,2)
    plt.plot(ll_search, "r")
    plt.plot(bst_search, "g")
    plt.plot(avl_search, "b")
    plt.show()
    plt.close()
    
    return ll_add, ll_search, bst_add, bst_search, avl_add, avl_search

        
        

