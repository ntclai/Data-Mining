"""
    Argument syntax:
        python main.py --input=input.csv --namefunction=A
    Example:
        python main.py --input=house-prices.csv --namefunction=ListMissingColumn
"""

def list_missing_column(listRow):
    """liệt kê các cột bị thiếu dữ liệu
    Args:
        listRow (list): các dòng dữ liệu được lưu trữ dưới dạng list

    Returns:
        listColumn (array): danh sách các cột bị thiêú dữ liệu
    """
    #tạo biến nhớ tạm để lưu kết quả
    temp = []
    #duyệt từng cột
    for key in listRow[0].keys():
        #reset biến đếm với từng cột
        count = 0
        #duyệt từng dòng dữ liệu
        for row in listRow:
            if (row[key] == ''):
                count += 1
                temp.append((key, count))
    #chuyển biến từ list về lại dictionary ban đầu
    listColumn = dict(temp)
    return listColumn