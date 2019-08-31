yaml_config = r"""
lookups:
  numbers:
    0: zero
    1: one
tables:
  BookSetMembers:
    fields:
      MemberId:
        format: None
        friendly name: MemberId
        ignore: 'no'
      Name:
        format: None
        friendly name: Name
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Type:
        format: None
        friendly name: Type
        ignore: 'no'
    ignore: 'no'
    name: BookSetMembers
  BookSetShareRights:
    fields:
      AccountId:
        format: None
        friendly name: AccountId
        ignore: 'no'
      BookSetId:
        format: None
        friendly name: BookSetId
        ignore: 'no'
      ErrorCode:
        format: None
        friendly name: ErrorCode
        ignore: 'no'
      MemberId:
        format: None
        friendly name: MemberId
        ignore: 'no'
      Permissions:
        format: None
        friendly name: Permissions
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SyncStatus:
        format: None
        friendly name: SyncStatus
        ignore: 'no'
    ignore: 'no'
    name: BookSetShareRights
  BookSets:
    fields:
      AccountId:
        format: None
        friendly name: AccountId
        ignore: 'no'
      FullyAppliedSyncToken:
        format: None
        friendly name: FullyAppliedSyncToken
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      IsHydrationNeeded:
        format: None
        friendly name: IsHydrationNeeded
        ignore: 'no'
      IsPushAllowed:
        format: None
        friendly name: IsPushAllowed
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      Name:
        format: None
        friendly name: Name
        ignore: 'no'
      OpenedBookId:
        format: None
        friendly name: OpenedBookId
        ignore: 'no'
      OwnerId:
        format: None
        friendly name: OwnerId
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SyncId:
        format: None
        friendly name: SyncId
        ignore: 'no'
      SyncToken:
        format: None
        friendly name: SyncToken
        ignore: 'no'
      SyncTokenVersion:
        format: None
        friendly name: SyncTokenVersion
        ignore: 'no'
      UpdatedDate:
        format: None
        friendly name: UpdatedDate
        ignore: 'no'
    ignore: 'no'
    name: BookSets
  GenericAutoSuggestStorage:
    fields:
      DateAccessed:
        format: None
        friendly name: DateAccessed
        ignore: 'no'
      DateUpdated:
        format: None
        friendly name: DateUpdated
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      IsShaGenerated:
        format: None
        friendly name: IsShaGenerated
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      Key:
        format: None
        friendly name: Key
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      URL:
        format: None
        friendly name: URL
        ignore: 'no'
      UseCount:
        format: None
        friendly name: UseCount
        ignore: 'no'
      Value:
        format: None
        friendly name: Value
        ignore: 'no'
    ignore: 'no'
    name: GenericAutoSuggestStorage
  PinningRules:
    fields:
      Host:
        format: None
        friendly name: Host
        ignore: 'no'
      Port:
        format: None
        friendly name: Port
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Scheme:
        format: None
        friendly name: Scheme
        ignore: 'no'
      UriHash:
        format: None
        friendly name: UriHash
        ignore: 'no'
    ignore: 'no'
    name: PinningRules
  UserDataSourceInfo:
    fields:
      DataSourceId:
        format: None
        friendly name: DataSourceId
        ignore: 'no'
      DataSourceType:
        format: None
        friendly name: DataSourceType
        ignore: 'no'
      LastCommunicationUTC:
        format: None
        friendly name: LastCommunicationUTC
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
    ignore: 'no'
    name: UserDataSourceInfo
  WebsitePermissions:
    fields:
      FullscreenPermissionStatus:
        format: None
        friendly name: FullscreenPermissionStatus
        ignore: 'no'
      LocationPermissionStatus:
        format: None
        friendly name: LocationPermissionStatus
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      URL:
        format: None
        friendly name: URL
        ignore: 'no'
      UrlHash:
        format: None
        friendly name: UrlHash
        ignore: 'no'
    ignore: 'no'
    name: WebsitePermissions
  AutoFormFillAddressStorage:
    fields:
      AddressLine1:
        format: None
        friendly name: AddressLine1
        ignore: 'no'
      AddressLine2:
        format: None
        friendly name: AddressLine2
        ignore: 'no'
      AddressLine3:
        format: None
        friendly name: AddressLine3
        ignore: 'no'
      AddressType:
        format: None
        friendly name: AddressType
        ignore: 'no'
      CedexCode:
        format: None
        friendly name: CedexCode
        ignore: 'no'
      City:
        format: None
        friendly name: City
        ignore: 'no'
      Country:
        format: None
        friendly name: Country
        ignore: 'no'
      CountryCode:
        format: None
        friendly name: CountryCode
        ignore: 'no'
      DateAccessed:
        format: function:file_timestamp
        friendly name: DateAccessed
        ignore: 'no'
      DateAdded:
        format: function:file_timestamp
        friendly name: DateAdded
        ignore: 'no'
      DateUpdated:
        format: function:file_timestamp
        friendly name: DateUpdated
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      Locality:
        format: None
        friendly name: Locality
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      State:
        format: None
        friendly name: State
        ignore: 'no'
      UseCount:
        format: None
        friendly name: UseCount
        ignore: 'no'
      ZipCode:
        format: None
        friendly name: ZipCode
        ignore: 'no'
    ignore: 'no'
    name: AutoFormFillAddressStorage
  AutoFormFillPaymentStorage:
    fields:
      AccountType:
        format: None
        friendly name: AccountType
        ignore: 'no'
      AddressItemGuid:
        format: None
        friendly name: AddressItemGuid
        ignore: 'no'
      AssociatedAccount:
        format: None
        friendly name: AssociatedAccount
        ignore: 'no'
      CardHolderFirstName:
        format: None
        friendly name: CardHolderFirstName
        ignore: 'no'
      CardHolderLastName:
        format: None
        friendly name: CardHolderLastName
        ignore: 'no'
      CardHolderMiddleName:
        format: None
        friendly name: CardHolderMiddleName
        ignore: 'no'
      CardType:
        format: None
        friendly name: CardType
        ignore: 'no'
      CreditCardNumber:
        format: None
        friendly name: CreditCardNumber
        ignore: 'no'
      DateAccessed:
        format: function:file_timestamp
        friendly name: DateAccessed
        ignore: 'no'
      DateAdded:
        format: function:file_timestamp
        friendly name: DateAdded
        ignore: 'no'
      DateUpdated:
        format: function:file_timestamp
        friendly name: DateUpdated
        ignore: 'no'
      ExpiryMonth:
        format: None
        friendly name: ExpiryMonth
        ignore: 'no'
      ExpiryYear:
        format: None
        friendly name: ExpiryYear
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      IsFromWallet:
        format: None
        friendly name: IsFromWallet
        ignore: 'no'
      IsUploadedToWallet:
        format: None
        friendly name: IsUploadedToWallet
        ignore: 'no'
      PaymentItemId:
        format: None
        friendly name: PaymentItemId
        ignore: 'no'
      PaymentMethodType:
        format: None
        friendly name: PaymentMethodType
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      UseCount:
        format: None
        friendly name: UseCount
        ignore: 'no'
    ignore: 'no'
    name: AutoFormFillPaymentStorage
  AutoFormFillStorage:
    fields:
      AddressItemGuid:
        format: None
        friendly name: AddressItemGuid
        ignore: 'no'
      CompanyName:
        format: None
        friendly name: CompanyName
        ignore: 'no'
      DateAccessed:
        format: function:file_timestamp
        friendly name: DateAccessed
        ignore: 'no'
      DateAdded:
        format: function:file_timestamp
        friendly name: DateAdded
        ignore: 'no'
      DateUpdated:
        format: function:file_timestamp
        friendly name: DateUpdated
        ignore: 'no'
      Email:
        format: None
        friendly name: Email
        ignore: 'no'
      FirstName:
        format: None
        friendly name: FirstName
        ignore: 'no'
      FormUrl:
        format: function:remove_null_bytes
        friendly name: FormUrl
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      JetStub_109_1:
        format: None
        friendly name: JetStub_109_1
        ignore: 'no'
      JetStub_109_256:
        format: None
        friendly name: JetStub_109_256
        ignore: 'no'
      JetStub_109_257:
        format: None
        friendly name: JetStub_109_257
        ignore: 'no'
      JetStub_109_258:
        format: None
        friendly name: JetStub_109_258
        ignore: 'no'
      JetStub_109_259:
        format: None
        friendly name: JetStub_109_259
        ignore: 'no'
      JetStub_109_260:
        format: None
        friendly name: JetStub_109_260
        ignore: 'no'
      JetStub_109_262:
        format: None
        friendly name: JetStub_109_262
        ignore: 'no'
      JetStub_109_271:
        format: None
        friendly name: JetStub_109_271
        ignore: 'no'
      JetStub_109_274:
        format: None
        friendly name: JetStub_109_274
        ignore: 'no'
      JetStub_109_275:
        format: None
        friendly name: JetStub_109_275
        ignore: 'no'
      LastName:
        format: None
        friendly name: LastName
        ignore: 'no'
      MiddleName:
        format: None
        friendly name: MiddleName
        ignore: 'no'
      Phone:
        format: None
        friendly name: Phone
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      UseCount:
        format: None
        friendly name: UseCount
        ignore: 'no'
    ignore: 'no'
    name: AutoFormFillStorage
  BhxActionsTable:
    fields:
      AppxId:
        format: None
        friendly name: AppxId
        ignore: 'no'
      BhxExtensionEnabled:
        format: None
        friendly name: BhxExtensionEnabled
        ignore: 'no'
      ExtensionId:
        format: None
        friendly name: ExtensionId
        ignore: 'no'
      Icon:
        format: None
        friendly name: Icon
        ignore: 'no'
      IsBrowserAction:
        format: None
        friendly name: IsBrowserAction
        ignore: 'no'
      Popup:
        format: None
        friendly name: Popup
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Title:
        format: function:remove_null_bytes
        friendly name: Title
        ignore: 'no'
    ignore: 'no'
    name: BhxActionsTable
  BhxContentScriptTable:
    fields:
      AppxId:
        format: None
        friendly name: AppxId
        ignore: 'no'
      BhxExtensionEnabled:
        format: None
        friendly name: BhxExtensionEnabled
        ignore: 'no'
      ContentScriptInfo:
        format: None
        friendly name: ContentScriptInfo
        ignore: 'no'
      ExtensionId:
        format: None
        friendly name: ExtensionId
        ignore: 'no'
      Permissions:
        format: None
        friendly name: Permissions
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      WebAccessibleResources:
        format: None
        friendly name: WebAccessibleResources
        ignore: 'no'
    ignore: 'no'
    name: BhxContentScriptTable
  BhxHostTable:
    fields:
      AppxId:
        format: None
        friendly name: AppxId
        ignore: 'no'
      BackgroundPage:
        format: None
        friendly name: BackgroundPage
        ignore: 'no'
      BackgroundScripts:
        format: None
        friendly name: BackgroundScripts
        ignore: 'no'
      ExtensionId:
        format: None
        friendly name: ExtensionId
        ignore: 'no'
      HasOptionalPermissions:
        format: None
        friendly name: HasOptionalPermissions
        ignore: 'no'
      IsPersistentPage:
        format: None
        friendly name: IsPersistentPage
        ignore: 'no'
      PermissionsBitField:
        format: None
        friendly name: PermissionsBitField
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      UrlMatches:
        format: None
        friendly name: UrlMatches
        ignore: 'no'
      UrlPermissions:
        format: None
        friendly name: UrlPermissions
        ignore: 'no'
    ignore: 'no'
    name: BhxHostTable
  BookAnnotations:
    fields:
      AddedDate:
        format: function:file_timestamp
        friendly name: AddedDate
        ignore: 'no'
      Context:
        format: None
        friendly name: Context
        ignore: 'no'
      HighlightColor:
        format: None
        friendly name: HighlightColor
        ignore: 'no'
      InkNoteBlobId:
        format: None
        friendly name: InkNoteBlobId
        ignore: 'no'
      InkNoteMetadataId:
        format: None
        friendly name: InkNoteMetadataId
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      IsMetadataUpToDate:
        format: None
        friendly name: IsMetadataUpToDate
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      Layout:
        format: None
        friendly name: Layout
        ignore: 'no'
      LineStyle:
        format: None
        friendly name: LineStyle
        ignore: 'no'
      OpenedBookId:
        format: None
        friendly name: OpenedBookId
        ignore: 'no'
      PageNumber:
        format: None
        friendly name: PageNumber
        ignore: 'no'
      ProductVersion:
        format: None
        friendly name: ProductVersion
        ignore: 'no'
      ProgressInBook:
        format: None
        friendly name: ProgressInBook
        ignore: 'no'
      ReadingPosition:
        format: None
        friendly name: ReadingPosition
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SyncStatus:
        format: None
        friendly name: SyncStatus
        ignore: 'no'
      TypedNoteText:
        format: function:remove_null_bytes
        friendly name: TypedNoteText
        ignore: 'no'
      UpdatedDate:
        format: function:file_timestamp
        friendly name: UpdatedDate
        ignore: 'no'
    ignore: 'no'
    name: BookAnnotations
  BookPushOperations:
    fields:
      AccountId:
        format: None
        friendly name: AccountId
        ignore: 'no'
      BlobId:
        format: None
        friendly name: BlobId
        ignore: 'no'
      Category:
        format: None
        friendly name: Category
        ignore: 'no'
      ErrorCount:
        format: None
        friendly name: ErrorCount
        ignore: 'no'
      ErrorRetry:
        format: None
        friendly name: ErrorRetry
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      MetadataId:
        format: None
        friendly name: MetadataId
        ignore: 'no'
      OpenedBookId:
        format: None
        friendly name: OpenedBookId
        ignore: 'no'
      Path:
        format: None
        friendly name: Path
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Timestamp:
        format: None
        friendly name: Timestamp
        ignore: 'no'
      Type:
        format: None
        friendly name: Type
        ignore: 'no'
      UserDataId:
        format: None
        friendly name: UserDataId
        ignore: 'no'
      Value:
        format: None
        friendly name: Value
        ignore: 'no'
    ignore: 'no'
    name: BookPushOperations
  Bookmarks:
    fields:
      AddedDate:
        format: function:file_timestamp
        friendly name: AddedDate
        ignore: 'no'
      BookId:
        format: None
        friendly name: BookId
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      PageNumber:
        format: None
        friendly name: PageNumber
        ignore: 'no'
      ProductVersion:
        format: None
        friendly name: ProductVersion
        ignore: 'no'
      ProgressInBook:
        format: None
        friendly name: ProgressInBook
        ignore: 'no'
      ReadingPosition:
        format: None
        friendly name: ReadingPosition
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SyncStatus:
        format: None
        friendly name: SyncStatus
        ignore: 'no'
      Title:
        format: function:remove_null_bytes
        friendly name: Title
        ignore: 'no'
      UpdatedDate:
        format: function:file_timestamp
        friendly name: UpdatedDate
        ignore: 'no'
    ignore: 'no'
    name: Bookmarks
  CARules:
    fields:
      Domain:
        format: function:remove_null_bytes
        friendly name: Domain
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Rule:
        format: None
        friendly name: Rule
        ignore: 'no'
      RuleType:
        format: None
        friendly name: RuleType
        ignore: 'no'
    ignore: 'no'
    name: CARules
  CloudLibrary:
    fields:
      AccountId:
        format: None
        friendly name: AccountId
        ignore: 'no'
      FullyAppliedSyncToken:
        format: None
        friendly name: FullyAppliedSyncToken
        ignore: 'no'
      IsPushAllowed:
        format: None
        friendly name: IsPushAllowed
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SyncToken:
        format: None
        friendly name: SyncToken
        ignore: 'no'
    ignore: 'no'
    name: CloudLibrary
  EdgeScenarioLogger:
    fields:
      Cookie:
        format: None
        friendly name: Cookie
        ignore: 'no'
      Data:
        format: None
        friendly name: Data
        ignore: 'no'
      Duration:
        format: None
        friendly name: Duration
        ignore: 'no'
      EndTime:
        format: None
        friendly name: EndTime
        ignore: 'no'
      InstanceCount:
        format: None
        friendly name: InstanceCount
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      IsIndividualItem:
        format: None
        friendly name: IsIndividualItem
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      ScenarioId:
        format: None
        friendly name: ScenarioId
        ignore: 'no'
      StartTime:
        format: None
        friendly name: StartTime
        ignore: 'no'
    ignore: 'no'
    name: EdgeScenarioLogger
  ExtensionIdsList:
    fields:
      DateUpdated:
        format: function:file_timestamp
        friendly name: DateUpdated
        ignore: 'no'
      ExtensionId:
        format: None
        friendly name: ExtensionId
        ignore: 'no'
      InstallStatus:
        format: None
        friendly name: InstallStatus
        ignore: 'no'
      InstallType:
        format: None
        friendly name: InstallType
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
    ignore: 'no'
    name: ExtensionIdsList
  ExtensionsList:
    fields:
      Author:
        format: None
        friendly name: Author
        ignore: 'no'
      BhxExtensionEnabled:
        format: None
        friendly name: BhxExtensionEnabled
        ignore: 'no'
      BhxExtensionId:
        format: None
        friendly name: BhxExtensionId
        ignore: 'no'
      BhxExtensionName:
        format: None
        friendly name: BhxExtensionName
        ignore: 'no'
      BhxInstallTime:
        format: None
        friendly name: BhxInstallTime
        ignore: 'no'
      Description:
        format: None
        friendly name: Description
        ignore: 'no'
      ExtensionOrigin:
        format: None
        friendly name: ExtensionOrigin
        ignore: 'no'
      HomepageUrl:
        format: function:remove_null_bytes
        friendly name: HomepageUrl
        ignore: 'no'
      InstallType:
        format: None
        friendly name: InstallType
        ignore: 'no'
      IsOfflineEnabled:
        format: None
        friendly name: IsOfflineEnabled
        ignore: 'no'
      Key:
        format: None
        friendly name: Key
        ignore: 'no'
      Locale:
        format: None
        friendly name: Locale
        ignore: 'no'
      ManifestVersion:
        format: None
        friendly name: ManifestVersion
        ignore: 'no'
      MinBrowserVersion:
        format: None
        friendly name: MinBrowserVersion
        ignore: 'no'
      OptionalPermissions:
        format: None
        friendly name: OptionalPermissions
        ignore: 'no'
      OptionsPage:
        format: None
        friendly name: OptionsPage
        ignore: 'no'
      Permissions:
        format: None
        friendly name: Permissions
        ignore: 'no'
      RootPath:
        format: None
        friendly name: RootPath
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SettingsFlags:
        format: None
        friendly name: SettingsFlags
        ignore: 'no'
      ShortName:
        format: None
        friendly name: ShortName
        ignore: 'no'
      UpdateVersion:
        format: None
        friendly name: UpdateVersion
        ignore: 'no'
      Version:
        format: None
        friendly name: Version
        ignore: 'no'
    ignore: 'no'
    name: ExtensionsList
  Favorites:
    fields:
      DateSyncedWithIE:
        format: function:file_timestamp
        friendly name: DateSyncedWithIE
        ignore: 'no'
      DateUpdated:
        format: function:file_timestamp
        friendly name: DateUpdated
        ignore: 'no'
      DisplayMode:
        format: None
        friendly name: DisplayMode
        ignore: 'no'
      FaviconFile:
        format: None
        friendly name: FaviconFile
        ignore: 'no'
      HashedUrl:
        format: None
        friendly name: HashedUrl
        ignore: 'no'
      IsAllowedToBeOrphan:
        format: None
        friendly name: IsAllowedToBeOrphan
        ignore: 'no'
      IsAwaitingDeletion:
        format: None
        friendly name: IsAwaitingDeletion
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      IsEnterprise:
        format: None
        friendly name: IsEnterprise
        ignore: 'no'
      IsFolder:
        format: None
        friendly name: IsFolder
        ignore: 'no'
      IsOrphaned:
        format: None
        friendly name: IsOrphaned
        ignore: 'no'
      IsWebNotes:
        format: None
        friendly name: IsWebNotes
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      OrderNumber:
        format: None
        friendly name: OrderNumber
        ignore: 'no'
      ParentId:
        format: None
        friendly name: ParentId
        ignore: 'no'
      RoamDisabled:
        format: None
        friendly name: RoamDisabled
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Title:
        format: function:remove_null_bytes
        friendly name: Title
        ignore: 'no'
      URL:
        format: function:remove_null_bytes
        friendly name: URL
        ignore: 'no'
    ignore: 'no'
    name: Favorites
  FileCleanup:
    fields:
      AccountStoreId:
        format: None
        friendly name: AccountStoreId
        ignore: 'no'
      FileName:
        format: None
        friendly name: FileName
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Timestamp:
        format: None
        friendly name: Timestamp
        ignore: 'no'
    ignore: 'no'
    name: FileCleanup
  Folder:
    fields:
      FolderPath:
        format: None
        friendly name: FolderPath
        ignore: 'no'
      Name:
        format: None
        friendly name: Name
        ignore: 'no'
      OriginalParentId:
        format: None
        friendly name: OriginalParentId
        ignore: 'no'
      ParentId:
        format: None
        friendly name: ParentId
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Type:
        format: None
        friendly name: Type
        ignore: 'no'
    ignore: 'no'
    name: Folder
  FolderStash:
    fields:
      FolderPath:
        format: None
        friendly name: FolderPath
        ignore: 'no'
      Name:
        format: None
        friendly name: Name
        ignore: 'no'
      OriginalParentId:
        format: None
        friendly name: OriginalParentId
        ignore: 'no'
      ParentId:
        format: None
        friendly name: ParentId
        ignore: 'no'
      RealStoreId:
        format: None
        friendly name: RealStoreId
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      StashChangeType:
        format: None
        friendly name: StashChangeType
        ignore: 'no'
      Type:
        format: None
        friendly name: Type
        ignore: 'no'
    ignore: 'no'
    name: FolderStash
  FreeFormInks:
    fields:
      AddedDate:
        format: function:file_timestamp
        friendly name: AddedDate
        ignore: 'no'
      Context:
        format: None
        friendly name: Context
        ignore: 'no'
      InkBlobId:
        format: None
        friendly name: InkBlobId
        ignore: 'no'
      InkMetadataId:
        format: None
        friendly name: InkMetadataId
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      IsMetadataUpToDate:
        format: None
        friendly name: IsMetadataUpToDate
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      OpenedBookId:
        format: None
        friendly name: OpenedBookId
        ignore: 'no'
      PageNumber:
        format: None
        friendly name: PageNumber
        ignore: 'no'
      ProductVersion:
        format: None
        friendly name: ProductVersion
        ignore: 'no'
      ProgressInBook:
        format: None
        friendly name: ProgressInBook
        ignore: 'no'
      ReadingPosition:
        format: None
        friendly name: ReadingPosition
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SyncStatus:
        format: None
        friendly name: SyncStatus
        ignore: 'no'
      UpdatedDate:
        format: function:file_timestamp
        friendly name: UpdatedDate
        ignore: 'no'
    ignore: 'no'
    name: FreeFormInks
  Library:
    fields:
      AccountId:
        format: None
        friendly name: AccountId
        ignore: 'no'
      AddedDate:
        format: function:file_timestamp
        friendly name: AddedDate
        ignore: 'no'
      Author:
        format: None
        friendly name: Author
        ignore: 'no'
      CoverUrl:
        format: function:remove_null_bytes
        friendly name: CoverUrl
        ignore: 'no'
      CurrentDownloadedVersion:
        format: None
        friendly name: CurrentDownloadedVersion
        ignore: 'no'
      Description:
        format: None
        friendly name: Description
        ignore: 'no'
      DevicePolicy:
        format: None
        friendly name: DevicePolicy
        ignore: 'no'
      DownloadDate:
        format: function:file_timestamp
        friendly name: DownloadDate
        ignore: 'no'
      DownloadErrorCode:
        format: None
        friendly name: DownloadErrorCode
        ignore: 'no'
      DownloadStatus:
        format: None
        friendly name: DownloadStatus
        ignore: 'no'
      EntitlementModifiedDate:
        format: function:file_timestamp
        friendly name: EntitlementModifiedDate
        ignore: 'no'
      FileType:
        format: None
        friendly name: FileType
        ignore: 'no'
      IsProtected:
        format: None
        friendly name: IsProtected
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      Language:
        format: None
        friendly name: Language
        ignore: 'no'
      LatestKnownVersion:
        format: None
        friendly name: LatestKnownVersion
        ignore: 'no'
      Market:
        format: None
        friendly name: Market
        ignore: 'no'
      OwnershipEndDate:
        format: function:file_timestamp
        friendly name: OwnershipEndDate
        ignore: 'no'
      OwnershipStartDate:
        format: function:file_timestamp
        friendly name: OwnershipStartDate
        ignore: 'no'
      OwnershipStatus:
        format: None
        friendly name: OwnershipStatus
        ignore: 'no'
      OwnershipType:
        format: None
        friendly name: OwnershipType
        ignore: 'no'
      ProductId:
        format: None
        friendly name: ProductId
        ignore: 'no'
      Publisher:
        format: None
        friendly name: Publisher
        ignore: 'no'
      PurchaseDate:
        format: function:file_timestamp
        friendly name: PurchaseDate
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Title:
        format: function:remove_null_bytes
        friendly name: Title
        ignore: 'no'
    ignore: 'no'
    name: Library
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
    ignore: 'no'
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
    ignore: 'no'
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
    ignore: 'no'
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
    ignore: 'no'
    name: MSysObjids
  OpenedBooks:
    fields:
      AccountId:
        format: None
        friendly name: AccountId
        ignore: 'no'
      FullyAppliedSyncToken:
        format: None
        friendly name: FullyAppliedSyncToken
        ignore: 'no'
      HasCloudAnnotations:
        format: None
        friendly name: HasCloudAnnotations
        ignore: 'no'
      HashId:
        format: None
        friendly name: HashId
        ignore: 'no'
      HighestKnownProductVersion:
        format: None
        friendly name: HighestKnownProductVersion
        ignore: 'no'
      IsPushAllowed:
        format: None
        friendly name: IsPushAllowed
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      PageNumber:
        format: None
        friendly name: PageNumber
        ignore: 'no'
      ProductId:
        format: None
        friendly name: ProductId
        ignore: 'no'
      ProgressInBook:
        format: None
        friendly name: ProgressInBook
        ignore: 'no'
      ReadingPosition:
        format: None
        friendly name: ReadingPosition
        ignore: 'no'
      ReadingPositionModifiedDate:
        format: function:file_timestamp
        friendly name: ReadingPositionModifiedDate
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SyncToken:
        format: None
        friendly name: SyncToken
        ignore: 'no'
      VersionNumber:
        format: None
        friendly name: VersionNumber
        ignore: 'no'
    ignore: 'no'
    name: OpenedBooks
  PackagedExtensionsStorage:
    fields:
      DateUpdated:
        format: function:file_timestamp
        friendly name: DateUpdated
        ignore: 'no'
      ExtensionId:
        format: None
        friendly name: ExtensionId
        ignore: 'no'
      HashedKey:
        format: None
        friendly name: HashedKey
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      Key:
        format: None
        friendly name: Key
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Value:
        format: None
        friendly name: Value
        ignore: 'no'
    ignore: 'no'
    name: PackagedExtensionsStorage
  PageSettings:
    fields:
      Domain:
        format: None
        friendly name: Domain
        ignore: 'no'
      PageSettings:
        format: None
        friendly name: PageSettings
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
    ignore: 'no'
    name: PageSettings
  ReadingList:
    fields:
      AddedDate:
        format: function:file_timestamp
        friendly name: AddedDate
        ignore: 'no'
      Description:
        format: None
        friendly name: Description
        ignore: 'no'
      DominantImageFile:
        format: None
        friendly name: DominantImageFile
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      JetStub_18_1:
        format: None
        friendly name: JetStub_18_1
        ignore: 'no'
      JetStub_18_2:
        format: None
        friendly name: JetStub_18_2
        ignore: 'no'
      LastAccessedDate:
        format: function:file_timestamp
        friendly name: LastAccessedDate
        ignore: 'no'
      MhtFile:
        format: None
        friendly name: MhtFile
        ignore: 'no'
      RoamDisabled:
        format: None
        friendly name: RoamDisabled
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Source:
        format: None
        friendly name: Source
        ignore: 'no'
      Title:
        format: function:remove_null_bytes
        friendly name: Title
        ignore: 'no'
      Type:
        format: None
        friendly name: Type
        ignore: 'no'
      URL:
        format: function:remove_null_bytes
        friendly name: URL
        ignore: 'no'
      UpdatedDate:
        format: function:file_timestamp
        friendly name: UpdatedDate
        ignore: 'no'
    ignore: 'no'
    name: ReadingList
  RowId:
    fields:
      MaxAllocatedRowId:
        format: None
        friendly name: MaxAllocatedRowId
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
    ignore: 'no'
    name: RowId
  SideLoadedExtensionsStorage:
    fields:
      DateUpdated:
        format: function:file_timestamp
        friendly name: DateUpdated
        ignore: 'no'
      ExtensionId:
        format: None
        friendly name: ExtensionId
        ignore: 'no'
      HashedKey:
        format: None
        friendly name: HashedKey
        ignore: 'no'
      IsDeleted:
        format: None
        friendly name: IsDeleted
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      Key:
        format: None
        friendly name: Key
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Value:
        format: None
        friendly name: Value
        ignore: 'no'
    ignore: 'no'
    name: SideLoadedExtensionsStorage
  SweptTabs:
    fields:
      DateSwept:
        format: function:file_timestamp
        friendly name: DateSwept
        ignore: 'no'
      EnterpriseID:
        format: None
        friendly name: EnterpriseID
        ignore: 'no'
      OrderNumber:
        format: None
        friendly name: OrderNumber
        ignore: 'no'
      RecoveryGuid:
        format: None
        friendly name: RecoveryGuid
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SweepGroupId:
        format: None
        friendly name: SweepGroupId
        ignore: 'no'
      Title:
        format: function:remove_null_bytes
        friendly name: Title
        ignore: 'no'
      URL:
        format: function:remove_null_bytes
        friendly name: URL
        ignore: 'no'
      WasSelected:
        format: None
        friendly name: WasSelected
        ignore: 'no'
    ignore: 'no'
    name: SweptTabs
  TopSites:
    fields:
      CreatedDateTimeUTC:
        format: function:file_timestamp
        friendly name: CreatedDateTimeUTC
        ignore: 'no'
      FaviconBackground:
        format: None
        friendly name: FaviconBackground
        ignore: 'no'
      FaviconForeground:
        format: None
        friendly name: FaviconForeground
        ignore: 'no'
      FaviconSource:
        format: None
        friendly name: FaviconSource
        ignore: 'no'
      FaviconUrl:
        format: function:remove_null_bytes
        friendly name: FaviconUrl
        ignore: 'no'
      IsTombstoned:
        format: None
        friendly name: IsTombstoned
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      SlotIndex:
        format: None
        friendly name: SlotIndex
        ignore: 'no'
      SourceType:
        format: None
        friendly name: SourceType
        ignore: 'no'
      Title:
        format: function:remove_null_bytes
        friendly name: Title
        ignore: 'no'
      TombstonedDateTimeUTC:
        format: function:file_timestamp
        friendly name: TombstonedDateTimeUTC
        ignore: 'no'
      URL:
        format: function:remove_null_bytes
        friendly name: URL
        ignore: 'no'
      UpdatedDateTimeUTC:
        format: function:file_timestamp
        friendly name: UpdatedDateTimeUTC
        ignore: 'no'
      UrlHash:
        format: None
        friendly name: UrlHash
        ignore: 'no'
    ignore: 'no'
    name: TopSites
  TypedUrls:
    fields:
      AccessDateTimeUTC:
        format: function:file_timestamp
        friendly name: AccessDateTimeUTC
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      URL:
        format: function:remove_null_bytes
        friendly name: URL
        ignore: 'no'
      UrlHash:
        format: None
        friendly name: UrlHash
        ignore: 'no'
      VisitCount:
        format: None
        friendly name: VisitCount
        ignore: 'no'
    ignore: 'no'
    name: TypedUrls
  UriToAppIdMapping:
    fields:
      ExpiryDateUTC:
        format: function:file_timestamp
        friendly name: ExpiryDateUTC
        ignore: 'no'
      HasAddOns:
        format: None
        friendly name: HasAddOns
        ignore: 'no'
      IsFree:
        format: None
        friendly name: IsFree
        ignore: 'no'
      ItemId:
        format: None
        friendly name: ItemId
        ignore: 'no'
      LastAccessedDateUTC:
        format: function:file_timestamp
        friendly name: LastAccessedDateUTC
        ignore: 'no'
      LastUpdatedDateUTC:
        format: function:file_timestamp
        friendly name: LastUpdatedDateUTC
        ignore: 'no'
      MatchedUrl:
        format: None
        friendly name: MatchedUrl
        ignore: 'no'
      PackageFamilyName:
        format: None
        friendly name: PackageFamilyName
        ignore: 'no'
      ProductId:
        format: None
        friendly name: ProductId
        ignore: 'no'
      ProductTitle:
        format: function:remove_null_bytes
        friendly name: ProductTitle
        ignore: 'no'
      RetryAttemptCount:
        format: None
        friendly name: RetryAttemptCount
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Status:
        format: None
        friendly name: Status
        ignore: 'no'
      Uri:
        format: None
        friendly name: Uri
        ignore: 'no'
      UriHash:
        format: None
        friendly name: UriHash
        ignore: 'no'
    ignore: 'no'
    name: UriToAppIdMapping
  UrlHistory:
    fields:
      AddTime:
        format: None
        friendly name: AddTime
        ignore: 'no'
      Domain:
        format: None
        friendly name: Domain
        ignore: 'no'
      FaviconTimeStamp:
        format: None
        friendly name: FaviconTimeStamp
        ignore: 'no'
      FaviconUrl:
        format: function:remove_null_bytes
        friendly name: FaviconUrl
        ignore: 'no'
      Flags:
        format: None
        friendly name: Flags
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Title:
        format: function:remove_null_bytes
        friendly name: Title
        ignore: 'no'
      URL:
        format: function:remove_null_bytes
        friendly name: URL
        ignore: 'no'
      UpdateTime:
        format: None
        friendly name: UpdateTime
        ignore: 'no'
      UrlHash:
        format: None
        friendly name: UrlHash
        ignore: 'no'
      VisitCount:
        format: None
        friendly name: VisitCount
        ignore: 'no'
    ignore: 'no'
    name: UrlHistory
  UrlVisit:
    fields:
      Domain:
        format: None
        friendly name: Domain
        ignore: 'no'
      RowId:
        format: None
        friendly name: RowId
        ignore: 'no'
      Title:
        format: function:remove_null_bytes
        friendly name: Title
        ignore: 'no'
      URL:
        format: function:remove_null_bytes
        friendly name: URL
        ignore: 'no'
      UrlHash:
        format: None
        friendly name: UrlHash
        ignore: 'no'
      VisitTime:
        format: None
        friendly name: VisitTime
        ignore: 'no'
    ignore: 'no'
    name: UrlVisit


"""

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

def remove_null_bytes(instr):
    return instr.replace('\x00','')


