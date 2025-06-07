from flask import Flask, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Box Design API is running!"

@app.route('/generate')
def generate_box_design():
    company_name = "WIZARD"
    slogan = "THE WORLD OF WIZARD"
    address = "Guangzhou, China"
    color_scheme = ["#D2691E", "#FFFFFF", "#8B4513"]
    output_path = "/tmp/box_design.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(200, 10, txt=company_name, ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=slogan, ln=True, align='C')
    pdf.cell(200, 10, txt=address, ln=True, align='C')

    pdf.set_fill_color(210, 105, 30)
    pdf.rect(10, 70, 60, 10, 'F')
    pdf.set_fill_color(255, 255, 255)
    pdf.rect(80, 70, 60, 10, 'F')
    pdf.set_fill_color(139, 69, 19)
    pdf.rect(150, 70, 60, 10, 'F')

    pdf.output(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)