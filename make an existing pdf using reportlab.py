from PyPDF2 import PdfReader
import os
# def mark_lab_manuals():
#     from reportlab.lib import colors, fonts
#     from reportlab.lib.pagesizes import letter, inch
#     from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
#     from reportlab.lib.styles import getSampleStyleSheet    
#     my_obj = []  
#     # Define the table data
#     data = [
#         ['<b>Assessment Rubric for Lab</b>', '', '', '', '', ''],
#         ['Performance metric', 'CLO', 'Able to complete the task \nover 80% (4-5)', 'Able to complete the task \n50-80% (2-3)', 'Able to complete the task \nbelow 50% (0-1)', 'Marks'],
#         ['Realization of experiment', '1', 'Executes without errors \nexcellent user prompts, \ngood use of symbols, \nspacing in output. \nThrough testing has been \ncompleted .', 'Executes without errors, \nuser prompts are \nunderstandable, \nminimum use of symbols \nor spacing in output. \nSome testing has been \ncompleted .', 'Does not execute due \nto syntax errors, \nruntime errors, user \nprompts are \nmisleading or non-\nexistent. No testing \nhas been completed.', ''],
#         ['Conducting experiment', '1', 'Able to make changes \nand answered all \nquestions.', 'Partially able to make \nchanges and few \nincorrect answers.', 'Unable to make \nchanges and answer \nall questions.', ''],
#         ['Computer use', '2', 'Document submission \ntimely.', 'Document submission \nlate.', 'Document \nsubmission not done.', ''],
#         ['Teamwork', '3', 'Actively engages and \ncooperates with other \ngroup member(s) in \neffective manner.', 'Cooperates with other \ngroup member(s) in a \nreasonable manner but \nconduct can be \nimproved.', 'Distracts or \ndiscourages other \ngroup members from \nconducting the \nexperiment', ''],
#         ['Laboratory safety \nand disciplinary \nrules', '3', 'Code comments are \nadded and does help the \nreader to understand the \ncode.', 'Code comments are \nadded and does not help \nthe reader to understand \nthe code.', 'Code comments are \nnot added.', ''],
#         ['Data collection', '3', 'Excellent use of white \nspace, creatively \norganized work, \nexcellent use of variables \nand constants, correct \nidentifiers for constants, \nNo line-wrap.', 'Includes name, and \nassignment, white space \nmakes the program fairly \neasy to read. Title, \norganized work, good use \nof variables.', 'Poor use of white \nspace (indentation, \nblank lines) \nmaking code hard to read, \ndisorganized and \nmessy.', ''],
#         ['Data analysis', '4', 'Solution is efficient, easy \nto understand, and \nmaintain .', 'A logical solution that is \neasy to follow but it is not \nthe most efficient.', 'A difficult and \ninefficient solution .', ''],
#         ['', '', 'Total (out of 35):', '', '', '']
#     ]

#     # Define column widths for each column
#     column_widths = [
#         1.5 * inch,  # Width for column 1
#         0.48 * inch,  # Width for column 2
#         1.5 * inch,  # Width for column 3
#         1.5 * inch,  # Width for column 4
#         1.5 * inch,  # Width for column 5
#         0.48 * inch   # Width for column 6
#     ]

#     # Define column widths for each column
#     row_heights = [
#         0.4 * inch,  # Width for column 1
#         0.4 * inch,  # Width for column 1
#         1.22 * inch,  # Width for column 2
#         0.61 * inch,  # Width for column 3
#         0.4 * inch,  # Width for column 4
#         0.89 * inch,  # Width for column 5
#         0.70 * inch,   # Width for column 6
#         1.21 * inch,  # Width for column 7
#         0.55 * inch,  # Width for column 8
#         0.3 * inch  # Width for column 8 
#     ]

#     # Create a PDF document
#     pdf = SimpleDocTemplate("table.pdf", pagesize=letter)

#     # Create a Table object
#     table = Table(data, colWidths=column_widths,rowHeights=row_heights)

#     # Define the style for the table
#     style = TableStyle([
#         ('BACKGROUND', (0, 0), (-1, 0), colors.white),
#         ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
#         ('ALIGN', (0, 0), (8, 8), 'LEFT'),
#         ('VALIGN', (0, 0), (8, 8), 'TOP'),
#         ('FONT', (0, 0), (-1, 0), 'Times-Roman'),
#         ('FONT', (0, 1), (-1, -1), 'Times-Roman'),  # Change font to Times New Roman
#         ('FONTSIZE', (0, 0), (-1, -1), 9), # Change font size to 9
#         ('GRID', (0, 1), (-1, -1), 0.25, colors.black),
#         ('LEFTPADDING', (0, 0), (-1, -1), 5),  # Add some left padding to the cells
#         ('SPAN',(0,9),(1,9)),
#         ('SPAN',(1,9),(2,9)),
#         ('SPAN',(2,9),(3,9)),
#         ('SPAN',(3,9),(4,9)),
        
#     ])

#     # Apply the style to the table
#     table.setStyle(style)
#     table.wrapOn(pdf, 0, 0)
#     # Add the table to the PDF document
#     pdf.build([table]) 

# mark_lab_manuals()
