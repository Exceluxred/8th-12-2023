# import pyperclip
# import subprocess

# def paste_from_clipboard_to_cmd():
#     # Get clipboard contents
#     clipboard_text = pyperclip.paste()

#     # Print to console (optional)
#     print("Clipboard contents:")
#     print(clipboard_text)

#     # Execute command in command prompt
#     subprocess.run(["cmd", "/c", "echo", clipboard_text])

# if __name__ == "__main__":
#     paste_from_clipboard_to_cmd()  ===================================================================================

# import pyperclip
# import subprocess
# import time

# def paste_from_clipboard_to_cmd():
#     last_clipboard_text = None
    
#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new, paste it to the command prompt
#         if clipboard_text != last_clipboard_text:
#             last_clipboard_text = clipboard_text
#             print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Execute command in command prompt
#             subprocess.run(["cmd", "/c", "echo", clipboard_text])
        
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_cmd()=======================================================

# import pyperclip
# import subprocess
# import time

# def paste_from_clipboard_to_cmd():
#     last_clipboard_text = None
#     pasted_texts = set()
    
#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new and hasn't been pasted before, paste it to the command prompt
#         if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
#             last_clipboard_text = clipboard_text
#             pasted_texts.add(clipboard_text)
#             #print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Execute command in command prompt
#             #subprocess.run(["cmd", "/c", "echo", clipboard_text])
        
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_cmd()====================

# import pyperclip
# import time
# import win32com.client as win32

# def paste_from_clipboard_to_word():
#     last_clipboard_text = None
#     pasted_texts = set()
    
#     # Start an instance of Word
#     word_app = win32.gencache.EnsureDispatch('Word.Application')
#     word_app.Visible = True
    
#     # Create a new document
#     doc = word_app.Documents.Add()

#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new and hasn't been pasted before, paste it to the Word document
#         if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
#             last_clipboard_text = clipboard_text
#             pasted_texts.add(clipboard_text)
#             print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Add the text to the Word document
#             doc.Content.InsertAfter(clipboard_text + '\n')
        
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_word()=========================================================

# import pyperclip
# import time
# import win32com.client as win32

# def paste_from_clipboard_to_word():
#     last_clipboard_text = None
#     pasted_texts = set()
    
#     # Start an instance of Word
#     word_app = win32.gencache.EnsureDispatch('Word.Application')
#     word_app.Visible = True
    
#     # Create a new document
#     doc = word_app.Documents.Add()

#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new and hasn't been pasted before, paste it to the Word document
#         if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
#             last_clipboard_text = clipboard_text
#             pasted_texts.add(clipboard_text)
#             print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Move to the end of the document and insert the clipboard text followed by a new paragraph
#             word_app.Selection.EndKey(Unit=6)  # Move the cursor to the end of the document
#             word_app.Selection.TypeText(clipboard_text)  # Insert the clipboard text
#             word_app.Selection.TypeParagraph()  # Simulate hitting Enter
            
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_word()===========================

# import pyperclip
# import time
# import win32com.client as win32

# def paste_from_clipboard_to_excel():
#     last_clipboard_text = None
#     pasted_texts = set()
    
#     # Start an instance of Excel
#     excel_app = win32.gencache.EnsureDispatch('Excel.Application')
#     excel_app.Visible = True
    
#     # Create a new workbook and select the first sheet
#     workbook = excel_app.Workbooks.Add()
#     sheet = workbook.Worksheets(1)

#     row = 1  # Start at the first row

#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new and hasn't been pasted before, paste it to the Excel sheet
#         if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
#             last_clipboard_text = clipboard_text
#             pasted_texts.add(clipboard_text)
#             print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Insert the clipboard text into the current row and move to the next row
#             sheet.Cells(row, 1).Value = clipboard_text
#             row += 1
        
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_excel()===================================================

# import pyperclip
# import time
# import win32com.client as win32

# def paste_from_clipboard_to_excel():
#     last_clipboard_text = None
#     pasted_texts = set()
    
#     # Start an instance of Excel
#     excel_app = win32.gencache.EnsureDispatch('Excel.Application')
#     excel_app.Visible = True
    
