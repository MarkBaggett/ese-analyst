yaml_config = r"""
lookups:
  LUID_interface_types:
    1: IF_TYPE_OTHER
    10: IF_TYPE_ISO88026_MAN
    100: IF_TYPE_VOICE_EM
    101: IF_TYPE_VOICE_FXO
    102: IF_TYPE_VOICE_FXS
    103: IF_TYPE_VOICE_ENCAP
    104: IF_TYPE_VOICE_OVERIP
    105: IF_TYPE_ATM_DXI
    106: IF_TYPE_ATM_FUNI
    107: IF_TYPE_ATM_IMA
    108: IF_TYPE_PPPMULTILINKBUNDLE
    109: IF_TYPE_IPOVER_CDLC
    11: IF_TYPE_STARLAN
    110: IF_TYPE_IPOVER_CLAW
    111: IF_TYPE_STACKTOSTACK
    112: IF_TYPE_VIRTUALIPADDRESS
    113: IF_TYPE_MPC
    114: IF_TYPE_IPOVER_ATM
    115: IF_TYPE_ISO88025_FIBER
    116: IF_TYPE_TDLC
    117': IF_TYPE_GIGABITETHERNET
    118: IF_TYPE_HDLC
    119: IF_TYPE_LAP_F
    12: IF_TYPE_PROTEON_10MBIT
    120: IF_TYPE_V37
    121: IF_TYPE_X25_MLP
    122: IF_TYPE_X25_HUNTGROUP
    123: IF_TYPE_TRANSPHDLC
    124: IF_TYPE_INTERLEAVE
    125: IF_TYPE_FAST
    126: IF_TYPE_IP
    127: IF_TYPE_DOCSCABLE_MACLAYER
    128: IF_TYPE_DOCSCABLE_DOWNSTREAM
    129: IF_TYPE_DOCSCABLE_UPSTREAM
    13: IF_TYPE_PROTEON_80MBIT
    130: IF_TYPE_A12MPPSWITCH
    131: IF_TYPE_TUNNEL
    132: IF_TYPE_COFFEE
    133: IF_TYPE_CES
    134: IF_TYPE_ATM_SUBINTERFACE
    135: IF_TYPE_L2_VLAN
    136: IF_TYPE_L3_IPVLAN
    137: IF_TYPE_L3_IPXVLAN
    138: IF_TYPE_DIGITALPOWERLINE
    139: IF_TYPE_MEDIAMAILOVERIP
    14: IF_TYPE_HYPERCHANNEL
    140: IF_TYPE_DTM
    141: IF_TYPE_DCN
    142: IF_TYPE_IPFORWARD
    143: IF_TYPE_MSDSL
    144: IF_TYPE_IEEE1394
    145: IF_TYPE_RECEIVE_ONLY
    15: IF_TYPE_FDDI
    16: IF_TYPE_LAP_B
    17: IF_TYPE_SDLC
    18: IF_TYPE_DS1
    19: IF_TYPE_E1
    2: IF_TYPE_REGULAR_1822
    20: IF_TYPE_BASIC_ISDN
    21: IF_TYPE_PRIMARY_ISDN
    22: IF_TYPE_PROP_POINT2POINT_SERIAL
    23: IF_TYPE_PPP
    24: IF_TYPE_SOFTWARE_LOOPBACK
    25: IF_TYPE_EON
    26: IF_TYPE_ETHERNET_3MBIT
    27: IF_TYPE_NSIP
    28: IF_TYPE_SLIP
    29: IF_TYPE_ULTRA
    3: IF_TYPE_HDH_1822
    30: IF_TYPE_DS3
    31: IF_TYPE_SIP
    32: IF_TYPE_FRAMERELAY
    33: IF_TYPE_RS232
    34: IF_TYPE_PARA
    35: IF_TYPE_ARCNET
    36: IF_TYPE_ARCNET_PLUS
    37: IF_TYPE_ATM
    38: IF_TYPE_MIO_X25
    39: IF_TYPE_SONET
    4: IF_TYPE_DDN_X25
    40: IF_TYPE_X25_PLE
    41: IF_TYPE_ISO88022_LLC
    42: IF_TYPE_LOCALTALK
    43: IF_TYPE_SMDS_DXI
    44: IF_TYPE_FRAMERELAY_SERVICE
    45: IF_TYPE_V35
    46: IF_TYPE_HSSI
    47: IF_TYPE_HIPPI
    48: IF_TYPE_MODEM
    49: IF_TYPE_AAL5
    5: IF_TYPE_RFC877_X25
    50: IF_TYPE_SONET_PATH
    51: IF_TYPE_SONET_VT
    52: IF_TYPE_SMDS_ICIP
    53: IF_TYPE_PROP_VIRTUAL
    54: IF_TYPE_PROP_MULTIPLEXOR
    55: IF_TYPE_IEEE80212
    56: IF_TYPE_FIBRECHANNEL
    57: IF_TYPE_HIPPIINTERFACE
    58: IF_TYPE_FRAMERELAY_INTERCONNECT
    59: IF_TYPE_AFLANE_8023
    6: IF_TYPE_ETHERNET_CSMACD
    60: IF_TYPE_AFLANE_8025
    61: IF_TYPE_CCTEMUL
    62: IF_TYPE_FASTETHER
    63: IF_TYPE_ISDN
    64: IF_TYPE_V11
    65: IF_TYPE_V36
    66: IF_TYPE_G703_64K
    67: IF_TYPE_G703_2MB
    68: IF_TYPE_QLLC
    69: IF_TYPE_FASTETHER_FX
    7: IF_TYPE_IS088023_CSMACD
    70: IF_TYPE_CHANNEL
    71: IF_TYPE_IEEE80211
    72: IF_TYPE_IBM370PARCHAN
    73: IF_TYPE_ESCON
    74: IF_TYPE_DLSW
    75: IF_TYPE_ISDN_S
    76: IF_TYPE_ISDN_U
    77: IF_TYPE_LAP_D
    78: IF_TYPE_IPSWITCH
    79: IF_TYPE_RSRB
    8: IF_TYPE_ISO88024_TOKENBUS
    80: IF_TYPE_ATM_LOGICAL
    81: IF_TYPE_DS0
    82: IF_TYPE_DS0_BUNDLE
    83: IF_TYPE_BSC
    84: IF_TYPE_ASYNC
    85: IF_TYPE_CNR
    86: IF_TYPE_ISO88025R_DTR
    87: IF_TYPE_EPLRS
    88: IF_TYPE_ARAP
    89: IF_TYPE_PROP_CNLS
    9: IF_TYPE_ISO88025_TOKENRING
    90: IF_TYPE_HOSTPAD
    91: IF_TYPE_TERMPAD
    92: IF_TYPE_FRAMERELAY_MPI
    93: IF_TYPE_X213
    94: IF_TYPE_ADSL
    95: IF_TYPE_RADSL
    96: IF_TYPE_SDSL
    97: IF_TYPE_VDSL
    98: IF_TYPE_ISO88025_CRFPRINT
    99: IF_TYPE_MYRINET
  known_sids:
    S-1-0: ' Null Authority'
    S-1-0-0: ' Nobody'
    S-1-1: ' World Authority'
    S-1-1-0: ' Everyone'
    S-1-16-0: ' Untrusted Mandatory Level '
    S-1-16-12288: ' High Mandatory Level '
    S-1-16-16384: ' System Mandatory Level '
    S-1-16-20480: ' Protected Process Mandatory Level '
    S-1-16-28672: ' Secure Process Mandatory Level '
    S-1-16-4096: ' Low Mandatory Level '
    S-1-16-8192: ' Medium Mandatory Level '
    S-1-16-8448: ' Medium Plus Mandatory Level '
    S-1-2: ' Local Authority'
    S-1-2-0: ' Local '
    S-1-2-1: ' Console Logon '
    S-1-3: ' Creator Authority'
    S-1-3-0: ' Creator Owner'
    S-1-3-1: ' Creator Group'
    S-1-3-2: ' Creator Owner Server'
    S-1-3-3: ' Creator Group Server'
    S-1-4: ' Non-unique Authority'
    S-1-5: ' NT Authority'
    S-1-5-1: ' Dialup'
    S-1-5-10: ' Principal Self'
    S-1-5-11: ' Authenticated Users'
    S-1-5-12: ' Restricted Code'
    S-1-5-13: ' Terminal Server Users'
    S-1-5-14: ' Remote Interactive Logon '
    S-1-5-15: ' This Organization '
    S-1-5-17: ' This Organization '
    S-1-5-18: ' Local System'
    S-1-5-19: ' NT Authority'
    S-1-5-2: ' Network'
    S-1-5-20: ' NT Authority'
    S-1-5-3: ' Batch'
    S-1-5-32-544: ' Administrators'
    S-1-5-32-545: ' Users'
    S-1-5-32-546: ' Guests'
    S-1-5-32-547: ' Power Users'
    S-1-5-32-548: ' Account Operators'
    S-1-5-32-549: ' Server Operators'
    S-1-5-32-550: ' Print Operators'
    S-1-5-32-551: ' Backup Operators'
    S-1-5-32-552: ' Replicators'
    S-1-5-32-554: ' BUILTIN\Pre-Windows 2000 Compatible Access'
    S-1-5-32-555: ' BUILTIN\Remote Desktop Users'
    S-1-5-32-556: ' BUILTIN\Network Configuration Operators'
    S-1-5-32-557: ' BUILTIN\Incoming Forest Trust Builders'
    S-1-5-32-558: ' BUILTIN\Performance Monitor Users'
    S-1-5-32-559: ' BUILTIN\Performance Log Users'
    S-1-5-32-560: ' BUILTIN\Windows Authorization Access Group'
    S-1-5-32-561: ' BUILTIN\Terminal Server License Servers'
    S-1-5-32-562: ' BUILTIN\Distributed COM Users'
    S-1-5-32-569: ' BUILTIN\Cryptographic Operators'
    S-1-5-32-573: ' BUILTIN\Event Log Readers '
    S-1-5-32-574: ' BUILTIN\Certificate Service DCOM Access '
    S-1-5-32-575: ' BUILTIN\RDS Remote Access Servers'
    S-1-5-32-576: ' BUILTIN\RDS Endpoint Servers'
    S-1-5-32-577: ' BUILTIN\RDS Management Servers'
    S-1-5-32-578: ' BUILTIN\Hyper-V Administrators'
    S-1-5-32-579: ' BUILTIN\Access Control Assistance Operators'
    S-1-5-32-580: ' BUILTIN\Remote Management Users'
    S-1-5-4: ' Interactive'
    S-1-5-6: ' Service'
    S-1-5-64-10: ' NTLM Authentication '
    S-1-5-64-14: ' SChannel Authentication '
    S-1-5-64-21: ' Digest Authentication '
    S-1-5-7: ' Anonymous'
    S-1-5-8: ' Proxy'
    S-1-5-80: ' NT Service '
    S-1-5-80-0: ' All Services '
    S-1-5-83-0: ' NT VIRTUAL MACHINE\Virtual Machines'
    S-1-5-9: ' Enterprise Domain Controllers'
  numbers:
    0: zero
    1: one
table_references:
  app_id:
    key: IdIndex
    table: SruDbIdMapTable
    value:
    - IdType
    - IdBlob
tables:
  MSysLocales:
    fields:
      Key:
        format: None
        friendly name: Key
        ignore: 'no'
      Type:
        format: None
        friendly name: Type
        ignore: 'no'
      iValue:
        format: None
        friendly name: iValue
        ignore: 'no'
    ignore: 'yes'
    name: MSysLocales
  MSysObjects:
    fields:
      CallbackData:
        format: None
        friendly name: CallbackData
        ignore: 'no'
      CallbackDependencies:
        format: None
        friendly name: CallbackDependencies
        ignore: 'no'
      ColtypOrPgnoFDP:
        format: None
        friendly name: ColtypOrPgnoFDP
        ignore: 'no'
      ConditionalColumns:
        format: None
        friendly name: ConditionalColumns
        ignore: 'no'
      DefaultValue:
        format: None
        friendly name: DefaultValue
        ignore: 'no'
      Flags:
        format: None
        friendly name: Flags
        ignore: 'no'
      Id:
        format: None
        friendly name: Id
        ignore: 'no'
      KeyFldIDs:
        format: None
        friendly name: KeyFldIDs
        ignore: 'no'
      KeyMost:
        format: None
        friendly name: KeyMost
        ignore: 'no'
      LCMapFlags:
        format: None
        friendly name: LCMapFlags
        ignore: 'no'
      LVChunkMax:
        format: None
        friendly name: LVChunkMax
        ignore: 'no'
      LocaleName:
        format: None
        friendly name: LocaleName
        ignore: 'no'
      Name:
        format: None
        friendly name: Name
        ignore: 'no'
      ObjidTable:
        format: None
        friendly name: ObjidTable
        ignore: 'no'
      PagesOrLocale:
        format: None
        friendly name: PagesOrLocale
        ignore: 'no'
      RecordOffset:
        format: None
        friendly name: RecordOffset
        ignore: 'no'
      RootFlag:
        format: None
        friendly name: RootFlag
        ignore: 'no'
      SeparateLV:
        format: None
        friendly name: SeparateLV
        ignore: 'no'
      SortID:
        format: None
        friendly name: SortID
        ignore: 'no'
      SpaceDeferredLVHints:
        format: None
        friendly name: SpaceDeferredLVHints
        ignore: 'no'
      SpaceHints:
        format: None
        friendly name: SpaceHints
        ignore: 'no'
      SpaceUsage:
        format: None
        friendly name: SpaceUsage
        ignore: 'no'
      Stats:
        format: None
        friendly name: Stats
        ignore: 'no'
      TemplateTable:
        format: None
        friendly name: TemplateTable
        ignore: 'no'
      TupleLimits:
        format: None
        friendly name: TupleLimits
        ignore: 'no'
      Type:
        format: None
        friendly name: Type
        ignore: 'no'
      VarSegMac:
        format: None
        friendly name: VarSegMac
        ignore: 'no'
      Version:
        format: None
        friendly name: Version
        ignore: 'no'
    ignore: 'yes'
    name: MSysObjects
  MSysObjectsShadow:
    fields:
      CallbackData:
        format: None
        friendly name: CallbackData
        ignore: 'no'
      CallbackDependencies:
        format: None
        friendly name: CallbackDependencies
        ignore: 'no'
      ColtypOrPgnoFDP:
        format: None
        friendly name: ColtypOrPgnoFDP
        ignore: 'no'
      ConditionalColumns:
        format: None
        friendly name: ConditionalColumns
        ignore: 'no'
      DefaultValue:
        format: None
        friendly name: DefaultValue
        ignore: 'no'
      Flags:
        format: None
        friendly name: Flags
        ignore: 'no'
      Id:
        format: None
        friendly name: Id
        ignore: 'no'
      KeyFldIDs:
        format: None
        friendly name: KeyFldIDs
        ignore: 'no'
      KeyMost:
        format: None
        friendly name: KeyMost
        ignore: 'no'
      LCMapFlags:
        format: None
        friendly name: LCMapFlags
        ignore: 'no'
      LVChunkMax:
        format: None
        friendly name: LVChunkMax
        ignore: 'no'
      LocaleName:
        format: None
        friendly name: LocaleName
        ignore: 'no'
      Name:
        format: None
        friendly name: Name
        ignore: 'no'
      ObjidTable:
        format: None
        friendly name: ObjidTable
        ignore: 'no'
      PagesOrLocale:
        format: None
        friendly name: PagesOrLocale
        ignore: 'no'
      RecordOffset:
        format: None
        friendly name: RecordOffset
        ignore: 'no'
      RootFlag:
        format: None
        friendly name: RootFlag
        ignore: 'no'
      SeparateLV:
        format: None
        friendly name: SeparateLV
        ignore: 'no'
      SortID:
        format: None
        friendly name: SortID
        ignore: 'no'
      SpaceDeferredLVHints:
        format: None
        friendly name: SpaceDeferredLVHints
        ignore: 'no'
      SpaceHints:
        format: None
        friendly name: SpaceHints
        ignore: 'no'
      SpaceUsage:
        format: None
        friendly name: SpaceUsage
        ignore: 'no'
      Stats:
        format: None
        friendly name: Stats
        ignore: 'no'
      TemplateTable:
        format: None
        friendly name: TemplateTable
        ignore: 'no'
      TupleLimits:
        format: None
        friendly name: TupleLimits
        ignore: 'no'
      Type:
        format: None
        friendly name: Type
        ignore: 'no'
      VarSegMac:
        format: None
        friendly name: VarSegMac
        ignore: 'no'
      Version:
        format: None
        friendly name: Version
        ignore: 'no'
    ignore: 'yes'
    name: MSysObjectsShadow
  MSysObjids:
    fields:
      objid:
        format: None
        friendly name: objid
        ignore: 'no'
      objidTable:
        format: None
        friendly name: objidTable
        ignore: 'no'
      type:
        format: None
        friendly name: type
        ignore: 'no'
    ignore: 'yes'
    name: MSysObjids
  SruDbCheckpointTable:
    fields:
      CheckpointId:
        format: None
        friendly name: CheckpointId
        ignore: 'no'
      NextIncId:
        format: None
        friendly name: NextIncId
        ignore: 'no'
      ProviderId:
        format: None
        friendly name: ProviderId
        ignore: 'no'
      RecordSet:
        format: None
        friendly name: RecordSet
        ignore: 'no'
      SeqNumber:
        format: None
        friendly name: SeqNumber
        ignore: 'no'
    ignore: 'no'
    name: SruDbCheckpointTable
  SruDbIdMapTable:
    fields:
      IdBlob:
        format: None
        friendly name: IdBlob
        ignore: 'no'
      IdIndex:
        format: None
        friendly name: IdIndex
        ignore: 'no'
      IdType:
        format: None
        friendly name: IdType
        ignore: 'no'
    ignore: 'no'
    name: SruDbIdMapTable
  '{5C8CF1C7-7257-4F13-B223-970EF5939312}':
    fields:
      AppId:
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AudioInS:
        format: None
        friendly name: AudioInS
        ignore: 'no'
      AudioInTimeline:
        format: None
        friendly name: AudioInTimeline
        ignore: 'no'
      AudioOutS:
        format: None
        friendly name: AudioOutS
        ignore: 'no'
      AudioOutTimeline:
        format: None
        friendly name: AudioOutTimeline
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      CompDirtiedS:
        format: None
        friendly name: CompDirtiedS
        ignore: 'no'
      CompDirtiedTimeline:
        format: None
        friendly name: CompDirtiedTimeline
        ignore: 'no'
      CompPropagatedS:
        format: None
        friendly name: CompPropagatedS
        ignore: 'no'
      CompPropagatedTimeline:
        format: None
        friendly name: CompPropagatedTimeline
        ignore: 'no'
      CompRenderedS:
        format: None
        friendly name: CompRenderedS
        ignore: 'no'
      CompRenderedTimeline:
        format: None
        friendly name: CompRenderedTimeline
        ignore: 'no'
      CpuTimeline:
        format: None
        friendly name: CpuTimeline
        ignore: 'no'
      Cycles:
        format: None
        friendly name: Cycles
        ignore: 'no'
      CyclesAttr:
        format: None
        friendly name: CyclesAttr
        ignore: 'no'
      CyclesAttrBreakdown:
        format: None
        friendly name: CyclesAttrBreakdown
        ignore: 'no'
      CyclesBreakdown:
        format: None
        friendly name: CyclesBreakdown
        ignore: 'no'
      CyclesWOB:
        format: None
        friendly name: CyclesWOB
        ignore: 'no'
      CyclesWOBBreakdown:
        format: None
        friendly name: CyclesWOBBreakdown
        ignore: 'no'
      DiskRaw:
        format: None
        friendly name: DiskRaw
        ignore: 'no'
      DiskTimeline:
        format: None
        friendly name: DiskTimeline
        ignore: 'no'
      DisplayRequiredS:
        format: None
        friendly name: DisplayRequiredS
        ignore: 'no'
      DisplayRequiredTimeline:
        format: None
        friendly name: DisplayRequiredTimeline
        ignore: 'no'
      DurationMS:
        format: None
        friendly name: DurationMS
        ignore: 'no'
      EndTime:
        format: None
        friendly name: EndTime
        ignore: 'no'
      Flags:
        format: None
        friendly name: Flags
        ignore: 'no'
      InFocusS:
        format: None
        friendly name: InFocusS
        ignore: 'no'
      InFocusTimeline:
        format: None
        friendly name: InFocusTimeline
        ignore: 'no'
      KeyboardInputS:
        format: None
        friendly name: KeyboardInputS
        ignore: 'no'
      KeyboardInputTimeline:
        format: None
        friendly name: KeyboardInputTimeline
        ignore: 'no'
      MBBBytesRaw:
        format: None
        friendly name: MBBBytesRaw
        ignore: 'no'
      MBBTailRaw:
        format: None
        friendly name: MBBTailRaw
        ignore: 'no'
      MBBTimeline:
        format: None
        friendly name: MBBTimeline
        ignore: 'no'
      MouseInputS:
        format: None
        friendly name: MouseInputS
        ignore: 'no'
      NetworkBytesRaw:
        format: None
        friendly name: NetworkBytesRaw
        ignore: 'no'
      NetworkTailRaw:
        format: None
        friendly name: NetworkTailRaw
        ignore: 'no'
      NetworkTimeline:
        format: None
        friendly name: NetworkTimeline
        ignore: 'no'
      PSMForegroundS:
        format: None
        friendly name: PSMForegroundS
        ignore: 'no'
      SpanMS:
        format: None
        friendly name: SpanMS
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      TimelineEnd:
        format: None
        friendly name: TimelineEnd
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: User Info
        ignore: 'no'
      UserInputS:
        format: None
        friendly name: UserInputS
        ignore: 'no'
      UserInputTimeline:
        format: None
        friendly name: UserInputTimeline
        ignore: 'no'
    ignore: 'no'
    name: 'Unknown1'
  '{7ACBBAA3-D029-4BE4-9A7A-0885927F1D8F}':
    fields:
      AppId:
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      EndTime:
        format: None
        friendly name: EndTime
        ignore: 'no'
      Flags:
        format: None
        friendly name: Flags
        ignore: 'no'
      StartTime:
        format: None
        friendly name: StartTime
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      Usage:
        format: None
        friendly name: Usage
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: User Info
        ignore: 'no'
    ignore: 'no'
    name: 'Unknown2'
  '{973F5D5C-1D90-4944-BE8E-24B94231A174}':
    fields:
      AppId:        
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      BytesRecvd:
        format: None
        friendly name: BytesRecvd
        ignore: 'no'
      BytesSent:
        format: None
        friendly name: BytesSent
        ignore: 'no'
      InterfaceLuid:
        format: function:lookup_luid
        friendly name: InterfaceLuid
        ignore: 'no'
      L2ProfileFlags:
        format: None
        friendly name: L2ProfileFlags
        ignore: 'no'
      L2ProfileId:
        format: function:lookup_wireless
        friendly name: L2ProfileId
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: User Info
        ignore: 'no'
    ignore: 'no'
    name: Network Usage
  '{B6D82AF1-F780-4E17-8077-6CB9AD8A6FC4}':
    fields:
      AppId:
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      Energy Data:
        format: None
        friendly name: Energy Data
        ignore: 'no'
      Metadata:
        format: None
        friendly name: Metadata
        ignore: 'no'
      Tag:
        format: None
        friendly name: Tag
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: User Info
        ignore: 'no'
    ignore: 'no'
    name: 'Unknown3'
  '{D10CA2FE-6FCF-4F6D-848E-B2E99266FA86}':
    fields:
      AppId:        
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      NetworkType:
        format: None
        friendly name: NetworkType
        ignore: 'no'
      NotificationType:
        format: None
        friendly name: NotificationType
        ignore: 'no'
      PayloadSize:
        format: None
        friendly name: PayloadSize
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: User Info
        ignore: 'no'
    ignore: 'no'
    name: Application Resource Usage
  '{D10CA2FE-6FCF-4F6D-848E-B2E99266FA89}':
    fields:
      AppId:
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      BackgroundBytesRead:
        format: None
        friendly name: BackgroundBytesRead
        ignore: 'no'
      BackgroundBytesWritten:
        format: None
        friendly name: BackgroundBytesWritten
        ignore: 'no'
      BackgroundContextSwitches:
        format: None
        friendly name: BackgroundContextSwitches
        ignore: 'no'
      BackgroundCycleTime:
        format: None
        friendly name: BackgroundCycleTime
        ignore: 'no'
      BackgroundNumReadOperations:
        format: None
        friendly name: BackgroundNumReadOperations
        ignore: 'no'
      BackgroundNumWriteOperations:
        format: None
        friendly name: BackgroundNumWriteOperations
        ignore: 'no'
      BackgroundNumberOfFlushes:
        format: None
        friendly name: BackgroundNumberOfFlushes
        ignore: 'no'
      FaceTime:
        format: None
        friendly name: FaceTime
        ignore: 'no'
      ForegroundBytesRead:
        format: None
        friendly name: ForegroundBytesRead
        ignore: 'no'
      ForegroundBytesWritten:
        format: None
        friendly name: ForegroundBytesWritten
        ignore: 'no'
      ForegroundContextSwitches:
        format: None
        friendly name: ForegroundContextSwitches
        ignore: 'no'
      ForegroundCycleTime:
        format: None
        friendly name: ForegroundCycleTime
        ignore: 'no'
      ForegroundNumReadOperations:
        format: None
        friendly name: ForegroundNumReadOperations
        ignore: 'no'
      ForegroundNumWriteOperations:
        format: None
        friendly name: ForegroundNumWriteOperations
        ignore: 'no'
      ForegroundNumberOfFlushes:
        format: None
        friendly name: ForegroundNumberOfFlushes
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: UserId
        ignore: 'no'
    ignore: 'no'
    name: 'Application Resources'
  '{DA73FB89-2BEA-4DDC-86B8-6E048C6DA477}':
    fields:
      AppId:
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      BinaryData:
        format: None
        friendly name: BinaryData
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: User Info
        ignore: 'no'
    ignore: 'no'
    name: 'Unknown4'
  '{DD6636C4-8929-4683-974E-22C046A43763}':
    fields:
      AppId:
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      ConnectStartTime:
        format: None
        friendly name: ConnectStartTime
        ignore: 'no'
      ConnectedTime:
        format: None
        friendly name: ConnectedTime
        ignore: 'no'
      InterfaceLuid:
        format: None
        friendly name: InterfaceLuid
        ignore: 'no'
      L2ProfileFlags:
        format: None
        friendly name: L2ProfileFlags
        ignore: 'no'
      L2ProfileId:
        format: function:lookup_wireless
        friendly name: L2ProfileId
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: User Info
        ignore: 'no'
    ignore: 'no'
    name: 'Network Connections'
  '{FEE4E14F-02A9-4550-B5CE-5FA2DA202E37}':
    fields:
      AppId:
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      ChargeLevel:
        format: None
        friendly name: ChargeLevel
        ignore: 'no'
      ConfigurationHash:
        format: None
        friendly name: ConfigurationHash
        ignore: 'no'
      CycleCount:
        format: None
        friendly name: CycleCount
        ignore: 'no'
      DesignedCapacity:
        format: None
        friendly name: DesignedCapacity
        ignore: 'no'
      EventTimestamp:
        format: None
        friendly name: EventTimestamp
        ignore: 'no'
      FullChargedCapacity:
        format: None
        friendly name: FullChargedCapacity
        ignore: 'no'
      StateTransition:
        format: None
        friendly name: StateTransition
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: User Info
        ignore: 'no'
    ignore: 'no'
    name: Energy Usage
  '{FEE4E14F-02A9-4550-B5CE-5FA2DA202E37}LT':
    fields:
      ActiveAcTime:
        format: None
        friendly name: ActiveAcTime
        ignore: 'no'
      ActiveDcTime:
        format: None
        friendly name: ActiveDcTime
        ignore: 'no'
      ActiveDischargeTime:
        format: None
        friendly name: ActiveDischargeTime
        ignore: 'no'
      ActiveEnergy:
        format: None
        friendly name: ActiveEnergy
        ignore: 'no'
      AppId:
        format: function:get_app_id
        friendly name: Application
        ignore: 'no'
      AutoIncId:
        format: None
        friendly name: AutoIncId
        ignore: 'no'
      ConfigurationHash:
        format: None
        friendly name: ConfigurationHash
        ignore: 'no'
      CsAcTime:
        format: None
        friendly name: CsAcTime
        ignore: 'no'
      CsDcTime:
        format: None
        friendly name: CsDcTime
        ignore: 'no'
      CsDischargeTime:
        format: None
        friendly name: CsDischargeTime
        ignore: 'no'
      CsEnergy:
        format: None
        friendly name: CsEnergy
        ignore: 'no'
      CycleCount:
        format: None
        friendly name: CycleCount
        ignore: 'no'
      DesignedCapacity:
        format: None
        friendly name: DesignedCapacity
        ignore: 'no'
      FullChargedCapacity:
        format: None
        friendly name: FullChargedCapacity
        ignore: 'no'
      TimeStamp:
        format: None
        friendly name: TimeStamp
        ignore: 'no'
      UserId:
        format: function:get_app_id
        friendly name: User Info
        ignore: 'no'
    ignore: 'no'
    name: Energy Usage (Long-Term)


"""
import struct
import codecs
import pathlib
import sys
from Registry.Registry import Registry

