import pyesedb
import yaml
import csv
import codecs
import struct
import uuid
import argparse
import pathlib
import importlib
import re
import sys
import os
import tempfile
import urllib.request
import subprocess
from Registry.Registry import Registry
from datetime import datetime,timedelta

def blob_to_string(chrblob):
    """Takes in a binary blob hex characters and does its best to convert it to a readable string.
       Works great for UTF-16 LE, UTF-16 BE, ASCII like data. Otherwise return it as hex.
    """
    try:
        chrblob = codecs.decode(chrblob,"hex")
    except:
        pass
    try:
        if re.match(b'^(?:[^\x00]\x00)+\x00\x00$', chrblob):
            binblob = chrblob.decode("utf-16-le").strip("\x00")
        elif re.match(b'^(?:\x00[^\x00])+\x00\x00$', chrblob):
            binblob = chrblob.decode("utf-16-be").strip("\x00")
        else:
            binblob = chrblob.decode("latin1").strip("\x00")
    except Exception as e:
        binblob = "" if not chrblob else codecs.decode(chrblob,"latin-1")
    return binblob

def ole_timestamp(binblob):
    """converts a hex encoded OLE time stamp to a time string"""
    try:
        td,ts = str(struct.unpack("<d",binblob)[0]).split(".")
        dt = datetime(1899,12,30,0,0,0) + timedelta(days=int(td),seconds=86400 * float("0.{}".format(ts)))
    except Exception as e:
        dt = "This field is incorrectly identified as an OLE timestamp in the template."
    return dt
 
def file_timestamp(binblob):
    """converts a hex encoded windows file time stamp to a time string"""
    try:
        dt = datetime(1601,1,1,0,0,0) + timedelta(microseconds=binblob/10)
    except:
        dt = "This field is incorrectly identified as a file timestamp in the template"
    return dt

def smart_retrieve(ese_table, ese_record_num, column_number):
    """Given a row and column will determine the format and retrieve a value from the ESE table"""
    rec = ese_table.get_record(ese_record_num)
    col_type = rec.get_column_type(column_number)
    col_data = rec.get_value_data(column_number)
    #print "rec:%s  col:%s type:%s %s" % (ese_record_num, column_number, col_type, ese_column_types[col_type])
    if col_type == pyesedb.column_types.BINARY_DATA:
        col_data = "" if not col_data else codecs.encode(col_data,"HEX")
    elif col_type == pyesedb.column_types.BOOLEAN:
        col_data = col_data if col_data else b'\x00' 
        col_data = struct.unpack('?',col_data)[0]
    elif col_type == pyesedb.column_types.CURRENCY:
        pass
    elif col_type == pyesedb.column_types.DATE_TIME:
        col_data = ole_timestamp(col_data)
    elif col_type == pyesedb.column_types.DOUBLE_64BIT:
        col_data = 0 if not col_data else struct.unpack('d',col_data)[0]
    elif col_type == pyesedb.column_types.FLOAT_32BIT:
        col_data = 0.0 if not col_data else struct.unpack('f',col_data)[0]
    elif col_type == pyesedb.column_types.GUID:
        col_data = 0 if not col_data else str(uuid.UUID(bytes = col_data))    
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
        col_data = "" if not col_data else codecs.encode(col_data,"HEX")
    elif col_type == pyesedb.column_types.LARGE_TEXT:
        col_data = blob_to_string(col_data)
    elif col_type == pyesedb.column_types.NULL:
        pass
    elif col_type == pyesedb.column_types.SUPER_LARGE_VALUE:
        col_data = "" if not col_data else codecs.encode(col_data,"HEX")
    elif col_type == pyesedb.column_types.TEXT:
        col_data = blob_to_string(col_data)   
    else:
        col_data = blob_to_string(col_data)    
    if col_data==None:
        col_data = "Empty"
    return col_data

