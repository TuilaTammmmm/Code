#include <iostream>
using namespace std;

class Node
{
public:
    int data; // Dữ liệu của nút
    Node *next; // Con trỏ trỏ đến nút tiếp theo
    Node(int value) // Hàm khởi tạo
    {
        data = value; // Gán giá trị cho nút
        next = nullptr; // Ban đầu nút không trỏ đến nút nào
    }
};

// Lớp SLinkedListWithTail đại diện cho danh sách liên kết đơn có con trỏ tail
class SLinkedListWithTail
{
private:
    Node *head; // Con trỏ trỏ đến nút đầu tiên
    Node *tail; // Con trỏ trỏ đến nút cuối cùng

public:
    SLinkedListWithTail() // Hàm khởi tạo
    {
        head = nullptr; // Ban đầu danh sách rỗng
        tail = nullptr; // Ban đầu danh sách rỗng
    }

    // Hàm thêm một nút vào cuối danh sách
    void addLast(int i)
    {
        Node *newNode = new Node(i); // Tạo nút mới
        if (head == nullptr) // Nếu danh sách rỗng
        {
            head = newNode; // Nút mới là nút đầu tiên
            tail = newNode; // Nút mới cũng là nút cuối cùng
        }
        else
        {
            tail->next = newNode; // Liên kết nút cuối hiện tại với nút mới
            tail = newNode; // Cập nhật nút cuối
        }
    }

    // Hàm xóa nút cuối cùng trong danh sách
    void Remove()
    {
        if (head == nullptr) // Nếu danh sách rỗng
        {
            return; // Không làm gì cả
        }

        if (head == tail) // Nếu danh sách chỉ có một nút
        {
            delete head; // Xóa nút đó
            head = nullptr; // Cập nhật danh sách rỗng
            tail = nullptr; // Cập nhật danh sách rỗng
            return;
        }

        Node *current = head; // Bắt đầu từ nút đầu tiên
        while (current->next != tail) // Tìm nút trước nút cuối
        {
            current = current->next;
        }

        delete tail; // Xóa nút cuối
        tail = current; // Cập nhật nút cuối
        tail->next = nullptr; // Đảm bảo nút cuối không trỏ đến nút nào
    }

    // Hàm duyệt qua danh sách và in ra các giá trị
    void traverse()
    {
        Node *current = head; // Bắt đầu từ nút đầu tiên
        while (current != nullptr) // Duyệt đến khi hết danh sách
        {
            cout << current->data << " "; // In giá trị của nút
            current = current->next; // Chuyển sang nút tiếp theo
        }
        cout << endl; // Xuống dòng sau khi in xong
    }
};

int main()
{
    SLinkedListWithTail list; // Tạo danh sách liên kết đơn
    cout << "Nhap n: "; // tiếng việt: Nhập n
    int n;
    cin >> n; // Nhập số lượng phần tử

    for (int i = 1; i <= n; i++) // Thêm các phần tử từ 1 đến n
    {
        list.addLast(i);
    }
    list.traverse(); // Duyệt và in danh sách

    list.Remove(); // Xóa phần tử cuối
    list.traverse(); // Duyệt và in danh sách sau khi xóa
    
    list.addLast(n + 1); // Thêm phần tử mới vào cuối danh sách
    list.traverse(); // Duyệt và in danh sách sau khi thêm
    return 0;
}