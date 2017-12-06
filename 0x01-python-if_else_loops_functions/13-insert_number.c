#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Insert a node in numeric order to a list
 * @head: beggining of list
 * @number: data to add to member n
 * Return: Address to new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *find = *head;
	listint_t *temp = NULL;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	temp->next = NULL;
	if (head == NULL)
		return (NULL);
	if (*head == NULL)
	{
		*head = temp;
		return (temp);
	}
	if (number < find->n)
	{
		temp->next = find;
		*head = temp;
		return (temp);
	}
	while (find->next)
	{
		if (number < find->next->n)
		{
			temp->next = find->next;
			find->next = temp;
			return (temp);
		}
		find = find->next;
	}
	find->next = temp;
	return (temp);
}
