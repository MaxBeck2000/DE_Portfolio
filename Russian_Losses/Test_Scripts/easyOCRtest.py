import easyocr
reader = easyocr.Reader(['en'])
result = reader.readtext('https://i.postimg.cc/brgtZnGT/1012-uaz452-capt.jpg')
for (bbox, text, prob) in result:
    print(f'Detected text: {text}')