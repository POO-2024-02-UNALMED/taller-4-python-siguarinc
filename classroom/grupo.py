from classroom.asignatura import Asignatura

class Grupo:
    grado= "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, *args, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista
        return lista
    def __str__(self):
        c= "Grupo de estudiantes: "+self._grupo
        return c
    
    @ classmethod
    def asignarNombre(cls, nombre):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre= "Grado 6"):
        cls.grado = nombre