def plugin_list():
    if getattr(sys, 'frozen', False):
        program_dir = pathlib.Path(sys.executable)
    elif __file__:
        program_dir = pathlib.Path(__file__)
    plugpaths = pathlib.Path(program_dir).parent.glob("*_plugin.py")
    plist = [x.name[:-3] for x in plugpaths]
    if not plist:
        plist = ['No Plugins found in path {}'.format(program_dir)]
    return plist

def make_config(database):
    yaml_struct = {'tables':{}}
    for each_table in database.tables:
        table_struct = {'name':each_table.name,'ignore':'no','fields':{}}
        for each_field in each_table.columns:
             field_struct = {}
             field_struct['friendly name'] = each_field.name
             field_struct['format'] = 'None'
             field_struct['ignore'] = 'no'
             table_struct['fields'][each_field.name] = field_struct
        yaml_struct['tables'][each_table.name] = table_struct
    lookups = {'lookups': {
        'numbers' : {0:'zero', 1:"one"},
        'known_sids' : { 'S-1-5-32-545': ' Users', 'S-1-5-32-544': ' Administrators', 'S-1-5-32-547': ' Power Users', 'S-1-5-32-546': ' Guests', 'S-1-5-32-569': ' BUILTIN\\Cryptographic Operators', 'S-1-16-16384': ' System Mandatory Level ', 'S-1-5-32-551': ' Backup Operators', 'S-1-16-8192': ' Medium Mandatory Level ', 'S-1-5-80': ' NT Service ', 'S-1-5-32-548': ' Account Operators', 'S-1-5-32-561': ' BUILTIN\\Terminal Server License Servers', 'S-1-5-64-14': ' SChannel Authentication ', 'S-1-5-32-562': ' BUILTIN\\Distributed COM Users', 'S-1-5-64-21': ' Digest Authentication ', 'S-1-5-19': ' NT Authority', 'S-1-3-0': ' Creator Owner', 'S-1-5-80-0': ' All Services ', 'S-1-5-20': ' NT Authority', 'S-1-5-18': ' Local System', 'S-1-5-32-552': ' Replicators', 'S-1-5-32-579': ' BUILTIN\\Access Control Assistance Operators', 'S-1-16-4096': ' Low Mandatory Level ', 'S-1-16-12288': ' High Mandatory Level ', 'S-1-2-0': ' Local ', 'S-1-16-0': ' Untrusted Mandatory Level ', 'S-1-5-3': ' Batch', 'S-1-5-2': ' Network', 'S-1-5-1': ' Dialup', 'S-1-5-7': ' Anonymous', 'S-1-5-6': ' Service', 'S-1-5-4': ' Interactive', 'S-1-5-9': ' Enterprise Domain Controllers', 'S-1-5-8': ' Proxy', 'S-1-5-32-550': ' Print Operators', 'S-1-0-0': ' Nobody', 'S-1-5-32-559': ' BUILTIN\\Performance Log Users', 'S-1-5-32-578': ' BUILTIN\\Hyper-V Administrators', 'S-1-5-32-549': ' Server Operators', 'S-1-2-1': ' Console Logon ', 'S-1-3-1': ' Creator Group', 'S-1-5-32-575': ' BUILTIN\\RDS Remote Access Servers', 'S-1-3-3': ' Creator Group Server', 'S-1-3-2': ' Creator Owner Server', 'S-1-5-32-556': ' BUILTIN\\Network Configuration Operators', 'S-1-5-32-557': ' BUILTIN\\Incoming Forest Trust Builders', 'S-1-5-32-554': ' BUILTIN\\Pre-Windows 2000 Compatible Access', 'S-1-5-32-573': ' BUILTIN\\Event Log Readers ', 'S-1-5-32-576': ' BUILTIN\\RDS Endpoint Servers', 'S-1-5-83-0': ' NT VIRTUAL MACHINE\\Virtual Machines', 'S-1-16-28672': ' Secure Process Mandatory Level ', 'S-1-5-11': ' Authenticated Users', 'S-1-1-0': ' Everyone', 'S-1-5-32-555': ' BUILTIN\\Remote Desktop Users', 'S-1-16-8448': ' Medium Plus Mandatory Level ', 'S-1-5-17': ' This Organization ', 'S-1-5-32-580': ' BUILTIN\\Remote Management Users', 'S-1-5-15': ' This Organization ', 'S-1-5-14': ' Remote Interactive Logon ', 'S-1-5-13': ' Terminal Server Users', 'S-1-5-12': ' Restricted Code', 'S-1-5-32-577': ' BUILTIN\\RDS Management Servers', 'S-1-5-10': ' Principal Self', 'S-1-3': ' Creator Authority', 'S-1-2': ' Local Authority', 'S-1-1': ' World Authority', 'S-1-0': ' Null Authority', 'S-1-5-32-574': ' BUILTIN\\Certificate Service DCOM Access ', 'S-1-5': ' NT Authority', 'S-1-4': ' Non-unique Authority', 'S-1-5-32-560': ' BUILTIN\\Windows Authorization Access Group', 'S-1-16-20480': ' Protected Process Mandatory Level ', 'S-1-5-64-10': ' NTLM Authentication ', 'S-1-5-32-558': ' BUILTIN\\Performance Monitor Users'},
        'LUID_interface_types': {1: 'IF_TYPE_OTHER', 2: 'IF_TYPE_REGULAR_1822', 3: 'IF_TYPE_HDH_1822', 4: 'IF_TYPE_DDN_X25', 5: 'IF_TYPE_RFC877_X25', 6: 'IF_TYPE_ETHERNET_CSMACD', 7: 'IF_TYPE_IS088023_CSMACD', 8: 'IF_TYPE_ISO88024_TOKENBUS', 9: 'IF_TYPE_ISO88025_TOKENRING', 10: 'IF_TYPE_ISO88026_MAN', 11: 'IF_TYPE_STARLAN', 12: 'IF_TYPE_PROTEON_10MBIT', 13: 'IF_TYPE_PROTEON_80MBIT', 14: 'IF_TYPE_HYPERCHANNEL', 15: 'IF_TYPE_FDDI', 16: 'IF_TYPE_LAP_B', 17: 'IF_TYPE_SDLC', 18: 'IF_TYPE_DS1', 19: 'IF_TYPE_E1', 20: 'IF_TYPE_BASIC_ISDN', 21: 'IF_TYPE_PRIMARY_ISDN', 22: 'IF_TYPE_PROP_POINT2POINT_SERIAL', 23: 'IF_TYPE_PPP', 24: 'IF_TYPE_SOFTWARE_LOOPBACK', 25: 'IF_TYPE_EON', 26: 'IF_TYPE_ETHERNET_3MBIT', 27: 'IF_TYPE_NSIP', 28: 'IF_TYPE_SLIP', 29: 'IF_TYPE_ULTRA', 30: 'IF_TYPE_DS3', 31: 'IF_TYPE_SIP', 32: 'IF_TYPE_FRAMERELAY', 33: 'IF_TYPE_RS232', 34: 'IF_TYPE_PARA', 35: 'IF_TYPE_ARCNET', 36: 'IF_TYPE_ARCNET_PLUS', 37: 'IF_TYPE_ATM', 38: 'IF_TYPE_MIO_X25', 39: 'IF_TYPE_SONET', 40: 'IF_TYPE_X25_PLE', 41: 'IF_TYPE_ISO88022_LLC', 42: 'IF_TYPE_LOCALTALK', 43: 'IF_TYPE_SMDS_DXI', 44: 'IF_TYPE_FRAMERELAY_SERVICE', 45: 'IF_TYPE_V35', 46: 'IF_TYPE_HSSI', 47: 'IF_TYPE_HIPPI', 48: 'IF_TYPE_MODEM', 49: 'IF_TYPE_AAL5', 50: 'IF_TYPE_SONET_PATH', 51: 'IF_TYPE_SONET_VT', 52: 'IF_TYPE_SMDS_ICIP', 53: 'IF_TYPE_PROP_VIRTUAL', 54: 'IF_TYPE_PROP_MULTIPLEXOR', 55: 'IF_TYPE_IEEE80212', 56: 'IF_TYPE_FIBRECHANNEL', 57: 'IF_TYPE_HIPPIINTERFACE', 58: 'IF_TYPE_FRAMERELAY_INTERCONNECT', 59: 'IF_TYPE_AFLANE_8023', 60: 'IF_TYPE_AFLANE_8025', 61: 'IF_TYPE_CCTEMUL', 62: 'IF_TYPE_FASTETHER', 63: 'IF_TYPE_ISDN', 64: 'IF_TYPE_V11', 65: 'IF_TYPE_V36', 66: 'IF_TYPE_G703_64K', 67: 'IF_TYPE_G703_2MB', 68: 'IF_TYPE_QLLC', 69: 'IF_TYPE_FASTETHER_FX', 70: 'IF_TYPE_CHANNEL', 71: 'IF_TYPE_IEEE80211', 72: 'IF_TYPE_IBM370PARCHAN', 73: 'IF_TYPE_ESCON', 74: 'IF_TYPE_DLSW', 75: 'IF_TYPE_ISDN_S', 76: 'IF_TYPE_ISDN_U', 77: 'IF_TYPE_LAP_D', 78: 'IF_TYPE_IPSWITCH', 79: 'IF_TYPE_RSRB', 80: 'IF_TYPE_ATM_LOGICAL', 81: 'IF_TYPE_DS0', 82: 'IF_TYPE_DS0_BUNDLE', 83: 'IF_TYPE_BSC', 84: 'IF_TYPE_ASYNC', 85: 'IF_TYPE_CNR', 86: 'IF_TYPE_ISO88025R_DTR', 87: 'IF_TYPE_EPLRS', 88: 'IF_TYPE_ARAP', 89: 'IF_TYPE_PROP_CNLS', 90: 'IF_TYPE_HOSTPAD', 91: 'IF_TYPE_TERMPAD', 92: 'IF_TYPE_FRAMERELAY_MPI', 93: 'IF_TYPE_X213', 94: 'IF_TYPE_ADSL', 95: 'IF_TYPE_RADSL', 96: 'IF_TYPE_SDSL', 97: 'IF_TYPE_VDSL', 98: 'IF_TYPE_ISO88025_CRFPRINT', 99: 'IF_TYPE_MYRINET', 100: 'IF_TYPE_VOICE_EM', 101: 'IF_TYPE_VOICE_FXO', 102: 'IF_TYPE_VOICE_FXS', 103: 'IF_TYPE_VOICE_ENCAP', 104: 'IF_TYPE_VOICE_OVERIP', 105: 'IF_TYPE_ATM_DXI', 106: 'IF_TYPE_ATM_FUNI', 107: 'IF_TYPE_ATM_IMA', 108: 'IF_TYPE_PPPMULTILINKBUNDLE', 109: 'IF_TYPE_IPOVER_CDLC', 110: 'IF_TYPE_IPOVER_CLAW', 111: 'IF_TYPE_STACKTOSTACK', 112: 'IF_TYPE_VIRTUALIPADDRESS', 113: 'IF_TYPE_MPC', 114: 'IF_TYPE_IPOVER_ATM', 115: 'IF_TYPE_ISO88025_FIBER', 116: 'IF_TYPE_TDLC', 117: 'IF_TYPE_GIGABITETHERNET', 118: 'IF_TYPE_HDLC', 119: 'IF_TYPE_LAP_F', 120: 'IF_TYPE_V37', 121: 'IF_TYPE_X25_MLP', 122: 'IF_TYPE_X25_HUNTGROUP', 123: 'IF_TYPE_TRANSPHDLC', 124: 'IF_TYPE_INTERLEAVE', 125: 'IF_TYPE_FAST', 126: 'IF_TYPE_IP', 127: 'IF_TYPE_DOCSCABLE_MACLAYER', 128: 'IF_TYPE_DOCSCABLE_DOWNSTREAM', 129: 'IF_TYPE_DOCSCABLE_UPSTREAM', 130: 'IF_TYPE_A12MPPSWITCH', 131: 'IF_TYPE_TUNNEL', 132: 'IF_TYPE_COFFEE', 133: 'IF_TYPE_CES', 134: 'IF_TYPE_ATM_SUBINTERFACE', 135: 'IF_TYPE_L2_VLAN', 136: 'IF_TYPE_L3_IPVLAN', 137: 'IF_TYPE_L3_IPXVLAN', 138: 'IF_TYPE_DIGITALPOWERLINE', 139: 'IF_TYPE_MEDIAMAILOVERIP', 140: 'IF_TYPE_DTM', 141: 'IF_TYPE_DCN', 142: 'IF_TYPE_IPFORWARD', 143: 'IF_TYPE_MSDSL', 144: 'IF_TYPE_IEEE1394', 145: 'IF_TYPE_RECEIVE_ONLY'}
        }}
    table_references = {'table_references' : {
        'app_id' : {'table':'SruDbIdMapTable',
                    'key':'IdIndex',
                    'value': ['IdType','IdBlob']}
    }}
    yaml_struct.update(lookups)
    yaml_struct.update(table_references)
    ese_config = 'yaml_config = r\"\"\"\n' + yaml.dump(yaml_struct) + """

\"\"\"

import struct
import codecs



def plugin_init(ese_database):
    #table_names = " ".join([x.name for x in ese_database.tables])
    #print("Received Arguments", args)
    #print("Plugin Initialized for ", table_names)
    # Setup any data structures required for yaml function calls
    return None

def plugin_modify_header(list_of_headers, table_name):
    #print("Plugin Processing headers", list_of_headers)
    # Modify headers as needed before commit to file
    return list_of_headers

#sample_total = 0
def plugin_modify_row(list_of_row_values, table_name):
    #global sample_total
    #print("Plugin Processing Row", list_of_row_values)
    #if table_name == "some target":
    #    sample_total += list_of_row_values[10] 
    # Modify list as needed before commit to file or keep totals
    return list_of_row_values

def plugin_end_of_file(csv_writer_object, table_name):
    #print("Plugin Finished file" )
    # Write header footers, calculations etc
    return None

def BinarySIDtoStringSID(sid_str):
    if not sid_str:
        return ""
    sid = codecs.decode(sid_str,"hex")
    str_sid_components = [sid[0]]
    # Now decode the 48-byte portion
    if len(sid) >= 8:
        subauthority_count = sid[1]
        identifier_authority = struct.unpack(">H", sid[2:4])[0]
        identifier_authority <<= 32
        identifier_authority |= struct.unpack(">L", sid[4:8])[0]
        str_sid_components.append(identifier_authority)
        start = 8
        for i in range(subauthority_count):
            authority = sid[start:start + 4]
            if not authority:
                break
            if len(authority) < 4:
                raise ValueError("In binary SID '%s', component %d has been truncated. "
                         "Expected 4 bytes, found %d: (%s)",
                         ",".join([str(ord(c)) for c in sid]), i,
                         len(authority), authority)
            str_sid_components.append(struct.unpack("<L", authority)[0])
            start += 4
            sid_str = "S-%s" % ("-".join([str(x) for x in str_sid_components]))
    sid_name = lookup("known_sids",sid_str)
    return "{} ({})".format(sid_str,sid_name)

def get_app_id(data):
    app_type, app_value = lookup("app_id", data)
    if app_type == 3:
        data = BinarySIDtoStringSID(app_value)
    elif app_type == 2:
        data = blob_to_string(app_value)
    return data
"""
    return ese_config