def load_registry_sids(reg_file):
    """Given Software hive find SID usernames"""
    sids = {}
    profile_key = r"Microsoft\Windows NT\CurrentVersion\ProfileList"
    tgt_value = "ProfileImagePath"
    try:
        reg_handle = Registry(reg_file)
        key_handle = reg_handle.open(profile_key)
        for eachsid in key_handle.subkeys():
            sids_path = eachsid.value(tgt_value).value()
            sids[eachsid.name()] = sids_path.split("\\")[-1]
    except Exception as e:
        print(str(e))
        return {}
    print("Loaded SIDS", sids)
    return sids

def load_interfaces(reg_file):
    try:
        reg_handle = Registry(reg_file)
        int_keys = reg_handle.open('Microsoft\\WlanSvc\\Interfaces')
    except Exception as e:
        print("I could not open the specified SOFTWARE registry key. It is usually located in \Windows\system32\config but is locked by the OS.")
        print("Error : ", str(e))
        return {}   
    profile_lookup = {}
    for eachinterface in int_keys.subkeys():
        if len(eachinterface.subkeys())==0:
            continue
        for eachprofile in eachinterface.subkey("Profiles").subkeys():
            profileid = [x.value() for x in eachprofile.values() if x.name()=="ProfileIndex"][0]
            metadata = eachprofile.subkey("MetaData").values()
            for eachvalue in metadata:
                if eachvalue.name()=="Channel Hints":
                    channelhintraw = eachvalue.value()
                    hintlength = struct.unpack("I", channelhintraw[0:4])[0]
                    name = channelhintraw[4:hintlength+4] 
                    profile_lookup[str(profileid)] = name
    return profile_lookup

