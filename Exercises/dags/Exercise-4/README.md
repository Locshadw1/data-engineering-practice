# Bài tập #4 - Chuyển đổi JSON sang CSV + Cấu trúc thư mục không đồng nhất

Trong bài tập thứ tư này, bạn sẽ tiếp tục thực hành kỹ năng Python của mình,
chúng ta sẽ tìm kiếm trong một cấu trúc thư mục không đồng nhất, cìm kiếm các file `json`.
Khi tìm thấy các file `json`, chúng ta sẽ chuyển đổi chúng thành các file `csv`.

Chúng ta có thể làm việc với ba package `Python` hữu ích, `glob`, `json`, và `csv`.

#### Thiết lập
1. Chuyển thư mục trong dòng lệnh 
   vào thư mục `Exercise-4` bằng lệnh `cd Exercises/Exercise-4`
   
2. Chạy `docker build --tag=exercise-4 .` để xây dựng image `Docker`.

3. Có một file gọi là `main.py` trong thư mục `Exercise-4`, đây
là nơi bạn sẽ đặt code `Python` để hoàn thành bài tập.
   
4. Khi bạn đã hoàn thành dự án hoặc muốn chạy thử code của mình,
   hãy chạy lệnh sau `docker-compose up run` từ trong thư mục `Exercises/Exercise-4`

#### Yêu cầu
Có một thư mục gọi là `data` trong thư mục hiện tại, `Exercises/Exercise-4`. Cũng có
các file `json` nằm ở nhiều vị trí khác nhau trong cấu trúc thư mục này.

Nhiệm vụ của bạn là sử dụng `Python` để tìm tất cả các file `json` nằm trong thư mục `data`.
Sau khi tìm thấy tất cả, đọc chúng bằng `Python` và chuyển đổi chúng thành các file `csv`, để làm điều này
bạn sẽ phải làm phẳng một số cấu trúc dữ liệu `json` lồng nhau.

Ví dụ, có một cấu trúc `{"type":"Point","coordinates":[-99.9,16.88333]}` phải được làm phẳng.

Nói chung, script của bạn nên thực hiện các bước sau ...
1. Duyệt qua thư mục `data` bằng `Python` và xác định tất cả các file `json`.
2. Tải tất cả các file `json`.
3. Làm phẳng cấu trúc dữ liệu `json`.
4. Ghi kết quả vào một file `csv`, một file cho mỗi file json, bao gồm cả tên tiêu đề. 