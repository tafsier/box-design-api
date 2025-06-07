from flask import Flask, request, send_file
from fpdf import FPDF
import requests
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Box Design API is Running!'

@app.route('/generate', methods=['POST'])
def generate_design():
    data = request.json

    company_name = data.get('company_name', 'Company')
    logo_url = data.get('logo_url')
    slogan = data.get('slogan', '')
    address = data.get('address', '')
    dieline_url = data.get('dieline_url')
    color_scheme = data.get('color_scheme', '#FFFFFF,#000000')
    product_type = data.get('product_type', 'PRODUCT')

    # تحميل صورة الشعار
    logo_response = requests.get(logo_url)
    logo_image = BytesIO(logo_response.content)

    # تحميل قالب الـ dieline
    dieline_response = requests.get(dieline_url)
    dieline_pdf = BytesIO(dieline_response.content)

    # إنشاء PDF جديد
    pdf = FPDF()
    pdf.add_page()

    # ألوان التصميم
    background, text_color = color_scheme.split(',')

    # إعداد الخلفية
    r, g, b = tuple(int(background[i:i+2], 16) for i in (1, 3, 5))
    pdf.set_fill_color(r, g, b)
    pdf.rect(0, 0, 210, 297, 'F')

    # إضافة الشعار
    with open("temp_logo.jpg", "wb") as f:
        f.write(logo_image.getbuffer())
    pdf.image("temp_logo.jpg", x=10, y=10, w=40)

    # النصوص
    pdf.set_font("Arial", "B", 14)
    pdf.set_text_color(0, 0, 0)
    pdf.set_xy(10, 60)
    pdf.multi_cell(0, 10, f"{company_name}\n{slogan}\n{address}\nProduct: {product_type}")

    # دمج قالب الـ dieline كصفحة جديدة
    output_path = "/tmp/output.pdf"
    with open(output_path, "wb") as f:
        f.write(dieline_pdf.getbuffer())

    # إلحاق التصميم الجديد كصفحة إضافية في النهاية
    pdf.output(output_path)

    return send_file(output_path, download_name="output.pdf", as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)