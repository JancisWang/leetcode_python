'''
easy

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-stack
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 辅助栈保持和数据栈同步（长度一致）
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []
        

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)
        else: self.helper.append(self.helper[-1])
        
    def pop(self) -> None:
        if self.data:
            self.data.pop()
            self.helper.pop()
        else: 
            print('the stack is null')
        

    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            print('the stack is null')

    def getMin(self) -> int:
        return self.helper[-1]
        

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# 辅助栈只记录目前为止的最小值， 不保持和数据栈长度同步
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = []
        

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.helper or x <= self.helper[-1]:
            self.helper.append(x)
        
    def pop(self) -> None:
        if self.data:
            temp = self.data.pop()
            if temp == self.helper[-1]:
                self.helper.pop()
        else: 
            print('the stack is null')
        
    def top(self) -> int:
        if self.data:
            return self.data[-1]
        else:
            print('the stack is null')

    def getMin(self) -> int:
        return self.helper[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()