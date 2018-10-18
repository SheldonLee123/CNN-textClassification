import xlrd

def strs(row):
    values = "";
    for i in range(len(row)):
        if i == len(row) - 1:
            values = values + str(row[i])
        else:
            values = values + str(row[i]) + ","
    return values

# 打卡文件
data = xlrd.open_workbook("DeepLearningData.xlsx")
sqlfile1 = open("Explicit", "w")
sqlfile2 = open("Ordinal", "w")
sqlfile3 = open("TempAns", "w")
sqlfile4 = open("Implicit", "w")
sqlfile5 = open("NotTimeQue", "w")

table = data.sheets()[0] # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.row_values(0)  # 某一行数据
# 打印出行数列数
print(nrows)
print(ncols)
print(colnames)
for ronum in range(1, 201):
    row = table.row_values(ronum)[0]
    sqlfile1.writelines(row + "\r") #将字符串写入新文件
for ronum in range(201, 401):
    row = table.row_values(ronum)[0]
    sqlfile2.writelines(row + "\r") #将字符串写入新文件
for ronum in range(401, 601):
    row = table.row_values(ronum)[0]
    sqlfile3.writelines(row + "\r") #将字符串写入新文件
for ronum in range(601, 801):
    row = table.row_values(ronum)[0]
    sqlfile4.writelines(row + "\r") #将字符串写入新文件
for ronum in range(801, 1001):
    row = table.row_values(ronum)[0]
    sqlfile5.writelines(row + "\r") #将字符串写入新文件

# 关闭写入的文件
sqlfile1.close()
sqlfile2.close()
sqlfile3.close()
sqlfile4.close()
sqlfile5.close()
