Project sử dụng Python phiên bản 3.8.5-64 bit. 
Chương trình được chạy trên hệ điều hành Ubuntu 20.04. 

Phần 1: cài đặt thư viện
File requirements.txt: tên các thư viện cần được cài đặt.
Cài đặt thư viên bằng câu lệnh trên termimal:
python3 -m pip install -r requirements.txt

Phần 2: crawl dữ liệu
Dữ liệu được crawl trên oto.com, xe.chotot.com,
Dữ liệu thô được lưu trữ trong thư mục dataset, dưới dạng file csv.
Do số lượng page của từng trang web là rất lớn, nên chúng em chỉ thực hiện demo dữ liệu trên số lượng page nhỏ.

Chạy code crawl
1. Crawl trên trang ChoTot
B1: dùng lệnh cd vào đến thư mục ChoTot: cd crawl\ChoTot
B2: sau đó chạy lệnh: scrapy crawl crawl_ChoTot
B3: Dữ liệu crawl về sẽ được hiển thị trên terminal

2. Crawl trên trang Carmudi
B1: Cài đặt hàng đợi Kafka
B2 Tạo topic: testTopiccc
B3: tạo Producer của Kafka để scapy ghi dữ liệu lên
B4: tạo consumer ghi ra file .txt
B5: chạy câu lệnh: scrapy carmudi để bắt đầu crawl

3. Crawl trên trang Oto.com
Chạy các cell trong file Oto.ipynb

Phần 3: Lập trình
Được chia làm 3 file, file tiền xử lý dữ liệu (preprocess.ipynb), file huấn luyện mô hình (train.pynb), và file dự đoán (predict.ipynb).
Các giá trị trong các cell đã được thiết lập sẵn, chỉ cần chạy là được.
