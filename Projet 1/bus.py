class busStop:
    def __init__ (self, name, arcs):
        self.name = name
        self.arcs = arcs

class link:
    def __init__ (self, arc, freeday):
        if (freeday):
            self.holyNameFrom = arc[0]
            self.holyNameTo = arc[1]
            self.holyTimeFrom = arc[2]
            self.holyTimeTo = arc[3]
            self.holyWeight = arc[4]
        else:
            self.nameFrom = arc[0]
            self.nameTo = arc[1]
            self.timeFrom = arc[2]
            self.timeTo = arc[3]
            self.weight = arc[4]