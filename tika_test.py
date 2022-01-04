import tika
tika.initVM()
from tika import parser
import re

# data = parser.from_file("test.pdf")
# content = data["content"].strip()

# with open("./output.txt", 'w', encoding='utf-8') as txt:
#     print(content, file=txt)
    
pdf_path = "kms_number.pdf" 

# PDF 파일에서 텍스트를 추출
raw_pdf = parser.from_file(pdf_path) 
# parsed_data_full = parser.from_file(pdf_path,xmlContent=True) 
# parsed_data_full = parsed_data_full['content']
contents = raw_pdf['content'] 

contents = contents.split(' ')
final_contents = []

for content in contents:
    final_contents.append(content.replace("\n",""))
    

for file in final_contents:
    rows = re.findall("\d", file)
    if len(rows) == 10:
        number = ''.join(rows)     
        print(number)
    

# print(final_contents)

