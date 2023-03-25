from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from django.contrib import messages
import fitz

listOfCoordinates = [
    {'page_number': 1, 'coordinate_name': "currency", 'x1': 90, 'y1': 125, 'width': 35,
        'height': 18, 'font_size': 15, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "amount_in_figures", 'x1': 375, 'y1': 125,
        'width': 200, 'height': 18, 'font_size': 15, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "amount_in_words", 'x1': 250, 'y1': 155,
        'width': 330, 'height': 45, 'font_size': 12, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "account_number", 'x1': 438, 'y1': 225,
        'width': 60, 'height': 18, 'font_size': 14.8, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "beneficiary_name", 'x1': 165, 'y1': 340,
        'width': 420, 'height': 18, 'font_size': 12, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "beneficiary_address", 'x1': 137, 'y1': 373,
        'width': 450, 'height': 30, 'font_size': 8.5, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "IMG_bank_reciept", 'x1': 10, 'y1': 430,
        'width': 500, 'height': 130, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},

    {'page_number': 2, 'coordinate_name': "beneficiary_name", 'x1': 45, 'y1': 90,
        'width': 215, 'height': 30, 'font_size': 12, 'font_family': 'tibo', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "beneficiary_address", 'x1': 45, 'y1': 120,
        'width': 215, 'height': 40, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "reference", 'x1': 465, 'y1': 180, 'width': 100,
        'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "date", 'x1': 465, 'y1': 195, 'width': 80,
        'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "due_date", 'x1': 465, 'y1': 210, 'width': 80,
        'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "IMG_bank_reciept", 'x1': 72, 'y1': 352,
        'width': 489, 'height': 173, 'font_size': 8, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "currency", 'x1': 310, 'y1': 605, 'width': 35,
        'height': 20, 'font_size': 15, 'font_family': 'tibo', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "amount_in_figures", 'x1': 345, 'y1': 605,
        'width': 200, 'height': 20, 'font_size': 15, 'font_family': 'tibo', 'color': (0, 0, 0)},

    {'page_number': 3, 'coordinate_name': 'beneficiary_name', 'x1': 72, 'y1': 280,
        'width': 470, 'height': 20, 'font_size': 12, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 3, 'coordinate_name': 'beneficiary_address', 'x1': 72, 'y1': 300,
        'width': 470, 'height': 30, 'font_size': 12, 'font_family': 'tiro', 'color': (0, 0, 0)},

    {'page_number': 4, 'coordinate_name': '', 'x1': 0, 'y1': 0, 'width': 0,
        'height': 0, 'font_size': 0, 'font_family': '', 'color': ()},

    {'page_number': 5, 'coordinate_name': 'beneficiary_name', 'x1': 72, 'y1': 450,
        'width': 470, 'height': 20, 'font_size': 12, 'font_family': 'tibo', 'color': (0, 0, 0)},
    {'page_number': 5, 'coordinate_name': 'IMG_beneficiary_stamp', 'x1': 72, 'y1': 475,
        'width': 120, 'height': 95, 'font_size': 8, 'font_family': 'tiro', 'color': (0, 0, 0)},

    {'page_number': 6, 'coordinate_name': 'date', 'x1': 490, 'y1': 95, 'width': 75,
        'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'account_number', 'x1': 140, 'y1': 240,
        'width': 100, 'height': 15, 'font_size': 11, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'reference', 'x1': 215, 'y1': 330, 'width': 140,
        'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'date', 'x1': 400, 'y1': 330, 'width': 60,
        'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'currency', 'x1': 90, 'y1': 360, 'width': 35,
        'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'amount_in_figures', 'x1': 365, 'y1': 365,
        'width': 70, 'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'currency', 'x1': 440, 'y1': 365, 'width': 50,
        'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'amount_in_words', 'x1': 65, 'y1': 378,
        'width': 365, 'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'beneficiary_name', 'x1': 190, 'y1': 450,
        'width': 380, 'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'beneficiary_address', 'x1': 70, 'y1': 470,
        'width': 245, 'height': 18, 'font_size': 7, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'country', 'x1': 355, 'y1': 470, 'width': 140,
        'height': 15, 'font_size': 11, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'beneficiary_bank', 'x1': 135, 'y1': 488,
        'width': 180, 'height': 12, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'country', 'x1': 355, 'y1': 485, 'width': 140,
        'height': 15, 'font_size': 11, 'font_family': 'tiro', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'date', 'x1': 485, 'y1': 520, 'width': 75,
        'height': 15, 'font_size': 10, 'font_family': 'tiro', 'color': (0, 0, 0)}
]


