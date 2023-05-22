"""
    Argument syntax:
        python main.py --input=input.csv --namefunction=A --rate=B --output=output.csv
    Example:
        python main.py --input=house-prices.csv --namefuction=DeleteMissingRow --rate=10 output=result.csv
"""
def delete_missing_row(listRow, missingRate): #hàm xóa dòng chứa giá trị với ngưỡng dữ liệu thiếu
    """
    Xóa các dòng bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trước
    Args:
        listRow (list): dữ liệu gốc được lưu trữ dưới dạng list
        missingRate: ngưỡng tỉ lệ thiếu cho trước 

    Returns:
        temp_listRow: dữ liệu sau khi đã xóa những dòng thiếu giá trị
    """
    newListRow = listRow.copy()
    #lấy số lượng các cột
    numOfAttribute = len(listRow[0].keys())

    #duyệt từng dòng
    for row in listRow:
        count = 0
        #duyệt từng thuộc tính trong dòng đó
        for key in listRow[0].keys():
            if (row[key] == ''):
                #đếm số lượng thuộc tính thiếu của dòng
                count += 1
            #nếu số lượng thuộc tính thiếu nhiều hơn hoặc bằng ngưỡng thì xóa dòng
            if (count >= (numOfAttribute*float(missingRate)/100)):
                newListRow.remove(row)
                break
    #trả về tập dữ liệu sau khi xóa dòng
    return newListRow