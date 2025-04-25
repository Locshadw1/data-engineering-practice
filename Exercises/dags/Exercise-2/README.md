# Bài tập #2 - Web Scraping và Tải File bằng Python

Trong bài tập thứ hai này, bạn sẽ tiếp tục thực hành kỹ năng Python của mình,
chúng ta sẽ mở rộng ý tưởng về việc tải file từ các nguồn `HTTP` bằng Python,
nhưng thêm một yếu tố mới.

Bạn sẽ phải "web scrap" một trang `HTML` để tìm kiếm một ngày cụ thể, và xác định
file chính xác để xây dựng URL mà bạn có thể tải xuống file đó.

#### Thiết lập
1. Chuyển thư mục trong dòng lệnh 
   vào thư mục `Exercise-2` bằng lệnh `cd Exercises/Exercise-2`
   
2. Chạy `docker build --tag=exercise-2 .` để xây dựng image `Docker`.

3. Có một file gọi là `main.py` trong thư mục `Exercise-2`, đây
là nơi bạn sẽ đặt code `Python` để hoàn thành bài tập.
   
4. Khi bạn đã hoàn thành dự án hoặc muốn chạy thử code của mình,
   hãy chạy lệnh sau `docker-compose up run` từ trong thư mục `Exercises/Exercise-2`

#### Yêu cầu
Bạn cần tải một file dữ liệu thời tiết từ một trang web của chính phủ.
Các file nằm ở vị trí được chỉ định sau đây.

https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/

Bạn đang tìm kiếm file được `Last Modified` (Sửa đổi lần cuối) vào `2024-01-19 10:27`, bạn
không thể gian lận bằng cách tự tìm số file. Bạn phải sử dụng Python để scrape
trang web này, tìm tên file tương ứng với timestamp này, `2024-01-19 10:27`

Sau khi bạn đã có file chính xác và tải xuống, bạn phải tải file
vào `Pandas` và tìm bản ghi có `HourlyDryBulbTemperature` cao nhất.
In các bản ghi này ra dòng lệnh.

Nói chung, script của bạn nên thực hiện các bước sau ...
1. Thử web scrap/tải xuống nội dung của `https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/`
2. Phân tích cấu trúc của nó, xác định cách tìm file tương ứng với `2024-01-19 10:27` bằng Python.
3. Xây dựng `URL` cần thiết để tải xuống file này, và ghi file cục bộ.
4. Mở file với `Pandas` và tìm các bản ghi có `HourlyDryBulbTemperature` cao nhất.
5. In kết quả này ra stdout/dòng lệnh/terminal. 