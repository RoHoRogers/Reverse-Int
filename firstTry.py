class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        negFlag = 0
        reverse = []
        
        for i in range(len(x)):
            if x[len(x)-i-1] == 0 and reverse:
                continue
            if x[len(x)-i-1] == '-':
                negFlag = 1
                continue
            reverse.append(x[len(x)-i-1])
        
        
        
        int_lst = [int(x) for x in reverse] 
        output = 0

        for x in range(len(int_lst)):
            if negFlag == 0:
                output += (int_lst[x] * (pow(10,(len(int_lst)-x-1))))
            else:
                output -= (int_lst[x] * (pow(10,(len(int_lst)-x-1))))
        
        if output > 2147483647 or output < -2147483648:
            return(0)
        return(output)
            
