Begin Dialog PythonDemo 40,21,298,188,"Python Demo", .displayIt
  OKButton 37,134,40,14, "OK", .OKButton1
  CancelButton 99,135,40,14, "Cancel", .CancelButton1
End Dialog
Dim bExitScript

Sub Main
	Call menu()
End Sub

Function menu()
	Dim dlg As PythonDemo
	Dim button As Integer
	
	button = Dialog(dlg)
End Function
