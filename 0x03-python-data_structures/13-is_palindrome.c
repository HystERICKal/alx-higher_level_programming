#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 *put_node - put an int node infront of list
 *@head: first list element
 *@list_n: add this to the list
 *Return: new element location or NULL
 */
listint_t *put_node(listint_t **head, const int list_n)
{
	listint_t *the_node;

	the_node = malloc(sizeof(listint_t));
	if (the_node == NULL)
		return (NULL);
	the_node->n = list_n;
	the_node->next = *head;
	*head = the_node;
	return (the_node);
}
/**
 *is_palindrome - checks if singly linked list is palindrome
 *@head: first list element
 *Return: 1 or 0 depending if palindrome or not
 */
int is_palindrome(listint_t **head)
{
	listint_t *the_temp_head = *head;
	listint_t *temp = NULL;
	listint_t *other_temp = NULL;

	if (*head == NULL || the_temp_head->next == NULL)
		return (1);

	for (; the_temp_head != NULL; the_temp_head = the_temp_head->next)
	{
		put_node(&temp, the_temp_head->n);
	}

	other_temp = temp;

	for (; *head != NULL; *head = (*head)->next)
	{
		if ((*head)->n != other_temp->n)
		{
			free_listint(temp);
			return (0);
		}
		other_temp = other_temp->next;
	}
	free_listint(temp);
	return (1);
}
