#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 1 if palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
listint_t *slow = *head, *fast = *head, *temp = *head, *dup = NULL;

if (*head == NULL || (*head)->next == NULL)
return (1);

while (1)
{
fast = fast->next->next;
if (!fast)
{
dup = slow->next;
break;
}
if (!fast->next)
{
dup = slow->next->next;
break;
}
slow = slow->next;
}

dup = reverse_listint(&dup);

while (dup && temp)
{
if (temp->n == dup->n)
{
dup = dup->next;
temp = temp->next;
}
else
return (0);
}

if (!dup)
return (1);

return (0);
}

/**
 * reverse_listint - Reverses a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the new head of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
listint_t *prev = NULL, *current = *head, *next = NULL;

while (current != NULL)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

*head = prev;
return (*head);
}
