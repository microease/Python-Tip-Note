# 光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。小Py光棍几十载，光棍自有光棍的快乐。让我们勇敢地面对光棍的身份吧，现在就证明自己：给你一个整数a，数出a在二进制表示下1的个数，并输出。
# 例如：a=7
# 则输出：3
# bin() 返回一个整数 int 或者长整数 long int 的二进制表示。
a = 7
n = 0
for i in bin(a):
    if i == "1":
        n += 1
print(n)