wireless_lookup = {}
def lookup_wireless(wireless_id):
    return wireless_lookup.get(str(wireless_id),"")

registry_sids = {}
def plugin_init(ese_database):
    global wireless_lookup
    global registry_sids
    #table_names = " ".join([x.name for x in ese_database.tables])
    #print("Received Arguments", args)
    if args and args[0].lower() == "live":
        live_path = pathlib.Path("c:\\Windows\\System32\\Config\\SOFTWARE")
        if live_path.exists():
            regpath = extract_live_file(live_path)
            wireless_lookup = load_interfaces(str(regpath))
            registry_sids = load_registry_sids(str(regpath))
        else:
            print("Unable to find the SOFTWARE registry on this system.")
    elif args and pathlib.Path(args[0]).exists():
        wireless_lookup = load_interfaces(args[0])
        registry_sids = load_registry_sids(str(args[0]))
    elif args:
        print(f"Registry file {str(args[0])} not found.")
    #print("Plugin Initialized for ", table_names)
    # Setup any data structures required for yaml function calls
    return None

def plugin_modify_header(list_of_headers, table_name):
    #print("Plugin Processing headers", list_of_headers)
    # Modify headers as needed before commit to file
    return list_of_headers

def plugin_modify_row(list_of_row_values, table_name):
    #print("Plugin Processing Row", list_of_row_values)
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
    if sid_str in registry_sids:
        sid_name = registry_sids.get(sid_str)
    else:
        sid_name = lookup("known_sids",sid_str)
    return "{} ({})".format(sid_str,sid_name)

def get_app_id(data):
    app_record = lookup("app_id", data)
    if not app_record:
        return "Application ID lookup failed."
    app_type, app_value = app_record  
    if app_type == 3:
        data = BinarySIDtoStringSID(app_value)
    else:
        data = blob_to_string(app_value)
    return data

def lookup_luid(luidval): 
    inttype = struct.unpack(">H6B", codecs.decode(format(luidval,'016x'),'hex'))[0] 
    return lookup("LUID_interface_types",inttype)
