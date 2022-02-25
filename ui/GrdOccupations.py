# -*- coding: utf-8 -*-

import dabo.ui
from dabo.dApp import dApp
if __name__ == "__main__":
    dabo.ui.loadUI("wx")
from GrdBase import GrdBase


class GrdOccupations(GrdBase):

    def afterInitAll(self):
        super(GrdOccupations, self).afterInitAll()
        biz = self.Form.getBizobj("Occupations")

        if not biz:
            # needed for testing
            class Biz(object):
                def getColCaption(self, caption):
                    return caption
            biz = Biz()



        # Delete or comment out any columns you don't want...
        self.addColumn(dabo.ui.dColumn(self, DataField="RecNo", 
                Caption=biz.getColCaption("RecNo"),
                Sortable=True, Searchable=True, Editable=False))

        self.addColumn(dabo.ui.dColumn(self, DataField="OccupationName", 
                Caption=biz.getColCaption("OccupationName"),
                Sortable=True, Searchable=True, Editable=False))


if __name__ == "__main__":
    from FrmOccupations import FrmOccupations
    app = dApp(MainFormClass=None)
    app.setup()
    class TestForm(FrmOccupations):
        def afterInit(self): pass
    frm = TestForm(Caption="Test Of GrdOccupations", Testing=True)
    test = GrdOccupations(frm)
    frm.Sizer.append1x(test)
    frm.show()
    app.start()
