#task: 统计并得到一个字符串中最高频次的字符

def getMaxTimes(str):
    dic= {}
    for char in str:
        if char in dic:
            dic[char] += 1
        else:
            dic[char]= 1

    sortedDic =sorted(dic.items(), key=lambda it: it[1], reverse=True)
    return sortedDic[0]

#测试
ss= 'This is a common interview question'
print(getMaxTimes(ss))