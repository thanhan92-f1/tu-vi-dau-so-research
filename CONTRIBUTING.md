# Đóng góp

Cảm ơn bạn muốn cải thiện dự án.

## Nguyên tắc

Mỗi thay đổi về quy tắc luận cần ghi:

- tên quy tắc;
- nguồn, ấn bản, chương/trang nếu có;
- trường phái;
- điều kiện áp dụng;
- phản chứng hoặc giới hạn;
- ví dụ kiểm thử;
- ảnh hưởng đến các kết luận hiện có.

Không thêm nội dung:

- khẳng định định mệnh tuyệt đối;
- chẩn đoán y khoa;
- nhận diện người âm cụ thể;
- nội dung sao chép dài từ sách có bản quyền;
- quy tắc không có nguồn nhưng được trình bày như sự thật cổ thư.

## Quy trình Pull Request

1. Tạo branch riêng.
2. Cập nhật tài liệu và test liên quan.
3. Chạy:

```bash
python3 scripts/validate_skill.py .
python3 -m unittest discover -s tests -v
```

4. Cập nhật `CHANGELOG.md` nếu thay đổi hành vi.
5. Trong PR, mô tả nguồn, lý do và trường hợp thử.

## Quy ước phiên bản

- `MAJOR`: thay đổi quy trình hoặc hợp đồng đầu ra không tương thích.
- `MINOR`: thêm chế độ, nguồn, schema hoặc khả năng mới.
- `PATCH`: sửa câu chữ, lỗi kiểm tra hoặc làm rõ quy tắc.
