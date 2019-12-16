Sub Main
	Call ExcelImport()	'C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\Copy of Year2018July2019JuneTransactionStatement.xlsx
	Call DirectExtraction()	'Copy of Year2018July2019JuneTransactionStatement-Sheet1.IMD
	Call ExcelImport1()	'C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\2019JulyTransactionStatement.xlsx
	Call DirectExtraction1()	'2019JulyTransactionStatement-Sheet1.IMD
	Call AppendDatabase()	'split2.IMD
	Call Summarization()	'Append Databases.IMD
	Call DirectExtraction2()	'Summarization.IMD
	Call ExportDatabaseXLSX()	'file.IMD
End Sub


' File - Import Assistant: Excel
Function ExcelImport
	Set task = Client.GetImportTask("ImportExcel")
	dbName = "C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\Copy of Year2018July2019JuneTransactionStatement.xlsx"
	task.FileToImport = dbName
	task.SheetToImport = "Sheet1"
	task.OutputFilePrefix = "Copy of Year2018July2019JuneTransactionStatement"
	task.FirstRowIsFieldName = "TRUE"
	task.EmptyNumericFieldAsZero = "TRUE"
	task.PerformTask
	dbName = task.OutputFilePath("Sheet1")
	Set task = Nothing
	Client.OpenDatabase(dbName)
End Function

' Data: Direct Extraction
Function DirectExtraction
	Set db = Client.OpenDatabase("Copy of Year2018July2019JuneTransactionStatement-Sheet1.IMD")
	Set task = db.Extraction
	task.AddFieldToInc "NAME"
	task.AddFieldToInc "TRANSACTION_DATE"
	task.AddFieldToInc "TRANSACTION_AMOUNT"
	task.AddFieldToInc "MERCHANT_NAME"
	dbName = "split.IMD"
	task.AddExtraction dbName, "", "TRANSACTION_DATE  > ""20180630"""
	task.CreateVirtualDatabase = False
	task.PerformTask 1, db.Count
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' File - Import Assistant: Excel
Function ExcelImport1
	Set task = Client.GetImportTask("ImportExcel")
	dbName = "C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\2019JulyTransactionStatement.xlsx"
	task.FileToImport = dbName
	task.SheetToImport = "Sheet1"
	task.OutputFilePrefix = "2019JulyTransactionStatement"
	task.FirstRowIsFieldName = "TRUE"
	task.EmptyNumericFieldAsZero = "TRUE"
	task.PerformTask
	dbName = task.OutputFilePath("Sheet1")
	Set task = Nothing
	Client.OpenDatabase(dbName)
End Function

' Data: Direct Extraction
Function DirectExtraction1
	Set db = Client.OpenDatabase("2019JulyTransactionStatement-Sheet1.IMD")
	Set task = db.Extraction
	task.AddFieldToInc "NAME"
	task.AddFieldToInc "TRANSACTION_DATE"
	task.AddFieldToInc "TRANSACTION_AMOUNT"
	task.AddFieldToInc "MERCHANT_NAME"
	dbName = "split2.IMD"
	task.AddExtraction dbName, "", "TRANSACTION_DATE > ""20190630"""
	task.CreateVirtualDatabase = False
	task.PerformTask 1, db.Count
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' File: Append Databases
Function AppendDatabase
	Set db = Client.OpenDatabase("split.IMD")
	Set task = db.AppendDatabase
	task.AddDatabase "split2.IMD"
	dbName = "Append Databases.IMD"
	task.PerformTask dbName, ""
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' Analysis: Summarization
Function Summarization
	Set db = Client.OpenDatabase("Append Databases.IMD")
	Set task = db.Summarization
	task.AddFieldToSummarize "NAME"
	task.AddFieldToSummarize "MERCHANT_NAME"
	task.AddFieldToTotal "TRANSACTION_AMOUNT"
	dbName = "Summarization.IMD"
	task.OutputDBName = dbName
	task.CreatePercentField = FALSE
	task.StatisticsToInclude = SM_SUM
	task.PerformTask
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' Data: Direct Extraction
Function DirectExtraction2
	Set db = Client.OpenDatabase("Summarization.IMD")
	Set task = db.Extraction
	task.IncludeAllFields
	dbName = "file.IMD"
	task.AddExtraction dbName, "", " NO_OF_RECS > 1  .AND.  TRANSACTION_AMOUNT_SUM > 4998"
	task.CreateVirtualDatabase = False
	task.PerformTask 1, db.Count
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' File - Export Database: XLSX
Function ExportDatabaseXLSX
	Set db = Client.OpenDatabase("file.IMD")
	Set task = db.ExportDatabase
	task.IncludeAllFields
	eqn = ""
	task.PerformTask "C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\User input\file.xlsx", "Database", "XLSX", 1, db.Count, eqn
	Set db = Nothing
	Set task = Nothing
End Function