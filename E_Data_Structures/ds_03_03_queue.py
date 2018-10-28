"""
queue - example
"""

import ds_03_00_users as DB
from A_Classes.user import User
from  B_Data_Structures import queue_built_in, queue_priority, queue_with_head, queue_with_head_and_tail

def main():

    queue = queue_built_in.Queue_built_in_list()
    queue = queue_with_head.Queue_with_head()
    queue = queue_with_head_and_tail.Queue_with_head_and_tail()
    queue = queue_priority.PriorityQueue()

    for user in DB.user_to_add:
        print(user)
        queue.insert(User(*user))

    print()
    while not queue.is_empty():
        print(queue.remove())

if __name__ == "__main__":
    main()
    print("Done!!")
