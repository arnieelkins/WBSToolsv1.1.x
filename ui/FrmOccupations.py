# -*- coding: utf-8 -*-

import os
import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
    dabo.ui.loadUI("wx")
from FrmBase import FrmBase
from GrdOccupations import GrdOccupations
from PagSelectOccupations import PagSelectOccupations
from PagEditOccupations import PagEditOccupations


class FrmOccupations(FrmBase):

    def initProperties(self):
        super(FrmOccupations, self).initProperties()
        self.NameBase = "frmOccupations"
        self.Caption = "Occupations"
        self.SelectPageClass = PagSelectOccupations
        self.BrowseGridClass = GrdOccupations
        self.EditPageClass = PagEditOccupations


    def afterInit(self):
        if not self.Testing:
            # Instantiate the bizobj and register it with dForm, and then let the
            # superclass take over.
            app = self.Application
            bizOccupations = app.biz.Occupations(app.dbConnection)
            self.addBizobj(bizOccupations)
        super(FrmOccupations, self).afterInit()


if __name__ == "__main__":
    app = dApp(MainFormClass=None)
    app.setup()
    frm = FrmOccupations(Caption="Test Of FrmOccupations", Testing=True)
    frm.show()
    app.start()
