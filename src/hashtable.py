# '''
# Linked List hash table key/value pair
# '''

# this is a full, complete linked list, this is all we need for chaining


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# our hash table that has capacity buckets that accept string keys...emulating the functionality of allocating memory, by making use of a python list


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    # capacity is how much we can fit in our hash table

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    # leading underscore means do not use it outside of the class...its private

        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''

    def _hash(self, key):

        return hash(key)

    # def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # pass

    '''
    Take an arbitrary key and return a valid integer index within the storage capacity of the hash table.
    '''
    # hash mod calls hash and returns the capacity
    # to get an index

    def _hash_mod(self, key):

        return self._hash(key) % self.capacity

        '''
        Store the value with the given key. Hash collisions should be handled with Linked List Chaining.
        '''

    def insert(self, key, value):

        # first we turn the key into an index in our array
        # index = self._hash_mod(key)
        # # check for an error
        # if self.storage[index]:
        #     print("ERROR: Key in use")
        # # key becomes our value
        # else:
        #     self.storage[index] = value

        # first we turn the key into an index in our array
        index = self._hash_mod(key)
        # our new linked pairs are being chained
        newLinkedPair = LinkedPair(key, value)
        # if theres storage in the index...
        if self.storage[index]:
            # store the value
            newLinkedPair.next = self.storage[index]
        self.storage[index] = newLinkedPair

        '''
        Remove the value stored with the given key. Print a warning if the key is not found.
        '''

    def remove(self, key):
        # first get the index of the key were removing
        index = self._hash_mod(key)
        # get the node at that index
        current = self.storage[index]
        prev = None

        # loop through each node looking for a key match
        while current is not None and current.key != key:
            # keep track of prev node
            prev = current
            # continue through nodes
            current = current.next

        # if found, currents value is equal to node with the key match
        if current is None:
            print("Key not found!")
        # if node with a match is at the head of the Linked List...
        else:
            if prev is None:
                # assign new head to be next element
                self.storage[index] = current.next
            else:
                prev.next = current.next

            print("Key removed!")

        '''
        Retrieve the value stored with the given key. Returns None if the key is not found.
        '''

    def retrieve(self, key):
        # # once again get the index
        # index = self._hash_mod(key)
        # # then were just returning storage at the index, it returns none if key isnt found since we've initialized our storage array and set
        # # everything to None to begin with
        # return self.storage[index]

        # once again get the index
        index = self._hash_mod(key)
        # if the value is found...
        if self.storaage[index]:
            # turn the linked list or value stored at that index into a variable
            temporary = self.storaage[index]
            # create a while loop for looping through the Linked List
            while temporary:
                # compare keys
                if temporary.key:
                    # if found, return value
                    return temporary.value
                # continue through Linked List
                temporary = temporary.next
        # if nothing is found
        return None

        '''
        Doubles the capacity of the hash table and rehash all key/value pairs.
        '''

    def resize(self):
        # pave our way for a new storage
        old_storage = self.storage.copy()
        # double the capacity
        self.capacity = self.capacity * 2
        # make new storage (none * capacity)
        self.storage = [None] * self.capacity
        # make our for each loop
        for bucket_item in old_storage:
            # re-insert everything in new key
            self.insert(bucket_item)

        # self.capacity *= 2
        # new_storage = [None] * self.capacity
        # for i in range(self.count):
        #     new_storage[i] = self.storage[i]
        # self.storage = new_storage


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
