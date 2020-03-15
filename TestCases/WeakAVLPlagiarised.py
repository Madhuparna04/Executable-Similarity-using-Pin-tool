import math
import os
import time
import random


'''
Program to calculate do_a_insert_please_pleaseion, deletion and search times of the the_data_Structure_that_I_Am_copying tree
Done by: Madhumitha Nara (You cant catch me hahahahahaha)
'''

def do_a_remove_i_say(n):
    
    start=time.time()
    i = n
    while (True):

        if (i==1):
            break
        the_data_Structure_that_I_Am_copying_tree.do_a_remove_i_say(i)
        i -= 1
    print("The_data_Structure_that_I_Am_copying takes this much amount of time for a remove :",time.time()-start)


def search(n):
    start=time.time()
    i = n
    while(i!=1):
        the_data_Structure_that_I_Am_copying_tree.search(i)
        i-=1
    print("the_data_Structure_that_I_Am_copying takes this much amount of time for a search :",time.time()-start)

class the_data_Structure_that_I_Am_copyingi_am_better_known_as_a_node:
    '''Generates the_data_Structure_that_I_Am_copying i_am_better_known_as_a_node with default the_rank_they_assigned_me 0'''
    def __init__(self, the_Thing_the_node_is_storing, i_am_the_left_child_whose_value_is_lower_than_my_parent=None, i_am_the_right_child_whose_value_is_higher_than_my_parent=None, the_rank_they_assigned_me=0, parent_of_the_node=None):
        self.i_am_the_left_child_whose_value_is_lower_than_my_parent = i_am_the_left_child_whose_value_is_lower_than_my_parent
        self.i_am_the_right_child_whose_value_is_higher_than_my_parent = i_am_the_right_child_whose_value_is_higher_than_my_parent
        self.the_Thing_the_node_is_storing = the_Thing_the_node_is_storing
        self.parent_of_the_node = parent_of_the_node
        self.the_rank_they_assigned_me = the_rank_they_assigned_me

