import argparse

# Чете аргументи подадени от терминала
def parse_arguments():
    parser = argparse.ArgumentParser(description="Analyze a log file for errors, warnings, and stats.")
    parser.add_argument("file", help="Path to the log file")
    parser.add_argument("-o", "--output", help="Path to save the report (optional)")
    return parser.parse_args()

# Форматира текстов отчет от изчислените данни
def build_report(lines, error_count, warning_count, common_message, percentages):
    report_lines = []
    report_lines.append("=== Log Analysis Report ===")
    report_lines.append(f"Total lines: {len(lines)}")
    report_lines.append(f"Errors: {error_count}")                             
    report_lines.append(f"Warnings: {warning_count}")
    report_lines.append(f"Most common message: {common_message}")
    for level, percent in percentages.items():
        report_lines.append(f"  {level}: {percent:.2f}%")
    return "\n".join(report_lines)

# Записва отчета във файл който е посочен в терминала
def save_report(report_text, output_path):
    with open(output_path, "w") as file:
        file.write(report_text)

# Функция която отваря файл и връща списък от редовете му
def read_log_file(file_path):
    try:
        with open(file_path,"r") as file:
            return file.readlines()
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)

# Функция която брои колко пъти се срещат думите ERROR и WARNING и връща двойка числа (error_count,warning_count) 
def count_log_levels(lines):    
    error_count = 0
    warning_count = 0
    for line in lines:
        if("ERROR" in line):
            error_count+=1
        elif("WARNING" in line):
            warning_count +=1
    return error_count, warning_count

# функция която намира кое е съобщението което се среща най-често и връща съобщението
def most_common_message(lines):
    message_counts = {}
    for line in lines:
        message = line.strip().split(" ", 3)[-1]
        message_counts[message] = message_counts.get(message, 0) + 1
    return max(message_counts, key=message_counts.get)
    
# Функция която изчислява какъв процент е всяко ниво и врръща речник {ниво: процент}
def percentage_levels(lines):
    total = 0
    level_counts = {}

    for line in lines:
        level = line.strip().split(" ", 3)[-2]
        level_counts[level] = level_counts.get(level,0)+1
        total += 1
    
    percentages = {}
    for level,count in level_counts.items():
        percentages[level] = (count/total) * 100
    
    return percentages
        


def main():
    args = parse_arguments()
    lines = read_log_file(args.file)

    if not lines:
        print("Log file is empty. Nothing to analyze.")
        exit(0)

    error_count, warning_count = count_log_levels(lines)
    common_message = most_common_message(lines)
    percentages = percentage_levels(lines)

    report_text = build_report(lines, error_count, warning_count, common_message, percentages)
    print(report_text)

    if args.output:
        save_report(report_text, args.output)
        print(f"\nReport saved to {args.output}")



    

if __name__ == "__main__":
        main()
