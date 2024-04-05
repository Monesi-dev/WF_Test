from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(filename):
    # Create a canvas object
    c = canvas.Canvas(filename, pagesize=letter)

    # Set font and size
    c.setFont("Helvetica", 12)

    # Write some text
    text = "Hello, this is a PDF generated using Python and ReportLab!"
    c.drawString(100, 700, text)

    # Save the PDF file
    c.save()

if __name__ == "__main__":
    filename = "generated_pdf.pdf"
    generate_pdf(filename)
    print(f"PDF generated successfully: {filename}")
