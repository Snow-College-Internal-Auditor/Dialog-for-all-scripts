import win32com.client as win32comclient

def creatOpen():
    idea = win32comclient.Dispatch(dispatch="Idea.IdeaClient")
    new_filename = idea.UniqueFileName("High Value")
    try:
        db = idea.opendatabase("Sample-Bank Transactions.IMD")
        task = db.Extraction()
        task.IncludeAllFields
        dbName = new_filename
        task.AddExtraction(dbName, "", "AMOUNT > 10000")
        task.PerformTask(1, db.Count)
    finally:
        idea.RefreshFileExplorer()
        task = None
        db = None  
        idea = None
        dbName = None

def export():
    idea = win32comclient.Dispatch(dispatch="Idea.IdeaClient")
    try:
        #File - Export Database: XLSX
        db = idea.opendatabase("High Value.IMD")
        task = db.ExportDatabase()
        task.IncludeAllFields
        eqn = ""
        task.to_excel(r"C:\Users\mckinnin.lloyd\Documents\Active Projects\P-card split\High Value.XLSX", "Database", "XLSX", 1, db.Count, eqn)
    finally:
        idea.RefreshFileExplorer()
        task = None
        db = None  
        idea = None

if __name__ == "__main__":
    creatOpen()
    export()

