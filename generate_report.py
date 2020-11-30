# Python modules
from fpdf import FPDF

# Local imports
from daily_counts import plot_daily_count_countries
from time_series_analysis import plot_countries
from create_case_maps import plot_usa_case_map
from helper import get_country_names, Mode

WIDTH = 210
HEIGHT = 297
countries = ["Morocco", "France", "Russia"]

def create_title(day, pdf):
	pdf.set_font('Arial', '', 24)
	pdf.ln(60)
	pdf.write(5, "Covid Analytics Report")
	pdf.ln(10)
	pdf.set_font('Arial', '', 16)
	pdf.write(4, f"{day}")
	pdf.ln(5)


def create_report(day, filename="report.pdf"):
	pdf = FPDF()
	''' First Page '''
	pdf.add_page()
	pdf.image("./resources/letterhead_cropped.png", 0, 0, WIDTH)
	pdf.image("Capture.jpg", WIDTH/2 - 50, 100, 100)
	create_title(day, pdf)

	'''' Second Page '''
	pdf.add_page()
	plot_daily_count_countries(countries, filename="test.png")
	pdf.image("test.png", 5, 30, (WIDTH-15)/2)

	plot_daily_count_countries(countries, mode=Mode.DEATHS, filename="test2.png")
	pdf.image("test2.png", 5 + (WIDTH-15)/2, 30, (WIDTH-15)/2)

	plot_countries(countries, days=14, filename="test3.png")
	pdf.image("test3.png", 5, 110, (WIDTH-15)/2)

	plot_countries(countries, days=14, mode=Mode.DEATHS, filename="test4.png")
	pdf.image("test4.png", 5+(WIDTH-15)/2, 110, (WIDTH-15)/2)

	
	pdf.output(filename)


if __name__ == '__main__':
	day = "10/10/2020"	
	create_report(day)