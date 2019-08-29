# ese-analyst

The tool ese2csv is intended to make analyzing and dumping any ese file simple.  Its options are

```
C:\>ese2csv.exe --help
usage: ese2csv.exe [-h] [--make-plugin] [--pluggin CONFIG] [--acquire-live]
                   [--list-tables] [--recurse]
                   [--dump-tables [DUMPTABLES [DUMPTABLES ...]]]
                   [--plugin-args [PLUGINARGS [PLUGINARGS ...]]]
                   ese_file

Find and dump ESE databases.

positional arguments:
  ese_file              This required file name is an ese database

optional arguments:
  -h, --help            show this help message and exit
  --make-plugin, -m     Produce an editable shell of a plugin for the
                        specified ese.
  --pluggin CONFIG, -p CONFIG
                        Use a plugin that defines fields in the ese database.
  --acquire-live, -a    Use FGET to extract locked file for processing.
  --list-tables, -l     List all tables in the ese.
  --recurse, -r         Recurse subdirectories to find ese in path.
  --dump-tables [DUMPTABLES [DUMPTABLES ...]], -d [DUMPTABLES [DUMPTABLES ...]]
                        Only dump tables listed here separated by spaces. End
                        this list with double dash if this is not followed by
                        additional optional arguments. --.
  --plugin-args [PLUGINARGS [PLUGINARGS ...]]
                        Arguments passed to plugin. End arguments with double
                        dash if this is not followed by additional optional
                        arguments. --.

```

The idea of ese2csv is to allow you to dump the data from any ESE database that the libesedb engine can read. However, you can also create a "plugin" for the ese file with the -m option that allows you to use YAML to define the formats for fields, gives them friendly names and provides functions for processing the database. The tool is distributed with one plugin.  The srudb_plugin.py can be used to dump the srum database.  The tool supports wildcards and directory recursion so you can search your drive and let the tool extract what ever it can find.

# Dump all the tables in the the srudb.dat file to a csv_files except those ignored by the YAML in the srum_plugin.py. Acquire a copy of the locked srudb.dat file before use. Pass a copy of the already unlocked SOFTWARE registry hive as a plugin argument.

```
C:>ese2csv.exe -p srum_plugin -a --plugin-args SOFTWARE C:\Windows\System32\sru\srudb.dat

```

# List the tables (-l) in an ese database.  File must not be locked by the OS. If it is use -a (acquire).

```
C:>ese2csv.exe -l C:\Windows\SoftwareDistribution\DataStore\DataStore.edb
C:\Windows\SoftwareDistribution\DataStore\DataStore.edb True
Table MSysObjects has 479 records
Table MSysObjectsShadow has 479 records
Table MSysObjids has 59 records
Table MSysLocales has 8 records
Table tbAUState has 0 records
Table tbCcrDownloadData has 0 records
Table tbComputerInfo has 0 records
Table tbDownloadJob has 0 records
Table tbEula has 0 records
Table tbFiles has 704 records
Table tbHistory has 71 records
Table tbServerConfig has 2 records
Table tbServerCookies has 27 records
Table tbServiceData has 3 records
Table tbScanTransInfo has 2 records
Table tbStoreVersion has 1 records
Table tbUpdateLocalizedProps has 950 records
Table tbUpdates has 2707 records
Table tbHiddenUpdates has 0 records
Table tbLocalUserIds has 1 records
Table tbTimers has 1 records
Table tbSLSData has 4 records
Table tbPerSrvUpdate9116a23d9de3a64d8a4bb43877bcb1b7 has 0 records
Table tbPerSrvUserUpdateData9116a23d9de3a64d8a4bb43877bcb1b7 has 0 records
Table tbPerSrvUpdateb4f4829443e3b643b1709a65bc822c77 has 1964 records
Table tbPerSrvUserUpdateDatab4f4829443e3b643b1709a65bc822c77 has 0 records
Table tbPerSrvUpdate7c8a5e85b4eca34cb0451dfa50104289 has 713 records
Table tbPerSrvUserUpdateData7c8a5e85b4eca34cb0451dfa50104289 has 0 records
```

