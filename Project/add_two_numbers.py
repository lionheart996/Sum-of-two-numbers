class Solution:
    def addTwoNumbers(self, l1, l2):

        reversed_list_1 = l1[::-1]
        reversed_list_2 = l2[::-1]

        first_num = ''
        second_num = ''

        for i in range(len(l1)):
            first_num += str(l1[i])
        for i in range(len(l2)):
            second_num += str(l2[i])

        sum = int(first_num) + int(second_num)

        list_of_sum = [ int(x) for x in str(sum) ]

        result = list_of_sum[::-1]

        return result


l1 = [9,9,9,9,9,9,9]

l2 = [9,9,9,9]

print(Solution().addTwoNumbers(l1, l2))