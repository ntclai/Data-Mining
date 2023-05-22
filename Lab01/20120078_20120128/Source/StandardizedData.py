"""
    Argument syntax:
        python main.py --input=input.csv --namefunction=A --method=B --columns: C D F --output=result.csv
    Example:
        python main.py --input=house-prices.csv --namefunction=StandardizedData --method=MINMAX --columns: ID alley --output=result.csv
    Note:+ nếu cột yêu cầu chuẩn hóa không phải dạng số (numeric) sẽ có thông báo ko chuẩn hóa được cho thuộc tính đó
         + tên các cột yêu cầu chuẩn hóa phải cách nhau 1 dấu cách    
         + tên method phải viết hoa hoặc viết thường toàn bộ               
"""
import math
import HelpFunction

# chuẩn hóa dữ liệu bằng phương thức MINMAX
def standardlized_data_by_MINMAX(dataset, attribute, newMAX, newMIN):
    # khởi tạo giá trị tối thiểu và tối đa cho tập dữ liệu
    min = dataset[attribute][0]
    max = dataset[attribute][0]
    numberOfInstances = dataset.shape[0]
    #tìm giá trị lớn nhất và nhỏ nhất
    for index in range(numberOfInstances):
        if (HelpFunction.is_nan(dataset[attribute][index]) == False):
            if (dataset[attribute][index] < min):#cập nhật lại giá trị min
                min =dataset[attribute][index]
            elif (dataset[attribute][index] > max):#cập nhật lại giá trị max
                max = dataset[attribute][index]
    #tiến hành chuẩn hóa dữ liệu
    tempArray = []
    for index in range(numberOfInstances):
        if (HelpFunction.is_nan(dataset[attribute][index]) == False):
            tempArray.append(round(float((float(dataset[attribute][index]) - float(min)) / (float(max) - float(min))*(newMAX - newMIN) + newMIN),3))
        else:
            tempArray.append(dataset[attribute][index])
    dataset[attribute]=tempArray

# chuẩn hóa dữ liệu bằng phương thức ZScore
def standardlized_data_by_ZScore(dataset, attribute):
    means = HelpFunction.calculate_mean(dataset[attribute])
    #tính giá trị phương sai
    numberOfInstances = dataset.shape[0]
    N =  numberOfInstances - HelpFunction.list_number_of_missing(dataset)[attribute]
    variance = 0
    for index in range(numberOfInstances):
        if (HelpFunction.is_nan(dataset[attribute][index]) == False):
            variance +=float(pow(float(dataset[attribute][index]-means),2) / N)
    #tính độ lệch chuẩn
    standardDeviation = math.sqrt(variance)
    #tiến hành chuẩn hóa dữ liệu
    tempArray = []
    for index in range(numberOfInstances):
        if (HelpFunction.is_nan(dataset[attribute][index]) == False):
            tempArray.append(round(float((float(dataset[attribute][index])-means)/standardDeviation),3))
        else:
            tempArray.append(dataset[attribute][index])
    dataset[attribute]=tempArray