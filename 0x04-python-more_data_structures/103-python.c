#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_bytes -  basic info about pybytes
 * @p: python pybyte
 */
void print_python_bytes(PyObject *p)
{
	int x = 0;
	long int hold;
	char *temp = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &temp, &hold);

	printf("  size: %li\n", hold);
	printf("  trying string: %s\n", temp);
	if (hold < 10)
		printf("  first %li bytes:", hold + 1);
	else
		printf("  first 10 bytes:");

	while (x <= hold && x < 10)
	{
		printf(" %02hhx", temp[x]);
		x++;
	}

	printf("\n");
}
/**
 * print_python_list -  basic info about pylist
 * @p: pylist
 */
void print_python_list(PyObject *p)
{
	PyListObject *bucket = (PyListObject *)p;
	long int hold = PyList_Size(p);
	int x = 0;
	const char *str_chr;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", hold);
	printf("[*] Allocated = %li\n", bucket->allocated);

	while (x < hold)
	{
		str_chr = (bucket->ob_item[x])->ob_type->tp_name;
		printf("Element %x: %s\n", x, str_chr);
		if (!strcmp(str_chr, "bytes"))
			print_python_bytes(bucket->ob_item[x]);

		x++;
	}
}
