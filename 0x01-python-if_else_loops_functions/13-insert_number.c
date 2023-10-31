#include "lists.h"
/**
 * insert_node - put number into linked list that is sorted
 * @head: first element of linked list
 * @number: number to put in
 * Return: address of new nod or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *the_node_container = *head, *new;

	new = malloc(sizeof(listint_t)); /*memory alloc*/

	if (new == NULL)
		return (NULL); /*fail*/
	new->n = number; /*the new number*/

	if (the_node_container == NULL || the_node_container->n >= number)
	{
		new->next = the_node_container;
		*head = new;
		return (new);
	}

	for (; the_node_container && the_node_container->next &&
			the_node_container->next->n < number;
			the_node_container = the_node_container->next)
		continue;

	new->next = the_node_container->next;
	the_node_container->next = new;

	return (new);
}
