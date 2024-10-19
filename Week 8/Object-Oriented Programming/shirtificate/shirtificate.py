from fpdf import FPDF


class PDF(FPDF):
    # img name , x , y , w & h
    def header(self):
        self.image("shirtificate.png", 10, 65, 190, 190)

        # set font format and style
        self.set_font("helvetica", "B", 45)

        # allign
        self.text(45, 45, "CS50 Shirtificate")

    def footer(self):
        self.set_font("helvetica", size=25)
        self.set_text_color(255, 255, 255)
        self.text(72, 140, f"{name} took CS50")


name = input("Name: ")
pdf = PDF()
pdf.add_page()
pdf.output("shirtificate.pdf")
