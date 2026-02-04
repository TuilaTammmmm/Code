import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc
from datetime import datetime

# -------------------------------------------------------------
# 1. THÔNG TIN KẾT NỐI
# -------------------------------------------------------------
SERVER = r'DUYTAM\SQLEXPRESS'
DATABASE = 'BTL_QUANLYPHONGKHAM'
USERNAME = 'sqlserver'
PASSWORD = '123456'
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

def get_connection():
    return pyodbc.connect(connection_string)

# Từ điển (Dictionaries) toàn cục để lưu trữ dữ liệu combobox
data_cache = {
    "benhnhan": {}, # { 'BN001': 'Nguyễn Văn A' }
    "nhanvien": {}, # { 'NV001': 'Trần Thị B' }
    "bacsi": {},     # { 'BS001': 'Bác Sĩ C' }
    "thuoc": {},     # { 'T001': 'Paracetamol' }
    "dichvu": {}      # { 'DV001': 'Khám Tổng Quát' }
}

def load_all_data_caches():
    """Tải tất cả dữ liệu danh mục vào cache để dùng cho Combobox"""
    try:
        with get_connection() as conn:
            cursor = conn.cursor()
            
            # 1. Bệnh Nhân
            cursor.execute("SELECT MaBenhNhan, HoTen FROM BenhNhan.BenhNhan")
            data_cache["benhnhan"] = {ma: ten for ma, ten in cursor.fetchall()}
            
            # 2. Nhân Viên (Tất cả)
            cursor.execute("SELECT MaNhanVien, HoTen FROM NhanVien.NhanVien")
            data_cache["nhanvien"] = {ma: ten for ma, ten in cursor.fetchall()}

            # 3. Bác Sĩ (Chỉ Bác Sĩ)
            cursor.execute("SELECT BS.MaBacSi, NV.HoTen FROM NhanVien.BacSi BS JOIN NhanVien.NhanVien NV ON BS.MaBacSi = NV.MaNhanVien")
            data_cache["bacsi"] = {ma: ten for ma, ten in cursor.fetchall()}

            # 4. Thuốc
            cursor.execute("SELECT MaThuoc, TenThuoc FROM Thuoc.Thuoc")
            data_cache["thuoc"] = {ma: ten for ma, ten in cursor.fetchall()}

            # 5. Dịch Vụ
            cursor.execute("SELECT MaDichVu, TenDichVu FROM DichVu.DichVu")
            data_cache["dichvu"] = {ma: ten for ma, ten in cursor.fetchall()}

    except Exception as e:
        messagebox.showerror("Lỗi Tải Dữ Liệu", f"Không thể tải dữ liệu danh mục: {e}")
def convert_name_to_password(name):
    """
    Chuyển đổi tên đầy đủ (ví dụ: 'Đào Duy Tâm') 
    thành mật khẩu không dấu, không cách, viết thường (ví dụ: 'daoduytam')
    """
    if not name:
        return ""
    
    s = name.lower()
    
    # Xóa dấu
    s = s.replace('á', 'a').replace('à', 'a').replace('ả', 'a').replace('ã', 'a').replace('ạ', 'a')
    s = s.replace('ă', 'a').replace('ằ', 'a').replace('ắ', 'a').replace('ẳ', 'a').replace('ẵ', 'a').replace('ặ', 'a')
    s = s.replace('â', 'a').replace('ầ', 'a').replace('ấ', 'a').replace('ẩ', 'a').replace('ẫ', 'a').replace('ậ', 'a')
    s = s.replace('é', 'e').replace('è', 'e').replace('ẻ', 'e').replace('ẽ', 'e').replace('ẹ', 'e')
    s = s.replace('ê', 'e').replace('ề', 'e').replace('ế', 'e').replace('ể', 'e').replace('ễ', 'e').replace('ệ', 'e')
    s = s.replace('í', 'i').replace('ì', 'i').replace('ỉ', 'i').replace('ĩ', 'i').replace('ị', 'i')
    s = s.replace('ó', 'o').replace('ò', 'o').replace('ỏ', 'o').replace('õ', 'o').replace('ọ', 'o')
    s = s.replace('ô', 'o').replace('ồ', 'o').replace('ố', 'o').replace('ổ', 'o').replace('ỗ', 'o').replace('ộ', 'o')
    s = s.replace('ơ', 'o').replace('ờ', 'o').replace('ớ', 'o').replace('ở', 'o').replace('ỡ', 'o').replace('ợ', 'o')
    s = s.replace('ú', 'u').replace('ù', 'u').replace('ủ', 'u').replace('ũ', 'u').replace('ụ', 'u')
    s = s.replace('ư', 'u').replace('ừ', 'u').replace('ứ', 'u').replace('ử', 'u').replace('ữ', 'u').replace('ự', 'u')
    s = s.replace('ý', 'y').replace('ỳ', 'y').replace('ỷ', 'y').replace('ỹ', 'y').replace('ỵ', 'y')
    s = s.replace('đ', 'd')
    
    # Xóa khoảng trắng
    s = s.replace(' ', '')
    
    return s


# #############################################################
# PHẦN 0: LỚP CỬA SỔ ĐĂNG NHẬP (ĐÃ CẬP NHẬT CHO BỆNH NHÂN)
# #############################################################

def center_window_on_screen(win, width, height):
    """Tính toán và căn giữa cửa sổ trên màn hình"""
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')

class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Đăng Nhập Hệ Thống")
        
        LOGIN_WIDTH = 300
        LOGIN_HEIGHT = 150
        center_window_on_screen(self, LOGIN_WIDTH, LOGIN_HEIGHT)
        
        self.resizable(False, False)
        
        self.user_role = None 
        self.user_id = None # <-- THÊM MỚI: Để lưu MaBenhNhan hoặc MaNhanVien
        
        self.transient(parent)
        self.grab_set()
        
        tk.Label(self, text="Mã Đăng Nhập (Mã NV hoặc Mã BN):").pack(pady=(10,0))
        self.entry_username = tk.Entry(self, width=30)
        self.entry_username.pack()

        tk.Label(self, text="Mật Khẩu:").pack(pady=(5,0))
        self.entry_password = tk.Entry(self, width=30, show="*")
        self.entry_password.pack()
        
        self.entry_password.bind("<Return>", self.check_login)

        tk.Button(self, text="Đăng Nhập", command=self.check_login).pack(pady=10)
        
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def check_login(self, event=None):
        username = self.entry_username.get()
        password_input = self.entry_password.get()

        if not username or not password_input:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập Mã Đăng Nhập và Mật Khẩu.", parent=self)
            return

        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                
                # BƯỚC 1: Thử đăng nhập với tư cách NHÂN VIÊN
                query_nv = "SELECT ChucVu FROM NhanVien.NhanVien WHERE MaNhanVien = ? AND MatKhau = ?"
                cursor.execute(query_nv, (username, password_input))
                result_nv = cursor.fetchone()
                
                if result_nv:
                    self.user_role = result_nv[0] # (ví dụ: 'Bác Sĩ', 'Thu Ngân')
                    self.user_id = username # Lưu MaNhanVien
                    self.destroy() 
                    return
                
                # BƯỚC 2: Nếu không phải Nhân Viên, thử đăng nhập với tư cách BỆNH NHÂN
                query_bn = "SELECT HoTen FROM BenhNhan.BenhNhan WHERE MaBenhNhan = ?"
                cursor.execute(query_bn, (username))
                result_bn = cursor.fetchone()
                
                if result_bn:
                    ho_ten_goc = result_bn[0]
                    mat_khau_chuan = convert_name_to_password(ho_ten_goc)
                    
                    # So sánh mật khẩu người dùng nhập (đã chuẩn hóa) với mật khẩu chuẩn
                    if convert_name_to_password(password_input) == mat_khau_chuan:
                        self.user_role = "BENHNHAN" # Vai trò đặc biệt
                        self.user_id = username # Lưu MaBenhNhan
                        self.destroy()
                        return
                
                # Nếu cả 2 đều thất bại
                messagebox.showerror("Lỗi Đăng Nhập", "Mã Đăng Nhập hoặc Mật Khẩu không đúng.", parent=self)
                
        except Exception as e:
            messagebox.showerror("Lỗi CSDL", f"Không thể kiểm tra đăng nhập: {e}", parent=self)

    def on_closing(self):
        self.user_role = None 
        self.user_id = None
        self.destroy()


  # #############################################################
# PHẦN 0.5: HÀM PHÂN QUYỀN (ĐÃ CẬP NHẬT CHO BỆNH NHÂN)
# #############################################################

def setup_ui_for_role(notebook, role, all_tabs):
    """
    Hàm này ẩn/hiện các tab dựa trên vai trò (ChucVu) của người dùng.
    """
    
    for tab in all_tabs.values():
        try:
            notebook.forget(tab)
        except tk.TclError:
            pass 
    
    role_check = role.strip()

    # === PHÂN QUYỀN MỚI ===
    
    if role_check == "BENHNHAN":
        # 1. Bệnh Nhân: Chỉ thấy 2 tab cá nhân
        notebook.add(all_tabs['tab_benhan_canhan'], text='Hồ Sơ Khám Bệnh Của Tôi')
        notebook.add(all_tabs['tab_thanhtoan_canhan'], text='Lịch Sử Thanh Toán Của Tôi')

    elif role_check == 'Lễ Tân' or role_check == 'Tiếp Nhận':
        # 2. Lễ tân
        notebook.add(all_tabs['tab_tiep_nhan'], text=' 1. TIẾP NHẬN ')
        notebook.add(all_tabs['tab_benh_nhan'], text='QL Bệnh Nhân')

    elif role_check == 'Bác Sĩ':
        # 3. Bác sĩ
        notebook.add(all_tabs['tab_kham_benh'], text=' 2. KHÁM BỆNH ')
        
    elif role_check == 'Thu Ngân':
        # 4. Thu ngân
        notebook.add(all_tabs['tab_thanh_toan'], text=' 3. THANH TOÁN ')
        notebook.add(all_tabs['tab_bao_cao'], text=' 4. BÁO CÁO (VIEW) ')

    elif role_check == 'Quản Lý':
        # 5. Quản Lý: Thấy TẤT CẢ
        notebook.add(all_tabs['tab_tiep_nhan'], text=' 1. TIẾP NHẬN ')
        notebook.add(all_tabs['tab_kham_benh'], text=' 2. KHÁM BỆNH ')
        notebook.add(all_tabs['tab_thanh_toan'], text=' 3. THANH TOÁN ')
        notebook.add(all_tabs['tab_bao_cao'], text=' 4. BÁO CÁO (VIEW) ')
        notebook.add(all_tabs['tab_benh_nhan'], text='QL Bệnh Nhân')
        notebook.add(all_tabs['tab_nhan_vien'], text='QL Nhân Viên')
        notebook.add(all_tabs['tab_bac_si'], text='QL Bác Sĩ')
        notebook.add(all_tabs['tab_thuoc'], text='QL Thuốc')
        notebook.add(all_tabs['tab_dich_vu'], text='QL Dịch Vụ')

    else: 
        # Trường hợp Admin (vai trò không khớp)
        messagebox.showwarning("Lỗi Phân Quyền", f"Vai trò '{role_check}' không xác định. Hiển thị quyền Admin.")
        # Sao chép quyền của Quản Lý
        notebook.add(all_tabs['tab_tiep_nhan'], text=' 1. TIẾP NHẬN ')
        notebook.add(all_tabs['tab_kham_benh'], text=' 2. KHÁM BỆNH ')
        notebook.add(all_tabs['tab_thanh_toan'], text=' 3. THANH TOÁN ')
        notebook.add(all_tabs['tab_bao_cao'], text=' 4. BÁO CÁO (VIEW) ')
        notebook.add(all_tabs['tab_benh_nhan'], text='QL Bệnh Nhân')
        notebook.add(all_tabs['tab_nhan_vien'], text='QL Nhân Viên')
        notebook.add(all_tabs['tab_bac_si'], text='QL Bác Sĩ')
        notebook.add(all_tabs['tab_thuoc'], text='QL Thuốc')
        notebook.add(all_tabs['tab_dich_vu'], text='QL Dịch Vụ')