def lookup(table, value):
    return yaml_config.get("lookups",{}).get(table, {}).get(value)

def extract_live_file(live_path):
    if not live_path.exists():
        print(f"The file specified for live aquisition was not found. {str(live_path)}")
        sys.exit(1)
    try:
        fget_file = tempfile.NamedTemporaryFile(mode="w+b", suffix=".exe",delete=False)
        extracted_file = tempfile.NamedTemporaryFile(mode="w+b", suffix = ".dat", delete=False)
        #print("Downloading fget.exe to {}".format(fget_file.name))
        try:
            fget_binary = urllib.request.urlopen('https://github.com/MarkBaggett/srum-dump/raw/master/FGET.exe').read()
        except Exception as e:
            raise(Exception(f"Unable to download FGET {str(e)}"))
        fget_file.write(fget_binary)
        fget_file.close()
        cmdline = r'{} -extract "{}" {}'.format(fget_file.name, str(live_path), extracted_file.name)
        #print(cmdline)
        phandle = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out1,_ = phandle.communicate()
        pathlib.Path(fget_file.name).unlink()
    except Exception as e:
        print("Unable to automatically extract file. {}".format(str(e)))
        return None
    if b"SUCCESS" in out1:
        return pathlib.Path(extracted_file.name)
    else:
        print("ERROR running FGET.EXE: {}".format(out1))
        sys.exit(1)