# Find all *.edb files in c:\ and list their table contents. -r (recurse) all subdirectories and -a (acquire live files) any locked files with FGET before you -l (list tables) list the tables.

```
C:\> ese2csv.exe -ral "C:\*.edb"
TABLE LISTING FOR ESE FILE C:\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb

Table MSysObjects has 858 records
Table MSysObjectsShadow has 858 records
Table MSysObjids has 55 records
Table MSysLocales has 8 records
Table CatalogManager_Properties has 0 records
Table CatalogStorageManager has 1 records
Table SystemIndex_Gthr has 3170 records
Table SystemIndex_GthrPth has 292 records
Table SystemIndex_1_Properties has 225 records
Table SystemIndex_1 has 18 records
<TRUNCATED>
```

# Recursivly (-r) go through every *.edb file in c:\. Acquire (-a) a copy of the locked file. Find the table named tbTimers in one of them and dump (-d) it.

```
C:\Users\Win10Lab\Desktop>ese2csv.exe -rad tbTimers -- "C:\*.edb"
Processing tbTimers

C:\Users\Win10Lab\Desktop>type tbTimers.csv
TimerId,ExpirationTime,IdleOnly,NetworkOnly
b'e763a82909861e4db7cd5668f857f1db',b'31354874915ed501',0,0
```

# Dump the dbTimers table without a plugin specifying the full path. Since no -a is provided the file must not be locked by the OS.

```
C:>ese2csv.exe -d tbTimers -- C:\Windows\SoftwareDistribution\DataStore\DataStore.edb
C:\Windows\SoftwareDistribution\DataStore\DataStore.edb True
Processing tbTimers

C:>type tbTimers.csv
TimerId,ExpirationTime,IdleOnly,NetworkOnly
b'e763a82909861e4db7cd5668f857f1db',b'eaaadd49c85dd501',0,0
```


# Make (-m) a srum plugin template (which requires editing)
```
C:>ese2csv.exe -ma c:\windows\system32\sru\srudb.dat > srudb_plugin.py
```

# After editing the YAML and functions in the new srum plugin use it (-p) to list new friendly table names
```
C:>ese2csv.exe -p srudb_plugin -l srudb.dat
srudb.dat True
Table MSysObjects aka MSysObjects has 262 records
Table MSysObjectsShadow aka MSysObjectsShadow has 262 records
Table MSysObjids aka MSysObjids has 41 records
Table MSysLocales aka MSysLocales has 7 records
Table SruDbIdMapTable aka SruDbIdMapTable has 33946 records
Table SruDbCheckpointTable aka SruDbCheckpointTable has 0 records
Table {D10CA2FE-6FCF-4F6D-848E-B2E99266FA89} aka Application Resources has 122856 records
Table {DD6636C4-8929-4683-974E-22C046A43763} aka Network Connections has 2599 records
Table {FEE4E14F-02A9-4550-B5CE-5FA2DA202E37} aka Energy Usage has 1736 records
Table {973F5D5C-1D90-4944-BE8E-24B94231A174} aka Network Usage has 14445 records
Table {FEE4E14F-02A9-4550-B5CE-5FA2DA202E37}LT aka Energy Usage (Long-Term) has 126 records
Table {D10CA2FE-6FCF-4F6D-848E-B2E99266FA86} aka Application Resource Usage has 3719 records
Table {DA73FB89-2BEA-4DDC-86B8-6E048C6DA477} aka Unknown4 has 13778 records
Table {5C8CF1C7-7257-4F13-B223-970EF5939312} aka Unknown1 has 16982 records
Table {7ACBBAA3-D029-4BE4-9A7A-0885927F1D8F} aka Unknown2 has 1544 records
Table {B6D82AF1-F780-4E17-8077-6CB9AD8A6FC4} aka Unknown3 has 98 records
```
# And dump a table based on its friendly name

```
C:>ese2csv.exe -p srudb_config -d "Network Usage" -- srudb.dat
srudb.dat True
Processing Network Usage
```





























