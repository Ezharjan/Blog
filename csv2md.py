import csv


# Read CSV file and extract data
def read_csv(file_name):
    data = []
    with open(file_name, "r", encoding="utf-8-sig") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            # print(row) # debug
            """
            读取时如果出现第一个键是'\ufeffCites'为不是'Cites'则意味着编码方式问题。
            为了解决这个问题，你可以在读取 CSV 文件时去掉这个 BOM 标记，可以通过在打开文件时指定 encoding='utf-8-sig' 来实现。utf-8-sig 编码是 UTF-8 编码的一种变体，会在文件开头自动忽略 BOM。
            \ufeff 是 Unicode 字节顺序标记 (BOM)，它有时会出现在以 UTF-8 编码保存的文件的开头。在某些编辑器中，为了表示文件编码方式，会在文件开头插入这个 BOM。在此情况下，文件开头出现了 \ufeffCites 这个键名，这意味着在 CSV 文件中 'Cites' 列名前面有一个 BOM 字节顺序标记。因此，在代码中读取列名时会出现键名前多出的 \ufeff 字符。
            """
            citation = {
                "Cites": row["Cites"],
                "Authors": row["Authors"],
                "Title": row["Title"],
                "Year": row["Year"],
                "Source": row["Source"],
                "ArticleURL": row["ArticleURL"],
                "Abstract": row["Abstract"],
            }
            data.append(citation)
    return data


# Sort data by the specified key
def sort_data(data, sort_by="Cites"):
    def convert_to_int(value):
        try:
            return int(value)
        except ValueError:
            return 0  # Assign 0 if the value is not convertible to int

    return sorted(data, key=lambda x: convert_to_int(x[sort_by]), reverse=True)


# Convert data to Markdown format
def generate_markdown(data):
    markdown = ""
    for item in data:
        markdown += f"[{item['Title']}]({item['ArticleURL']})\n"
        markdown += f"  - **Authors:** {item['Authors']}\n"
        markdown += f"  - **Year:** {item['Year']}\n"
        markdown += f"  - **Cites:** {item['Cites']}\n"
        markdown += f"  - **Abstract:** {item['Abstract']}\n\n"
        # markdown += f"<br> \n\n"
    return markdown


# Main program
def main():
    file_name = input("Please enter the file name: ")
    sort_by = input("Enter 'Cites' or 'Year' to sort by: ").strip()
    if sort_by not in ["Cites", "Year"]:
        sort_by = "Cites"

    data = read_csv(file_name)
    sorted_data = sort_data(data, sort_by)
    markdown_content = generate_markdown(sorted_data)

    # Set title and output file name based on sort type
    title = "### Sorted by Year" if sort_by == "Year" else "### Sorted by Citations"
    output_file_name = f"output_sort_by_{sort_by.lower()}.md"

    with open(output_file_name, "w", encoding="utf-8") as md_file:
        md_file.write(f"{title}\n\n")
        md_file.write(markdown_content)

    print("Markdown file generated successfully.")


if __name__ == "__main__":
    main()
