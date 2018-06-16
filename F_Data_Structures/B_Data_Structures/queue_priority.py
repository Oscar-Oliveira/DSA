"""
PriorityQueue
"""

from B_Data_Structures.queue_built_in import Queue_built_in_list

class PriorityQueue(Queue_built_in_list):

    def remove(self):
        pos = 0
        for i in range(1, len(self.Items)):
            if self.Items[i] > self.Items[pos]:
                pos = i
        return_value = self.Items[pos]
        del self.Items[pos]
        return return_value
