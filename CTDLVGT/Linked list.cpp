#include <iostream>
using namespace std;

struct Node {
    int data;
    Node* next;
    Node(int value) : data(value), next(nullptr) {}
};

class SLinkedList {
private:
    Node* head;

public:
    SLinkedList() : head(nullptr) {}

    void addFirst(int value) {
        Node* newNode = new Node(value);
        newNode->next = head;
        head = newNode;
    }

    void deleteHead() {
        if (head) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }

    void print() {
        Node* temp = head;
        while (temp) {
            cout << temp->data << " -> ";
            temp = temp->next;
        }
        cout << "NULL" << endl;
    }

    ~SLinkedList() {
        Node* temp;
        while (head) {
            temp = head;
            head = head->next;
            delete temp;
        }
    }
};

int main() {
    SLinkedList list;
    int n;
    cout << "Nhap so luong phan tu n: ";
    cin >> n;

    for (int i = n; i >= 1; i--) {
        list.addFirst(i);
    }

    cout << "Danh sach lien ket ban dau: ";
    list.print();

    list.deleteHead();
    cout << "Danh sach sau khi xoa phan tu dau: ";
    list.print();

    return 0;
}
