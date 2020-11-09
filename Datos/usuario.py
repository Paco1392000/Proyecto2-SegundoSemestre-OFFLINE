class Usuario:
    def __init__(self, id, nombre, apellido, edad, usuario, contrasena):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.usuario = usuario
        self.contrasena = contrasena

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad

    
    def getUsuario(self):
        return self.usuario

    def getContrasena(self):
        return self.contrasena

    def setId(self, id):
        self.id = id

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setEdad(self, edad):
        self.edad = edad

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setContrasena(self, contrasena):
        self.contrasena = contrasena