def convert_coordinates_to_page_details(coordinates_list):
    page_details = {}
    for coordinate in coordinates_list:
        page_number = coordinate['page_number']
        coordinate_name = coordinate['coordinate_name']
        x1 = coordinate['x1']
        y1 = coordinate['y1']
        width = coordinate['width']
        height = coordinate['height']
        font_size = coordinate['font_size']
        font_family = coordinate['font_family']
        color = coordinate['color']

        if page_number not in page_details:
            page_details[page_number] = []
        if coordinate_name != '':
            page_details[page_number].append(
                (coordinate_name, [x1, y1, x1+width, y1+height, font_size, font_family, color]))
    return page_details

# Create your views here.


def index(request):
    return render(request, 'index.html')


def convertPDF(request):
    if request.method == 'POST':

        # open the PDF file
        pdf_doc = fitz.open("./static/pdfTemplates/main_template.pdf")

        # convert listOfCoordinates to page_details dictionary
        page_details = convert_coordinates_to_page_details(listOfCoordinates)

        # process PDF file
        path, fileName = pdfGenerator(
            request, pdf_doc=pdf_doc, page_details=page_details)

        pdf_file = open(path, 'rb')

        # Create a Django FileResponse object with the processed PDF byte string
        response = FileResponse(pdf_file, content_type='application/pdf')

        # Set the filename for the download
        response['Content-Disposition'] = f'attachment; filename={ fileName }'

        #messages.success(request, 'The file has been downloaded!')

        return response

    return render(request, 'pdfForm.html')


def pdfGenerator(request, pdf_doc, page_details):
    # loop through the page of the PDF
    for page_number, page in enumerate(pdf_doc, start=1):
        for field_name, (x1, y1, width, height, font_size, font_family, color) in page_details[page_number]:
            # create a new box with the desired coordinates
            box = fitz.Rect(x1, y1, width, height)

            if field_name[:3] == "IMG":
                image = request.FILES[field_name]
                image.seek(0)
                # Load the image
                image = fitz.Pixmap(image.read())
                page.insert_image(box, pixmap=image)
                del image
            else:
                field_value = request.POST.get(field_name, '')
                
                if field_name == "amount_in_figures":
                    amount = int(field_value)
                    field_value = '{:,}'.format(amount).replace(',', ' ')
                    
                if page_number == 3:
                    if field_name == "beneficiary_name":
                        field_value += " en ses bureaux sis Business"
                    else:
                        field_value += ' (hereinafter called "Partenaire")'

                if page_number == 5 and field_name == "beneficiary_name":
                    field_value += ", DIRECTEUR"

                if field_name == "account_number" and  page_number == 1:
                    field_value = " "+field_value[0]+"   "+field_value[1]+"   "+field_value[2]
                if field_name == "account_number" and  page_number == 6:
                    field_value = "301090012" + field_value

                options = {"fontname":font_family, "fontsize":font_size, "color":color}
                page.insert_textbox(box, field_value, **options)

    path, fileName = createFilePathAndFileName()

    pdf_doc.save(path)

    return path, fileName


def createFilePathAndFileName():
    # Generate the current datetime
    now = datetime.now()

    # Convert the datetime object to a string with a custom format and remove the space between characters
    now_str = now.strftime("%Y%m%d %H%M%S").replace(" ", '_')

    path = f"./static/pdfTemplates/coverted_files/{now_str}-processed_template.pdf"

    fileName = f"{now_str}-processed_template.pdf"

    return path, fileName
