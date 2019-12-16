Sub Main
	Call ExcelImport()	'C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\Copy of Year2018July2019JuneTransactionStatement.xlsx
	Call DirectExtraction()	'Copy of Year2018July2019JuneTransactionStatement1-Sheet1.IMD
	Call DirectExtraction1()	'Copy of Year2018July2019JuneTransactionStatement1-Sheet1.IMD
	Call AppendField()	'negative2.IMD
	Call JoinDatabase()	'negative2.IMD
End Sub


' File - Import Assistant: Excel
Function ExcelImport
	Set task = Client.GetImportTask("ImportExcel")
	dbName = "C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\Copy of Year2018July2019JuneTransactionStatement.xlsx"
	task.FileToImport = dbName
	task.SheetToImport = "Sheet1"
	task.OutputFilePrefix = "Copy of Year2018July2019JuneTransactionStatement1"
	task.FirstRowIsFieldName = "TRUE"
	task.EmptyNumericFieldAsZero = "TRUE"
	task.PerformTask
	dbName = task.OutputFilePath("Sheet1")
	Set task = Nothing
	Client.OpenDatabase(dbName)
End Function

' Data: Direct Extraction
Function DirectExtraction
	Set db = Client.OpenDatabase("Copy of Year2018July2019JuneTransactionStatement1-Sheet1.IMD")
	Set task = db.Extraction
	task.IncludeAllFields
	dbName = "negative2.IMD"
	task.AddExtraction dbName, "", "TRANSACTION_AMOUNT < 0"
	task.CreateVirtualDatabase = False
	task.PerformTask 1, db.Count
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' Data: Direct Extraction
Function DirectExtraction1
	Set db = Client.OpenDatabase("Copy of Year2018July2019JuneTransactionStatement1-Sheet1.IMD")
	Set task = db.Extraction
	task.IncludeAllFields
	dbName = "positive2.IMD"
	task.AddExtraction dbName, "", "TRANSACTION_AMOUNT > 0"
	task.CreateVirtualDatabase = False
	task.PerformTask 1, db.Count
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' Append Field
Function AppendField
	Set db = Client.OpenDatabase("negative2.IMD")
	Set task = db.TableManagement
	Set field = db.TableDef.NewField
	field.Name = "ABSOULUTE_VALUE"
	field.Description = ""
	field.Type = WI_VIRT_NUM
	field.Equation = "@Abs(TRANSACTION_AMOUNT)"
	field.Decimals = 2
	task.AppendField field
	task.PerformTask
	Set task = Nothing
	Set db = Nothing
	Set field = Nothing
End Function

' File: Join Databases
Function JoinDatabase
	Set db = Client.OpenDatabase("negative2.IMD")
	Set task = db.JoinDatabase
	task.FileToJoin "positive2.IMD"
	task.AddPFieldToInc "NAME"
	task.AddPFieldToInc "TRANSACTION_DATE"
	task.AddPFieldToInc "TRANSACTION_AMOUNT"
	task.AddPFieldToInc "MERCHANT_CATEGORY_CODE_GROUP_CODE"
	task.AddPFieldToInc "MERCHANT_CATEGORY_CODE_GROUP_DESCRIPTION"
	task.AddPFieldToInc "MERCHANT_CATEGORY_CODE"
	task.AddPFieldToInc "MERCHANT_CATEGORY_CODE_DESCRIPTION"
	task.AddPFieldToInc "MERCHANT_NAME"
	task.AddPFieldToInc "ABSOULUTE_VALUE"
	task.AddSFieldToInc "TRANSACTION_DATE"
	task.AddSFieldToInc "TRANSACTION_AMOUNT"
	task.AddMatchKey "ABSOULUTE_VALUE", "TRANSACTION_AMOUNT", "A"
	task.CreateVirtualDatabase = False
	dbName = "Join Databases.IMD"
	task.PerformTask dbName, "", WI_JOIN_MATCH_ONLY
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function