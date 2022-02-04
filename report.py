from fpdf import FPDF
from datetime import datetime

HEIGHT = 200
WIDTH = 297


def presentation():
    pdf = FPDF('L', 'mm', 'A4')
    pdf.set_auto_page_break(0)
    pdf.add_page()
    pdf.image('A4-1.png', x=0, y=0, w=297)
    pdf.ln(30)
    pdf.set_text_color(62, 127, 136)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(270, 5, 'Presentation results for 2019', 0, 2, 'C')
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    pdf.cell(260, 5, '      Analysis of e-commerce performance revealed the following trends:', 0, 2, 'W')
    pdf.cell(260, 5, '1. Bestsellers of 2019 were the following products: AAA Batteries (4-pack) - 14.8%, '
                     'AA Batteries (4-pack) - 13.2%, USB-C Charging Cable -  ', 0, 2, 'W')
    pdf.cell(260, 5, '11.5%, and Lightning Charging Cable - 11.1%. ', 0, 2, 'W')
    pdf.cell(260, 5, '2. Withal following items showed reverse trends: LG Washing Machine, LG Dryer, '
                     '20in Monitor, and Google Phone were the least selling items. ', 0, 2, 'W')
    pdf.cell(260, 5, '3. The highest percentage of sales fell on domestic state - California. ', 0, 2, 'W')
    pdf.cell(260, 5, '4. At the same time revenue on new markets - Oregon and Washington showed '
                     'good trends. ', 0, 2, 'W')
    pdf.cell(260, 5, '5. It is recommended to pay attention to the situation in the state Maine.    ', 0, 2, 'W')
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 14)
    pdf.image('distribution_of_products.png', x=10, y=101, w=155)
    pdf.image('distribution_states.png', x=145, y=98, w=125)
    now = datetime.now()
    print()
    pdf.set_xy(10, (HEIGHT-15))
    pdf.set_font('Arial', 'I', 6)
    pdf.cell(270, 4, f'by Dmytro Zuzuk                                                                                 '
                     f'                                                                                                '
                     f'                                                                                                '
                     f'                       {now.strftime("%Y-%m-%d %H:%M:%S")}                                      '
                     f'  Page 1', 1, 2, 'C', )
    pdf.set_auto_page_break(0)
    pdf.add_page()
    pdf.image('A4-1.png', x=0, y=0, w=297)
    pdf.ln(30)
    pdf.set_font('Arial', '', 12)
    pdf.cell(270, 5, '      With regard to marketing policy in 2019, we draw attention to the following:', 0, 2, 'W')
    pdf.cell(270, 5, '1. According to statistics, the largest number of orders was made in the period from '
                     '11 am to 1 pm and from 6 pm to 8 pm. ', 0, 2, 'W')
    pdf.cell(270, 5, 'Respectively, it is the best time to show customers advertisements in social media to'
                     ' push sales. Besides, we dare to suggest that timeframe', 0, 2, 'W')
    pdf.cell(270, 5, 'from 11 pm to 8 am is the best time to promo discounts, resulting in a number of spontaneous'
                     ' orders.', 0, 2, 'W')
    pdf.cell(270, 5, '2. The most complementary sets of products in 2019 were the following: '
                     '(Google Phone, USB-C Charging Cable, Wired Headphones);', 0, 2, 'W')
    pdf.cell(140, 5, '(iPhone, Lightning Charging Cable, Wired Headphones); (iPhone, Lightning Charging Cable,'
                     ' Apple Airpods Headphones) ', 0, 2, 'W')
    pdf.cell(140, 5, 'which should be taken into account when compiling marketing activities.', 0, 2, 'W')
    pdf.cell(140, 5, '3. Dependency of quantity of orders to the price showed that customer', 0, 2, 'W')
    pdf.cell(140, 5, 'is sensitive to prices and makes orders of cheap items more easily,', 0, 2, 'W')
    pdf.cell(140, 5, 'while the demand for Apple devices can be considered as stable.', 0, 2, 'W')
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 14)
    pdf.image('distribution_of_orders.png', x=10, y=95, w=135)
    pdf.image('dependency_ordered_price.png', x=145, y=72, w=135)
    pdf.set_xy(10, (HEIGHT-15))
    pdf.set_font('Arial', 'I', 6)
    pdf.cell(270, 4, f'by Dmytro Zuzuk                                                                                 '
                     f'                                                                                                '
                     f'                                                                                                '
                     f'                       {now.strftime("%Y-%m-%d %H:%M:%S")}                                      '
                     f'  Page 2', 1, 2, 'C', )
    pdf.set_auto_page_break(0)
    pdf.add_page()
    pdf.image('A4-1.png', x=0, y=0, w=297)
    pdf.ln(30)
    pdf.set_font('Arial', '', 12)
    pdf.cell(270, 5, '      General sales statistics did not reveal any unusual features in 2019.', 0, 2, 'W')
    pdf.cell(270, 5, '1. December remains the most active month of the year. The activity of promotions in November did'
                     ' not show the expected results and remained ', 0, 2, 'W')
    pdf.cell(270, 5, 'at the level of previous years. It is traditionally recommended to concentrate marketing efforts,'
                     'including Black-sales in January and September.', 0, 2, 'W')
    pdf.cell(270, 5, '2. The Top-sellers in 2019 became San Fransisco, Los Angeles and New York, at the same time'
                     'Portland (ME) needs special attention. ', 0, 2, 'W')
    pdf.cell(270, 5, 'Cities Austin, Dallas and Portland(OR) have significant development potential', 0, 2, 'W')
    pdf.cell(270, 5, 'that should be taken into account.', 0, 2, 'W')
    pdf.ln(5)
    pdf.image('Dynamic_of_sales.png', x=10, y=60, w=150)
    pdf.image('sales_by_cities.png', x=160, y=62, w=120)
    pdf.set_xy(10, (HEIGHT-15))
    pdf.set_font('Arial', 'I', 6)
    pdf.cell(270, 4, f'by Dmytro Zuzuk                                                                                 '
                     f'                                                                                                '
                     f'                                                                                                '
                     f'                       {now.strftime("%Y-%m-%d %H:%M:%S")}                                      '
                     f'  Page 3', 1, 2, 'C', )
    pdf.output('report.pdf', 'F')


if __name__ == '__main__':
    presentation()
