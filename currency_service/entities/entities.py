from datetime import datetime


class Currency:
    Code = ""
    Name = ""
    High = None
    Low = None
    VarBid = None
    Bid = None
    Ask = None
    LastUpdate = None

    def __init__(self, code, name, high, low, varBid, bid, ask):
        self.Code = code
        self.LastUpdate = datetime.now().time()
        self.Name = name
        self.High = high
        self.Low = low
        self.VarBid = varBid
        self.Bid = bid
        self.Ask = ask
