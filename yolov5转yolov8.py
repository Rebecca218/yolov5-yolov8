import os
import glob

def verify_and_normalize_labels(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    txt_files = glob.glob(os.path.join(input_dir, '*.txt'))
    
    for txt_file in txt_files:
        with open(txt_file, 'r') as f:
            lines = f.readlines()
        
        normalized_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 5:
                class_id, x_center, y_center, width, height = map(float, parts)
                
                # 确保所有值都在正确的范围内
                class_id = int(class_id)
                x_center = max(0, min(1, x_center))
                y_center = max(0, min(1, y_center))
                width = max(0, min(1, width))
                height = max(0, min(1, height))
                
                normalized_line = f"{class_id} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n"
                normalized_lines.append(normalized_line)
            else:
                print(f"警告：在文件 {txt_file} 中发现无效行: {line.strip()}")
        
        output_file = os.path.join(output_dir, os.path.basename(txt_file))
        with open(output_file, 'w') as f:
            f.writelines(normalized_lines)
    
    print(f"验证和规范化完成。结果保存在 {output_dir}")

# 使用示例
input_directory = 'path/to/yolov5/labels'
output_directory = 'path/to/yolov8/labels'
verify_and_normalize_labels(input_directory, output_directory)

