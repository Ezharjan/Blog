with open('output.txt', 'r') as file:
    lines = file.readlines()

week_no = 0
with open('processed_file.txt', 'w') as file:
    for i, line in enumerate(lines):
        if not line.strip():  # 检查行是否为空行
            week_no += 1
            file.write(f'Week {week_no}')
        file.write(line)
