#define PY_SSIZE_CLEAN
#include <Python.h>

int
main(int argc, char *argv[])
{
	Py_Initialize();
	pName = PyUnicode_DecodeFSDefault(argv[1]);
	pModule = PyImport_Import(pName);
}