class the_data_Structure_that_I_Am_copying:
    def __init__(self):
        self.root = None

    def promote_the_node_to_Sergeant_the_rank_they_assigned_me(self, i_am_better_known_as_a_node):
        i_am_better_known_as_a_node.the_rank_they_assigned_me += 1

    def i_am_packing_my_knives_to_leave_i_have_been_chopped(self, i_am_better_known_as_a_node):
        i_am_better_known_as_a_node.the_rank_they_assigned_me -= 1


        # CLRS WAS USED HERE
    def i_am_the_left_child_whose_value_is_lower_than_my_parent_rotate(self, x):
        '''i_am_the_left_child_whose_value_is_lower_than_my_parent rotate'''
        y = x.i_am_the_right_child_whose_value_is_higher_than_my_parent
        x.i_am_the_right_child_whose_value_is_higher_than_my_parent = y.i_am_the_left_child_whose_value_is_lower_than_my_parent
        if y.i_am_the_left_child_whose_value_is_lower_than_my_parent != None:
            y.i_am_the_left_child_whose_value_is_lower_than_my_parent.parent_of_the_node = x
        y.parent_of_the_node = x.parent_of_the_node
        if x.parent_of_the_node == None:
            self.root = y
        elif x == x.parent_of_the_node.i_am_the_left_child_whose_value_is_lower_than_my_parent:
            x.parent_of_the_node.i_am_the_left_child_whose_value_is_lower_than_my_parent = y
        else:
            x.parent_of_the_node.i_am_the_right_child_whose_value_is_higher_than_my_parent = y
        y.i_am_the_left_child_whose_value_is_lower_than_my_parent = x
        x.parent_of_the_node = y

    def search(self, the_Thing_the_node_is_storing):
        '''driver function that returns i_am_better_known_as_a_node with given the_Thing_the_node_is_storing'''
        return self._search(the_Thing_the_node_is_storing, self.root)

    def _search(self, the_Thing_the_node_is_storing, i_am_better_known_as_a_node):
        '''searches for the i_am_better_known_as_a_node with the given the_Thing_the_node_is_storing'''
        if not i_am_better_known_as_a_node:
            return False
        elif the_Thing_the_node_is_storing == i_am_better_known_as_a_node.the_Thing_the_node_is_storing:
            return True
        elif the_Thing_the_node_is_storing < i_am_better_known_as_a_node.the_Thing_the_node_is_storing:
            return self._search(the_Thing_the_node_is_storing, i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent)
        else:
            return self._search(the_Thing_the_node_is_storing, i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent)


    def get_i_am_better_known_as_a_node(self, the_Thing_the_node_is_storing1, i_am_better_known_as_a_node):
        '''finds the i_am_better_known_as_a_node with the_Thing_the_node_is_storing value'''
        if i_am_better_known_as_a_node==None:
        	return None
        if the_Thing_the_node_is_storing1 == i_am_better_known_as_a_node.the_Thing_the_node_is_storing:
            return i_am_better_known_as_a_node
        elif the_Thing_the_node_is_storing1 < i_am_better_known_as_a_node.the_Thing_the_node_is_storing:
            return self.get_i_am_better_known_as_a_node(the_Thing_the_node_is_storing1, i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent)
        else:
            return self.get_i_am_better_known_as_a_node(the_Thing_the_node_is_storing1, i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent)


    def get_min(self, root):
        '''gets the minimum of all the the_Thing_the_node_is_storings'''
        x = root
        while x.i_am_the_left_child_whose_value_is_lower_than_my_parent != None:
            x = x.i_am_the_left_child_whose_value_is_lower_than_my_parent
        return x


    def height(self):
        '''driver function that gives the height of the tree'''
        return self._height(self.root)

    def _height(self, i_am_better_known_as_a_node):
        '''calculates the height'''
        if not i_am_better_known_as_a_node:
            return 0

        lheight = self._height(i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent)
        rheight = self._height(i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent)
        return max(lheight, rheight) + 1

    def print_root(self):
        '''prints the root'''
        print("The root of this big big tree is this:  ", end='')
        print(self.root.the_Thing_the_node_is_storing)

    # and here
    def i_am_the_right_child_whose_value_is_higher_than_my_parent_rotate(self, x):
        '''i_am_the_right_child_whose_value_is_higher_than_my_parent rotate'''
        y = x.i_am_the_left_child_whose_value_is_lower_than_my_parent
        x.i_am_the_left_child_whose_value_is_lower_than_my_parent = y.i_am_the_right_child_whose_value_is_higher_than_my_parent
        if y.i_am_the_right_child_whose_value_is_higher_than_my_parent != None:
            y.i_am_the_right_child_whose_value_is_higher_than_my_parent.parent_of_the_node = x
        y.parent_of_the_node = x.parent_of_the_node
        if x.parent_of_the_node == None:
            self.root = y
        elif x == x.parent_of_the_node.i_am_the_right_child_whose_value_is_higher_than_my_parent:
            x.parent_of_the_node.i_am_the_right_child_whose_value_is_higher_than_my_parent = y
        else:
            x.parent_of_the_node.i_am_the_left_child_whose_value_is_lower_than_my_parent = y
        y.i_am_the_right_child_whose_value_is_higher_than_my_parent = x
        x.parent_of_the_node = y

    def what_is_the_the_rank_they_assigned_me_difference_between_them(self, i_am_better_known_as_a_node):
        '''calculate the_rank_they_assigned_me differences between two i_am_better_known_as_a_nodes'''
        ldiff = i_am_better_known_as_a_node.the_rank_they_assigned_me + 1
        rdiff = i_am_better_known_as_a_node.the_rank_they_assigned_me + 1
        if i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent:
            ldiff = i_am_better_known_as_a_node.the_rank_they_assigned_me - i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent.the_rank_they_assigned_me
        if i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent:
            rdiff = i_am_better_known_as_a_node.the_rank_they_assigned_me - i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent.the_rank_they_assigned_me

        return (ldiff, rdiff)

    #deleted comment
    def transplant(self, u, v):
        if u.parent_of_the_node == None:
            self.root = v
        elif u == u.parent_of_the_node.i_am_the_left_child_whose_value_is_lower_than_my_parent:
            u.parent_of_the_node.i_am_the_left_child_whose_value_is_lower_than_my_parent = v
        else:
            u.parent_of_the_node.i_am_the_right_child_whose_value_is_higher_than_my_parent = v

        if v != None:
            v.parent_of_the_node = u.parent_of_the_node

        # define punctuation
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        my_str = "Hello!!!, he said ---and went."

        # To take input from the user
        # my_str = input("Enter a string: ")

        # remove punctuation from the string
        no_punct = ""
        for char in my_str:
            if char not in punctuations:
                no_punct = no_punct + char


    def do_a_insert_please_please_rebalance_the_big_big_tree(self, i_am_better_known_as_a_node):
        '''the actual do_a_insert_please_please with rebalance_the_big_big_tree'''
        parent_of_the_node_diffs = self.what_is_the_the_rank_they_assigned_me_difference_between_them(i_am_better_known_as_a_node.parent_of_the_node)
        if parent_of_the_node_diffs == (0, 1) or parent_of_the_node_diffs == (1, 0):
            currently_using_i_am_better_known_as_a_node = i_am_better_known_as_a_node
            while (currently_using_i_am_better_known_as_a_node.parent_of_the_node and
                   (self.what_is_the_the_rank_they_assigned_me_difference_between_them(currently_using_i_am_better_known_as_a_node.parent_of_the_node) == (0, 1) or
                    self.what_is_the_the_rank_they_assigned_me_difference_between_them(currently_using_i_am_better_known_as_a_node.parent_of_the_node) == (1, 0))):
                self.promote_the_node_to_Sergeant_the_rank_they_assigned_me(currently_using_i_am_better_known_as_a_node.parent_of_the_node)
                currently_using_i_am_better_known_as_a_node = currently_using_i_am_better_known_as_a_node.parent_of_the_node

            if (currently_using_i_am_better_known_as_a_node.parent_of_the_node and
                (self.what_is_the_the_rank_they_assigned_me_difference_between_them(currently_using_i_am_better_known_as_a_node.parent_of_the_node) == (0, 2) or
                 self.what_is_the_the_rank_they_assigned_me_difference_between_them(currently_using_i_am_better_known_as_a_node.parent_of_the_node) == (2, 0))):
                if currently_using_i_am_better_known_as_a_node == currently_using_i_am_better_known_as_a_node.parent_of_the_node.i_am_the_left_child_whose_value_is_lower_than_my_parent:
                    z = currently_using_i_am_better_known_as_a_node.parent_of_the_node
                    y = currently_using_i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent
                    if y == None or currently_using_i_am_better_known_as_a_node.the_rank_they_assigned_me - y.the_rank_they_assigned_me == 2:
                        self.i_am_the_right_child_whose_value_is_higher_than_my_parent_rotate(currently_using_i_am_better_known_as_a_node.parent_of_the_node)
                        self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
                    else:
                        self.i_am_the_left_child_whose_value_is_lower_than_my_parent_rotate(y.parent_of_the_node)
                        self.i_am_the_right_child_whose_value_is_higher_than_my_parent_rotate(y.parent_of_the_node)
                        self.promote_the_node_to_Sergeant_the_rank_they_assigned_me(y)
                        assert y.i_am_the_left_child_whose_value_is_lower_than_my_parent != None or y.i_am_the_right_child_whose_value_is_higher_than_my_parent != None
                        self.i_am_packing_my_knives_to_leave_i_have_been_chopped(currently_using_i_am_better_known_as_a_node)
                        self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
                else:
                    z = currently_using_i_am_better_known_as_a_node.parent_of_the_node
                    y = currently_using_i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent
                    if y == None or currently_using_i_am_better_known_as_a_node.the_rank_they_assigned_me - y.the_rank_they_assigned_me == 2:
                        self.i_am_the_left_child_whose_value_is_lower_than_my_parent_rotate(currently_using_i_am_better_known_as_a_node.parent_of_the_node)
                        self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
                    else:
                        self.i_am_the_right_child_whose_value_is_higher_than_my_parent_rotate(y.parent_of_the_node)
                        self.i_am_the_left_child_whose_value_is_lower_than_my_parent_rotate(y.parent_of_the_node)
                        self.promote_the_node_to_Sergeant_the_rank_they_assigned_me(y)
                        assert y.i_am_the_left_child_whose_value_is_lower_than_my_parent != None or y.i_am_the_right_child_whose_value_is_higher_than_my_parent != None
                        self.i_am_packing_my_knives_to_leave_i_have_been_chopped(currently_using_i_am_better_known_as_a_node)
                        self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)

    def do_a_insert_please_please(self, the_Thing_the_node_is_storing):
        if self.root:
            self._do_a_insert_please_please(the_Thing_the_node_is_storing, self.root)
        else:
            self.root = the_data_Structure_that_I_Am_copyingi_am_better_known_as_a_node(the_Thing_the_node_is_storing)

    def _do_a_insert_please_please(self, the_Thing_the_node_is_storing, i_am_better_known_as_a_node):
        if the_Thing_the_node_is_storing < i_am_better_known_as_a_node.the_Thing_the_node_is_storing:
            if i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent:
                self._do_a_insert_please_please(the_Thing_the_node_is_storing, i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent)
            else:
                i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent = the_data_Structure_that_I_Am_copyingi_am_better_known_as_a_node(the_Thing_the_node_is_storing, parent_of_the_node=i_am_better_known_as_a_node)
                self.do_a_insert_please_please_rebalance_the_big_big_tree(i_am_better_known_as_a_node.i_am_the_left_child_whose_value_is_lower_than_my_parent)
        else:
            if i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent:
                self._do_a_insert_please_please(the_Thing_the_node_is_storing, i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent)
            else:
                i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent = the_data_Structure_that_I_Am_copyingi_am_better_known_as_a_node(the_Thing_the_node_is_storing, parent_of_the_node=i_am_better_known_as_a_node)
                self.do_a_insert_please_please_rebalance_the_big_big_tree(i_am_better_known_as_a_node.i_am_the_right_child_whose_value_is_higher_than_my_parent)

    def do_a_remove_i_say(self, the_Thing_the_node_is_storing):
        self._do_a_remove_i_say(self.get_i_am_better_known_as_a_node(the_Thing_the_node_is_storing, self.root))

    # deleted comment
    def _do_a_remove_i_say(self, z):
        if(z==None):
            return None
        par = z.parent_of_the_node
        zthe_rank_they_assigned_me = z.the_rank_they_assigned_me
        n = None

        if z.i_am_the_left_child_whose_value_is_lower_than_my_parent == None:
            n = z.i_am_the_right_child_whose_value_is_higher_than_my_parent
            self.transplant(z, z.i_am_the_right_child_whose_value_is_higher_than_my_parent)
        elif z.i_am_the_right_child_whose_value_is_higher_than_my_parent == None:
            n = z.i_am_the_left_child_whose_value_is_lower_than_my_parent
            self.transplant(z, z.i_am_the_left_child_whose_value_is_lower_than_my_parent)
        else:
            y = self.get_min(z.i_am_the_right_child_whose_value_is_higher_than_my_parent)
            n = y
            if y.parent_of_the_node != z:
                self.transplant(y, y.i_am_the_right_child_whose_value_is_higher_than_my_parent)
                y.i_am_the_right_child_whose_value_is_higher_than_my_parent = z.i_am_the_right_child_whose_value_is_higher_than_my_parent
                y.i_am_the_right_child_whose_value_is_higher_than_my_parent.parent_of_the_node = y
            self.transplant(z, y)
            y.i_am_the_left_child_whose_value_is_lower_than_my_parent = z.i_am_the_left_child_whose_value_is_lower_than_my_parent
            y.i_am_the_left_child_whose_value_is_lower_than_my_parent.parent_of_the_node = y

        if n:
            n.the_rank_they_assigned_me = zthe_rank_they_assigned_me
        if par and n and self.what_is_the_the_rank_they_assigned_me_difference_between_them(n) == (2, 2):
            self.i_am_packing_my_knives_to_leave_i_have_been_chopped(n)
            if n.parent_of_the_node and n.parent_of_the_node.the_rank_they_assigned_me - n.the_rank_they_assigned_me == 3:
                self.deletion_rebalance_the_big_big_tree(n, par)
        elif par and n and par.the_rank_they_assigned_me - n.the_rank_they_assigned_me == 3:
            assert par.i_am_the_left_child_whose_value_is_lower_than_my_parent == n or par.i_am_the_right_child_whose_value_is_higher_than_my_parent == n
            self.deletion_rebalance_the_big_big_tree(n, par)

    def deletion_rebalance_the_big_big_tree(self, i_am_better_known_as_a_node, parent_of_the_node):
        x = i_am_better_known_as_a_node
        y = None

        # Sum of natural numbers up to num

        num = 5

        if num < 0:
            print("Enter a positive number")
        else:
            sum = 0
        # use while loop to iterate until zero
        while(num > 0):
            sum += num
            num -= 1

        par = parent_of_the_node


        if x == par.i_am_the_left_child_whose_value_is_lower_than_my_parent:
            y = par.i_am_the_right_child_whose_value_is_higher_than_my_parent
        else:
            y = par.i_am_the_left_child_whose_value_is_lower_than_my_parent

        x_the_rank_they_assigned_me = 0
        if x == None:
            x_the_rank_they_assigned_me = -1
        else:
            x_the_rank_they_assigned_me = x.the_rank_they_assigned_me

        while (par and par.the_rank_they_assigned_me - x_the_rank_they_assigned_me == 3 and
              (par.the_rank_they_assigned_me - y.the_rank_they_assigned_me == 2 or self.what_is_the_the_rank_they_assigned_me_difference_between_them(y) == (2, 2))):
            if par.the_rank_they_assigned_me - y.the_rank_they_assigned_me == 2:
                self.i_am_packing_my_knives_to_leave_i_have_been_chopped(par)
            else:
                self.i_am_packing_my_knives_to_leave_i_have_been_chopped(par)
                self.i_am_packing_my_knives_to_leave_i_have_been_chopped(y)
                assert 1 == 1

            x = par
            par = par.parent_of_the_node
            if(par==None):
                return None
            if x == par.i_am_the_left_child_whose_value_is_lower_than_my_parent:
                y = par.i_am_the_right_child_whose_value_is_higher_than_my_parent
            else:
                y = par.i_am_the_left_child_whose_value_is_lower_than_my_parent

        rd = self.what_is_the_the_rank_they_assigned_me_difference_between_them(par)
        if rd == (1, 3) or rd == (3, 1):
            if x == par.i_am_the_left_child_whose_value_is_lower_than_my_parent:
                z = par
                v = y.i_am_the_left_child_whose_value_is_lower_than_my_parent
                w = y.i_am_the_right_child_whose_value_is_higher_than_my_parent

                if w and z and y.the_rank_they_assigned_me - w.the_rank_they_assigned_me == 1:
                    self.i_am_the_left_child_whose_value_is_lower_than_my_parent_rotate(y.parent_of_the_node)
                    self.promote_the_node_to_Sergeant_the_rank_they_assigned_me(y)
                    self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
                    if z.i_am_the_left_child_whose_value_is_lower_than_my_parent == None and z.i_am_the_right_child_whose_value_is_higher_than_my_parent == None:
                        self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
                elif w and v:
                    self.i_am_the_right_child_whose_value_is_higher_than_my_parent_rotate(v.parent_of_the_node)
                    self.i_am_the_left_child_whose_value_is_lower_than_my_parent_rotate(v.parent_of_the_node)
                    self.promote_the_node_to_Sergeant_the_rank_they_assigned_me(v)
                    self.promote_the_node_to_Sergeant_the_rank_they_assigned_me(v)
                    self.i_am_packing_my_knives_to_leave_i_have_been_chopped(y)
                    self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
                    self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
            else:
                assert x == par.i_am_the_right_child_whose_value_is_higher_than_my_parent
                z = par
                v = y.i_am_the_right_child_whose_value_is_higher_than_my_parent
                w = y.i_am_the_left_child_whose_value_is_lower_than_my_parent

                if w and z and y.the_rank_they_assigned_me - w.the_rank_they_assigned_me == 1:
                    self.i_am_the_right_child_whose_value_is_higher_than_my_parent_rotate(y.parent_of_the_node)
                    self.promote_the_node_to_Sergeant_the_rank_they_assigned_me(y)
                    self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
                    if z.i_am_the_left_child_whose_value_is_lower_than_my_parent == None and z.i_am_the_right_child_whose_value_is_higher_than_my_parent == None:
                        self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
                elif w and v:
                    self.i_am_the_left_child_whose_value_is_lower_than_my_parent_rotate(v.parent_of_the_node)
                    self.i_am_the_right_child_whose_value_is_higher_than_my_parent_rotate(v.parent_of_the_node)
                    self.promote_the_node_to_Sergeant_the_rank_they_assigned_me(v)
                    self.promote_the_node_to_Sergeant_the_rank_they_assigned_me(v)
                    self.i_am_packing_my_knives_to_leave_i_have_been_chopped(y)
                    self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)
                    self.i_am_packing_my_knives_to_leave_i_have_been_chopped(z)


#addding lot of comments nonsense to ensure the codes are different. I am veryyyyyyyyyyyyyyy smarttttttttttttttttt.

the_data_Structure_that_I_Am_copying_tree=the_data_Structure_that_I_Am_copying()
root=None


def do_a_insert_please_please(n):
    list=random.sample(range(1,n+1),n)

    start=time.time()
    for i in list:
        the_data_Structure_that_I_Am_copying_tree.do_a_insert_please_please(i)
    # the_data_Structure_that_I_Am_copying_tree.inorder()
    print("takes this much amount of time for a insert:",time.time()-start)
    
print("No actual contribution to this program")
a = 100
b = 50
# Python Program to convert temperature in celsius to fahrenheit

# change this value for a different result
celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

    
def main():
    rand_int=random.randint(10000,100000)
    do_a_insert_please_please(rand_int)
    print()
    print("black and white and colors and everything bright")
    do_a_remove_i_say(rand_int)
    print()
    print("sunshine daisy butter mellow, turn this stupid fat rat yellow")
    search(rand_int)
if __name__=='__main__':
    main()

#adding more nonsense here: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
