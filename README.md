## 1 Two Sum(求两数之和)
**题目**：给定一个数组nums，和target。使nums中的nums[i]+nums[j]=target，返回key

**解法**：可以通过2次循环爆破，也可以单循环。target-nums[i]相减，判断结果是不是在nums中，若有返回index.

**小结**：``enumerate(sequence, [start=0])``将一个可遍历的列表、元组或字符串 组合为一个索引序列，同时返回index和value，常用于for.
