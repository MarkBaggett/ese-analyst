import pyesedb
import openpyxl
import argparse
import struct
import uuid



parser = argparse.ArgumentParser(description="Given an ESE database this will create a sample template file for ese_dump.py")
parser.add_argument("ESE_INFILE", help ="Specify a valid filename (optionally with path) to the ESE (.dat) file to create a template for.")
parser.add_argument("--XLS_OUTFILE",dest="xlsoutfile", help = "Specify a Full path to the new XLS file that will be created. If not provided it will create an xlsx file with the same prefix as the ESE filename.")

options = parser.parse_args()

if not options.xlsoutfile:
    options.xlsoutfile = options.ESE_INFILE+".xlsx"

def blob_to_string(binblob):
    try:
        if re.match('^[ -~]+\x00?$', binblob.decode("utf-16-le")):
            binblob = binblob.decode("utf-16-le").strip("\x00")
        elif re.match('^[ -~]+\x00?$', binblob.decode("utf-16-be")):
            binblob = binblob.decode("utf-16-be").strip("\x00")
        elif re.match('^[ -~]+\x00?$', binblob.encode("ascii","ignore")):
            binblob = binblob.encode("ascii","ignore").strip("\x00")
    except:
        binblob = "" if not binblob else binblob.encode("HEX")
    return binblob

def smart_retrieve(ese_table, ese_record_num, column_number):
    ese_column_types = {0: 'NULL', 1: 'BOOLEAN', 2: 'INTEGER_8BIT_UNSIGNED', 3: 'INTEGER_16BIT_SIGNED', 4: 'INTEGER_32BIT_SIGNED', 5: 'CURRENCY', 6: 'FLOAT_32BIT', 7: 'DOUBLE_64BIT', 8: 'DATE_TIME', 9: 'BINARY_DATA', 10: 'TEXT', 11: 'LARGE_BINARY_DATA', 12: 'LARGE_TEXT', 13: 'SUPER_LARGE_VALUE', 14: 'INETEGER_32BIT_UNSIGNED', 15: 'INTEGER_64BIT_SIGNED', 16: 'GUID', 17: 'INTEGER_16BIT_UNSIGNED'}
    rec = ese_table.get_record(ese_record_num)
    col_type = rec.get_column_type(column_number)
    col_data = rec.get_value_data(column_number)
    #print "rec:%s  col:%s type:%s %s" % (ese_record_num, column_number, col_type, ese_column_types[col_type])
    if col_type == pyesedb.column_types.BINARY_DATA:
        col_data = "" if not col_data else col_data.encode("HEX")
    elif col_type == pyesedb.column_types.BOOLEAN:
        col_data = struct.unpack('?',col_data)[0]
    elif col_type == pyesedb.column_types.CURRENCY:
        pass
    elif col_type == pyesedb.column_types.DATE_TIME:
        pass
    elif col_type == pyesedb.column_types.DOUBLE_64BIT:
        col_data = 0 if not col_data else struct.unpack('d',col_data)[0]
    elif col_type == pyesedb.column_types.FLOAT_32BIT:
        col_data = 0.0 if not col_data else struct.unpack('f',col_data)[0]
    elif col_type == pyesedb.column_types.GUID:
	col_data = str(uuid.UUID(col_data.encode('hex')))    
    elif col_type == pyesedb.column_types.INTEGER_16BIT_SIGNED:
	col_data = 0 if not col_data else struct.unpack('h',col_data)[0]
    elif col_type == pyesedb.column_types.INTEGER_16BIT_UNSIGNED:
        col_data = 0 if not col_data else struct.unpack('H',col_data)[0]
    elif col_type == pyesedb.column_types.INTEGER_32BIT_SIGNED:
        col_data =  0 if not col_data else struct.unpack('i',col_data)[0]
    elif col_type == pyesedb.column_types.INTEGER_32BIT_UNSIGNED:
        col_data = 0 if not col_data else struct.unpack('I',col_data)[0]
    elif col_type == pyesedb.column_types.INTEGER_64BIT_SIGNED:
        col_data = 0 if not col_data else struct.unpack('q',col_data)[0]
    elif col_type == pyesedb.column_types.INTEGER_8BIT_UNSIGNED:
        col_data = 0 if not col_data else struct.unpack('B',col_data)[0]
    elif col_type == pyesedb.column_types.LARGE_BINARY_DATA:
        col_data = "" if not col_data else col_data.encode("HEX")
    elif col_type == pyesedb.column_types.LARGE_TEXT:
        col_data = blob_to_string(col_data)
    elif col_type == pyesedb.column_types.NULL:
        pass
    elif col_type == pyesedb.column_types.SUPER_LARGE_VALUE:
        col_data = "" if not col_data else col_data.encode("HEX")
    elif col_type == pyesedb.column_types.TEXT:
        col_data = blob_to_string(col_data)       
    if col_data==None:
        col_data = "Empty"
    return col_data


ese_db = pyesedb.open(options.ESE_INFILE)
target_wb = openpyxl.Workbook()

#Now create the worksheet in the new xls file with the same name as the template
sheet_count = 1
#Now copy the header values and header formats from the template
for each_table in [ x.name for x in ese_db.tables ]:
    xls_sheet = target_wb.create_sheet(title="GiveMeAName"+str(sheet_count))
    table = ese_db.get_table_by_name(each_table)
    #rows = table.get_number_of_records()
    cols = table.get_number_of_columns()
    xls_sheet["A1"] = each_table
    xls_sheet.append([x.name for x in table.columns])
    xls_sheet.append(["DELETE THESE INSTRUCTIONS - This row should contain formating instruction that is used post process formatting of the data in each columns.  You can optionally have a format command for each column being dumped.  Sample format commands include   1) OLE:[TimeDate Format String]  This interprets the column data as a Windows OLE Date Time stamp Example - OLE:%Y-%m-%d %H:%M:%S  2) FILE:[TimeDate Format String]   This interprets the column as a Window File system time stamp.  Example: FILE:%Y-%m-%d %H:%M:%S 3) Others format commands include base16 (convert database field to hex),base2 (to binary),md5,sha1 and sha256 (hash the data). "])
    xls_sheet.append(["RENAME-ME to a human readable column Name for " + x.name for x in table.columns])
    xls_sheet.append([])
    xls_sheet.append(['This line and everything below it is ignored and not included in the resulting spreadsheet. Below you will find some a sample data taken from inside the database for the given table so you can determine what you are looking at and how to format it.'])
    num_recs = 2 if table.get_number_of_records() > 2 else table.get_number_of_records()
    for row in range(num_recs):
	rec_list = []
	for each_col in range(cols):
            rec_list.append(smart_retrieve(table,row,each_col))
	print rec_list
	xls_sheet.append(rec_list)

#    secondrow = ese_db.getNextRow(table)
#    xls_sheet.append(secondrow.values())

firstsheet=target_wb.get_sheet_by_name("Sheet")
target_wb.remove_sheet(firstsheet)
target_wb.save(options.xlsoutfile)



