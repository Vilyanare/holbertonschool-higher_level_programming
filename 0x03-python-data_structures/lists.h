#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;
/**
 * struct listintrev_s - singly linked list
 * @n: integer
 * @next: points to the next node
 * @oadd: address of node in non reversed list
 *
 * Description: reversed list holding address of lisint_t node
 */
typedef struct listintrev_s
{
    int n;
    struct listintrev_s *next;
    struct listint_s *oadd;
} listintrev_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
void free_listintrev(listintrev_t *head);
listintrev_t *revlist(listint_t *head);
int is_palindrome(listint_t **head);

#endif /* LISTS_H */