def extract_live_ese(tgt_file):
    try:
        tmp_dir = tempfile.mkdtemp()
        esentutl_path = pathlib.Path(os.environ.get("COMSPEC")).parent / "esentutl.exe"
        tgt_path = pathlib.Path(tgt_file)
        destination = pathlib.Path(tmp_dir) / tgt_path.name
        if not tgt_path.exists():
            print("Unable to live aquire ese file {}. Target ESE path not found.".format(str(tgt_path)))
            sys.exit(1)
        if esentutl_path.exists():
            print(f"Extracting {str(tgt_path)} with esentutl.exe")
            cmdline = r'{} /y "{}" /vss /d "{}"'.format(str(esentutl_path), str(tgt_path), str(destination))
        else:
            print("ESENTUTL.EXE not found.  Reverting to fget.")
            return extract_live_file(tgt_file)
        print(cmdline)
        phandle = subprocess.Popen(cmdline, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out1,_ = phandle.communicate()
    except Exception as e:
        print("Error during live ese aquisition {}\n{}\n".format(str(e)))
        return None
    if b"success" in out1.lower():
        return destination
    else:
        print("Unable to determine success or failure. \n{}\n".format( out1.decode() ))
    return None

def create_csv(database, table_name, yaml= {}):
    friendly_table_name = table_name
    table_yaml = yaml.get('tables',{}).get(table_name,{})
    if args.verbose and not table_yaml:
        print(f"YAML WARNING: Table {table_name} is not defined in the YAML.")
    else:
        friendly_table_name = yaml.get('tables',{}).get(table_name,{}).get("name",table_name)
        ignore_table = table_yaml.get("ignore","no") == "yes"
        if ignore_table:
            print(f"Table {friendly_table_name} ignored because of YAML setting.")
            return
    fcount = 1
    dest_file = pathlib.Path(args.outpath) / (friendly_table_name+".csv")
    while dest_file.exists():
        dest_file = pathlib.Path.cwd() / (friendly_table_name+f"({fcount}).csv")
        fcount += 1
    with dest_file.open("w", newline = "") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        print(f"Processing {friendly_table_name}")
        ese_table = database.get_table_by_name(table_name)
        header_row = []
        for each_field in ese_table.columns:
            name = each_field.name
            if table_yaml:
                field_yaml = table_yaml.get("fields",{}).get(each_field.name,{})
                if args.verbose and not field_yaml:
                        print (f"YAML WARNING: Format specifier missing in yaml for field {name} in {table_name}")
                name = field_yaml.get('name',each_field.name)
                ignore_field = field_yaml.get('ignore','no') == "yes"
                if ignore_field:
                    continue
            header_row.append(name)
        if yaml_config and hasattr(plugin,"plugin_modify_header"):
            header_row = plugin.plugin_modify_header(header_row,table_name)
        csv_writer.writerow(header_row)
        for rec_entry_num in range(ese_table.number_of_records):
            data_row = []
            for each_field in range(ese_table.number_of_columns):
                field_name = ese_table.columns[each_field].name
                data = smart_retrieve(ese_table,rec_entry_num, each_field)
                if table_yaml:
                    ignore_field = table_yaml.get("fields",{}).get(field_name,{}).get('ignore','no') == "yes"
                    if ignore_field:
                        continue
                    data_format = yaml.get('tables',{}).get(table_name,{}).get("fields",{}).get(field_name,{}).get('format',"")
                    if data_format.startswith("function:"):
                        func_call = data_format.split(":")[1]
                        data = plugin.__dict__.get(func_call,lambda x:f"{data_format} not found")(data)
                    elif data_format.startswith("lookup:"):
                        data = lookup(data_format.split(":")[1],data)     
                data_row.append(data)
            if yaml_config and hasattr(plugin,"plugin_modify_row"):
                data_row = plugin.plugin_modify_row(data_row, table_name)
            csv_writer.writerow(data_row)
        if yaml_config and hasattr(plugin,"plugin_end_of_file"):
                plugin.plugin_end_of_file(csv_writer, table_name)


def load_yaml_table_refs(ese_db, plugin):
    for each_table_reference in yaml_config.get("table_references",[]):
        table_ref_value = yaml_config.get("table_references").get(each_table_reference)
        try:
            lookup_name = table_ref_value.get("table")
            lookup_key = table_ref_value.get("key")
            lookup_value = table_ref_value.get("value")
            lookup_table = {}
            ese_table = ese_db.get_table_by_name(lookup_name)
            column_lookup = dict([(x.name,index) for index,x in enumerate(ese_table.columns)])
            for eachrow in range(ese_table.number_of_records):
                val_list = []
                for each_val in lookup_value:
                    val_list.append(smart_retrieve(ese_table, eachrow, column_lookup.get(each_val)))
                keyval = smart_retrieve(ese_table, eachrow, column_lookup.get(lookup_key))
                lookup_table[keyval] = val_list
            yaml_config.get('lookups')[each_table_reference] = lookup_table
        except Exception as e:
            raise(e)
    return yaml_config     

parser = argparse.ArgumentParser(description="Find and dump ESE databases.")
parser.add_argument("--make-plugin", "-m", dest="makeconfig", help="Produce an editable shell of a plugin for the specified ese.",action="store_true")
parser.add_argument("--pluggin", "-p", choices = plugin_list(), dest="config", help="Use a plugin that defines fields in the ese database.")
parser.add_argument("--outpath", "-o", dest="outpath", default = str(pathlib.Path.cwd()), help="The directory to which the CSV(s) will be written.")
parser.add_argument("--acquire-live", "-a", dest="acquire", help="Use FGET to extract locked file for processing.",action="store_true")
parser.add_argument("--verbose", "-v", dest="verbose", help="Generate Verbose output for debugging.",action="store_true")
parser.add_argument("--list-tables", "-l", dest="listtables", help="List all tables in the ese.",action="store_true")
parser.add_argument("--recurse", "-r", dest="recurse", help="Recurse subdirectories to find ese in path.",action="store_true")
parser.add_argument("--dump-tables", "-d", dest="dumptables", help="Only dump tables listed here separated by spaces. End this list with double dash if this is not followed by additional optional arguments. --.",nargs = "*")
parser.add_argument("--plugin-args", dest="pluginargs", default = [], help="Arguments passed to plugin. End arguments with double dash if this is not followed by additional optional arguments. --.",nargs = "*")
parser.add_argument("ese_file", help = "This required file name is an ese database")
args = parser.parse_args()

if args.outpath and not (pathlib.Path(args.outpath).exists() and pathlib.Path(args.outpath).is_dir()):
    print("The specified output path is inaccessible.")
    sys.exit(1)

edb_list = pathlib.Path(args.ese_file)
if args.recurse:
    edb_list = edb_list.parent.rglob(edb_list.name)
else:
    edb_list = edb_list.parent.glob(edb_list.name)

yaml_config = {}
if args.config:
    if getattr(sys, 'frozen', False):
        program_dir = pathlib.Path(sys.executable)
    elif __file__:
        program_dir = pathlib.Path(__file__)
    sys.path.append(str(program_dir.resolve().parent))
    sys.path.append(str(pathlib.Path.cwd()))
    try: 
        plugin = importlib.import_module(args.config)
    except Exception as e:
        print(f"Unable to import plugin {args.config}. Proceeding without plugin. {str(e)}")
    else:
        yaml_config = yaml.safe_load(plugin.yaml_config)
        plugin.smart_retrieve = smart_retrieve
        plugin.blob_to_string = blob_to_string
        plugin.lookup = lookup
        plugin.ole_timestatmp = ole_timestamp
        plugin.file_timestamp = file_timestamp
        plugin.extract_live_file = extract_live_file
        plugin.extract_live_ese = extract_live_ese
        plugin.args = args.pluginargs

file_count = 0
for edb_path in edb_list:
    edb_path_original = str(edb_path)
    file_count += 1
    print(f"Processing File {edb_path_original}")

    if not edb_path.exists():
        print(f"File {edb_path_original} not found. Skipping it!")
        continue

    if args.acquire:
        edb_path = extract_live_ese(edb_path)

    ese_db = pyesedb.file()
    try:
        ese_db.open(str(edb_path))
    except Exception as e:
        if "libesedb_file_open_wide" in str(e):
            print("Not an ese file. Skipping.")
        else:
            print(f"Unable to open ESE. Perhaps it is locked (try -a) or it is not an ese. \n\n{str(e)}\n")
        if args.acquire:
            edb_path.unlink()
        continue

    if yaml_config:
            yaml_config = load_yaml_table_refs(ese_db, plugin)
            if hasattr(plugin,"plugin_init"):
                plugin.plugin_init(ese_db)

    if args.makeconfig:
        ese_config = make_config(ese_db)
        print(ese_config)
    elif args.listtables:
        print(f"TABLE LISTING FOR ESE FILE {str(edb_path_original)}\n")
        for eachtable in ese_db.tables:
            if not yaml_config:
                try:
                    print(f"Table {eachtable.name} has {eachtable.number_of_records} records")
                except Exception as e:
                    print(f"Table {eachtable.name} {str(e)}")
            else:
                friendly_name = yaml_config.get('tables',{}).get(eachtable.name,{}).get("name",eachtable.name)
                try:
                    print(f"Table {eachtable.name} aka {friendly_name} has {eachtable.number_of_records} records") 
                except Exception as e:
                    print(f"Table {eachtable.name} aka {friendly_name}")
        print(f"\nDone listing {str(edb_path_original)}\n")
    else:
        for eachtable in ese_db.tables:
            friendly_name = yaml_config.get('tables',{}).get(eachtable.name,{}).get("name",eachtable.name)
            if args.dumptables and (eachtable.name not in args.dumptables) and (friendly_name not in args.dumptables):
                continue
            create_csv(ese_db, eachtable.name, yaml_config )

    ese_db.close()
    if args.acquire:
        edb_path.unlink()

print(f"{file_count} files matched the file path criteria specified.")