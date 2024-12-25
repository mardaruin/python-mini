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

static PyObject* multiply_matrices(PyObject* mat1, PyObject* mat2) {
    Py_ssize_t rows1 = PyList_Size(mat1);
    Py_ssize_t cols1 = PyList_Size(PyList_GetItem(mat1, 0));
    Py_ssize_t rows2 = PyList_Size(mat2);
    Py_ssize_t cols2 = PyList_Size(PyList_GetItem(mat2, 0));

    if (cols1 != rows2) {
        PyErr_Format(PyExc_ValueError, "Матрицы имеют несовместимые размеры");
        return NULL;
    }

    PyObject* result = PyList_New(rows1);
    for (Py_ssize_t i = 0; i < rows1; ++i) {
        PyObject* row = PyList_New(cols2);
        for (Py_ssize_t j = 0; j < cols2; ++j) {
            double sum = 0.0;
            for (Py_ssize_t k = 0; k < cols1; ++k) {
                double a = PyFloat_AsDouble(PyList_GetItem(PyList_GetItem(mat1, i), k));
                double b = PyFloat_AsDouble(PyList_GetItem(PyList_GetItem(mat2, k), j));
                sum += a * b;
            }
            PyList_SetItem(row, j, PyFloat_FromDouble(sum));
        }
        PyList_SetItem(result, i, row);
    }
    return result;
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

    PyObject* result = mat_obj;
    for (int p = 1; p < power; ++p) {
        result = multiply_matrices(result, mat_obj);
    }

    return result;
}