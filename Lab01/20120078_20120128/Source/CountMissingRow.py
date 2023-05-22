"""
    Argument syntax:
        python main.py --input=input.csv --namefunction=A
    Example:
        python main.py --input=house-prices.csv --namefunction=CountMissingRow
"""

def count_missing_row(listRow):
    """đếm số dòng bị thiếu dữ liệu
    Args:
        listRow (list): dữ liệu được lưu trữ dưới dạng list

    Returns:
        count (int): số dòng bị thiếu dữ liệu
    """
    count=0
    #Duyệt từng dòng
    for row in listRow:
        #xét từng giá trị của cột trong dòng đó
        for key in listRow[0].keys():
            if row[key] == '':
                count += 1
                break
    return count
