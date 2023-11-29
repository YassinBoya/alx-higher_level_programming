#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
*insert_node - a function that insert a numebr into a sorted linked list
*@head: the linked list
*@number: number to add
*Return: the nwe list with the new number added
*/

listint_t *insert_node(listint_t **head, int number)
{
listint_t *current = *head, *new = NULL, *temp = NULL;

if (!head)
return (NULL);
new = malloc(sizeof(listint_t));

if (!new)
return (NULL);

new->n = number;
new->next = NULL;

if (!*head || (*head)->n > number)
{
new->next = *head;
return (*head = new);
}
else
{
while (current && current->n < number)
{
temp = current;
current = current->next;
}
temp->next = new;
new->next = current;
}
return (new);
}

