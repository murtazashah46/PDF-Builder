from datetime import datetime
from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from django.contrib import messages
import fitz

listOfCoordinates = [
    {'page_number': 1, 'coordinate_name': "currency", 'x1': 94, 'y1': 126, 'width': 101,
        'height': 18, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "amount_in_figures", 'x1': 375, 'y1': 126,
        'width': 186, 'height': 18, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "amount_in_words", 'x1': 252, 'y1': 151,
        'width': 313, 'height': 18, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "account_number", 'x1': 442, 'y1': 224,
        'width': 54, 'height': 17, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "beneficiary_name", 'x1': 165, 'y1': 338,
        'width': 393, 'height': 18, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "beneficiary_address", 'x1': 137, 'y1': 363,
        'width': 421, 'height': 18, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 1, 'coordinate_name': "IMG_bank_reciept", 'x1': 22, 'y1': 428,
        'width': 503, 'height': 115, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},

    {'page_number': 2, 'coordinate_name': "beneficiary_name", 'x1': 29, 'y1': 108,
        'width': 215, 'height': 32, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "beneficiary_address", 'x1': 29, 'y1': 144,
        'width': 215, 'height': 44, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "reference", 'x1': 468, 'y1': 180, 'width': 82,
        'height': 15, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "date", 'x1': 468, 'y1': 198, 'width': 82,
        'height': 33, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "due_date", 'x1': 468, 'y1': 216, 'width': 82,
        'height': 15, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "IMG_bank_reciept", 'x1': 72, 'y1': 352,
        'width': 489, 'height': 173, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "currency", 'x1': 309, 'y1': 604, 'width': 72,
        'height': 22, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 2, 'coordinate_name': "amount_in_figures", 'x1': 396, 'y1': 604,
        'width': 144, 'height': 22, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},

    {'page_number': 3, 'coordinate_name': 'beneficiary_name', 'x1': 72, 'y1': 288,
        'width': 460, 'height': 10, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 3, 'coordinate_name': 'beneficiary_address', 'x1': 72, 'y1': 306,
        'width': 460, 'height': 21, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},

    {'page_number': 4, 'coordinate_name': '', 'x1': 0, 'y1': 0, 'width': 0,
        'height': 0, 'font_size': 0, 'font_family': '', 'color': ()},

    {'page_number': 5, 'coordinate_name': 'beneficiary_name', 'x1': 72, 'y1': 478,
        'width': 468, 'height': 15, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 5, 'coordinate_name': 'IMG_beneficiary_stamp', 'x1': 72, 'y1': 511,
        'width': 115, 'height': 264, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},

    {'page_number': 6, 'coordinate_name': 'date', 'x1': 468, 'y1': 100, 'width': 75,
        'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'account_number', 'x1': 138, 'y1': 244,
        'width': 78, 'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'reference', 'x1': 216, 'y1': 334, 'width': 129,
        'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'date', 'x1': 396, 'y1': 334, 'width': 57,
        'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'currency', 'x1': 90, 'y1': 363, 'width': 39,
        'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'amount_in_figures', 'x1': 367, 'y1': 360,
        'width': 68, 'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'currency', 'x1': 443, 'y1': 360, 'width': 35,
        'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'amount_in_words', 'x1': 90, 'y1': 378,
        'width': 338, 'height': 14, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'beneficiary_name', 'x1': 176, 'y1': 457,
        'width': 302, 'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'beneficiary_address', 'x1': 68, 'y1': 469,
        'width': 234, 'height': 17, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'country', 'x1': 356, 'y1': 471, 'width': 144,
        'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'beneficiary_bank', 'x1': 136, 'y1': 491,
        'width': 166, 'height': 9, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'country', 'x1': 356, 'y1': 489, 'width': 144,
        'height': 21, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)},
    {'page_number': 6, 'coordinate_name': 'date', 'x1': 486, 'y1': 522, 'width': 54,
        'height': 11, 'font_size': 8, 'font_family': 'Arial', 'color': (0, 0, 0)}
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

        messages.success(request, 'The file has been downloaded!')

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
                # print(x1, y1, width, height)
                page.insert_textbox(box, field_value)

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