#     # Create a new workbook and select the first sheet
#     workbook = excel_app.Workbooks.Add()
#     sheet = workbook.Worksheets(1)

#     row = 1  # Start at the first row

#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new and hasn't been pasted before, paste it to the Excel sheet
#         if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
#             last_clipboard_text = clipboard_text
#             pasted_texts.add(clipboard_text)
#             print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Insert the clipboard text into the current row
#             cell = sheet.Cells(row, 1)
#             cell.Value = clipboard_text
            
#             # Simulate double-clicking the cell to enter edit mode
#             cell.Select()
#             excel_app.SendKeys("{F2}")  # F2 key enters edit mode in Excel
#             time.sleep(0.1)
#             excel_app.SendKeys("{ENTER}")  # Enter key exits edit mode and moves to the next cell
            
#             # Move to the next row
#             row += 1
        
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_excel()========================


# import pyperclip
# import time
# import win32com.client as win32

# def paste_from_clipboard_to_excel():
#     last_clipboard_text = None
#     pasted_texts = set()
    
#     # Start an instance of Excel
#     excel_app = win32.gencache.EnsureDispatch('Excel.Application')
#     excel_app.Visible = True
    
#     # Create a new workbook and select the first sheet
#     workbook = excel_app.Workbooks.Add()
#     sheet = workbook.Worksheets(1)

#     row = 1  # Start at the first row

#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new and hasn't been pasted before, paste it to the Excel sheet
#         if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
#             last_clipboard_text = clipboard_text
#             pasted_texts.add(clipboard_text)
#             print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Insert the clipboard text into the current row
#             cell = sheet.Cells(row, 1)
#             cell.Value = clipboard_text

#             # Check if the clipboard text is a URL and add it as a hyperlink
#             if clipboard_text.startswith('http://') or clipboard_text.startswith('https://'):
#                 sheet.Hyperlinks.Add(Anchor=cell, Address=clipboard_text, TextToDisplay=clipboard_text)
            
#             # Simulate double-clicking the cell to enter edit mode
#             cell.Select()
#             excel_app.SendKeys("{F2}")  # F2 key enters edit mode in Excel
#             time.sleep(0.1)
#             excel_app.SendKeys("{ENTER}")  # Enter key exits edit mode and moves to the next cell
            
#             # Move to the next row
#             row += 1
        
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_excel()

# import pyperclip
# import time
# import win32com.client as win32

# def paste_from_clipboard_to_excel():
#     last_clipboard_text = None
#     pasted_texts = set()
    
#     # Start an instance of Excel
#     excel_app = win32.gencache.EnsureDispatch('Excel.Application')
#     excel_app.Visible = True
    
#     # Create a new workbook and select the first sheet
#     workbook = excel_app.Workbooks.Add()
#     sheet = workbook.Worksheets(1)

#     row = 1  # Start at the first row

#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new and hasn't been pasted before, paste it to the Excel sheet
#         if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
#             last_clipboard_text = clipboard_text
#             pasted_texts.add(clipboard_text)
#             print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Insert the clipboard text into the current row
#             cell = sheet.Cells(row, 1)
#             cell.Value = clipboard_text

#             # Check if the clipboard text is a URL and add it as a hyperlink
#             if clipboard_text.startswith('http://') or clipboard_text.startswith('https://'):
#                 sheet.Hyperlinks.Add(Anchor=cell, Address=clipboard_text, TextToDisplay=clipboard_text)
            
#             # Simulate double-clicking the cell to enter edit mode
#             cell.Select()
#             excel_app.SendKeys("{F2}")  # F2 key enters edit mode in Excel
#             time.sleep(0.1)
#             excel_app.SendKeys("{ENTER}")  # Enter key exits edit mode and moves to the next cell
            
#             # Move to the next row
#             row += 1
        
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_excel()

# import pyperclip
# import time
# import win32com.client as win32

# def paste_from_clipboard_to_excel():
#     last_clipboard_text = None
#     pasted_texts = set()
    
#     # Start an instance of Excel
#     excel_app = win32.Dispatch('Excel.Application')
#     excel_app.Visible = True
    
#     # Create a new workbook and select the first sheet
#     workbook = excel_app.Workbooks.Add()
#     sheet = workbook.Worksheets(1)

