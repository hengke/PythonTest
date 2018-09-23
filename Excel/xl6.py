#!/usr/bin/env python

from win32com.client import Dispatch
import win32com.client
# import win32api
import os


class Excel:
    def __init__(self, filename=None):
        self.xlApp = win32com.client.Dispatch('Excel.Application')
        if filename:
            self.filename = filename
            if os.path.exists(self.filename):
                self.xlBook = self.xlApp.Workbooks.Open(filename)
            else:
                self.xlBook = self.xlApp.Workbooks.Add()
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = 'Untitle'

    def save(self, newfilename=None):
        if newfilename:
            self.filename = newfilename
        self.xlBook.SaveAs(self.filename)

    def close(self):
        self.xlBook.Close(SaveChanges=0)
        del self.xlApp

    def copySheet(self, before):
        # "copy sheet"
        shts = self.xlBook.Worksheets
        shts(1).Copy(None, shts(1))

    def newSheet(self, newSheetName):
        sheet=self.xlBook.Worksheets.Add()
        sheet.Name=newSheetName
        sheet.Activate()

    def activateSheet(self,sheetName):
        self.xlBook.Worksheets(sheetName).Activate()

    def activeSheet(self):
        return self.xlApp.ActiveSheet;

    def getCell(self, row, col,sheet=None):
        # "Get value of one cell"
        if sheet:
            sht = self.xlBook.Worksheets(sheet)
        else:
            sht=self.xlApp.ActiveSheet
        return sht.Cells(row, col).Value

    def setCell(self, row, col, value,sheet='Sheet1'):
        # "set value of one cell"
        if sheet:
            sht = self.xlBook.Worksheets(sheet)
        else:
            sht=self.xlApp.ActiveSheet

        sht.Cells(row, col).Value = value
