import sys
import csv
import pandas as pd
import ListMissingColumn
import CountMissingRow
import ImputeMissingValue
import DeleteMissingRow
import DeleteMissingColumn
import DeleteDuplicateInstance
import StandardizedData
import CalculateAttribute
import HelpFunction

#Hàm đọc file csv cần tiền xử lý dữ liệu
def readFile(inputFile):
    #tạo biến để lưu dữ liệu đọc được
    listRow = []
    with open(inputFile) as file:
        reader = csv.DictReader(file)
        for row in reader:
            listRow.append(row)      
    return listRow

#Hàm ghi file dữ liệu đã được tiền xử lý
def writeFile(outputFile,listRow):
    with open(outputFile, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = listRow[0].keys())
        writer.writeheader()
        for row in listRow:
            writer.writerow(row)

#Xử lý tham số dòng lệnh nhận từ console và chạy các chức năng
if __name__ == '__main__':

    inputFileName = str(sys.argv[1]).split("=")[1]
    inputFunctionName = str(sys.argv[2]).split("=")[1]
    outputFileName = str(sys.argv[len(sys.argv)-1].split("=")[1])

    listRow = readFile(inputFileName)

    #1. Extract columns with missing values
    if (inputFunctionName == "ListMissingColumn"):
        result = ListMissingColumn.list_missing_column(listRow)
        if any (result):
            print("\nList of attributes and the number of its missing values:")       
            for x, y in result.items():
                print(x , ':' ,  y , 'missing values')
        else:
            print("\nDataset has no attribute with missing value!\n")
    
    #2. Count the number of lines with missing data.
    elif (inputFunctionName == "CountMissingRow"):
        result=CountMissingRow.count_missing_row(listRow)
        print("\nNumber of rows with missing data:", result, "\n")

    #3. Fill in the missing value using mean, median (for numeric properties) and mode (for the categorical attribute).
    elif (inputFunctionName == "ImputeMissingValue"):
        method=str(sys.argv[3]).split("=")[1]
        if (method == "mean" or method=="MEAN"):
            result = ImputeMissingValue.impute_mean(listRow)
            writeFile(outputFileName, result)
        elif (method == "median" or method == "MEDIAN"):
                result = ImputeMissingValue.impute_median(listRow)
                writeFile(outputFileName, result)

    #4. Deleting rows containing more than a particular number of missing values
    elif (inputFunctionName == "DeleteMissingRow"):
        result = DeleteMissingRow.delete_missing_row(listRow, str(sys.argv[3].split("=")[1]))
        writeFile(outputFileName, result)

    #5. Deleting columns containing more than a particular number of missing values
    elif (inputFunctionName == "DeleteMissingColumn"):
        result = DeleteMissingColumn.delete_missing_column(listRow, str(sys.argv[3].split("=")[1]))
        writeFile(outputFileName, result)
        
    #6. Delete duplicate samples.
    elif (inputFunctionName == "DeleteDuplicateInstance"):
        result = DeleteDuplicateInstance.delete_duplicate(listRow)
        writeFile(outputFileName, result)

    #7. Normalize a numeric attribute using min-max and Z-score methods
    elif (inputFunctionName == "StandardizedData"):
        output = sys.argv[len(sys.argv)-1].split("=")[1]
        method = sys.argv[3].split("=")[1]
        dataset = pd.read_csv(inputFileName)
        attributes = list(dataset)
        typeOfAttribute = HelpFunction.get_type_of_attributes(dataset)
        columns = []#chứa các thuộc tính được yêu cầu chuẩn hóa

        for index in range(5,len(sys.argv)-1,1):
            check=False
            for attribute in attributes:
                if (attribute.lower()==sys.argv[index].lower()):
                    columns.append(attribute)
                    check=True
                    break
            if (check==False):
                print(sys.argv[index] + " is invalid")
        for col in columns:
            if (typeOfAttribute[col] > 2):
                print(col + " isn't numeric, can't standardize!\n")
                columns.remove(col)
        if (method=="MINMAX" or method =="minmax"):
            for col in columns:
                StandardizedData.standardlized_data_by_MINMAX(dataset,col,1.0,0.0)
        elif (method=="ZSCORE" or method =="zscore"):
            for col in columns:
                StandardizedData.standardlized_data_by_ZScore(dataset,col)
        else:
            print("The program does not have the method you choose, methods available are MinMax or ZScore\n")
            exit(0)
        dataset.to_csv(output)

    #8.	Performing addition, subtraction, multiplication, and division between two numerical attributes.
    elif (inputFunctionName == "CalculateAttribute"):
        expression=sys.argv[3].split("=")[1]
        result = CalculateAttribute.calculate(listRow, expression)
        if (result == 0):
            print("Wrong input expression!")
        else:
            writeFile(outputFileName, result)
    else:
        print("The preprocessor function you requested was not found!\n")
        exit(0)







    