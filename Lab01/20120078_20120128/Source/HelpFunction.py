"""
    Chức hàm hỗ trợ cho việc cài đặt các chức năng khác        
"""

import numpy as np
import ListMissingColumn

#tính giá trị trung bình của một mảng
def calculate_mean(array):
    sum = 0
    numOfValues = 0
    checkNanArray = is_nan_array(array)
    for i in range(array.shape[0]):
        if (checkNanArray[i] == False):#giá trị Not NaN
            sum += array[i]
            numOfValues += 1
    return round((sum / numOfValues), 2)

#tính giá trị trung vị (median) của một mảng
def calculate_median(array):
    array.sort()
    n = len(array)
    result = 0
    if (n % 2 == 0):
        index1 = array[n//2]
        index2 = array[n//2 - 1]
        result = (index1 + index2)/2
    else:
        result = array[n//2]
    return result

#tìm giá trị mode của một mảng
def find_mode(array):
    #sort lại list array
    array.sort()
    L1 = []
    i = 0
    result = []
    while i < len(array):
        #dùng L1 để lưu lại đếm số lần giá trị của dữ liệu trong array
        L1.append(array.count(array[i]))
        i += 1
    # chuyển array và L1 thành dictionary với key là giá trị của array còn values là số lần xuất hiện
    d1 = dict(zip(array, L1))
    for (k, v) in d1.items():
        if v == max(L1):
            #nếu key đó có value lớn nhất thì thêm giá trị đã đề cập đó vào res
            result.append(k)
    return result

def get_all_numeric(listRow):
    listNum = []
    #kiểm tra các thuộc tính có là dạng numeric hay không?
    for key in listRow[0].keys():
        for row in listRow:
            if (row[key] != ''):
                if (row[key].count('.') != 0):
                    listNum.append(key)
                    break
                else:
                    if (row[key].isnumeric()):
                        listNum.append(key)
                        break
    return listNum

def list_categorical_attribute(listRow):
    #lưu các cột kiểu categorical bị thiếu dữ liệu
    list_categorical = []
    #lưu các cột  kiểu numeric bị thiếu dữ liệu
    list_numeric = list_numeric_attribute(listRow)
    #Xét trong các cột bị thiếu dữ liệu
    for key in ListMissingColumn.list_missing_column(listRow).keys():
        #nếu cột đang xét mà không phải là cột kiểu numeric thì nó là cột kiểu categorical
        if key not in list_numeric:
            #thêm cột đó vào danh sách các cột kiểu categorical
            list_categorical.append(key)
    return list_categorical

def list_numeric_attribute(listRow):
    list_numeric = []
    #tận dụng câu 1 để lấy các cột bị thiếu dữ liệu
    for key in ListMissingColumn.list_missing_column(listRow).keys():
        #Duyệt từng dòng trong cột bị thiếu
        for row in listRow:
            #Nếu dòng đó có dữ liệu
            if row[key] != '':
                #kiểm có dấu chấm trong dữ liệu đó không (tức là xem thử có phải số thực không)
                if row[key].count('.') != 0:
                    #thêm cột đó vào ds cột bị thiếu dữ liệu numberic và break để xét cột tiếp theo
                    list_numeric.append(key)
                    break
                else:
                    #nếu không có dấu chấm thì dùng method isnumeric của python để kiểm tra xem có phải numeric hay không
                    if row[key].isnumeric():
                        #thêm cột đó vào ds cột bị thiếu dữ liệu numberic và break để xét cột tiếp theo
                        list_numeric.append(key)
                        break
    #Trả về danh sách cột thuộc kiểu numeric bị thiếu dữ liệu
    return list_numeric

#kiểm tra số có là nan
def is_nan(num):
    return num != num

#kiểm tra mảng nan hay ko
def is_nan_array(array):
    checkNanArray = [] #mảng chứa hai giá trị TRUE/FALSE tương ứng với giá trị của array tại đó là NaN hay ko NaN
    for x in array:
        checkNanArray.append(is_nan(x)) #TRUE: NaN, FALSE: Not NaN
    return checkNanArray

#lấy số lượng dữ liệu thiếu trong thuộc tính
def list_number_of_missing(dataset):
    numberOfMissing = {}
    attributes = list(dataset)
    numOfInstances = dataset.shape[0]
    for attribute in attributes: 
        missingArray = is_nan_array(dataset[attribute]) 
        count = 0
        for index in range(numOfInstances):
            count += int(missingArray[index])
        numberOfMissing[attribute] = count
    return numberOfMissing

#lấy kiểu dữ liệu của thuộc tính
def get_type_of_attributes(dataset):
    typeOfAttributes = {} 
    attributes = list(dataset) 
    numberOfMissing = list_number_of_missing(dataset)
    numOfInstances = dataset.shape[0]
    for attribute in attributes:
        #thuộc tính không có giá trị
        if (numberOfMissing[attribute] == numOfInstances):
            typeOfAttributes[attribute] = 4
            continue
        for index in range(numOfInstances):
            if (is_nan(dataset[attribute][index]) == False):
                getType=type(dataset[attribute][index])
                #thuộc tính có kiểu dữ liệu int
                if (getType == int or getType == np.int64):
                    typeOfAttributes[attribute] = 1
                #thuộc tính có kiểu dữ liệu float
                elif (getType == float or getType == np.float64):
                    typeOfAttributes[attribute] = 2
                #thuộc tính có kiểu dữ liệu dạng chuỗi
                else:
                    typeOfAttributes[attribute] = 3
                break
    return typeOfAttributes
