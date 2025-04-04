#include <iostream>
using namespace std;

class Node
{
public:
    int data;
    Node *next;
    Node(int value)
    {
        data = value;
        next = nullptr;
    }
};

class SLinkedListWithTail
{
private:
    Node *head;
    Node *tail;

public:
    SLinkedListWithTail()
    {
        head = nullptr;
        tail = nullptr;
    }

    void addLast(int i)
    {
        Node *newNode = new Node(i);
        if (head == nullptr)
        {
            head = newNode;
            tail = newNode;
        }
        else
        {
            tail->next = newNode;
            tail = newNode;
        }
    }

    void Remove()
    {
        if (head == nullptr)
        {
            return;
        }

        if (head == tail)
        {
            delete head;
            head = nullptr;
            tail = nullptr;
            return;
        }

        Node *current = head;
        while (current->next != tail)
        {
            current = current->next;
        }

        delete tail;
        tail = current;
        tail->next = nullptr;
    }

    void traverse()
    {
        Node *current = head;
        while (current != nullptr)
        {
            cout << current->data << " ";
            current = current->next;
        }
        cout << endl;
    }

    ~SLinkedListWithTail()
    {
        while (head != nullptr)
        {
            Node *temp = head;
            head = head->next;
            delete temp;
        }
    }
};

int main()
{
    SLinkedListWithTail list;
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        list.addLast(i);
    }
    list.traverse();
    list.Remove();
    list.traverse();
    list.addLast(n + 1);
    list.traverse();
    return 0;
}