#     row = 1  # Start at the first row

#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new and hasn't been pasted before, paste it to the Excel sheet
#         if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
#             last_clipboard_text = clipboard_text
#             pasted_texts.add(clipboard_text)
#             print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Insert the clipboard text into the current row
#             cell = sheet.Cells(row, 1)
#             cell.Value = clipboard_text

#             # Check if the clipboard text is a URL and add it as a hyperlink
#             if clipboard_text.startswith('http://') or clipboard_text.startswith('https://'):
#                 sheet.Hyperlinks.Add(Anchor=cell, Address=clipboard_text, TextToDisplay=clipboard_text)
            
#             # Select the cell and enter edit mode programmatically
#             cell.Select()
#             cell.Activate()
#             excel_app.ActiveCell.Offset(1, 0).Select()  # Move to the next cell
            
#             # Move to the next row
#             row += 1
        
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_excel()

# import pyperclip
# import time
# import win32com.client as win32

# def paste_from_clipboard_to_excel():
#     last_clipboard_text = None
#     pasted_texts = set()
    
#     # Start an instance of Excel
#     excel_app = win32.Dispatch('Excel.Application')
#     excel_app.Visible = True  # Ensure the Excel application is visible
    
#     # Create a new workbook and select the first sheet
#     workbook = excel_app.Workbooks.Add()
#     sheet = workbook.Worksheets(1)

#     row = 1  # Start at the first row

#     while True:
#         # Get current clipboard contents
#         clipboard_text = pyperclip.paste()
        
#         # If clipboard content is new and hasn't been pasted before, paste it to the Excel sheet
#         if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
#             last_clipboard_text = clipboard_text
#             pasted_texts.add(clipboard_text)
#             print("New clipboard contents detected:")
#             print(clipboard_text)
            
#             # Insert the clipboard text into the current row
#             cell = sheet.Cells(row, 1)
#             cell.Value = clipboard_text

#             # Check if the clipboard text is a URL and add it as a hyperlink
#             if clipboard_text.startswith('http://') or clipboard_text.startswith('https://'):
#                 sheet.Hyperlinks.Add(Anchor=cell, Address=clipboard_text, TextToDisplay=clipboard_text)
            
#             # Move to the next cell in the row to simulate hitting Enter
#             next_cell = sheet.Cells(row + 1, 1)
#             next_cell.Select()
            
#             # Move to the next row
#             row += 1
        
#         # Sleep for a short period to avoid excessive CPU usage
#         time.sleep(1)

# if __name__ == "__main__":
#     paste_from_clipboard_to_excel()


import pyperclip
import time
import win32com.client as win32

def paste_from_clipboard_to_excel():
    last_clipboard_text = None
    pasted_texts = set()
    
    # Start an instance of Excel
    excel_app = win32.DispatchEx('Excel.Application')
    excel_app.Visible = True  # Ensure the Excel application is visible
    
    # Create a new workbook and select the first sheet
    workbook = excel_app.Workbooks.Add()
    sheet = workbook.Worksheets(1)

    row = 1  # Start at the first row

    while True:
        # Get current clipboard contents
        clipboard_text = pyperclip.paste()
        
        # If clipboard content is new and hasn't been pasted before, paste it to the Excel sheet
        if clipboard_text != last_clipboard_text and clipboard_text not in pasted_texts:
            last_clipboard_text = clipboard_text
            pasted_texts.add(clipboard_text)
            print("New clipboard contents detected:")
            print(clipboard_text)
            
            # Insert the clipboard text into the current row
            cell = sheet.Cells(row, 1)
            cell.Value = clipboard_text

            # Check if the clipboard text is a URL and add it as a hyperlink
            if clipboard_text.startswith('http://') or clipboard_text.startswith('https://'):
                sheet.Hyperlinks.Add(Anchor=cell, Address=clipboard_text, TextToDisplay=clipboard_text)
            
            # Move to the next cell in the row to simulate hitting Enter
            next_cell = sheet.Cells(row + 1, 1)
            next_cell.Select()
            
            # Move to the next row
            row += 1
        
        # Sleep for a short period to avoid excessive CPU usage
        time.sleep(1)

if __name__ == "__main__":
    paste_from_clipboard_to_excel()