# #############################################################
# PHẦN 1: TAB NGHIỆP VỤ 1 - TIẾP NHẬN
# #############################################################
def create_tiepnhan_tab(tab_frame):
    widgets_tn = {}

    def get_combobox_key_from_value(combobox, data_dict):
        value_selected = combobox.get()
        for key, value in data_dict.items():
            if value == value_selected:
                return key
        return None

    def refresh_comboboxes_tn():
        """Cập nhật danh sách cho combobox"""
        load_all_data_caches() 
        widgets_tn['combo_benh_nhan']['values'] = list(data_cache["benhnhan"].values())
        widgets_tn['combo_nhan_vien']['values'] = list(data_cache["nhanvien"].values())
        fetch_luotkham_moi_tao()

    def fetch_luotkham_moi_tao():
        tree_lk = widgets_tn['tree_luotkham_moi']
        for row in tree_lk.get_children(): tree_lk.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = """
                    SELECT lk.MaLuotKham, bn.HoTen, lk.NgayKham
                    FROM TacVu.LuotKham lk
                    JOIN BenhNhan.BenhNhan bn ON lk.MaBenhNhan = bn.MaBenhNhan
                    WHERE lk.TrangThai = N'Mới Tạo'
                    ORDER BY lk.NgayKham DESC
                """
                cursor.execute(query)
                if not tree_lk["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_lk["columns"] = columns; tree_lk["show"] = "headings"
                    for col in columns:
                        tree_lk.heading(col, text=col); tree_lk.column(col, width=150)
                rows = cursor.fetchall()
                for row in rows:
                    tree_lk.insert("", "end", values=list(row))
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lấy Lượt Khám Mới: {e}")

    def create_luot_kham():
        ma_luot_kham = widgets_tn['entry_ma_luot_kham'].get()
        ma_benh_nhan = get_combobox_key_from_value(widgets_tn['combo_benh_nhan'], data_cache["benhnhan"])
        ma_nhan_vien = get_combobox_key_from_value(widgets_tn['combo_nhan_vien'], data_cache["nhanvien"])
        
        if not ma_luot_kham or not ma_benh_nhan or not ma_nhan_vien:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập Mã Lượt Khám và chọn Bệnh Nhân, Nhân Viên")
            return
            
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = """
                    INSERT INTO TacVu.LuotKham (MaLuotKham, TrangThai, NgayKham, MaBenhNhan, MaNhanVien_TiepNhan)
                    VALUES (?, N'Mới Tạo', GETDATE(), ?, ?)
                """
                cursor.execute(query, (ma_luot_kham, ma_benh_nhan, ma_nhan_vien))
                conn.commit()
            messagebox.showinfo("Thành công", f"Đã tạo Lượt Khám {ma_luot_kham}!")
            widgets_tn['entry_ma_luot_kham'].delete(0, 'end')
            fetch_luotkham_moi_tao() # Tải lại danh sách
        except pyodbc.IntegrityError:
            messagebox.showerror("Lỗi", f"Mã Lượt Khám '{ma_luot_kham}' đã tồn tại.")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tạo Lượt Khám: {e}")

    # --- GUI Tab Tiếp Nhận ---
    form_frame = tk.LabelFrame(tab_frame, text="Tạo Lượt Khám Mới")
    form_frame.pack(pady=10, padx=20, fill="x")

    tk.Label(form_frame, text="Mã Lượt Khám (*):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    widgets_tn['entry_ma_luot_kham'] = tk.Entry(form_frame, width=40)
    widgets_tn['entry_ma_luot_kham'].grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(form_frame, text="Chọn Bệnh Nhân (*):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    widgets_tn['combo_benh_nhan'] = ttk.Combobox(form_frame, width=38, state="readonly")
    widgets_tn['combo_benh_nhan'].grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(form_frame, text="Nhân Viên Tiếp Nhận (*):").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    widgets_tn['combo_nhan_vien'] = ttk.Combobox(form_frame, width=38, state="readonly")
    widgets_tn['combo_nhan_vien'].grid(row=2, column=1, padx=5, pady=5)
    
    tk.Button(form_frame, text="TẠO LƯỢT KHÁM", command=create_luot_kham, bg="#0275d8", fg="white").grid(row=1, column=2, rowspan=2, padx=20, ipady=10)

    display_frame = tk.LabelFrame(tab_frame, text="Danh Sách Chờ Khám (Trạng thái: Mới Tạo)")
    display_frame.pack(pady=10, padx=20, fill="both", expand=True)
    
    tk.Button(display_frame, text="Tải Lại Danh Sách", command=refresh_comboboxes_tn).pack(pady=10)
    
    tree_scroll = tk.Scrollbar(display_frame); tree_scroll.pack(side="right", fill="y")
    widgets_tn['tree_luotkham_moi'] = ttk.Treeview(display_frame, yscrollcommand=tree_scroll.set)
    widgets_tn['tree_luotkham_moi'].pack(fill="both", expand=True)
    tree_scroll.config(command=widgets_tn['tree_luotkham_moi'].yview)
    
    refresh_comboboxes_tn()

# #############################################################
# PHẦN 2: TAB NGHIỆP VỤ 2 - KHÁM BỆNH (ĐÃ SỬA LỖI)
# #############################################################
def create_khambenh_tab(tab_frame):
    widgets_kb = {}
    current_ma_luot_kham = tk.StringVar()
    current_ma_ho_so = tk.StringVar()

    def get_combobox_key_from_value(combobox, data_dict):
        value_selected = combobox.get()
        for key, value in data_dict.items():
            if value == value_selected:
                return key
        return None

    def refresh_comboboxes_kb():
        """Tải dữ liệu cho tab này"""
        load_all_data_caches() 
        widgets_kb['combo_bac_si']['values'] = list(data_cache["bacsi"].values())
        widgets_kb['combo_dich_vu']['values'] = list(data_cache["dichvu"].values())
        widgets_kb['combo_thuoc']['values'] = list(data_cache["thuoc"].values())
        fetch_luotkham_cho_kham() 

    def fetch_luotkham_cho_kham():
        """Tải danh sách Lượt Khám 'Mới Tạo'"""
        tree_lk = widgets_kb['tree_cho_kham']
        for row in tree_lk.get_children(): tree_lk.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = """
                    SELECT lk.MaLuotKham, bn.HoTen, lk.NgayKham
                    FROM TacVu.LuotKham lk
                    JOIN BenhNhan.BenhNhan bn ON lk.MaBenhNhan = bn.MaBenhNhan
                    WHERE lk.TrangThai = N'Mới Tạo' ORDER BY lk.NgayKham ASC
                """
                cursor.execute(query)
                if not tree_lk["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_lk["columns"] = columns; tree_lk["show"] = "headings"
                    for col in columns: tree_lk.heading(col, text=col); tree_lk.column(col, width=120)
                for row in cursor.fetchall(): tree_lk.insert("", "end", values=list(row))
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể lấy Lượt Khám Chờ: {e}")

    def on_luotkham_select(event):
        """Khi bác sĩ chọn 1 lượt khám"""
        selected_item = widgets_kb['tree_cho_kham'].focus()
        if not selected_item: return
        item_values = widgets_kb['tree_cho_kham'].item(selected_item, 'values')
        
        current_ma_luot_kham.set(item_values[0])
        widgets_kb['label_luot_kham_chon'].config(text=f"Đang chọn: {item_values[0]} - {item_values[1]}")
        
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = "SELECT * FROM TacVu.HoSoKham WHERE MaLuotKham = ?"
                cursor.execute(query, (current_ma_luot_kham.get()))
                ho_so = cursor.fetchone()
                
                if ho_so: # Đã có hồ sơ
                    current_ma_ho_so.set(ho_so.MaHoSo)
                    widgets_kb['entry_ma_ho_so'].delete(0, 'end'); widgets_kb['entry_ma_ho_so'].insert(0, ho_so.MaHoSo)
                    widgets_kb['entry_ly_do'].delete(0, 'end'); widgets_kb['entry_ly_do'].insert(0, ho_so.LyDoKham or "")
                    widgets_kb['entry_chan_doan'].delete(0, 'end'); widgets_kb['entry_chan_doan'].insert(0, ho_so.ChanDoan or "")
                    widgets_kb['entry_ghi_chu_bs'].delete(0, 'end'); widgets_kb['entry_ghi_chu_bs'].insert(0, ho_so.GhiChu or "")
                    widgets_kb['combo_bac_si'].set(data_cache["bacsi"].get(ho_so.MaBacSi, ""))
                    widgets_kb['btn_save_ho_so'].config(text="Cập Nhật Hồ Sơ", bg="#f0ad4e")
                    fetch_chi_tiet_dv()
                    fetch_chi_tiet_thuoc()
                    enable_chi_tiet_frames(True)
                else: # Chưa có hồ sơ
                    clear_ho_so_form()
                    enable_chi_tiet_frames(False) 
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tải hồ sơ: {e}")

    def clear_ho_so_form():
        current_ma_ho_so.set("")
        widgets_kb['entry_ma_ho_so'].delete(0, 'end')
        widgets_kb['entry_ly_do'].delete(0, 'end')
        widgets_kb['entry_chan_doan'].delete(0, 'end')
        widgets_kb['entry_ghi_chu_bs'].delete(0, 'end')
        widgets_kb['combo_bac_si'].set("")
        widgets_kb['btn_save_ho_so'].config(text="Lưu Hồ Sơ", bg="#5cb85c")
        
    def enable_chi_tiet_frames(enable=True):
        """Bật/tắt các frame kê đơn và dịch vụ"""
        state = "normal" if enable else "disabled"
        widgets_kb['btn_add_dv'].config(state=state)
        widgets_kb['btn_add_thuoc'].config(state=state)
        widgets_kb['btn_complete_kham'].config(state=state)
        widgets_kb['combo_dich_vu'].config(state="readonly" if enable else "disabled")
        widgets_kb['combo_thuoc'].config(state="readonly" if enable else "disabled")
        widgets_kb['entry_sl_dv'].config(state=state)
        widgets_kb['entry_ket_qua_dv'].config(state=state) # <-- SỬA LỖI
        widgets_kb['entry_sl_thuoc'].config(state=state)
        widgets_kb['entry_lieu_dung'].config(state=state)
        if not enable:
            for tree in [widgets_kb['tree_dv_da_them'], widgets_kb['tree_thuoc_da_them']]:
                for row in tree.get_children(): tree.delete(row)

    def save_ho_so_kham():
        ma_ho_so = widgets_kb['entry_ma_ho_so'].get()
        ma_luot_kham = current_ma_luot_kham.get()
        ma_bac_si = get_combobox_key_from_value(widgets_kb['combo_bac_si'], data_cache["bacsi"])
        ly_do = widgets_kb['entry_ly_do'].get() or None
        chan_doan = widgets_kb['entry_chan_doan'].get() or "Chưa có chẩn đoán"
        ghi_chu = widgets_kb['entry_ghi_chu_bs'].get() or None

        if not ma_ho_so or not ma_luot_kham or not ma_bac_si:
            messagebox.showwarning("Thiếu thông tin", "Mã Hồ Sơ, Lượt Khám và Bác Sĩ là bắt buộc")
            return

        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                if current_ma_ho_so.get(): # Cập nhật
                    query = "UPDATE TacVu.HoSoKham SET LyDoKham = ?, ChanDoan = ?, GhiChu = ?, MaBacSi = ? WHERE MaHoSo = ? AND MaLuotKham = ?"
                    cursor.execute(query, (ly_do, chan_doan, ghi_chu, ma_bac_si, ma_ho_so, ma_luot_kham))
                else: # Thêm mới
                    query = "INSERT INTO TacVu.HoSoKham (MaHoSo, LyDoKham, ChanDoan, GhiChu, MaLuotKham, MaBacSi) VALUES (?, ?, ?, ?, ?, ?)"
                    cursor.execute(query, (ma_ho_so, ly_do, chan_doan, ghi_chu, ma_luot_kham, ma_bac_si))
                conn.commit()
            
            messagebox.showinfo("Thành công", f"Đã lưu Hồ Sơ {ma_ho_so}")
            current_ma_ho_so.set(ma_ho_so)
            enable_chi_tiet_frames(True) 
            widgets_kb['btn_save_ho_so'].config(text="Cập Nhật Hồ Sơ", bg="#f0ad4e")

        except pyodbc.IntegrityError as e:
            if "PRIMARY KEY" in str(e): messagebox.showerror("Lỗi", f"Mã Hồ Sơ '{ma_ho_so}' đã tồn tại.")
            elif "FOREIGN KEY" in str(e): messagebox.showerror("Lỗi", "Lỗi Khóa Ngoại (MaLuotKham hoặc MaBacSi).")
            elif "UNIQUE constraint" in str(e): messagebox.showerror("Lỗi", f"Lượt Khám '{ma_luot_kham}' đã có Hồ Sơ.")
            else: messagebox.showerror("Lỗi", f"Lỗi CSDL: {e}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lưu Hồ Sơ: {e}")

    def fetch_chi_tiet_dv():
        tree = widgets_kb['tree_dv_da_them']
        for row in tree.get_children(): tree.delete(row)
        if not current_ma_ho_so.get(): return
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = "SELECT dv.TenDichVu, ct.SoLuong, ct.KetQua FROM DichVu.ChiTietDichVu ct JOIN DichVu.DichVu dv ON ct.MaDichVu = dv.MaDichVu WHERE ct.MaHoSo = ?"
                cursor.execute(query, (current_ma_ho_so.get()))
                if not tree["columns"]:
                    tree["columns"] = ("TenDichVu", "SoLuong", "KetQua"); tree["show"] = "headings"
                    tree.heading("TenDichVu", text="Tên Dịch Vụ"); tree.heading("SoLuong", text="SL")
                    tree.heading("KetQua", text="Kết Quả"); tree.column("SL", width=40)
                for row in cursor.fetchall(): tree.insert("", "end", values=[("" if v is None else v) for v in row])
        except Exception as e: messagebox.showerror("Lỗi", f"Lỗi tải chi tiết DV: {e}")

    def add_dich_vu():
        ma_ho_so = current_ma_ho_so.get()
        ma_dich_vu = get_combobox_key_from_value(widgets_kb['combo_dich_vu'], data_cache["dichvu"])
        so_luong = widgets_kb['entry_sl_dv'].get()
        ket_qua = widgets_kb['entry_ket_qua_dv'].get() or None # <-- SỬA LỖI: Lấy kết quả
        
        if not ma_dich_vu or not so_luong:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn Dịch Vụ và nhập Số Lượng")
            return
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                # SỬA LỖI: Thêm cột KetQua vào INSERT
                query = "INSERT INTO DichVu.ChiTietDichVu (MaHoSo, MaDichVu, SoLuong, KetQua) VALUES (?, ?, ?, ?)"
                cursor.execute(query, (ma_ho_so, ma_dich_vu, int(so_luong), ket_qua))
                conn.commit()
            fetch_chi_tiet_dv() 
            widgets_kb['entry_sl_dv'].delete(0, 'end')
            widgets_kb['entry_ket_qua_dv'].delete(0, 'end')
        except pyodbc.IntegrityError:
            messagebox.showerror("Lỗi", "Dịch vụ này đã được thêm vào hồ sơ.")
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể thêm Dịch Vụ: {e}")

    def fetch_chi_tiet_thuoc():
        tree = widgets_kb['tree_thuoc_da_them']
        for row in tree.get_children(): tree.delete(row)
        if not current_ma_ho_so.get(): return
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = "SELECT t.TenThuoc, ct.SoLuong, ct.LieuDung FROM Thuoc.ChiTietDonThuoc ct JOIN Thuoc.Thuoc t ON ct.MaThuoc = t.MaThuoc WHERE ct.MaHoSo = ?"
                cursor.execute(query, (current_ma_ho_so.get()))
                if not tree["columns"]:
                    tree["columns"] = ("TenThuoc", "SoLuong", "LieuDung"); tree["show"] = "headings"
                    tree.heading("TenThuoc", text="Tên Thuốc"); tree.heading("SoLuong", text="SL")
                    tree.heading("LieuDung", text="Liều Dùng"); tree.column("SL", width=40)
                for row in cursor.fetchall(): tree.insert("", "end", values=[("" if v is None else v) for v in row])
        except Exception as e: messagebox.showerror("Lỗi", f"Lỗi tải chi tiết Thuốc: {e}")

    def add_thuoc():
        ma_ho_so = current_ma_ho_so.get()
        ma_thuoc = get_combobox_key_from_value(widgets_kb['combo_thuoc'], data_cache["thuoc"])
        so_luong = widgets_kb['entry_sl_thuoc'].get()
        lieu_dung = widgets_kb['entry_lieu_dung'].get()

        if not ma_thuoc or not so_luong or not lieu_dung:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn Thuốc, nhập Số Lượng và Liều Dùng")
            return
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = "INSERT INTO Thuoc.ChiTietDonThuoc (MaHoSo, MaThuoc, SoLuong, LieuDung) VALUES (?, ?, ?, ?)"
                cursor.execute(query, (ma_ho_so, ma_thuoc, int(so_luong), lieu_dung))
                conn.commit()
            fetch_chi_tiet_thuoc()
            widgets_kb['entry_sl_thuoc'].delete(0, 'end')
            widgets_kb['entry_lieu_dung'].delete(0, 'end')
        except pyodbc.IntegrityError:
            messagebox.showerror("Lỗi", "Thuốc này đã được thêm vào hồ sơ.")
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể thêm Thuốc: {e}")

    def complete_kham():
        ma_luot_kham = current_ma_luot_kham.get()
        if not current_ma_ho_so.get():
            messagebox.showwarning("Chưa có Hồ Sơ", "Vui lòng Lưu Hồ Sơ Khám trước khi hoàn tất")
            return
        
        if messagebox.askyesno("Xác nhận", f"Hoàn tất khám cho Lượt {ma_luot_kham} và gửi đi Thanh Toán?"):
            try:
                with get_connection() as conn:
                    cursor = conn.cursor()
                    query = "UPDATE TacVu.LuotKham SET TrangThai = N'Chờ Thanh Toán' WHERE MaLuotKham = ?"
                    cursor.execute(query, (ma_luot_kham))
                    conn.commit()
                messagebox.showinfo("Thành công", "Đã gửi Lượt Khám đi thanh toán!")
                clear_ho_so_form()
                enable_chi_tiet_frames(False)
                widgets_kb['label_luot_kham_chon'].config(text="Chưa chọn Lượt Khám")
                fetch_luotkham_cho_kham()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể hoàn tất khám: {e}")

    # --- GUI Tab Khám Bệnh ---
    frame_chon_lk = tk.LabelFrame(tab_frame, text="1. Chọn Lượt Khám (Trạng thái: Mới Tạo)")
    frame_chon_lk.pack(pady=10, padx=20, fill="x")
    tk.Button(frame_chon_lk, text="Tải Lại DS Chờ Khám", command=refresh_comboboxes_kb).pack(side="left", padx=10)
    widgets_kb['label_luot_kham_chon'] = tk.Label(frame_chon_lk, text="Chưa chọn Lượt Khám", fg="blue", font=('Arial', 10, 'bold'))
    widgets_kb['label_luot_kham_chon'].pack(side="left", padx=10)
    tree_lk_scroll = tk.Scrollbar(frame_chon_lk, orient="vertical")
    widgets_kb['tree_cho_kham'] = ttk.Treeview(frame_chon_lk, height=5, yscrollcommand=tree_lk_scroll.set)
    tree_lk_scroll.config(command=widgets_kb['tree_cho_kham'].yview); tree_lk_scroll.pack(side="right", fill="y")
    widgets_kb['tree_cho_kham'].pack(fill="x", expand=True, padx=(10,0))
    widgets_kb['tree_cho_kham'].bind("<<TreeviewSelect>>", on_luotkham_select)

    frame_ho_so = tk.LabelFrame(tab_frame, text="2. Tạo/Cập Nhật Hồ Sơ Khám")
    frame_ho_so.pack(pady=10, padx=20, fill="x")
    tk.Label(frame_ho_so, text="Mã Hồ Sơ (*):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    widgets_kb['entry_ma_ho_so'] = tk.Entry(frame_ho_so, width=20); widgets_kb['entry_ma_ho_so'].grid(row=0, column=1, padx=5, pady=5)
    tk.Label(frame_ho_so, text="Bác Sĩ Khám (*):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    widgets_kb['combo_bac_si'] = ttk.Combobox(frame_ho_so, width=30, state="readonly"); widgets_kb['combo_bac_si'].grid(row=1, column=1, padx=5, pady=5, columnspan=2)
    tk.Label(frame_ho_so, text="Lý Do Khám:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
    widgets_kb['entry_ly_do'] = tk.Entry(frame_ho_so, width=40); widgets_kb['entry_ly_do'].grid(row=0, column=3, padx=5, pady=5)
    tk.Label(frame_ho_so, text="Chẩn Đoán (*):").grid(row=1, column=2, padx=5, pady=5, sticky="w")
    widgets_kb['entry_chan_doan'] = tk.Entry(frame_ho_so, width=40); widgets_kb['entry_chan_doan'].grid(row=1, column=3, padx=5, pady=5)
    tk.Label(frame_ho_so, text="Ghi Chú BS:").grid(row=2, column=2, padx=5, pady=5, sticky="w")
    widgets_kb['entry_ghi_chu_bs'] = tk.Entry(frame_ho_so, width=40); widgets_kb['entry_ghi_chu_bs'].grid(row=2, column=3, padx=5, pady=5)
    widgets_kb['btn_save_ho_so'] = tk.Button(frame_ho_so, text="Lưu Hồ Sơ", command=save_ho_so_kham, bg="#5cb85c", fg="white")
    widgets_kb['btn_save_ho_so'].grid(row=0, column=4, rowspan=2, padx=20, ipady=5)

    frame_chi_tiet = tk.LabelFrame(tab_frame, text="3. Kê Đơn & Dịch Vụ (Chỉ bật khi đã Lưu Hồ Sơ)")
    frame_chi_tiet.pack(pady=10, padx=20, fill="both", expand=True)

    frame_dv = tk.Frame(frame_chi_tiet); frame_dv.pack(side="left", fill="both", expand=True, padx=10)
    tk.Label(frame_dv, text="Chọn Dịch Vụ:").pack(anchor="w")
    widgets_kb['combo_dich_vu'] = ttk.Combobox(frame_dv, width=30, state="disabled"); widgets_kb['combo_dich_vu'].pack(fill="x")
    tk.Label(frame_dv, text="Số Lượng:").pack(anchor="w")
    widgets_kb['entry_sl_dv'] = tk.Entry(frame_dv, width=10, state="disabled"); widgets_kb['entry_sl_dv'].pack(anchor="w")
    tk.Label(frame_dv, text="Kết Quả:").pack(anchor="w") # <-- SỬA LỖI
    widgets_kb['entry_ket_qua_dv'] = tk.Entry(frame_dv, width=30, state="disabled"); widgets_kb['entry_ket_qua_dv'].pack(fill="x") # <-- SỬA LỖI
    widgets_kb['btn_add_dv'] = tk.Button(frame_dv, text="+ Thêm Dịch Vụ", command=add_dich_vu, state="disabled"); widgets_kb['btn_add_dv'].pack(pady=5)
    tree_dv_scroll = tk.Scrollbar(frame_dv, orient="vertical")
    widgets_kb['tree_dv_da_them'] = ttk.Treeview(frame_dv, height=5, yscrollcommand=tree_dv_scroll.set)
    tree_dv_scroll.config(command=widgets_kb['tree_dv_da_them'].yview); tree_dv_scroll.pack(side="right", fill="y")
    widgets_kb['tree_dv_da_them'].pack(fill="both", expand=True)

    frame_thuoc = tk.Frame(frame_chi_tiet); frame_thuoc.pack(side="right", fill="both", expand=True, padx=10)
    tk.Label(frame_thuoc, text="Chọn Thuốc:").pack(anchor="w")
    widgets_kb['combo_thuoc'] = ttk.Combobox(frame_thuoc, width=30, state="disabled"); widgets_kb['combo_thuoc'].pack(fill="x")
    tk.Label(frame_thuoc, text="Số Lượng:").pack(anchor="w")
    widgets_kb['entry_sl_thuoc'] = tk.Entry(frame_thuoc, width=10, state="disabled"); widgets_kb['entry_sl_thuoc'].pack(anchor="w")
    tk.Label(frame_thuoc, text="Liều Dùng (*):").pack(anchor="w")
    widgets_kb['entry_lieu_dung'] = tk.Entry(frame_thuoc, width=30, state="disabled"); widgets_kb['entry_lieu_dung'].pack(fill="x")
    widgets_kb['btn_add_thuoc'] = tk.Button(frame_thuoc, text="+ Thêm Thuốc", command=add_thuoc, state="disabled"); widgets_kb['btn_add_thuoc'].pack(pady=5)
    tree_thuoc_scroll = tk.Scrollbar(frame_thuoc, orient="vertical")
    widgets_kb['tree_thuoc_da_them'] = ttk.Treeview(frame_thuoc, height=5, yscrollcommand=tree_thuoc_scroll.set)
    tree_thuoc_scroll.config(command=widgets_kb['tree_thuoc_da_them'].yview); tree_thuoc_scroll.pack(side="right", fill="y")
    widgets_kb['tree_thuoc_da_them'].pack(fill="both", expand=True)

    widgets_kb['btn_complete_kham'] = tk.Button(tab_frame, text="HOÀN TẤT KHÁM (Gửi đi Thanh Toán)", command=complete_kham, bg="#d9534f", fg="white", font=('Arial', 12, 'bold'), state="disabled")
    widgets_kb['btn_complete_kham'].pack(pady=10, ipady=10)
    
    refresh_comboboxes_kb()
    clear_ho_so_form()
    enable_chi_tiet_frames(False)

# #############################################################
# PHẦN 3: TAB NGHIỆP VỤ 3 - THANH TOÁN (ĐÃ SỬA LỖI)
# #############################################################
def create_thanhtoan_tab(tab_frame):
    
    widgets_tt = {}

    def fetch_luotkham_chua_thanh_toan():
        tree_lk = widgets_tt['tree_luotkham']
        for row in tree_lk.get_children(): tree_lk.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = """
                    SELECT lk.MaLuotKham, bn.HoTen, lk.NgayKham, lk.TrangThai
                    FROM TacVu.LuotKham lk
                    JOIN BenhNhan.BenhNhan bn ON lk.MaBenhNhan = bn.MaBenhNhan
                    WHERE lk.TrangThai = N'Chờ Thanh Toán'
                """
                cursor.execute(query)
                if not tree_lk["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_lk["columns"] = columns; tree_lk["show"] = "headings"
                    for col in columns:
                        tree_lk.heading(col, text=col); tree_lk.column(col, width=150)
                rows = cursor.fetchall()
                for row in rows:
                    tree_lk.insert("", "end", values=list(row))
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lấy Lượt Khám: {e}")

    def on_luotkham_select(event):
        # SỬA LỖI: Bật state='normal' trước khi insert
        try:
            selected_item = widgets_tt['tree_luotkham'].focus()
            if not selected_item: return
            item_values = widgets_tt['tree_luotkham'].item(selected_item, 'values')
            
            ma_luot_kham = item_values[0]; ten_benh_nhan = item_values[1]
            clear_entries_tt() # Xóa form
            
            # --- SỬA LỖI: Bật 'normal' để cho phép insert ---
            widgets_tt['entry_ma_luot_kham'].config(state='normal')
            widgets_tt['entry_ten_benh_nhan'].config(state='normal')
            
            widgets_tt['entry_ma_luot_kham'].insert(0, ma_luot_kham)
            widgets_tt['entry_ten_benh_nhan'].insert(0, ten_benh_nhan)
            
            # Trả lại 'readonly'
            widgets_tt['entry_ma_luot_kham'].config(state='readonly')
            widgets_tt['entry_ten_benh_nhan'].config(state='readonly')
            # --- Hết sửa lỗi ---

            tong_tien_dv = 0; tong_tien_thuoc = 0
            with get_connection() as conn:
                cursor = conn.cursor()
                query_dv = """
                    SELECT SUM(ct.SoLuong * dv.DonGia) FROM DichVu.ChiTietDichVu ct
                    JOIN TacVu.HoSoKham hs ON ct.MaHoSo = hs.MaHoSo
                    JOIN DichVu.DichVu dv ON ct.MaDichVu = dv.MaDichVu
                    WHERE hs.MaLuotKham = ?
                """
                cursor.execute(query_dv, (ma_luot_kham))
                result_dv = cursor.fetchone()[0]
                tong_tien_dv = float(result_dv) if result_dv else 0

                query_thuoc = """
                    SELECT SUM(ct.SoLuong * t.DonGia) FROM Thuoc.ChiTietDonThuoc ct
                    JOIN TacVu.HoSoKham hs ON ct.MaHoSo = hs.MaHoSo
                    JOIN Thuoc.Thuoc t ON ct.MaThuoc = t.MaThuoc
                    WHERE hs.MaLuotKham = ?
                """
                cursor.execute(query_thuoc, (ma_luot_kham))
                result_thuoc = cursor.fetchone()[0]
                tong_tien_thuoc = float(result_thuoc) if result_thuoc else 0

            # --- SỬA LỖI: Bật 'normal' để insert tiền ---
            widgets_tt['entry_tien_dv'].config(state='normal')
            widgets_tt['entry_tien_thuoc'].config(state='normal')
            
            widgets_tt['entry_tien_dv'].insert(0, f"{tong_tien_dv:.0f}")
            widgets_tt['entry_tien_thuoc'].insert(0, f"{tong_tien_thuoc:.0f}")
            
            widgets_tt['entry_tien_dv'].config(state='readonly')
            widgets_tt['entry_tien_thuoc'].config(state='readonly')
            # --- Hết sửa lỗi ---
            
            update_final_total()
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tính toán chi phí: {e}")

    def update_final_total(*args):
        try:
            tien_dv = float(widgets_tt['entry_tien_dv'].get() or 0)
            tien_thuoc = float(widgets_tt['entry_tien_thuoc'].get() or 0)
            giam_tru = float(widgets_tt['entry_giam_tru'].get() or 0)
            tong_tien = (tien_dv + tien_thuoc) - giam_tru
            
            widgets_tt['entry_tong_tien'].config(state='normal')
            widgets_tt['entry_tong_tien'].delete(0, 'end')
            widgets_tt['entry_tong_tien'].insert(0, f"{tong_tien:.0f}")
            widgets_tt['entry_tong_tien'].config(state='readonly')
        except ValueError: pass 

    def process_payment():
        ma_thanh_toan = widgets_tt['entry_ma_thanh_toan'].get()
        ma_luot_kham = widgets_tt['entry_ma_luot_kham'].get()
        ma_thu_ngan = widgets_tt['entry_ma_thu_ngan'].get()
        hinh_thuc_tt = widgets_tt['entry_hinh_thuc_tt'].get()
        
        # --- SỬA LỖI: Chia nhỏ validation để báo lỗi chính xác ---
        if not ma_luot_kham:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng chọn một Lượt Khám từ danh sách trên.")
            return
        if not ma_thanh_toan or not ma_thu_ngan or not hinh_thuc_tt:
            messagebox.showwarning("Thiếu thông tin", "Vui lòng nhập Mã Thanh Toán, Hình Thức TT và Mã Thu Ngân.")
            return
        # --- Hết sửa lỗi ---
            
        try:
            tien_dv = float(widgets_tt['entry_tien_dv'].get() or 0)
            tien_thuoc = float(widgets_tt['entry_tien_thuoc'].get() or 0)
            giam_tru = float(widgets_tt['entry_giam_tru'].get() or 0)
            
            if messagebox.askyesno("Xác nhận", f"Thanh toán cho Lượt Khám {ma_luot_kham}?"):
                with get_connection() as conn:
                    cursor = conn.cursor()
                    query_insert_tt = """
                        INSERT INTO ThanhToan.ThanhToan 
                        (MaThanhToan, HinhThucThanhToan, NgayThanhToan, TongTienDichVu, TongTienThuoc, GiamTru, MaLuotKham, MaNhanVien_ThuNgan)
                        VALUES (?, ?, GETDATE(), ?, ?, ?, ?, ?)
                    """
                    cursor.execute(query_insert_tt, (ma_thanh_toan, hinh_thuc_tt, tien_dv, tien_thuoc, giam_tru, ma_luot_kham, ma_thu_ngan))
                    
                    query_update_lk = "UPDATE TacVu.LuotKham SET TrangThai = N'Đã Thanh Toán' WHERE MaLuotKham = ?"
                    cursor.execute(query_update_lk, (ma_luot_kham))
                    conn.commit()
                messagebox.showinfo("Thành công", "Đã thanh toán thành công!")
                clear_entries_tt(); fetch_luotkham_chua_thanh_toan()
        except pyodbc.IntegrityError as e:
            if "PRIMARY KEY" in str(e): messagebox.showerror("Lỗi", f"Mã Thanh Toán '{ma_thanh_toan}' đã tồn tại.")
            elif "FOREIGN KEY" in str(e): messagebox.showerror("Lỗi", f"Mã Thu Ngân '{ma_thu_ngan}' không tồn tại.")
            else: messagebox.showerror("Lỗi", f"Lỗi ràng buộc CSDL: {e}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể xử lý thanh toán: {e}")

    def clear_entries_tt():
        # SỬA LỖI: Đảm bảo TẤT CẢ các ô đều 'normal' trước khi xóa
        for key in ['entry_ma_thanh_toan', 'entry_ma_luot_kham', 'entry_ten_benh_nhan', 
                    'entry_tien_dv', 'entry_tien_thuoc', 'entry_giam_tru', 
                    'entry_tong_tien', 'entry_hinh_thuc_tt', 'entry_ma_thu_ngan']:
            widgets_tt[key].config(state='normal')
            widgets_tt[key].delete(0, 'end')
        
        widgets_tt['entry_giam_tru'].insert(0, "0")
        widgets_tt['entry_hinh_thuc_tt'].insert(0, "Tiền mặt")
        
        # Đặt lại readonly
        widgets_tt['entry_ma_luot_kham'].config(state='readonly')
        widgets_tt['entry_ten_benh_nhan'].config(state='readonly')
        widgets_tt['entry_tien_dv'].config(state='readonly')
        widgets_tt['entry_tien_thuoc'].config(state='readonly')
        widgets_tt['entry_tong_tien'].config(state='readonly')


    # --- GUI Tab Thanh Toán ---
    display_frame = tk.LabelFrame(tab_frame, text="Danh Sách Chờ Thanh Toán (Chọn 1 Lượt Khám)")
    display_frame.pack(pady=10, padx=20, fill="both", expand=True)
    tk.Button(display_frame, text="Tải Lại Danh Sách Chờ", command=fetch_luotkham_chua_thanh_toan).pack(pady=10)
    tree_scroll = tk.Scrollbar(display_frame); tree_scroll.pack(side="right", fill="y")
    tree_scroll_x = tk.Scrollbar(display_frame, orient="horizontal"); tree_scroll_x.pack(side="bottom", fill="x")
    widgets_tt['tree_luotkham'] = ttk.Treeview(display_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_x.set)
    widgets_tt['tree_luotkham'].pack(fill="both", expand=True)
    tree_scroll.config(command=widgets_tt['tree_luotkham'].yview); tree_scroll_x.config(command=widgets_tt['tree_luotkham'].xview)
    widgets_tt['tree_luotkham'].bind("<<TreeviewSelect>>", on_luotkham_select)

    form_frame = tk.LabelFrame(tab_frame, text="Chi Tiết Hóa Đơn")
    form_frame.pack(pady=10, padx=20, fill="x")
    tk.Label(form_frame, text="Mã Thanh Toán (*):").grid(row=0, column=0, padx=5, pady=5, sticky="e")
    widgets_tt['entry_ma_thanh_toan'] = tk.Entry(form_frame, width=25); widgets_tt['entry_ma_thanh_toan'].grid(row=0, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Mã Lượt Khám:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
    widgets_tt['entry_ma_luot_kham'] = tk.Entry(form_frame, width=25, state='readonly'); widgets_tt['entry_ma_luot_kham'].grid(row=1, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Tên Bệnh Nhân:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
    widgets_tt['entry_ten_benh_nhan'] = tk.Entry(form_frame, width=25, state='readonly'); widgets_tt['entry_ten_benh_nhan'].grid(row=2, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Tổng Tiền DV (auto):").grid(row=0, column=2, padx=5, pady=5, sticky="e")
    widgets_tt['entry_tien_dv'] = tk.Entry(form_frame, width=25, state='readonly'); widgets_tt['entry_tien_dv'].grid(row=0, column=3, padx=5, pady=5)
    tk.Label(form_frame, text="Tổng Tiền Thuốc (auto):").grid(row=1, column=2, padx=5, pady=5, sticky="e")
    widgets_tt['entry_tien_thuoc'] = tk.Entry(form_frame, width=25, state='readonly'); widgets_tt['entry_tien_thuoc'].grid(row=1, column=3, padx=5, pady=5)
    giam_tru_var = tk.StringVar(); giam_tru_var.trace("w", update_final_total)
    tk.Label(form_frame, text="Giảm Trừ:").grid(row=2, column=2, padx=5, pady=5, sticky="e")
    widgets_tt['entry_giam_tru'] = tk.Entry(form_frame, width=25, textvariable=giam_tru_var); widgets_tt['entry_giam_tru'].grid(row=2, column=3, padx=5, pady=5)
    tk.Label(form_frame, text="Tổng Tiền Cuối (auto):", font=('Arial', 10, 'bold')).grid(row=3, column=2, padx=5, pady=5, sticky="e")
    widgets_tt['entry_tong_tien'] = tk.Entry(form_frame, width=25, state='readonly', font=('Arial', 10, 'bold')); widgets_tt['entry_tong_tien'].grid(row=3, column=3, padx=5, pady=5)
    tk.Label(form_frame, text="Hình Thức TT (*):").grid(row=0, column=4, padx=5, pady=5, sticky="e")
    widgets_tt['entry_hinh_thuc_tt'] = tk.Entry(form_frame, width=25); widgets_tt['entry_hinh_thuc_tt'].grid(row=0, column=5, padx=5, pady=5)
    tk.Label(form_frame, text="Mã Thu Ngân (*):").grid(row=1, column=4, padx=5, pady=5, sticky="e")
    widgets_tt['entry_ma_thu_ngan'] = tk.Entry(form_frame, width=25); widgets_tt['entry_ma_thu_ngan'].grid(row=1, column=5, padx=5, pady=5)
    
    button_frame = tk.Frame(tab_frame); button_frame.pack(pady=10, padx=20, fill="x")
    tk.Button(button_frame, text="XÁC NHẬN THANH TOÁN", command=process_payment, bg="#4CAF50", fg="white", font=('Arial', 12, 'bold')).pack(side="left", padx=10, pady=10, ipady=10)
    tk.Button(button_frame, text="Xóa Form", command=clear_entries_tt).pack(side="left", padx=10)
    
    fetch_luotkham_chua_thanh_toan()
    clear_entries_tt()

# #############################################################
# PHẦN 4: TAB BÁO CÁO (TỪ VIEW)
# #############################################################
def create_report_tab(tab_frame):
    
    def fetch_report_data(tree_report):
        for row in tree_report.get_children(): tree_report.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                # Tên VIEW bạn cung cấp
                query = "SELECT * FROM vw_ThongTinKhamBenhChiTiet"
                cursor.execute(query)
                
                if not tree_report["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_report["columns"] = columns; tree_report["show"] = "headings"
                    for col in columns:
                        tree_report.heading(col, text=col)
                        tree_report.column(col, width=120, anchor='w')
                
                rows = cursor.fetchall()
                for row in rows:
                    display_row = ["" if v is None else v for v in row]
                    tree_report.insert("", "end", values=display_row)
                    
        except pyodbc.Error as e:
            if e.args[0] == '42S02': 
                messagebox.showerror("Lỗi CSDL", "Không tìm thấy View 'vw_ThongTinKhamBenhChiTiet'.\nBạn đã chạy script CREATE VIEW trong SQL Server chưa?")
            else: messagebox.showerror("Lỗi", f"Không thể lấy dữ liệu báo cáo: {e}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Lỗi không xác định: {e}")

    # --- GUI Tab Báo Cáo ---
    main_frame = tk.Frame(tab_frame); main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    tk.Button(main_frame, text="Tải Lại Báo Cáo", command=lambda: fetch_report_data(tree_report)).pack(pady=10)
    display_frame = tk.LabelFrame(main_frame, text="Thông tin chi tiết")
    display_frame.pack(fill="both", expand=True)
    tree_scroll_y = tk.Scrollbar(display_frame); tree_scroll_y.pack(side="right", fill="y")
    tree_scroll_x = tk.Scrollbar(display_frame, orient="horizontal"); tree_scroll_x.pack(side="bottom", fill="x")
    tree_report = ttk.Treeview(display_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
    tree_report.pack(fill="both", expand=True)
    tree_scroll_y.config(command=tree_report.yview); tree_scroll_x.config(command=tree_report.xview)
    
    fetch_report_data(tree_report)
# #############################################################
# PHẦN 4.5: TAB BỆNH NHÂN - XEM HỒ SƠ (MỚI)
# #############################################################
def create_benhan_canhan_tab(tab_frame, ma_benh_nhan):
    
    def fetch_benh_an_ca_nhan(tree_report):
        for row in tree_report.get_children():
            tree_report.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                # Dùng VIEW đã ALTER ở BƯỚC 1, lọc theo MaBenhNhan
                query = """
                    SELECT NgayKham, TenBacSi, ChuyenKhoa, ChanDoan, LyDoKham, GhiChuBacSi 
                    FROM vw_ThongTinKhamBenhChiTiet
                    WHERE MaBenhNhan = ?
                    ORDER BY NgayKham DESC
                """
                cursor.execute(query, (ma_benh_nhan))
                
                if not tree_report["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_report["columns"] = columns; tree_report["show"] = "headings"
                    for col in columns:
                        tree_report.heading(col, text=col)
                        tree_report.column(col, width=150, anchor='w')
                
                rows = cursor.fetchall()
                for row in rows:
                    display_row = ["" if v is None else v for v in row]
                    tree_report.insert("", "end", values=display_row)
                    
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lấy lịch sử khám bệnh: {e}")

    # --- GUI Tab Báo Cáo ---
    main_frame = tk.Frame(tab_frame); main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    tk.Button(main_frame, text="Tải Lại Hồ Sơ", 
              command=lambda: fetch_benh_an_ca_nhan(tree_report)).pack(pady=10)
    display_frame = tk.LabelFrame(main_frame, text="Lịch sử khám bệnh của bạn")
    display_frame.pack(fill="both", expand=True)
    tree_scroll_y = tk.Scrollbar(display_frame); tree_scroll_y.pack(side="right", fill="y")
    tree_scroll_x = tk.Scrollbar(display_frame, orient="horizontal"); tree_scroll_x.pack(side="bottom", fill="x")
    tree_report = ttk.Treeview(display_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
    tree_report.pack(fill="both", expand=True)
    tree_scroll_y.config(command=tree_report.yview); tree_scroll_x.config(command=tree_report.xview)
    
    fetch_benh_an_ca_nhan(tree_report)

# #############################################################
# PHẦN 4.6: TAB BỆNH NHÂN - XEM THANH TOÁN (MỚI)
# #############################################################
def create_thanhtoan_canhan_tab(tab_frame, ma_benh_nhan):
    
    def fetch_thanh_toan_ca_nhan(tree_report):
        for row in tree_report.get_children():
            tree_report.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = """
                    SELECT tt.MaThanhToan, tt.NgayThanhToan, tt.TongTienDichVu, tt.TongTienThuoc, tt.GiamTru,
                           (tt.TongTienDichVu + tt.TongTienThuoc - tt.GiamTru) AS TongCong,
                           tt.HinhThucThanhToan
                    FROM ThanhToan.ThanhToan tt
                    JOIN TacVu.LuotKham lk ON tt.MaLuotKham = lk.MaLuotKham
                    WHERE lk.MaBenhNhan = ?
                    ORDER BY tt.NgayThanhToan DESC
                """
                cursor.execute(query, (ma_benh_nhan))
                
                if not tree_report["columns"]:
                    columns = [col[0] for col in cursor.description]
                    tree_report["columns"] = columns; tree_report["show"] = "headings"
                    for col in columns:
                        tree_report.heading(col, text=col)
                        tree_report.column(col, width=120, anchor='e')
                
                rows = cursor.fetchall()
                for row in rows:
                    display_row = [f"{v:.0f}" if isinstance(v, (int, float)) else ("" if v is None else v) for v in row]
                    tree_report.insert("", "end", values=display_row)
                    
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể lấy lịch sử thanh toán: {e}")

    # --- GUI Tab Báo Cáo ---
    main_frame = tk.Frame(tab_frame); main_frame.pack(fill="both", expand=True, padx=10, pady=10)
    tk.Button(main_frame, text="Tải Lại Lịch Sử Thanh Toán", 
              command=lambda: fetch_thanh_toan_ca_nhan(tree_report)).pack(pady=10)
    display_frame = tk.LabelFrame(main_frame, text="Lịch sử thanh toán của bạn")
    display_frame.pack(fill="both", expand=True)
    tree_scroll_y = tk.Scrollbar(display_frame); tree_scroll_y.pack(side="right", fill="y")
    tree_scroll_x = tk.Scrollbar(display_frame, orient="horizontal"); tree_scroll_x.pack(side="bottom", fill="x")
    tree_report = ttk.Treeview(display_frame, yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
    tree_report.pack(fill="both", expand=True)
    tree_scroll_y.config(command=tree_report.yview); tree_scroll_x.config(command=tree_report.xview)
    
    fetch_thanh_toan_ca_nhan(tree_report)

# #############################################################
# PHẦN 5: TAB QUẢN LÝ BỆNH NHÂN (CRUD)
# #############################################################
def create_benhnhan_tab(tab_frame):
    widgets_bn = {}
    
    def fetch_data_bn():
        tree_bn = widgets_bn['tree_bn']
        for row in tree_bn.get_children(): tree_bn.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = "SELECT MaBenhNhan, HoTen, SoDienThoai, NgaySinh, GioiTinh, DiaChi FROM [BenhNhan].[BenhNhan]"
                cursor.execute(query)
                if not tree_bn["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_bn["columns"] = columns; tree_bn["show"] = "headings" 
                    for col in columns:
                        tree_bn.heading(col, text=col); tree_bn.column(col, width=100)
                rows = cursor.fetchall()
                data_cache["benhnhan"].clear() # Xóa cache cũ
                for row in rows:
                    display_row = ["" if v is None else v for v in row]
                    tree_bn.insert("", "end", values=display_row)
                    data_cache["benhnhan"][row[0]] = row[1] # Cập nhật cache
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể lấy dữ liệu Bệnh Nhân: {e}")

    def insert_data_bn():
        values = (widgets_bn['entry_ma_bn'].get(), widgets_bn['entry_ten_bn'].get(), widgets_bn['entry_sdt_bn'].get() or None, widgets_bn['entry_ngaysinh_bn'].get() or None, widgets_bn['entry_gioitinh_bn'].get() or None, widgets_bn['entry_diachi_bn'].get() or None)
        if not values[0] or not values[1]: messagebox.showwarning("Thiếu thông tin", "Mã Bệnh Nhân và Họ Tên là bắt buộc"); return
        try:
            with get_connection() as conn: cursor = conn.cursor(); query = "INSERT INTO [BenhNhan].[BenhNhan] (MaBenhNhan, HoTen, SoDienThoai, NgaySinh, GioiTinh, DiaChi) VALUES (?, ?, ?, ?, ?, ?)"; cursor.execute(query, values); conn.commit()
            messagebox.showinfo("Thành công", "Đã thêm Bệnh Nhân!"); clear_entries_bn(); fetch_data_bn()
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể thêm Bệnh Nhân: {e}")
    def update_data_bn():
        values = (widgets_bn['entry_ten_bn'].get(), widgets_bn['entry_sdt_bn'].get() or None, widgets_bn['entry_ngaysinh_bn'].get() or None, widgets_bn['entry_gioitinh_bn'].get() or None, widgets_bn['entry_diachi_bn'].get() or None, widgets_bn['entry_ma_bn'].get())
        if not values[5]: messagebox.showwarning("Chưa chọn", "Vui lòng chọn bệnh nhân để sửa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Sửa bệnh nhân {values[5]}?"):
                with get_connection() as conn: cursor = conn.cursor(); query = "UPDATE [BenhNhan].[BenhNhan] SET HoTen = ?, SoDienThoai = ?, NgaySinh = ?, GioiTinh = ?, DiaChi = ? WHERE MaBenhNhan = ?"; cursor.execute(query, values); conn.commit()
                messagebox.showinfo("Thành công", "Đã sửa Bệnh Nhân!"); clear_entries_bn(); fetch_data_bn()
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể sửa Bệnh Nhân: {e}")
    def delete_data_bn():
        ma_bn = widgets_bn['entry_ma_bn'].get()
        if not ma_bn: messagebox.showwarning("Chưa chọn", "Vui lòng chọn bệnh nhân để xóa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Xóa Bệnh Nhân '{ma_bn}'?"):
                with get_connection() as conn: cursor = conn.cursor(); query = "DELETE FROM [BenhNhan].[BenhNhan] WHERE MaBenhNhan = ?"; cursor.execute(query, (ma_bn)); conn.commit()
                messagebox.showinfo("Thành công", "Đã xóa Bệnh Nhân!"); clear_entries_bn(); fetch_data_bn()
        except pyodbc.IntegrityError: messagebox.showerror("Lỗi", "Không thể xóa: Bệnh nhân này đã có dữ liệu liên quan (Lượt Khám).")
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể xóa Bệnh Nhân: {e}")
    def on_row_select_bn(event):
        try:
            selected_item = widgets_bn['tree_bn'].focus();
            if not selected_item: return
            item_values = widgets_bn['tree_bn'].item(selected_item, 'values'); clear_entries_bn()
            widgets_bn['entry_ma_bn'].insert(0, item_values[0]); widgets_bn['entry_ten_bn'].insert(0, item_values[1]); widgets_bn['entry_sdt_bn'].insert(0, item_values[2]); widgets_bn['entry_ngaysinh_bn'].insert(0, item_values[3]); widgets_bn['entry_gioitinh_bn'].insert(0, item_values[4]); widgets_bn['entry_diachi_bn'].insert(0, item_values[5])
            widgets_bn['entry_ma_bn'].config(state='readonly')
        except Exception: pass
    def clear_entries_bn():
        widgets_bn['entry_ma_bn'].config(state='normal'); widgets_bn['entry_ma_bn'].delete(0, 'end'); widgets_bn['entry_ten_bn'].delete(0, 'end'); widgets_bn['entry_sdt_bn'].delete(0, 'end'); widgets_bn['entry_ngaysinh_bn'].delete(0, 'end'); widgets_bn['entry_gioitinh_bn'].delete(0, 'end'); widgets_bn['entry_diachi_bn'].delete(0, 'end')

    # --- GUI Tab Bệnh Nhân ---
    form_frame = tk.LabelFrame(tab_frame, text="Thông tin Bệnh Nhân"); form_frame.pack(pady=10, padx=20, fill="x")
    tk.Label(form_frame, text="Mã BN:").grid(row=0, column=0, padx=5, pady=5, sticky="e"); widgets_bn['entry_ma_bn'] = tk.Entry(form_frame, width=30); widgets_bn['entry_ma_bn'].grid(row=0, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Họ Tên:").grid(row=1, column=0, padx=5, pady=5, sticky="e"); widgets_bn['entry_ten_bn'] = tk.Entry(form_frame, width=30); widgets_bn['entry_ten_bn'].grid(row=1, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="SĐT:").grid(row=2, column=0, padx=5, pady=5, sticky="e"); widgets_bn['entry_sdt_bn'] = tk.Entry(form_frame, width=30); widgets_bn['entry_sdt_bn'].grid(row=2, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Ngày Sinh (YYYY-MM-DD):").grid(row=0, column=2, padx=5, pady=5, sticky="e"); widgets_bn['entry_ngaysinh_bn'] = tk.Entry(form_frame, width=30); widgets_bn['entry_ngaysinh_bn'].grid(row=0, column=3, padx=5, pady=5)
    tk.Label(form_frame, text="Giới Tính:").grid(row=1, column=2, padx=5, pady=5, sticky="e"); widgets_bn['entry_gioitinh_bn'] = tk.Entry(form_frame, width=30); widgets_bn['entry_gioitinh_bn'].grid(row=1, column=3, padx=5, pady=5)
    tk.Label(form_frame, text="Địa Chỉ:").grid(row=2, column=2, padx=5, pady=5, sticky="e"); widgets_bn['entry_diachi_bn'] = tk.Entry(form_frame, width=30); widgets_bn['entry_diachi_bn'].grid(row=2, column=3, padx=5, pady=5)
    button_frame = tk.Frame(tab_frame); button_frame.pack(pady=5, padx=20, fill="x")
    tk.Button(button_frame, text="Thêm Mới", command=insert_data_bn, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Sửa", command=update_data_bn, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa", command=delete_data_bn, bg="#ff6666", fg="white", width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa Trắng Form", command=clear_entries_bn, width=15).pack(side="left", padx=10)
    display_frame = tk.LabelFrame(tab_frame, text="Danh Sách Bệnh Nhân"); display_frame.pack(pady=10, padx=20, fill="both", expand=True)
    tk.Button(display_frame, text="Tải Lại Dữ Liệu", command=fetch_data_bn).pack(pady=10); tree_scroll = tk.Scrollbar(display_frame); tree_scroll.pack(side="right", fill="y"); tree_scroll_x = tk.Scrollbar(display_frame, orient="horizontal"); tree_scroll_x.pack(side="bottom", fill="x")
    widgets_bn['tree_bn'] = ttk.Treeview(display_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_x.set); widgets_bn['tree_bn'].pack(fill="both", expand=True); tree_scroll.config(command=widgets_bn['tree_bn'].yview); tree_scroll_x.config(command=widgets_bn['tree_bn'].xview); widgets_bn['tree_bn'].bind("<<TreeviewSelect>>", on_row_select_bn); fetch_data_bn()

# #############################################################
# PHẦN 6: TAB QUẢN LÝ NHÂN VIÊN (CRUD)
# #############################################################
def create_nhanvien_tab(tab_frame):
    widgets_nv = {}
    TABLE_NAME_NV = "[NhanVien].[NhanVien]"

    def fetch_data_nv():
        tree_nv = widgets_nv['tree_nv']
        for row in tree_nv.get_children(): tree_nv.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = f"SELECT MaNhanVien, HoTen, SoDienThoai, ChucVu, MatKhau FROM {TABLE_NAME_NV}" # Thêm MatKhau
                cursor.execute(query)
                if not tree_nv["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_nv["columns"] = columns; tree_nv["show"] = "headings"
                    for col in columns:
                        tree_nv.heading(col, text=col); tree_nv.column(col, width=150)
                rows = cursor.fetchall()
                data_cache["nhanvien"].clear() 
                for row in rows:
                    display_row = ["" if v is None else v for v in row]
                    tree_nv.insert("", "end", values=display_row)
                    data_cache["nhanvien"][row[0]] = row[1] 
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể lấy dữ liệu Nhân Viên: {e}")

    def insert_data_nv():
        values = (
            widgets_nv['entry_ma_nv'].get(), widgets_nv['entry_ten_nv'].get(),
            widgets_nv['entry_sdt_nv'].get() or None, widgets_nv['entry_chucvu_nv'].get(),
            widgets_nv['entry_matkhau_nv'].get() or '123' # Lấy mk, nếu trống thì là 123
        )
        if not values[0] or not values[1] or not values[3]: messagebox.showwarning("Thiếu thông tin", "Mã, Tên, và Chức Vụ là bắt buộc"); return
        try:
            with get_connection() as conn: cursor = conn.cursor(); query = f"INSERT INTO {TABLE_NAME_NV} (MaNhanVien, HoTen, SoDienThoai, ChucVu, MatKhau) VALUES (?, ?, ?, ?, ?)"; cursor.execute(query, values); conn.commit()
            messagebox.showinfo("Thành công", "Đã thêm Nhân Viên!"); clear_entries_nv(); fetch_data_nv()
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể thêm Nhân Viên: {e}")
    def update_data_nv():
        values = (
            widgets_nv['entry_ten_nv'].get(), widgets_nv['entry_sdt_nv'].get() or None,
            widgets_nv['entry_chucvu_nv'].get(), widgets_nv['entry_matkhau_nv'].get() or '123', # Lấy mk
            widgets_nv['entry_ma_nv'].get()
        )
        if not values[4]: messagebox.showwarning("Chưa chọn", "Vui lòng chọn nhân viên để sửa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Sửa nhân viên {values[4]}?"):
                with get_connection() as conn: cursor = conn.cursor(); query = f"UPDATE {TABLE_NAME_NV} SET HoTen = ?, SoDienThoai = ?, ChucVu = ?, MatKhau = ? WHERE MaNhanVien = ?"; cursor.execute(query, values); conn.commit()
                messagebox.showinfo("Thành công", "Đã sửa Nhân Viên!"); clear_entries_nv(); fetch_data_nv()
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể sửa Nhân Viên: {e}")
    def delete_data_nv():
        ma_nv = widgets_nv['entry_ma_nv'].get()
        if not ma_nv: messagebox.showwarning("Chưa chọn", "Vui lòng chọn nhân viên để xóa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Xóa Nhân Viên '{ma_nv}'?"):
                with get_connection() as conn: cursor = conn.cursor(); query = f"DELETE FROM {TABLE_NAME_NV} WHERE MaNhanVien = ?"; cursor.execute(query, (ma_nv)); conn.commit()
                messagebox.showinfo("Thành công", "Đã xóa Nhân Viên!"); clear_entries_nv(); fetch_data_nv()
        except pyodbc.IntegrityError: messagebox.showerror("Lỗi", "Không thể xóa: Nhân viên này đã là Bác Sĩ hoặc liên quan (Lượt Khám, Thanh Toán).")
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể xóa Nhân Viên: {e}")
    def on_row_select_nv(event):
        try:
            selected_item = widgets_nv['tree_nv'].focus();
            if not selected_item: return
            item_values = widgets_nv['tree_nv'].item(selected_item, 'values'); clear_entries_nv()
            widgets_nv['entry_ma_nv'].insert(0, item_values[0]); widgets_nv['entry_ten_nv'].insert(0, item_values[1]); widgets_nv['entry_sdt_nv'].insert(0, item_values[2]); widgets_nv['entry_chucvu_nv'].insert(0, item_values[3]); widgets_nv['entry_matkhau_nv'].insert(0, item_values[4])
            widgets_nv['entry_ma_nv'].config(state='readonly')
        except Exception: pass
    def clear_entries_nv():
        widgets_nv['entry_ma_nv'].config(state='normal'); widgets_nv['entry_ma_nv'].delete(0, 'end'); widgets_nv['entry_ten_nv'].delete(0, 'end'); widgets_nv['entry_sdt_nv'].delete(0, 'end'); widgets_nv['entry_chucvu_nv'].delete(0, 'end'); widgets_nv['entry_matkhau_nv'].delete(0, 'end')

    # --- GUI Tab Nhân Viên ---
    form_frame = tk.LabelFrame(tab_frame, text="Thông tin Nhân Viên"); form_frame.pack(pady=10, padx=20, fill="x")
    tk.Label(form_frame, text="Mã NV:").grid(row=0, column=0, padx=5, pady=5, sticky="e"); widgets_nv['entry_ma_nv'] = tk.Entry(form_frame, width=30); widgets_nv['entry_ma_nv'].grid(row=0, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Họ Tên:").grid(row=1, column=0, padx=5, pady=5, sticky="e"); widgets_nv['entry_ten_nv'] = tk.Entry(form_frame, width=30); widgets_nv['entry_ten_nv'].grid(row=1, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="SĐT:").grid(row=0, column=2, padx=5, pady=5, sticky="e"); widgets_nv['entry_sdt_nv'] = tk.Entry(form_frame, width=30); widgets_nv['entry_sdt_nv'].grid(row=0, column=3, padx=5, pady=5)
    tk.Label(form_frame, text="Chức Vụ:").grid(row=1, column=2, padx=5, pady=5, sticky="e"); widgets_nv['entry_chucvu_nv'] = tk.Entry(form_frame, width=30); widgets_nv['entry_chucvu_nv'].grid(row=1, column=3, padx=5, pady=5)
    tk.Label(form_frame, text="Mật Khẩu:").grid(row=2, column=0, padx=5, pady=5, sticky="e"); widgets_nv['entry_matkhau_nv'] = tk.Entry(form_frame, width=30); widgets_nv['entry_matkhau_nv'].grid(row=2, column=1, padx=5, pady=5)
    
    button_frame = tk.Frame(tab_frame); button_frame.pack(pady=5, padx=20, fill="x")
    tk.Button(button_frame, text="Thêm Mới", command=insert_data_nv, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Sửa", command=update_data_nv, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa", command=delete_data_nv, bg="#ff6666", fg="white", width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa Trắng Form", command=clear_entries_nv, width=15).pack(side="left", padx=10)
    display_frame = tk.LabelFrame(tab_frame, text="Danh Sách Nhân Viên"); display_frame.pack(pady=10, padx=20, fill="both", expand=True)
    tk.Button(display_frame, text="Tải Lại Dữ Liệu", command=fetch_data_nv).pack(pady=10); tree_scroll = tk.Scrollbar(display_frame); tree_scroll.pack(side="right", fill="y"); tree_scroll_x = tk.Scrollbar(display_frame, orient="horizontal"); tree_scroll_x.pack(side="bottom", fill="x")
    widgets_nv['tree_nv'] = ttk.Treeview(display_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_x.set); widgets_nv['tree_nv'].pack(fill="both", expand=True); tree_scroll.config(command=widgets_nv['tree_nv'].yview); tree_scroll_x.config(command=widgets_nv['tree_nv'].xview); widgets_nv['tree_nv'].bind("<<TreeviewSelect>>", on_row_select_nv); fetch_data_nv()

# #############################################################
# PHẦN 7: TAB QUẢN LÝ BÁC SĨ (CRUD)
# #############################################################
def create_bacsi_tab(tab_frame):
    widgets_bs = {}
    TABLE_NAME_BS = "[NhanVien].[BacSi]"

    def fetch_data_bs():
        tree_bs = widgets_bs['tree_bs']
        for row in tree_bs.get_children(): tree_bs.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = f"SELECT BS.MaBacSi, NV.HoTen, BS.ChuyenKhoa FROM {TABLE_NAME_BS} AS BS JOIN [NhanVien].[NhanVien] AS NV ON BS.MaBacSi = NV.MaNhanVien"
                cursor.execute(query)
                if not tree_bs["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_bs["columns"] = columns; tree_bs["show"] = "headings"
                    for col in columns:
                        tree_bs.heading(col, text=col); tree_bs.column(col, width=200)
                rows = cursor.fetchall()
                data_cache["bacsi"].clear() 
                for row in rows:
                    tree_bs.insert("", "end", values=list(row))
                    data_cache["bacsi"][row[0]] = row[1] 
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể lấy dữ liệu Bác Sĩ: {e}")

    def insert_data_bs():
        values = (widgets_bs['entry_ma_bs'].get(), widgets_bs['entry_chuyenkhoa_bs'].get())
        if not values[0] or not values[1]: messagebox.showwarning("Thiếu thông tin", "Mã Bác Sĩ và Chuyên Khoa là bắt buộc"); return
        try:
            with get_connection() as conn: cursor = conn.cursor(); query = f"INSERT INTO {TABLE_NAME_BS} (MaBacSi, ChuyenKhoa) VALUES (?, ?)"; cursor.execute(query, values); conn.commit()
            messagebox.showinfo("Thành công", "Đã thêm Bác Sĩ!"); clear_entries_bs(); fetch_data_bs()
        except pyodbc.IntegrityError: messagebox.showerror("Lỗi", f"Không thể thêm: Mã Bác Sĩ '{values[0]}' không tồn tại trong bảng Nhân Viên hoặc đã là Bác Sĩ.")
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể thêm Bác Sĩ: {e}")
    def update_data_bs():
        values = (widgets_bs['entry_chuyenkhoa_bs'].get(), widgets_bs['entry_ma_bs'].get())
        if not values[1]: messagebox.showwarning("Chưa chọn", "Vui lòng chọn bác sĩ để sửa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Sửa bác sĩ {values[1]}?"):
                with get_connection() as conn: cursor = conn.cursor(); query = f"UPDATE {TABLE_NAME_BS} SET ChuyenKhoa = ? WHERE MaBacSi = ?"; cursor.execute(query, values); conn.commit()
                messagebox.showinfo("Thành công", "Đã sửa Bác Sĩ!"); clear_entries_bs(); fetch_data_bs()
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể sửa Bác Sĩ: {e}")
    def delete_data_bs():
        ma_bs = widgets_bs['entry_ma_bs'].get()
        if not ma_bs: messagebox.showwarning("Chưa chọn", "Vui lòng chọn bác sĩ để xóa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Xóa Bác Sĩ '{ma_bs}'?"):
                with get_connection() as conn: cursor = conn.cursor(); query = f"DELETE FROM {TABLE_NAME_BS} WHERE MaBacSi = ?"; cursor.execute(query, (ma_bs)); conn.commit()
                messagebox.showinfo("Thành công", "Đã xóa Bác Sĩ!"); clear_entries_bs(); fetch_data_bs()
        except pyodbc.IntegrityError: messagebox.showerror("Lỗi", "Không thể xóa: Bác sĩ này đã có Hồ Sơ Khám liên quan.")
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể xóa Bác Sĩ: {e}")
    def on_row_select_bs(event):
        try:
            selected_item = widgets_bs['tree_bs'].focus();
            if not selected_item: return
            item_values = widgets_bs['tree_bs'].item(selected_item, 'values'); clear_entries_bs()
            widgets_bs['entry_ma_bs'].insert(0, item_values[0]); widgets_bs['entry_ten_bs'].insert(0, item_values[1]); widgets_bs['entry_chuyenkhoa_bs'].insert(0, item_values[2])
            widgets_bs['entry_ma_bs'].config(state='readonly'); widgets_bs['entry_ten_bs'].config(state='readonly')
        except Exception: pass
    def clear_entries_bs():
        widgets_bs['entry_ma_bs'].config(state='normal'); widgets_bs['entry_ten_bs'].config(state='normal'); widgets_bs['entry_ma_bs'].delete(0, 'end'); widgets_bs['entry_ten_bs'].delete(0, 'end'); widgets_bs['entry_chuyenkhoa_bs'].delete(0, 'end')

    # --- GUI Tab Bác Sĩ ---
    form_frame = tk.LabelFrame(tab_frame, text="Thông tin Bác Sĩ (Mã BS phải có trong Tab Nhân Viên)"); form_frame.pack(pady=10, padx=20, fill="x")
    tk.Label(form_frame, text="Mã Bác Sĩ:").grid(row=0, column=0, padx=5, pady=5, sticky="e"); widgets_bs['entry_ma_bs'] = tk.Entry(form_frame, width=30); widgets_bs['entry_ma_bs'].grid(row=0, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Họ Tên (từ NV):").grid(row=1, column=0, padx=5, pady=5, sticky="e"); widgets_bs['entry_ten_bs'] = tk.Entry(form_frame, width=30); widgets_bs['entry_ten_bs'].grid(row=1, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Chuyên Khoa:").grid(row=0, column=2, padx=5, pady=5, sticky="e"); widgets_bs['entry_chuyenkhoa_bs'] = tk.Entry(form_frame, width=30); widgets_bs['entry_chuyenkhoa_bs'].grid(row=0, column=3, padx=5, pady=5)
    button_frame = tk.Frame(tab_frame); button_frame.pack(pady=5, padx=20, fill="x")
    tk.Button(button_frame, text="Thêm Mới", command=insert_data_bs, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Sửa", command=update_data_bs, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa", command=delete_data_bs, bg="#ff6666", fg="white", width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa Trắng Form", command=clear_entries_bs, width=15).pack(side="left", padx=10)
    display_frame = tk.LabelFrame(tab_frame, text="Danh Sách Bác Sĩ"); display_frame.pack(pady=10, padx=20, fill="both", expand=True)
    tk.Button(display_frame, text="Tải Lại Dữ Liệu", command=fetch_data_bs).pack(pady=10); tree_scroll = tk.Scrollbar(display_frame); tree_scroll.pack(side="right", fill="y"); tree_scroll_x = tk.Scrollbar(display_frame, orient="horizontal"); tree_scroll_x.pack(side="bottom", fill="x")
    widgets_bs['tree_bs'] = ttk.Treeview(display_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_x.set); widgets_bs['tree_bs'].pack(fill="both", expand=True); tree_scroll.config(command=widgets_bs['tree_bs'].yview); tree_scroll_x.config(command=widgets_bs['tree_bs'].xview); widgets_bs['tree_bs'].bind("<<TreeviewSelect>>", on_row_select_bs); fetch_data_bs()

# #############################################################
# PHẦN 8: TAB QUẢN LÝ THUỐC (CRUD)
# #############################################################
def create_thuoc_tab(tab_frame):
    widgets_thuoc = {}
    TABLE_NAME_THUOC = "[Thuoc].[Thuoc]"

    def fetch_data_thuoc():
        tree_thuoc = widgets_thuoc['tree_thuoc']
        for row in tree_thuoc.get_children(): tree_thuoc.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = f"SELECT MaThuoc, TenThuoc, DonViTinh, DonGia, SoLuongTon FROM {TABLE_NAME_THUOC}"
                cursor.execute(query)
                if not tree_thuoc["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_thuoc["columns"] = columns; tree_thuoc["show"] = "headings" 
                    for col in columns:
                        tree_thuoc.heading(col, text=col); tree_thuoc.column(col, width=120)
                rows = cursor.fetchall()
                data_cache["thuoc"].clear() 
                for row in rows:
                    display_row = ["" if v is None else v for v in row]
                    tree_thuoc.insert("", "end", values=display_row)
                    data_cache["thuoc"][row[0]] = row[1] 
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể lấy dữ liệu Thuốc: {e}")

    def insert_data_thuoc():
        values = (widgets_thuoc['entry_ma_thuoc'].get(), widgets_thuoc['entry_ten_thuoc'].get(), widgets_thuoc['entry_dvt_thuoc'].get() or None, widgets_thuoc['entry_dongia_thuoc'].get() or 0, widgets_thuoc['entry_soluong_thuoc'].get() or 0)
        if not values[0] or not values[1]: messagebox.showwarning("Thiếu thông tin", "Mã Thuốc và Tên Thuốc là bắt buộc"); return
        try:
            with get_connection() as conn: cursor = conn.cursor(); query = f"INSERT INTO {TABLE_NAME_THUOC} (MaThuoc, TenThuoc, DonViTinh, DonGia, SoLuongTon) VALUES (?, ?, ?, ?, ?)"; cursor.execute(query, (values[0], values[1], values[2], float(values[3]), int(values[4]))); conn.commit()
            messagebox.showinfo("Thành công", "Đã thêm Thuốc!"); clear_entries_thuoc(); fetch_data_thuoc()
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể thêm Thuốc: {e}")
    def update_data_thuoc():
        values = (widgets_thuoc['entry_ten_thuoc'].get(), widgets_thuoc['entry_dvt_thuoc'].get() or None, widgets_thuoc['entry_dongia_thuoc'].get() or 0, widgets_thuoc['entry_soluong_thuoc'].get() or 0, widgets_thuoc['entry_ma_thuoc'].get())
        if not values[4]: messagebox.showwarning("Chưa chọn", "Vui lòng chọn thuốc để sửa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Sửa thuốc {values[4]}?"):
                with get_connection() as conn: cursor = conn.cursor(); query = f"UPDATE {TABLE_NAME_THUOC} SET TenThuoc = ?, DonViTinh = ?, DonGia = ?, SoLuongTon = ? WHERE MaThuoc = ?"; cursor.execute(query, (values[0], values[1], float(values[2]), int(values[3]), values[4])); conn.commit()
                messagebox.showinfo("Thành công", "Đã sửa Thuốc!"); clear_entries_thuoc(); fetch_data_thuoc()
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể sửa Thuốc: {e}")
    def delete_data_thuoc():
        ma_thuoc = widgets_thuoc['entry_ma_thuoc'].get()
        if not ma_thuoc: messagebox.showwarning("Chưa chọn", "Vui lòng chọn thuốc để xóa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Xóa Thuốc '{ma_thuoc}'?"):
                with get_connection() as conn: cursor = conn.cursor(); query = f"DELETE FROM {TABLE_NAME_THUOC} WHERE MaThuoc = ?"; cursor.execute(query, (ma_thuoc)); conn.commit()
                messagebox.showinfo("Thành công", "Đã xóa Thuốc!"); clear_entries_thuoc(); fetch_data_thuoc()
        except pyodbc.IntegrityError: messagebox.showerror("Lỗi", "Không thể xóa: Thuốc này đã có dữ liệu liên quan (Đơn Thuốc).")
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể xóa Thuốc: {e}")
    def on_row_select_thuoc(event):
        try:
            selected_item = widgets_thuoc['tree_thuoc'].focus();
            if not selected_item: return
            item_values = widgets_thuoc['tree_thuoc'].item(selected_item, 'values'); clear_entries_thuoc()
            widgets_thuoc['entry_ma_thuoc'].insert(0, item_values[0]); widgets_thuoc['entry_ten_thuoc'].insert(0, item_values[1]); widgets_thuoc['entry_dvt_thuoc'].insert(0, item_values[2]); widgets_thuoc['entry_dongia_thuoc'].insert(0, item_values[3]); widgets_thuoc['entry_soluong_thuoc'].insert(0, item_values[4])
            widgets_thuoc['entry_ma_thuoc'].config(state='readonly')
        except Exception: pass
    def clear_entries_thuoc():
        widgets_thuoc['entry_ma_thuoc'].config(state='normal'); widgets_thuoc['entry_ma_thuoc'].delete(0, 'end'); widgets_thuoc['entry_ten_thuoc'].delete(0, 'end'); widgets_thuoc['entry_dvt_thuoc'].delete(0, 'end'); widgets_thuoc['entry_dongia_thuoc'].delete(0, 'end'); widgets_thuoc['entry_soluong_thuoc'].delete(0, 'end')

    # --- GUI Tab Thuốc ---
    form_frame = tk.LabelFrame(tab_frame, text="Thông tin Thuốc"); form_frame.pack(pady=10, padx=20, fill="x")
    tk.Label(form_frame, text="Mã Thuốc:").grid(row=0, column=0, padx=5, pady=5, sticky="e"); widgets_thuoc['entry_ma_thuoc'] = tk.Entry(form_frame, width=30); widgets_thuoc['entry_ma_thuoc'].grid(row=0, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Tên Thuốc:").grid(row=1, column=0, padx=5, pady=5, sticky="e"); widgets_thuoc['entry_ten_thuoc'] = tk.Entry(form_frame, width=30); widgets_thuoc['entry_ten_thuoc'].grid(row=1, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Đơn Vị Tính:").grid(row=2, column=0, padx=5, pady=5, sticky="e"); widgets_thuoc['entry_dvt_thuoc'] = tk.Entry(form_frame, width=30); widgets_thuoc['entry_dvt_thuoc'].grid(row=2, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Đơn Giá:").grid(row=0, column=2, padx=5, pady=5, sticky="e"); widgets_thuoc['entry_dongia_thuoc'] = tk.Entry(form_frame, width=30); widgets_thuoc['entry_dongia_thuoc'].grid(row=0, column=3, padx=5, pady=5)
    tk.Label(form_frame, text="Số Lượng Tồn:").grid(row=1, column=2, padx=5, pady=5, sticky="e"); widgets_thuoc['entry_soluong_thuoc'] = tk.Entry(form_frame, width=30); widgets_thuoc['entry_soluong_thuoc'].grid(row=1, column=3, padx=5, pady=5)
    button_frame = tk.Frame(tab_frame); button_frame.pack(pady=5, padx=20, fill="x")
    tk.Button(button_frame, text="Thêm Mới", command=insert_data_thuoc, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Sửa", command=update_data_thuoc, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa", command=delete_data_thuoc, bg="#ff6666", fg="white", width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa Trắng Form", command=clear_entries_thuoc, width=15).pack(side="left", padx=10)
    display_frame = tk.LabelFrame(tab_frame, text="Danh Sách Thuốc"); display_frame.pack(pady=10, padx=20, fill="both", expand=True)
    tk.Button(display_frame, text="Tải Lại Dữ Liệu", command=fetch_data_thuoc).pack(pady=10); tree_scroll = tk.Scrollbar(display_frame); tree_scroll.pack(side="right", fill="y"); tree_scroll_x = tk.Scrollbar(display_frame, orient="horizontal"); tree_scroll_x.pack(side="bottom", fill="x")
    widgets_thuoc['tree_thuoc'] = ttk.Treeview(display_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_x.set); widgets_thuoc['tree_thuoc'].pack(fill="both", expand=True); tree_scroll.config(command=widgets_thuoc['tree_thuoc'].yview); tree_scroll_x.config(command=widgets_thuoc['tree_thuoc'].xview); widgets_thuoc['tree_thuoc'].bind("<<TreeviewSelect>>", on_row_select_thuoc); fetch_data_thuoc()

# #############################################################
# PHẦN 9: TAB QUẢN LÝ DỊCH VỤ (CRUD)
# #############################################################
def create_dichvu_tab(tab_frame):
    widgets_dv = {}
    TABLE_NAME_DV = "[DichVu].[DichVu]"

    def fetch_data_dv():
        tree_dv = widgets_dv['tree_dv']
        for row in tree_dv.get_children(): tree_dv.delete(row)
        try:
            with get_connection() as conn:
                cursor = conn.cursor()
                query = f"SELECT MaDichVu, TenDichVu, MoTa, DonGia FROM {TABLE_NAME_DV}"
                cursor.execute(query)
                if not tree_dv["columns"]:
                    columns = [column[0] for column in cursor.description]
                    tree_dv["columns"] = columns; tree_dv["show"] = "headings"
                    for col in columns:
                        tree_dv.heading(col, text=col); tree_dv.column(col, width=150)
                rows = cursor.fetchall()
                data_cache["dichvu"].clear() 
                for row in rows:
                    display_row = ["" if v is None else v for v in row]
                    tree_dv.insert("", "end", values=display_row)
                    data_cache["dichvu"][row[0]] = row[1] 
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể lấy dữ liệu Dịch Vụ: {e}")

    def insert_data_dv():
        values = (widgets_dv['entry_ma_dv'].get(), widgets_dv['entry_ten_dv'].get(), widgets_dv['entry_mota_dv'].get() or None, widgets_dv['entry_dongia_dv'].get() or 0)
        if not values[0] or not values[1]: messagebox.showwarning("Thiếu thông tin", "Mã và Tên Dịch Vụ là bắt buộc"); return
        try:
            with get_connection() as conn: cursor = conn.cursor(); query = f"INSERT INTO {TABLE_NAME_DV} (MaDichVu, TenDichVu, MoTa, DonGia) VALUES (?, ?, ?, ?)"; cursor.execute(query, (values[0], values[1], values[2], float(values[3]))); conn.commit()
            messagebox.showinfo("Thành công", "Đã thêm Dịch Vụ!"); clear_entries_dv(); fetch_data_dv()
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể thêm Dịch Vụ: {e}")
    def update_data_dv():
        values = (widgets_dv['entry_ten_dv'].get(), widgets_dv['entry_mota_dv'].get() or None, widgets_dv['entry_dongia_dv'].get() or 0, widgets_dv['entry_ma_dv'].get())
        if not values[3]: messagebox.showwarning("Chưa chọn", "Vui lòng chọn dịch vụ để sửa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Sửa dịch vụ {values[3]}?"):
                with get_connection() as conn: cursor = conn.cursor(); query = f"UPDATE {TABLE_NAME_DV} SET TenDichVu = ?, MoTa = ?, DonGia = ? WHERE MaDichVu = ?"; cursor.execute(query, (values[0], values[1], float(values[2]), values[3])); conn.commit()
                messagebox.showinfo("Thành công", "Đã sửa Dịch Vụ!"); clear_entries_dv(); fetch_data_dv()
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể sửa Dịch Vụ: {e}")
    def delete_data_dv():
        ma_dv = widgets_dv['entry_ma_dv'].get()
        if not ma_dv: messagebox.showwarning("Chưa chọn", "Vui lòng chọn dịch vụ để xóa"); return
        try:
            if messagebox.askyesno("Xác nhận", f"Xóa Dịch Vụ '{ma_dv}'?"):
                with get_connection() as conn: cursor = conn.cursor(); query = f"DELETE FROM {TABLE_NAME_DV} WHERE MaDichVu = ?"; cursor.execute(query, (ma_dv)); conn.commit()
                messagebox.showinfo("Thành công", "Đã xóa Dịch Vụ!"); clear_entries_dv(); fetch_data_dv()
        except pyodbc.IntegrityError: messagebox.showerror("Lỗi", "Không thể xóa: Dịch Vụ này đã có dữ liệu liên quan (Chi Tiết Dịch Vụ).")
        except Exception as e: messagebox.showerror("Lỗi", f"Không thể xóa Dịch Vụ: {e}")
    def on_row_select_dv(event):
        try:
            selected_item = widgets_dv['tree_dv'].focus();
            if not selected_item: return
            item_values = widgets_dv['tree_dv'].item(selected_item, 'values'); clear_entries_dv()
            widgets_dv['entry_ma_dv'].insert(0, item_values[0]); widgets_dv['entry_ten_dv'].insert(0, item_values[1]); widgets_dv['entry_mota_dv'].insert(0, item_values[2]); widgets_dv['entry_dongia_dv'].insert(0, item_values[3])
            widgets_dv['entry_ma_dv'].config(state='readonly')
        except Exception: pass
    def clear_entries_dv():
        widgets_dv['entry_ma_dv'].config(state='normal'); widgets_dv['entry_ma_dv'].delete(0, 'end'); widgets_dv['entry_ten_dv'].delete(0, 'end'); widgets_dv['entry_mota_dv'].delete(0, 'end'); widgets_dv['entry_dongia_dv'].delete(0, 'end')

    # --- GUI Tab Dịch Vụ ---
    form_frame = tk.LabelFrame(tab_frame, text="Thông tin Dịch Vụ"); form_frame.pack(pady=10, padx=20, fill="x")
    tk.Label(form_frame, text="Mã DV:").grid(row=0, column=0, padx=5, pady=5, sticky="e"); widgets_dv['entry_ma_dv'] = tk.Entry(form_frame, width=30); widgets_dv['entry_ma_dv'].grid(row=0, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Tên Dịch Vụ:").grid(row=1, column=0, padx=5, pady=5, sticky="e"); widgets_dv['entry_ten_dv'] = tk.Entry(form_frame, width=30); widgets_dv['entry_ten_dv'].grid(row=1, column=1, padx=5, pady=5)
    tk.Label(form_frame, text="Mô Tả:").grid(row=0, column=2, padx=5, pady=5, sticky="e"); widgets_dv['entry_mota_dv'] = tk.Entry(form_frame, width=30); widgets_dv['entry_mota_dv'].grid(row=0, column=3, padx=5, pady=5)
    tk.Label(form_frame, text="Đơn Giá:").grid(row=1, column=2, padx=5, pady=5, sticky="e"); widgets_dv['entry_dongia_dv'] = tk.Entry(form_frame, width=30); widgets_dv['entry_dongia_dv'].grid(row=1, column=3, padx=5, pady=5)
    button_frame = tk.Frame(tab_frame); button_frame.pack(pady=5, padx=20, fill="x")
    tk.Button(button_frame, text="Thêm Mới", command=insert_data_dv, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Sửa", command=update_data_dv, width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa", command=delete_data_dv, bg="#ff6666", fg="white", width=12).pack(side="left", padx=10); tk.Button(button_frame, text="Xóa Trắng Form", command=clear_entries_dv, width=15).pack(side="left", padx=10)
    display_frame = tk.LabelFrame(tab_frame, text="Danh Sách Dịch Vụ"); display_frame.pack(pady=10, padx=20, fill="both", expand=True)
    tk.Button(display_frame, text="Tải Lại Dữ Liệu", command=fetch_data_dv).pack(pady=10); tree_scroll = tk.Scrollbar(display_frame); tree_scroll.pack(side="right", fill="y"); tree_scroll_x = tk.Scrollbar(display_frame, orient="horizontal"); tree_scroll_x.pack(side="bottom", fill="x")
    widgets_dv['tree_dv'] = ttk.Treeview(display_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_x.set); widgets_dv['tree_dv'].pack(fill="both", expand=True); tree_scroll.config(command=widgets_dv['tree_dv'].yview); tree_scroll_x.config(command=widgets_dv['tree_dv'].xview); widgets_dv['tree_dv'].bind("<<TreeviewSelect>>", on_row_select_dv); fetch_data_dv()





# #############################################################
#
# PHẦN 10: TẠO GUI CHÍNH VÀ CÁC TAB (ĐÃ CẬP NHẬT CHO BỆNH NHÂN)
#
# #############################################################

def create_toolbar(root, user_role, user_id):
    toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
    
    tk.Button(toolbar, text=" 🔒 Đăng Xuất", 
              command=root.destroy, 
              bg="#d9534f", fg="white").pack(side=tk.RIGHT, padx=5, pady=5)
    
    # Hiển thị tên (chưa tối ưu) hoặc Mã
    display_name = user_id 
    if user_role == "BENHNHAN":
        display_role = "Bệnh Nhân"
        # Lấy tên bệnh nhân từ cache
        display_name = data_cache["benhnhan"].get(user_id, user_id)
    else:
        display_role = user_role
        
    tk.Label(toolbar, text=f"Người dùng: {display_name} | Chức vụ: {display_role}", 
             font=('Arial', 10, 'bold'), fg="#0275d8").pack(side=tk.LEFT, padx=10, pady=5)
    
    toolbar.pack(fill='x')


def run_main_application():
    
    MAIN_WIDTH = 1200
    MAIN_HEIGHT = 800

    while True:
        root = tk.Tk()
        root.title("Hệ Thống Quản Lý Phòng Khám")
        center_window_on_screen(root, MAIN_WIDTH, MAIN_HEIGHT)

        login_window = LoginWindow(root)
        root.wait_window(login_window) 
        
        user_role = login_window.user_role 
        user_id = login_window.user_id # <-- Lấy ID

        if user_role and user_id:
            # --- ĐĂNG NHẬP THÀNH CÔNG ---
            try:
                root.deiconify() 
                load_all_data_caches()

                create_toolbar(root, user_role, user_id) # <-- Truyền ID vào Toolbar
                
                notebook = ttk.Notebook(root)
                
                # Tạo TẤT CẢ CÁC Frame (bao gồm cả tab của BN)
                tab_tiep_nhan = ttk.Frame(notebook); tab_kham_benh = ttk.Frame(notebook)
                tab_thanh_toan = ttk.Frame(notebook); tab_bao_cao = ttk.Frame(notebook)
                tab_benh_nhan = ttk.Frame(notebook); tab_nhan_vien = ttk.Frame(notebook)
                tab_bac_si = ttk.Frame(notebook); tab_thuoc = ttk.Frame(notebook)
                tab_dich_vu = ttk.Frame(notebook)
                tab_benhan_canhan = ttk.Frame(notebook) # <-- TAB BỆNH NHÂN MỚI
                tab_thanhtoan_canhan = ttk.Frame(notebook) # <-- TAB BỆNH NHÂN MỚI
                
                all_tabs = {
                    "tab_tiep_nhan": tab_tiep_nhan, "tab_kham_benh": tab_kham_benh, "tab_thanh_toan": tab_thanh_toan,
                    "tab_bao_cao": tab_bao_cao, "tab_benh_nhan": tab_benh_nhan, "tab_nhan_vien": tab_nhan_vien,
                    "tab_bac_si": tab_bac_si, "tab_thuoc": tab_thuoc, "tab_dich_vu": tab_dich_vu,
                    "tab_benhan_canhan": tab_benhan_canhan, # <-- TAB BỆNH NHÂN MỚI
                    "tab_thanhtoan_canhan": tab_thanhtoan_canhan # <-- TAB BỆNH NHÂN MỚI
                }

                notebook.pack(expand=True, fill='both', padx=10, pady=10)

                # Tạo nội dung cho TẤT CẢ các tab
                create_tiepnhan_tab(tab_tiep_nhan); create_khambenh_tab(tab_kham_benh)
                create_thanhtoan_tab(tab_thanh_toan); create_report_tab(tab_bao_cao)
                create_benhnhan_tab(tab_benh_nhan); create_nhanvien_tab(tab_nhan_vien)
                create_bacsi_tab(tab_bac_si); create_thuoc_tab(tab_thuoc)
                create_dichvu_tab(tab_dich_vu)
                # Tạo tab cho Bệnh nhân và truyền Mã Bệnh Nhân vào
                create_benhan_canhan_tab(tab_benhan_canhan, user_id) 
                create_thanhtoan_canhan_tab(tab_thanhtoan_canhan, user_id)
                
                # Áp dụng phân quyền
                root.title(f"Hệ Thống Quản Lý Phòng Khám - (Vai trò: {user_role})")
                setup_ui_for_role(notebook, user_role, all_tabs)

                root.mainloop()
            
            except Exception as e:
                root.destroy() 
                messagebox.showerror("Lỗi Nghiêm Trọng Khi Khởi Động", 
                                     f"Không thể tải dữ liệu ứng dụng: {e}\n"
                                     "Vui lòng kiểm tra kết nối CSDL và các VIEW.")
        
        else:
            root.destroy()
            break 

if __name__ == "__main__":
    run_main_application()