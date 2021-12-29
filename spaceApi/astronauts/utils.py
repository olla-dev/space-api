
import tempfile
import requests
from django.core import files


nationalities = {
    "Afghan":"Afghanistan",
    "African":"Africa",
    "Algerian":"Algeria",
    "American":"United States",
    "Antiguans":"Antigua And Barbuda",
    "Argentine":"Argentina",
    "Argentinean":"Argentina",
    "Argentinian":"Argentina",
    "Argentino":"Argentina",
    "Armenian":"Armenia",
    "Aussie":"Australia",
    "Australian":"Australia",
    "Australianb":"Australia",
    "Australien":"Australia",
    "Austrian":"Austria",
    "Soviet": "USSR",
    "French": "France",
    "Spanish": "Spain",
    "German": "Germany",
    "Italian": "Italy",
    "Japanse": "Japan",
    "Chinese": "China",
    "Canadian": "Canada",
    "British": "UK",
    "Russian": "Russia",
    "Ukrainian": "Ukraine",
    "Soviet Union": "USSR",
    "United States": "USA",
    "Soviet (formerly)Russian": ["USSR", "Russia"],
    "Soviet/Russian": ["USSR", "Russia"],
    "Soviet / Russian": ["USSR", "Russia"],
    "Soviet Union Russia": ["USSR", "Russia"],
    "Belarusian": "Belarusia",
    "Polish": "Poland",
    "Bulgarian": "Bulgaria",
    "Cuban": "Cuba",
    "Soviet / Ukrainian": ["USSR", "Ukraine"],
    "Australian-American": "USA",
    "Saudi Arabian": "KSA",
    "Dutch": "Netherlands",
    "Mexican": "Mexico",
    "Costa Rican and American": ["USA", "Costa Rica"],
    "Soviet Union (1991)\nRussian (after 1991)": ["USSR", "Russia"]
}

def nationality_to_country(demonym):
    if demonym in nationalities:
        return nationalities[demonym.replace(u'\xa0', u' ').strip()]
    else:
        return "Unknown"

def download_image_to_model(url, file_name, obj):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        # Create a temporary file
        lf = tempfile.NamedTemporaryFile()

        # Read the streamed image in sections
        for block in r.iter_content(1024 * 8):
            # If no more file then stop
            if not block:
                break

            # Write image block to temporary file
            lf.write(block)

        # Save the temporary image to the model#
        # This saves the model so be sure that it is valid
        obj.photo.save(file_name, files.File(lf))