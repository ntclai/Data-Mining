"""
    Argument syntax:
        python main.py --input=input.csv --namefunction=A --rate=B --output=output.csv
    Example:
        python main.py --input=house-prices.csv --namefunction=DeleteMissingColumn --rate=10 --output=result.csv
"""
def delete_missing_column(listRow, missingRate):
    """
    Xóa các cột bị thiếu dữ liệu với ngưỡng tỉ lệ thiếu cho trướcS
    Args:
        listRow (list): dữ liệu gốc được lưu trữ dưới dạng list
        missingRate: ngưỡng tỉ lệ thiếu cho trước 

    Returns:
        temp_listRow: dữ liệu sau khi đã xóa những dòng thiếu giá trị
    """
    newListRow = []   
    for i in range(len(listRow)):
        b = listRow[i].copy()
        newListRow.append(b)

    #lấy số lượng các dòng 
    numRow = len(listRow)
    #duyệt từng cột
    for key in listRow[0].keys():
        #với mỗi cột thì reset biến đếm
        count = 0
        #duyệt từng dòng trong cột
        for row in listRow:
            #nếu ở dòng đó mà cột không có dữ liệu thì tăng biến đếm
            if (row[key] == ''):
                count += 1
            #nếu lượng dữ liệu thiếu trong cột vượt ngưỡng ban đầu thì xóa cột đó và chuyển sang duyệt cột tiếp theo
            if (count >= (numRow*float(missingRate)/100)):
                for index in range(len(listRow)):
                    newListRow[index].pop(key)
                break
    #trả vệ tập dữ liệu mới sau khi xóa cột
    return newListRow