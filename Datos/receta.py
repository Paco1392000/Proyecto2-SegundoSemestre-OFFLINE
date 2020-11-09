class Receta:
    def __init__(self, id, autor, titulo, resumen, ingredientes, procedimiento, tiempo, imagen):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.resumen = resumen
        self.ingredientes = ingredientes
        self.procedimiento = procedimiento
        self.tiempo = tiempo
        self.imagen = imagen

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id
        
    def getAutor(self):
        return self.autor
    
    def setAutor(self, autor):
        self.autor = autor

    def getTitulo(self):
        return self.titulo

    def setTitulo(self, titulo):
        self.titulo = titulo

    def getResumen(self):
        return self.resumen

    def setResumen(self, resumen):
        self.resumen = resumen

    def getIngredientes(self):
        return self.ingredientes

    def setIngredientes(self, ingredientes):
        self.ingredientes = ingredientes

    def getProcedimiento(self):
        return self.procedimiento

    def setProcedimiento(self, procedimiento):
        self.procedimiento = procedimiento

    def getTiempo(self):
        return self.tiempo

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def getImagen(self):
        return self.imagen

    def setImagen(self, imagen):
        self.imagen = imagen
    
    

    
    
    

    

    

    

    
