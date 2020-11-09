class Comentario:
    def __init__(self, id, us_name, id_recet, description, fech, re_name):
        self.id = id
        self.us_name = us_name
        self.id_recet = id_recet
        self.description = description
        self.fech = fech
        self.re_name = re_name
    
    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getUs_name(self):
        return self.us_name

    def setUs_name(self, us_name):
        self.us_name = us_name

    def getId_recet(self):
        return self.id_recet

    def setId_recet(self, id_recet):
        self.id_recet = id_recet

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getFech(self):
        return self.fech

    def setFech(self, fech):
        self.fech = fech

    def getRe_name(self):
        return self.re_name

    def setRe_name(self, re_name):
        self.re_name = re_name


        