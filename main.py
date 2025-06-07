from fpdf import FPDF
import os

# إعداد بيانات الشركة
company_name = "WIZARD"
slogan = "THE WORLD OF WIZARD"
address = "Guangzhou, China"
color_scheme = ["#D2691E", "#FFFFFF", "#8B4513"]

# إنشاء ملف PDF
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()

# إعداد الألوان والخطوط
pdf.set_font("Arial", 'B', 24)
pdf.set_text_color(0, 0, 0)
pdf.set_fill_color(210, 105, 30)  # اللون البني (من color_scheme)

# العنوان
pdf.cell(0, 20, f"{company_name} - Packaging", 0, 1, 'C', fill=True)

# الشعار النصي
pdf.set_font("Arial", '', 14)
pdf.set_fill_color(255, 255, 255)
pdf.cell(0, 10, slogan, 0, 1, 'C')

# العنوان
pdf.set_font("Arial", '', 10)
pdf.multi_cell(0, 5, address, 0, 'C')

# حفظ الملف
output_path = "output.pdf"
pdf.output(output_path)
print(f"✅ Design generated: {output_path}")