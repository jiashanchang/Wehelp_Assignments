# 要求一：函式與流程控制
# 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。
# 其中你可以假設 max 一定大於 min 且為整數，step 為正整數。
# 提醒：請勿更動題目中任何已經寫好的程式。

def calculate(min, max, step):
    sum = 0
    # 從min開始，不算max，間隔step
    for i in range(min, max, step):
        sum += i
    if((sum+step) != max):
        print(sum+max)
    else:
        print(sum)

print("Answers for subject 1：")

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

print("==============================")

# 要求二：Python 字典與列表、JavaScript 物件與陣列
# 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
# manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量不定的情況。
# 提醒：請勿更動題目中任何已經寫好的程式。

def avg(data):

    total = 0
    count = 0
    for key in data:
        dic=data[key]
        
        for forkey in dic:
            
            if (forkey["manager"]) ==False:

                total+=forkey["salary"]
                count=count+1
    average = total / count
    print(average)

print("Answers for subject 2：")

avg({
"employees":[
{
"name":"John",
"salary":30000,
"manager":False
},
{
"name":"Bob",
"salary":60000,
"manager":True
},
{
"name":"Jenny",
"salary":50000,
"manager":False
},
{
"name":"Tony",
"salary":40000,
"manager":False
}
]
}) # 呼叫 avg 函式

print("==============================")

# 要求三：完成以下函式，最後能印出程式中註解所描述的結果。
# 提醒：請勿更動題目中任何已經寫好的程式。

def func(a):
    def fu(x,y):
        return(a + x * y)
    return(fu)

print("Answers for subject 3：")

result=func(2)(3, 4)
print(result)
result=func(5)(1, -5)
print(result)
result=func(-3)(2, 9)
print(result)

# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

print("==============================")

# 要求四：找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
# 提醒：請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

def maxProduct(nums):
    arr_len = len(nums) 
    if (arr_len < 2): 
        print("no exists") 
        return      
    x = nums[0]; y = nums[1] 
    
    for i in range(0, arr_len): 

        for j in range(i + 1, arr_len): 
            if (nums[i] * nums[j] > x * y): 
                x = nums[i]; y = nums[j] 
    
    print (x * y)

print("Answers for subject 4：")

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

print("==============================")

# 要求五：Given an array of integers, show indices of the two numbers such that they add up to a
# specific target. You can assume that each input would have exactly one solution, and you
# can not use the same element twice.

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
result=twoSum([2, 11, 7, 15], 9)

print("Answers for subject 5：")

print(result) # show [0, 2] because nums[0]+nums[2] is 9

print("==============================")