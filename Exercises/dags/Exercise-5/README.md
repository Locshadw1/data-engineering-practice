# Bài tập #5 - Mô hình hóa dữ liệu cho Postgres + Python

Trong bài tập thứ năm này, bạn sẽ làm việc trên một số chủ đề khác nhau,
mô hình hóa dữ liệu, Python, và Postgres. Đây là những vấn đề phổ biến trong 
kỹ thuật dữ liệu.

#### Thiết lập
1. Chuyển thư mục trong dòng lệnh 
   vào thư mục `Exercise-5` bằng lệnh `cd Exercises/Exercise-5`
   
2. Chạy `docker build --tag=exercise-5 .` để xây dựng image `Docker`.

3. Có một file gọi là `main.py` trong thư mục `Exercise-5`, đây
là nơi bạn sẽ đặt code `Python` để hoàn thành bài tập.
   
4. Khi bạn đã hoàn thành dự án hoặc muốn chạy thử code của mình,
   hãy chạy lệnh sau `docker-compose up run` từ trong thư mục `Exercises/Exercise-5`

#### Yêu cầu
Có một thư mục gọi là `data` trong thư mục hiện tại, `Exercises/Exercise-5`. Cũng có
3 file `csv` nằm trong thư mục đó. Mở từng file và kiểm tra nó, 
nhiệm vụ đầu tiên là tạo một script `sql` với `DDL` để chứa
một câu lệnh `CREATE` cho mỗi file dữ liệu. Hãy nhớ suy nghĩ về các kiểu dữ liệu. 
Ngoài ra, các câu lệnh `CREATE` này nên bao gồm các chỉ mục cho mỗi bảng, cũng như
các khóa chính và khóa ngoại.

Sau khi bạn đã hoàn thành script `sql` này, chúng ta phải kết nối với `Postgres` bằng cách sử dụng package `Python`
gọi là `psycopg2`. Sau khi kết nối, chúng ta sẽ chạy script `sql` của mình trên cơ sở dữ liệu.

Lưu ý: Script `main.py` mặc định đã có cấu hình kết nối Python để kết nối
với phiên bản `Postgres` được tự động khởi động bởi `Docker` khi bạn chạy
lệnh `docker-compose up run` (từ trong thư mục `Exercises/Exercise-5`).

Cuối cùng, chúng ta sẽ sử dụng `psycopg2` để chèn dữ liệu từ mỗi file `csv` vào bảng mà bạn đã tạo.

Nói chung, script của bạn nên thực hiện các bước sau ...
1. Kiểm tra từng file `csv` trong thư mục `data`. Thiết kế một câu lệnh `CREATE` cho mỗi file.
2. Đảm bảo bạn có các chỉ mục, khóa chính và khóa ngoại.
3. Sử dụng `psycopg2` để kết nối với `Postgres` trên `localhost` và cổng mặc định.
4. Tạo các bảng trên cơ sở dữ liệu.
5. Nhập các file `csv` vào các bảng bạn đã tạo, cũng sử dụng `psycopg2`. 