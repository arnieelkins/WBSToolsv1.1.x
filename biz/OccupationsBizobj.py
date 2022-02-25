# -*- coding: utf-8 -*-
### Dabo Class Designer code. You many freely edit the code,
### but do not change the comments containing:
###         'Dabo Code ID: XXXX',
### as these are needed to link the code to the objects.

import dabo
class OccupationsBizobj(dabo.biz.dBizobj):
    def afterInit(self):
        #self.AutoPopulatePK = True
        #self.SaveNewUnchanged = True
        self.DataSource = "Occupations"
        self.KeyField = "OccupationRecNo"
        self.addFrom("Occupations")
        self.addField("OccupationRecNo")
        self.addField("OccupationName")

    def validateRecord(self):
        """Returning anything other than an empty string from
        this method will prevent the data from being saved.
        """
        return ""

    def getAvailableTypes(self):
        """Return a 2-tuple of lists of the types and their keys."""
        crs = self.getTempCursor()
        crs.execute("select OccupationRecNo, OccupationName from Occupations")
        ds = crs.getDataSet()
        # Create the lists
        names = [rec["OccupationName"] for rec in ds]
        keys = [rec["OccupationRecNo"] for rec in ds]
        return (names, keys)