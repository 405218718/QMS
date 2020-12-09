import xlwings as xw
import pandas as pd
import numpy as np

app = xw.App(visible=False, add_book=False)  # 创建应用
# visible=True   显示Excel工作簿；False  不显示工作簿
# add_book=False   不再新建一个工作簿;True  另外再新建一个工作簿
# app.screen_updating = False
# :屏幕更新，就是说代码对于excel的操作你可以看见，关闭实时更新可以加快脚本运行。默认是True。
# wb = app.books.add()    # 创建新的工作薄
# sht = wb.sheets.add("test")  # 新建工作表
# sht.delete()      # 删除工作表

# sheet = wb.sheets.add(name=None,before=None,after=None)
# # 参数：name：新建工作表名称；before创建的工作表位置在哪个工作表前面；after：创建位置在哪个工作表后面；
# # before和after参数可以传入数字，也可以传入已有的工作表名称，传入数字n表示从左往右第n个sheet位置
# # before和after参数不传，创建sheet默认在当前活动工作表左侧


wb = app.books.open(r'C:\Users\fanwei\Desktop\CPM修改模费用.xlsx')  # 打开工作簿
bsheets = wb.sheets     # 显示当前工作簿中所有表单
sheets_list = []
for on in bsheets:
    sheets_list.append(wb.sheets[on].name)      # 列表内加入工作表名称
print(sheets_list)
sht = wb.sheets('明细')   # 打开工作表
rowss = sht.used_range.last_cell.row      # 读取sht的总行数
columnss = sht.used_range.last_cell.column   # 读取sht的总行列

date = sht.range((1, 1)).options(pd.DataFrame, expand='table').value    # 将读取全部数据，输出类型为DataFrame
# print(date)
pf = pd.pivot_table(date, index=[u'设计部门', u'钳工部门'], values=[u'异常加工费', u'异常材料费'], aggfunc=np.sum, fill_value=1, margins=1)
if 'Sheet' in sheets_list:
    wb.sheets('Sheet').clear()    # 清除格式和内容
else:
    wb.sheets.add("Sheet")  # 新建工作表
sht = wb.sheets('Sheet')   # 打开工作表
# df_1 = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['col1', 'col2', 'col3'], index=['a', 'b'])
# sht.range("A1").value = df_1
sht.range("A1").value = pf

# pandas.pivot_table(*data*, *values=None*, *index=None*, *columns=None*, *aggfunc='mean'*, *fill_value=None*,*margins=False*, *dropna=True*, *margins_name='All'*, *observed=False*)
# # data：dataframe格式数据
# # values：需要汇总计算的列，可多选
# # index：行分组键，一般是用于分组的列名或其他分组键，作为结果DataFrame的行索引
# # columns：列分组键，一般是用于分组的列名或其他分组键，作为结果DataFrame的列索引
# # aggfunc：聚合函数或函数列表，默认为平均值
# # fill_value：设定缺失替换值
# # margins：是否添加行列的总计
# # dropna：默认为True，如果列的所有值都是NaN，将不作为计算列，False时，被保留
# # margins_name：汇总行列的名称，默认为All
# # observed：是否显示观测值
# sht.range('a1').value = [[1], [2], [3], [4], [5]]   # 列方向（嵌套列表）
# sht.range('a2').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10, 20, 30]]  # 写入两行数据
# aa = sht.range('A2').expand('right').address    # 'up', 'down', 'left', 'right'方向（“上” ，“下” ，“右” ，“左”之一）
# print(sht.range(aa).value)
# aa = sht.range('A2').expand().address   # 以A2 行、列 最大有效数据范围
# print(sht.range(aa).value)
# print(sht.range(aa).columns[1])
# print(sht.range(aa).rows[1])
# # print(sht.shapes)           # 返回sht的行数和列数
# print(sht.range(aa).rows.count)      # 读取sht指定范围的行数
# print(sht.range(aa).columns.count)   # 读取sht指定范围的行列
# print(sht.used_range.last_cell.row)      # 读取sht的总行数
# print(sht.used_range.last_cell.column)   # 读取sht的总行列
#
#
#
# print(sht.range((10, 1), (11, 3)).value)   # 读取10行第1列 到 第11行第2列
# print(sht.range('A2').options(expand='table').value)   # 'table'扩展为'down'和'right'，其他可用选项分别可用于列或行扩展
# # [['Foo 1', 'Foo 2', 'Foo 3'], [10, 20, 30]]
# #
# # sht.range('a1').value = [['a', 1], ['b', 2]]
# # print(sht.range('a1:c2').options(dict).value)  # 以列为字典
# # # {'a': 1.0, 'b': 2.0}
# #
# # sht.range('a4').value = [['a', 'b'], [1, 2]]
# # print(sht.range('a4:b5').options(dict, transpose=True).value)     # 以行为字典
# # # {'a': 1.0, 'b': 2.0}



# wb.save(r'C:\Users\fanwei\Desktop\Track.xlsx')  # 保存工作簿

# app.kill()  # 终止进程，强制退出。
wb.save()  # 保存工作簿
wb.close()  # 关闭工作簿
app.quit()  # 在不保存的情况下，退出excel程序。