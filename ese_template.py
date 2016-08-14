from impacket import ese
import openpyxl
import argparse


parser = argparse.ArgumentParser(description="Given an ESE database this will create a sample template file for ese_dump.py")
parser.add_argument("ESE_INFILE", help ="Specify a valid filename (optionally with path) to the ESE (.dat) file to create a template for.")
parser.add_argument("--XLS_OUTFILE",dest="xlsoutfile", help = "Specify a Full path to the new XLS file that will be created. If not provided it will create an xlsx file with the same prefix as the ESE filename.")

options = parser.parse_args()

if not options.xlsoutfile:
    options.xlsoutfile = options.ESE_INFILE+".xlsx"

ese_db = ese.ESENT_DB(options.ESE_INFILE)
target_wb = openpyxl.Workbook()

#Now create the worksheet in the new xls file with the same name as the template
sheet_count = 1
#Now copy the header values and header formats from the template
for each_table in ese_db._ESENT_DB__tables:
    xls_sheet = target_wb.create_sheet(title="GiveMeAName"+str(sheet_count))
    table = ese_db.openTable(each_table)
    firstrow = ese_db.getNextRow(table)
    if not firstrow:
        continue
    xls_sheet["A1"] = each_table
    xls_sheet.append([str(x).replace("\00","") for x in firstrow.keys()])
    xls_sheet.append(["DELETE THESE INSTRUCTIONS - This row should contain formating instruction that is used post process formatting of the data in each columns.  You can optionally have a format command for each column being dumped.  Sample format commands include   1) OLE:[TimeDate Format String]  This interprets the column data as a Windows OLE Date Time stamp Example - OLE:%Y-%m-%d %H:%M:%S  2) FILE:[TimeDate Format String]   This interprets the column as a Window File system time stamp.  Example: FILE:%Y-%m-%d %H:%M:%S 3) Others format commands include base16 (convert database field to hex),base2 (to binary),md5,sha1 and sha256 (hash the data). "])
    xls_sheet.append(["RENAME-ME to a human readable column Name for "+x for x in firstrow.keys()])
    xls_sheet.append([])
    xls_sheet.append(['This line and everything below it is ignored and not included in the resulting spreadsheet. Below you will find some a sample data taken from inside the database for the given table so you can determine what you are looking at and how to format it.'])
    xls_sheet.append([str(x).replace("\00","") for x in firstrow.values()])
#    secondrow = ese_db.getNextRow(table)
#    xls_sheet.append(secondrow.values())
   
    

firstsheet=target_wb.get_sheet_by_name("Sheet")
target_wb.remove_sheet(firstsheet)
target_wb.save(options.xlsoutfile)



