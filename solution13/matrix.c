#include <Python.h>
#include <math.h>

static PyObject *matrix_power(PyObject* self, PyObject* args);

static PyMethodDef ForeignMethods[] = {
    {"matrix_power", matrix_power, METH_VARARGS, "Возведение матрицы в степень"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef foreignmodule = {
   PyModuleDef_HEAD_INIT,
   "foreign",     /* name of module */
   "",          /* module documentation, may be NULL */
   -1,               /* size of per-interpreter state of the module,
                        or -1 if the module keeps state in global variables. */
   ForeignMethods
};

PyMODINIT_FUNC PyInit_foreign(void) {
   return PyModule_Create(&foreignmodule);
}

// Реализация функции
static PyObject *matrix_power(PyObject* self, PyObject* args) {
    PyObject* mat_obj;
    int power;

    if (!PyArg_ParseTuple(args, "Oi", &mat_obj, &power)) {
        return NULL; // Ошибка парсинга аргументов
    }

    Py_ssize_t rows = PyList_Size(mat_obj); // Количество строк
    Py_ssize_t cols = PyList_Size(PyList_GetItem(mat_obj, 0)); // Количество столбцов

    PyObject *result_mat = PyList_New(rows);
    for (int i = 0; i < rows; i++) {
        PyObject *row = PyList_New(cols);
        for (int j = 0; j < cols; j++) {
            double value = pow(PyFloat_AsDouble(PyList_GetItem(PyList_GetItem(mat_obj, i), j)), power);
            PyList_SetItem(row, j, PyFloat_FromDouble(value));
        }
        PyList_SetItem(result_mat, i, row);
    }

    return result_mat;
}