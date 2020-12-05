import xlwings as xw

app = xw.App(visible=False, add_book=False)  # 创建应用
# visible=True   显示Excel工作簿；False  不显示工作簿
# add_book=False   不再新建一个工作簿;True  另外再新建一个工作簿
# app.screen_updating = False
# :屏幕更新，就是说代码对于excel的操作你可以看见，关闭实时更新可以加快脚本运行。默认是True。
wb = app.books.add()    # 创建新的工作薄
sht = wb.sheets.add("test")  # 新建工作表
sht.range('a1').value = [[1], [2], [3], [4], [5]]   # 列方向（嵌套列表）
sht.range('a2').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10, 20, 30]]  # 写入两行数据
print(sht.shape)           # 返回sht的行数和列数
print(sht.rows.count)      # 读取sht的总行数
print(sht.columns.count)   # 读取sht的总行列

print(sht.range((10, 1), (11, 3)).value)   # 读取10行第1列 到 第11行第2列

sht.range('a1').value = [['a', 1], ['b', 2]]
print(sht.range('a1:b2').options(dict).value)  # 以列为字典
# {'a': 1.0, 'b': 2.0}

sht.range('a4').value = [['a', 'b'], [1, 2]]
print(sht.range('a4:b5').options(dict, transpose=True).value)     # 以行为字典
# {'a': 1.0, 'b': 2.0}



wb.save(r'C:\Users\fanwei\Desktop\Track.xlsx')  # 保存工作簿
wb.close()  # 关闭工作簿
app.kill()  # 终止进程，强制退出。
# quit()  # 在不保存的情况下，退出excel程序。