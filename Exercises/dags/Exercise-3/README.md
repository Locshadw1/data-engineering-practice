# Bài tập #3 - Boto3 AWS + s3 + Python

Trong bài tập thứ ba này, bạn sẽ tiếp tục thực hành kỹ năng Python của mình,
chúng ta sẽ mở rộng ý tưởng về việc tải file và bắt đầu bằng cách 
lấy file từ một bucket `s3` trên `aws` trong một quy trình nhiều bước.

Làm việc với package `Python` `boto3` để tương tác với `aws` là rất
phổ biến, và điều này sẽ đảm bảo bạn được giới thiệu về chủ đề đó.

#### Thiết lập
1. Chuyển thư mục trong dòng lệnh 
   vào thư mục `Exercise-3` bằng lệnh `cd Exercises/Exercise-3`
   
2. Chạy `docker build --tag=exercise-3 .` để xây dựng image `Docker`.

3. Có một file gọi là `main.py` trong thư mục `Exercise-3`, đây
là nơi bạn sẽ đặt code `Python` để hoàn thành bài tập.
   
4. Khi bạn đã hoàn thành dự án hoặc muốn chạy thử code của mình,
   hãy chạy lệnh sau `docker-compose up run` từ trong thư mục `Exercises/Exercise-3`

#### Yêu cầu
AWS cung cấp một số dữ liệu web "common crawl", có sẵn trên `s3` mà không cần
quyền đặc biệt. http://commoncrawl.org/the-data/get-started/

Nhiệm vụ của bạn gồm hai phần, tải xuống một file `.gz` nằm trong bucket s3 `commoncrawl`
và key `crawl-data/CC-MAIN-2022-05/wet.paths.gz` bằng cách sử dụng `boto3`.

Sau khi tải xuống file này, bạn phải giải nén file, mở nó, và 
tải xuống uri file nằm ở dòng đầu tiên bằng cách sử dụng `boto3` một lần nữa. Lưu trữ 
file cục bộ và lặp qua các dòng của file, in từng dòng ra `stdout`.

Nói chung, script của bạn nên thực hiện các bước sau ...
1. Sử dụng `boto3` để tải xuống file từ s3 nằm ở bucket `commoncrawl` và key `crawl-data/CC-MAIN-2022-05/wet.paths.gz`
2. Giải nén và mở file này bằng Python (gợi ý, nó chỉ là văn bản).
3. Lấy `uri` từ dòng đầu tiên của file này.
4. Một lần nữa, tải xuống file `uri` đó từ `s3` bằng cách sử dụng `boto3` một lần nữa.
5. In từng dòng, lặp đến stdout/dòng lệnh/terminal.

Điểm thêm: 

1. KHÔNG tải toàn bộ file cuối cùng vào bộ nhớ trước khi in từng dòng,
hãy stream file.
   
2. KHÔNG tải file `.gz` ban đầu xuống đĩa, hãy tải xuống, giải nén và đọc nó trong bộ nhớ. 