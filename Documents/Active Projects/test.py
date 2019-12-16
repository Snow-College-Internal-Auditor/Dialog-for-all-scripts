import win32com.client as win32comclient

if __name__ == "__main__":
    idea = win32comclient.Dispatch(dispatch="Idea.IdeaClient")
    new_filename = idea.UniqueFileName("High Value")
    try:
        db = idea.opendatabase(new_filename)
        task = db.Extraction()
        task.IncludeAllFields
        task.AddExtraction(new_filename, "", "AMOUNT > 10000")
        task.PerformTask(1, db.Count)
    finally:
        idea.RefreshFileExplorer()
        task = None
        db = None
        idea = None

