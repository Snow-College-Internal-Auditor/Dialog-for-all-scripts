Sub Main
	Call ExcelImport()	'C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\2019JulyTransactionStatement.xlsx
	Call DirectExtraction()	'2019JulyTransactionStatement-Sheet1.IMD
	Call Summarization()	'Split.IMD
	Call DirectExtraction1()	'Summarization.IMD
	Call ExportDatabaseXLSX()	'Over 4998.IMD
End Sub


' File - Import Assistant: Excel
Function ExcelImport
	Set task = Client.GetImportTask("ImportExcel")
	dbName = "C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\2019AugTransactionStatement.xlsx"
	task.FileToImport = dbName
	task.SheetToImport = "Sheet1"
	task.OutputFilePrefix = "2019AugTransactionStatement"
	task.FirstRowIsFieldName = "TRUE"
	task.EmptyNumericFieldAsZero = "TRUE"
	task.PerformTask
	dbName = task.OutputFilePath("Sheet1")
	Set task = Nothing
	Client.OpenDatabase(dbName)
End Function

' Data: Direct Extraction
Function DirectExtraction
	Set db = Client.OpenDatabase("2019AugTransactionStatement-Sheet1.IMD")
	Set task = db.Extraction
	task.AddFieldToInc "NAME"
	task.AddFieldToInc "TRANSACTION_DATE"
	task.AddFieldToInc "TRANSACTION_AMOUNT"
	task.AddFieldToInc "MERCHANT_CATEGORY_CODE_DESCRIPTION"
	task.AddFieldToInc "MERCHANT_NAME"
	dbName = "Split1.IMD"
	task.AddExtraction dbName, "", ""
	task.CreateVirtualDatabase = False
	task.PerformTask 1, db.Count
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' Analysis: Summarization
Function Summarization
	Set db = Client.OpenDatabase("Split1.IMD")
	Set task = db.Summarization
	task.AddFieldToSummarize "NAME"
	task.AddFieldToSummarize "MERCHANT_NAME"
	task.AddFieldToSummarize "TRANSACTION_DATE"
	task.AddFieldToSummarize "TRANSACTION_AMOUNT"
	task.AddFieldToTotal "TRANSACTION_AMOUNT"
	dbName = "Summarization1.IMD"
	task.OutputDBName = dbName
	task.CreatePercentField = FALSE
	task.StatisticsToInclude = SM_SUM
	task.PerformTask
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' Data: Direct Extraction
Function DirectExtraction1
	Set db = Client.OpenDatabase("Summarization1.IMD")
	Set task = db.Extraction
	task.IncludeAllFields
	dbName = "Over 4998_1.IMD"
	task.AddExtraction dbName, "", "TRANSACTION_AMOUNT_SUM > 4998"
	task.CreateVirtualDatabase = False
	task.PerformTask 1, db.Count
	Set task = Nothing
	Set db = Nothing
	Client.OpenDatabase (dbName)
End Function

' File - Export Database: XLSX
Function ExportDatabaseXLSX
	Set db = Client.OpenDatabase("Over 4998_1.IMD")
	Set task = db.ExportDatabase
	task.IncludeAllFields
	task.AddKey "NO_OF_RECS", "D"
	eqn = ""
	task.PerformTask "C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\Over 4998_1.XLSX", "Database", "XLSX", 1, db.Count, eqn
	Set db = Nothing
	Set task = Nothing
End Function