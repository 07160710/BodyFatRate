# 输入
# 身高
personHeight = input("请输入身高（m）：")
personHeight = float(personHeight)
# 体重
personWeight = input("请输入体重（kg）：")
personWeight = float(personWeight)
# 年龄
personAge = input("请输入年龄：")
personAge = int(personAge)
# 性别
personSex = input("请输入性别（男生就输入1，女就输入0）：")
personSex = int(personSex)
# 处理数据
# 计算体脂率
# BMI = 体重（kg） /  （身高 * 身高）（m）
# 体脂率 = 1.2 * BMI + 0.23 * 年龄 - 5.4 -10.8 * 性别（男：1，女 ：0）
BMI = personWeight / (personHeight * personHeight)
fatRate = 1.2 * BMI + 0.23 * personAge - 5.4 - 10.8 * personSex
# 判断体脂率是否正常范围内
# 男正常为 15% - 18%  女正常为25% - 28%

minNum = 0.15 + 0.10 * (1-personSex)
maxNum = 0.18 + 0.10 * (1-personSex)
result = minNum < fatRate < maxNum

# 输出
print("你的体脂率是%f" % fatRate)
# if else 判断语句
if result == True:
    print("你的体脂率符合标准",)
else:
    print("你的体脂率不符合标准", )

