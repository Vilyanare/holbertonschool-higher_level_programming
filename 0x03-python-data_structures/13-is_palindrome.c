#include "lists.h"
/**
 * free_listintrev - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listintrev(listintrev_t *head)
{
    listintrev_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
/**
 * revlist - reverse a listint_t list
 * @head: head of listint_t list
 * Return: address to head of reversed list
 */
listintrev_t *revlist(listint_t *head)
{
	listintrev_t *rev = NULL, *temp = NULL;

	while (head)
	{
		temp = malloc(sizeof(listintrev_t));
		if (temp == NULL)
		{
			if (rev)
				free_listintrev(rev);
			return (NULL);
		}
		temp->n = head->n;
		temp->oadd = head;
		if (rev)
			temp->next = rev;
		else
			temp->next = NULL;
		rev = temp;
		head = head->next;
	}
	return (rev);
}
/**
 * is_palindrome - check to see if data in a linked list is a palindrome
 * @head: head of linked list
 * Return: 0 if not 1 if is palindrome
 */
int is_palindrome(listint_t **head)
{
	listintrev_t *revfront = NULL;
	listint_t *front = NULL;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	front = *head;
	revfront = revlist(*head);
	while (revfront->n == front->n)
	{
		if (revfront->oadd == front || front->next == revfront->oadd)
			return (1);
		revfront = revfront->next;
		front = front->next;

	}
	return (0);
}
