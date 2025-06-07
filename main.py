from flask import Flask, send_file
from fpdf import FPDF
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "🎉 Box Design API is Running!"

@app.route("/generate")
def generate_pdf():
    # بيانات جاهزة لتوليد عينة تصميم
    company_name = "Wizard"
    slogan = "THE WORLD OF WIZARD"
    address = "Guangzhou, China"
    color_scheme = "#D2691E, #FFFFFF, #8B4513"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Company: {company_name}", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Slogan: {slogan}", ln=True)
    pdf.cell(0, 10, f"Address: {address}", ln=True)
    pdf.cell(0, 10, f"Color Scheme: {color_scheme}", ln=True)

    output_file = "output.pdf"
    pdf.output(output_file)

    return send_file(output_file, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)