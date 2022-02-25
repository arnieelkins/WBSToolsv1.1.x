# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
###         'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

## *!* ## Dabo Code ID: dButton-dPanel-297
def onHit(self, evt):
    self.Form.next()


## *!* ## Dabo Code ID: dButton-dPanel-492
def onHit(self, evt):
    #new button
    self.Form.addOccupation()


## *!* ## Dabo Code ID: dButton-dPanel-718
def onHit(self, evt):
    #delete button
    self.Form.deleteOccupation()


## *!* ## Dabo Code ID: dButton-dPanel-133
def onHit(self, evt):
    self.Form.save()


## *!* ## Dabo Code ID: dButton-dPanel-697
def onHit(self, evt):
    self.Form.last()


## *!* ## Dabo Code ID: dButton-dPanel-613
def onHit(self, evt):
    self.Form.first()


## *!* ## Dabo Code ID: dButton-dPanel-507
def onHit(self, evt):
    self.Form.prior()


## *!* ## Dabo Code ID: dForm-top
def initProperties(self):
    self.SaveRestorePosition = True
    app = self.Application
    self.FontSize = app.PreferenceManager.getValue("fontsize")
    self.Icon = "icons/wbs.ico"


def afterInitAll(self):
    self.requery()


def addOccupation(self):
    try:
        self.new()
        dlg = dabo.ui.info('Output from save operation = ' + str(self.save()) + '.\n')
        self.requery()
    except:
        dabo.ui.exclaim('Uh oh, something went wrong!  Better check the log file!  ' + str(traceback.format_exc()))


def deleteOccupation(self):
    app = self.Application
    bizObj = self.PrimaryBizobj
    currentRecord = bizObj.Record
    fields = ['OccupationRecNo', 'OccupationName']
    tempString = ''
    for field in fields:
        tempString = tempString + str(field) + ' = ' + str(currentRecord[field]) + '\n'
    response = dabo.ui.areYouSure(message = 'You are about to delete this record!\n' + tempString,
                                    defaultNo = True,
                                    cancelButton = False,
                                    requestUserAttention=True)
    if response == True:
        try:
            dlg = dabo.ui.info('Output from delete operation = ' + str(bizObj.delete()) + '.\n')
            self.requery()
        except:
            dabo.ui.exclaim("Uh oh, something went wrong!  Better check the log file!")


def createBizobjs(self):
    app = self.Application
    occupationsBizobj = app.biz.OccupationsBizobj(app.dbConnection)
    self.addBizobj(occupationsBizobj)


## *!* ## Dabo Code ID: dButton-dPanel
def onHit(self, evt):
    self.Form.requery()
