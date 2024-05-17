import json

# Đọc dữ liệu từ file JSON

def file_processing(temp):
# Khởi tạo mảng để chứa các cặp text và box
    with open(temp, 'r', encoding='utf-8') as file:
        data = json.load(file)
    merged_data = []

    # Duyệt qua danh sách các cặp key-value từ dữ liệu JSON
    for item in data:
        # Lấy text và box từ cặp key-value
        key_text = item['key']['text']
        key_box = item['key']['box']
        value_text = item['value']['text']
        value_box = item['value']['box']

        # Thêm cặp text và box vào mảng gộp
        merged_data.append({
            'key_text': key_text,
            'key_box': key_box,
            'value_text': value_text,
            'value_box': value_box
        })

    # Tìm chỉ số của phần tử đầu tiên có 'chẩn đoán' hoặc 'đoán' trong key_text hoặc value_text
    index = None
    for i, item in enumerate(merged_data):
        key_text_lower = item['key_text'].lower()
        value_text_lower = item['value_text'].lower()
        if 'chẩn đoán' in key_text_lower or 'đoán' in key_text_lower or 'chẩn đoán' in value_text_lower or 'đoán' in value_text_lower or 'chẩn' in value_text_lower or 'chẩn' in key_text_lower:
            index = i
            break

    # Nếu không tìm thấy "chẩn đoán" hoặc "đoán", lấy toàn bộ mảng
    if index is None:
        selected_data = merged_data
    else:
        selected_data = merged_data[index:]

    # In ra mảng đã chọn
    # for item in selected_data:
    #     print(item)
    class MergedData:
        def __init__(self, key_text, key_box, value_texts, value_boxes):
            self.key_text = key_text
            self.key_box = key_box
            self.value_texts = value_texts
            self.value_boxes = value_boxes

    def merge_data(merged_data):
        merged_selected_data = []

        for item1 in merged_data:
            merged_key_text = item1['key_text']
            merged_key_box = item1['key_box']
            merged_value_texts = []
            merged_value_boxes = []

            for item2 in merged_data:
                if item1['key_box'] == item2['key_box']:
                    merged_value_texts.append(item2['value_text'])
                    merged_value_boxes.append(item2['value_box'])

            # Thêm vào danh sách mới nếu chưa tồn tại
            if not any(item.key_text == merged_key_text for item in merged_selected_data):
                merged_selected_data.append(MergedData(merged_key_text, merged_key_box, merged_value_texts, merged_value_boxes))

        return merged_selected_data

    # Sử dụng class và phương thức để gộp merged_data
    merged_selected_data = merge_data(selected_data)

    #In ra kết quả đã gộp
    # for item in merged_selected_data:
    #     print("Key Text:", item.key_text)
    #     print("Key Box:", item.key_box)
    #     for i in range(len(item.value_texts)):
    #         print("Value Text:", item.value_texts[i])
    #         print("Value Box:", item.value_boxes[i])
    #     print()
    # Khởi tạo danh sách để lưu thông tin theo thứ tự
    # Khởi tạo danh sách để lưu thông tin theo thứ tự
    # Khởi tạo danh sách thông thường
    output_list = []

    # Duyệt qua mỗi đối tượng MergedData
    for item in merged_selected_data:
        # Thêm key text và key box vào danh sách
        output_list.append(item.key_text)
        output_list.append(' '.join(map(str, item.key_box)))
        
        # Duyệt qua mỗi giá trị và hộp giá trị trong value_texts và value_boxes
        for i in range(len(item.value_texts)):
            output_list.append(item.value_texts[i])
            output_list.append(' '.join(map(str, item.value_boxes[i])))

    # In ra danh sách thông thường đã tạo
    #print(output_list)
    index = len(output_list) - 1  # Bắt đầu từ phần tử cuối cùng
    seen = set()  # Tạo một tập hợp để lưu trữ các phần tử đã xuất hiện

    while index >= 0:
        if isinstance(output_list[index], str):
            if output_list[index] in seen:
                del output_list[index]
                del output_list[index-1]
            else:
                seen.add(output_list[index])
                seen.add(output_list[index-1])
        index -= 2  # Di chuyển về phía trước 2 bước

    # # print(output_list)
    # for index, item in enumerate(output_list):
    #     if index % 2 == 0:
    #         print(item)

    found_diagnosis = False  # Biến cờ để đánh dấu khi gặp chuỗi "Chẩn đoán"
    for index, item in enumerate(output_list):
        if isinstance(item, str) and "chẩn đoán" in item.lower() or "chẩn" in item.lower() or "đoán" in item.lower() or "đoàn" in item.lower() or "chần" in item.lower():
            found_diagnosis = True  # Đánh dấu đã tìm thấy chuỗi "Chẩn đoán"
            if index % 2 == 0:
                print(item)  # In ra chuỗi "Chẩn đoán"
        elif found_diagnosis:  # Nếu đã tìm thấy chuỗi "Chẩn đoán", in ra các phần tử từ vị trí đó trở đi
            if index % 2 == 0:
                print(item)

    # Nếu không tìm thấy chuỗi "Chẩn đoán", in ra toàn bộ danh sách
    if not found_diagnosis:
        for index, item in enumerate(output_list):
            if index % 2 == 0:
                print(item)