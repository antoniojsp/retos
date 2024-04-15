#https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        '''
        First, we create a hashmap that use "size"as key and the list of indexes as  values.
        '''
        for i, j in enumerate(groupSizes):
            if j not in groups:
                groups[j] = []
            groups[j].append(i)

        print(groups)

        '''
        Now, we go through the hash map and check if the size of the group and the length of the array
        is equal. If they are, we add it to the result list, if not, we divide it to create different
        groups of the right size and add each one to the result list.
        '''
        result = []
        for size, indexes in groups.items():
            if len(indexes) == size:
                result.append(indexes)
            else:
                for i in range(0, len(indexes), size):
                    result.append(indexes[i: i +i])

        return result