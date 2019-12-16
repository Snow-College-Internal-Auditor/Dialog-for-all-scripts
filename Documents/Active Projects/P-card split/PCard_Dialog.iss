Dim listbox1$() AS string

Begin Dialog PCard 56,16,363,198,"Purchasing Card", .displayIt
  OKButton 10,143,40,14, "OK", .OKButton1
  CancelButton 120,143,40,14, "Cancel", .CancelButton1
  Text 10,8,58,14, "Create Database", .Text2
  Text 81,9,208,13, "Text", .creatdbFileName
  GroupBox 73,2,219,27, .GroupBox2
  PushButton 298,9,25,14, "...", .creatdbFilebtn
  Text 10,40,56,16, "Sheet To Import", .Text1
  DropListBox 81,40,208,13, listbox1$(), .DropListBox1
End Dialog


Dim sFilename As String
Dim sImportFile As String 
Dim bExitScript As Boolean 

Sub Main
	Call dialogBox()
End Sub

Function dialogBox()
	Dim dlg As PCard
	Dim button As Integer
	On Error Resume Next
	button = Dialog(dlg)
	If button = 0  Then bExitScript = True
End Function 

Function displayIt(ControllD$, Action%, SuppValue%)
	Dim bExitMenu As Boolean 
	Select Case Action%
		Case 1

		Case 2
			Select Case ControllD$
				Case "creatdbFilebtn"
					sImportFile = ExcelImport()
				Case "OKButton1"
					bExitMenu = True
					Client.OpenDatabase(sImportFile)
				Case "CancelButton1"
					bExitMenu = True
					bExitMenu = True
			End Select
	End Select
	If bExitMenu Then
		displayIt = 0
	Else
		displayIt = 1
	End If
	If sImportFile  = ""Then 
		'will display in the txtFilename box if no database has been selected or is already open
		DlgText "creatdbFileName","Please select a filename"
	Else
		'only shows the name of the file not the whole file path
		DlgText "creatdbFileName", iSplit(sImportFile  ,"","\",1,1)
	End If 
End Function 

Function ExcelImport As String 
	Dim obj As Object
	Dim task As Object
	Set task = Client.GetImportTask("ImportExcel")
	Set obj = client.commondialogs
		ExcelImport = obj.fileopen("","","All Files (*.*)|*.*||;")
	task.FileToImport = ExcelImport
	task.SheetToImport = "Carbon Total"
	task.OutputFilePrefix = "CountryEmissions"
	task.FirstRowIsFieldName = "TRUE"
	task.EmptyNumericFieldAsZero = "TRUE"
	task.PerformTask
	ExcelImport = task.OutputFilePath("Carbon Total")
	Set task = Nothing
	'Client.OpenDatabase(ExcelImport)
End Function