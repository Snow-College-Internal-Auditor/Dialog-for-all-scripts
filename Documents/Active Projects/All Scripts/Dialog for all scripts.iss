Begin Dialog NewDialog 50,10,310,104,"All Scripts", .NewDialog
  Text 14,5,81,11, "Split Transaction", .Text1
  Text 112,6,81,11, "Personal Purchaes", .Text2
  Text 203,6,81,12, "Double Reimbursement", .Text3
  PushButton 9,22,68,14, "Whole Year", .PushButton1
  PushButton 9,42,68,14, "Exact Month", .PushButton2
  PushButton 108,22,68,14, "Personal Purchaes", .PushButton3
  PushButton 205,22,68,14, "Whole Pull", .PushButton4
End Dialog
Dim dlg As NewDialog

Sub Main
	Call DialogCall()
End Sub

Function DialogCall()
	button = Dialog(dlg)
	If button = 1 Then
		Client.RunIDEAScriptEx "C:\Users\mckinnin.lloyd\Documents\Active Projects\Pcard-Split-Transaction\Split Transaction\whole_year.iss", "", "", "", ""
	ElseIf button = 2 Then
		Client.RunIDEAScriptEx "C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\Split Transaction\Pulls_one_month.iss", "", "", "", ""
	ElseIf button = 3 Then
		Client.RunIDEAScriptEx "C:\Users\mckinnin.lloyd\Documents\Active Projects\Personal Purchas\P-card_Personal_Purchases\Personal_Purchases.iss", "", "", "", ""
	ElseIf button = 4 Then
		Client.RunIDEAScriptEx "C:\Users\mckinnin.lloyd\Documents\Active Projects\Double-Reimbursement\Main Script\Whole_Pull.iss", "", "", "", ""
	End If
End Function
