#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info - prints some basic info about pylists
 * @p: the infamous list
 */
void print_python_list_info(PyObject *p)
{
	int x = 0; /*counter*/

	/*get size of the PyObject like this...*/
	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));

	/*Allocated elements*/
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	while (x < Py_SIZE(p))
	{
		/*Name of the type*/
		printf("Element %d: %s\n", x, Py_TYPE(PyList_GetItem(p, x))->tp_name);
		x++;
	}

}
