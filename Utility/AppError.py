class AppError (object):
    HasError = True
    TheError = None
    TheData = None
    def __init__(self):
        self.HasError = True
        self.TheError = "Some Application Related Error"
        self.TheData = None
    def __str__(self):
        return self.TheError