"""
    Argument syntax:
        python main.py --input=house-prices.csv --namefunction=A --expression=B --output=result.csv
    Example:
        python main.py --input=house-prices.csv --namefunction=CalculateAttribute --expression=Id+LotFrontage --output=result.csv
    Note: thuộc tính chứa kết quả phép tính sẽ có tên giống expression
"""
import HelpFunction

#hàm xử lý chuỗi biểu thức nhập vào
def handle_expression_string(listRow, expression):  
    # tách chuỗi biểu thức thành list, mỗi phần tử trong list ứng với một toán hạng và toán tử
    operator = ['+', '-', '*', '/']
    a = []
    b = ''
    count = 0
    for i in expression:
        if (i not in operator):
            b = b + i
        else:
            a.append(b)
            a.append(i)
            b = ''
        count += 1
        if (count == len(expression)):
            a.append(b)
    x = HelpFunction.get_all_numeric(listRow)
    for key in a:
        if (key not in operator):
            if (key not in x):
                return 0
    return a

def calculate(listRow, expression):
    tempListRow = []
    for i in range(len(listRow)):
        row = listRow[i].copy()
        tempListRow.append(row)

    newExpression = handle_expression_string(listRow, expression)
    count = 0
    if (newExpression == 0):
        return 0
    else:
        # xét từng dòng
        for row in tempListRow:
            sum = []
            check = 0
            for i in range(len(newExpression)):
                if (newExpression[i] == '+' or newExpression[i] == '-' or newExpression[i] == '*' or newExpression[i] == '/'):
                    sum.append(newExpression[i])
                else:
                    # kiểm tra giá trị tại cột đó có rỗng hay không, nếu có thì kết quả bên cột mới là rỗng
                    if (row[newExpression[i]] == ''):
                        check = 1
                        tempListRow[count][expression] = ''
                        break
                    else:
                        sum.append(row[newExpression[i]])
            # nếu ở tất cả các cột đều có giá trị thì tính giá trị cho cột mới
            if (check == 0):
                # tính toán giá trị biểu thức số học
                newAttribute = eval(''.join(sum))
                # thêm thuộc tính kết quả vào trong listRow
                tempListRow[count][expression] = newAttribute
            count += 1
        return tempListRow
