"""
    Argument syntax:
        python main.py --input=input.csv --namefunction=A --output=output.csv
    Example:
        python main.py --input=house-prices.csv --namefunction=DeleteDuplicateInstance --output=result.csv
"""

def delete_duplicate(listRow):
    """
    Xóa các mẫu dữ liệu trùng lặp
    Args:
        listRow (list): dữ liệu gốc được lưu trữ dưới dạng list

    Returns:
        temp_listRow: dữ liệu sau khi đã xóa những mẫu trùng lặp nhau
    """
    #tạo 1 set để chứa các dòng không bị trùng (dùng tính chất của set để loại bỏ trùng lặp)
    seen = set()
    #tạo 1 biến để lưu lại tập dữ liệu mới
    newListRow = []
    #duyệt từng dòng
    for row in listRow:
        #tạo biến row mang kiểu dữ liệu tuple của dòng đó
        temp = tuple(row.items())
        #nếu temp chưa từng xuất hiện trong set thì thêm vào set và tập dữ liệu mới
        if temp not in seen:
            seen.add(temp)
            newListRow.append(row)
    #trả về tập dữ liệu mới sau khi đã loại bỏ các dòng trùng lặp
    return newListRow 