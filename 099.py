# 每门课程的成绩分为五个等级：A,B,C,D,F(注意没有E),它们分别代表可以获得4,3,2,1,0个绩点.
# 现在给你一个由大写字母构成的列表L，请你计算平均绩点，保留小数点后两位。
# 若L中包含非法成绩等级，则输出-1.
# 如：
# L = ["A", "B", "C", "D", "F"]
# 则输出2.00

L = ["A", "B", "C", "D", "F"]
count = 0
flag = 1
for i in L:
    if i not in L:
        print("-1")
        flag = 0
    if i == "A":
        count += 4
    if i == "B":
        count += 3
    if i == "C":
        count += 2
    if i == "D":
        count += 1
    if i == "F":
        count += 0
if flag == 1:
    print("%0.2f" % (count / len(L)))
