"""
    Argument syntax:
        python main.py --input=input.csv --namefunction=A --method=B--output=result.csv
    Example:
        python main.py --input=house-prices.csv --namefunction=ImputeMissingValue --method=MEAN --output=result.csv
    Note: tên method phải viết hoa hoặc viết thường toàn bộ          
"""
import HelpFunction

def impute_mean(listRow): #hàm tính mean và điền các giá trị vào cột
    #Cập nhật các dữ liệu bị thiếu kiểu categorical
    listRow = impute_mode(listRow)
    mean = []
    #xét các cột kiểu numeric mà bị thiếu dữ liệu
    for key in HelpFunction.list_numeric_attribute(listRow):
        sum = 0
        count = 0
        #xét các dòng không bị thiếu dữ liệu để tính mean
        for row in listRow:
            if row[key] != '':
                count += 1
                sum += float(row[key])
        average = sum / count
        #thêm mean của cột đó vào 1 biến nhớ
        mean.append((key, average))

    #chuyển biến thành kiểu dictionary
    mean = dict(mean)
    #cập nhật các giá trị bị thiếu bằng mean của của thuộc tính
    for key in listRow[0].keys():
        if key in mean.keys():
            for row in listRow:
                if row[key] == '':
                    row[key] = mean[key]
    #trả về listRow mới đã được điền đầy đủ các thuộc tính thiếu bằng mean và mode
    return listRow

def impute_median(listRow):#hàm tính median và điền các giá trị vào cột
    #Cập nhật các dữ liệu bị thiếu kiểu categorical
    listRow = impute_mode(listRow)
    median = []
    #xét các cột kiểu numeric mà bị thiếu dữ liệu
    for key in HelpFunction.list_numeric_attribute(listRow):
        array = []
        #xét các dòng không bị thiếu dữ liệu để tính median
        for row in listRow:
            if (row[key] != ''):
                array.append(float(row[key]))
        #để tính median ta cần sắp xếp dữ liệu tăng dần
        medianOfArray = HelpFunction.calculate_median(array)
        #thêm median của cột đó vào 1 biến nhớ
        median.append((key, medianOfArray))
    #chuyển biến thành kiểu dictionary    
    median = dict(median)

    #cập nhật các giá trị bị thiếu bằng median của của thuộc tính
    for key in listRow[0].keys():
        if (key in median.keys()):
            for row in listRow:
                if (row[key] == ''):
                    row[key] = median[key]
    #trả về listRow mới đã được điền đầy đủ các thuộc tính thiếu bằng median và mode
    return listRow

def impute_mode(listRow):#hàm tính mode và điền các giá trị thiếu bằng giá trị mode
    mode = []
    #Xét các cột kiểu categorical bị thiếu dữ liệu
    for key in HelpFunction.list_categorical_attribute(listRow):
        array = []
        #với mỗi cột thì reset lại biến nhớ
        #xét các dòng không bị thiếu dữ liệu để tính mediaan
        for row in listRow:
            if (row[key] != ''):
                #nếu dòng không rỗng thì thêm nó vào biến nhớ array
                array.append(row[key])
        #tìm giá trị mode của array
        result = HelpFunction.find_mode(array)

        if (len(result) == 0):
            #nếu cột đó là rỗng, thì giá trị của cột đó không thể có giá trị mode
            mode.append((key, ''))
        else:
            #nếu không thì thêm giá trị của thuộc tính xuất hiện nhiều nhất cùng tên cột đó vào mode
            for str in result:
                mode.append((key, str))
    #chuyển kiểu dữ liệu về dictionary
    mode = dict(mode)
    #cập nhật lại các thuộc tính categorical thiếu dữ liệu theo mode
    for key in listRow[0].keys():
        if (key in mode.keys()):
            for row in listRow:
                if (row[key] == ''):
                    row[key] = mode[key]
    #trả về listRow mới đã cập nhật lại các thuộc tính categorical thiếu dữ liệu theo mode
    return listRow