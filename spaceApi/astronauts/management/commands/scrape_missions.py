from django.core.management.base import BaseCommand, CommandError
from bs4 import BeautifulSoup
import requests
from astronauts.models import Mission, MissionImage
import tempfile
import re

from django.core import files

def remove_wikipedia_link(s):
    return re.sub('\[.*?\]', '', s)

def getMissionLinks(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    link_table = soup.find_all('table')[1]
    links = []

    for link in link_table.find_all('a'):
        links.append("https://en.wikipedia.org/" + link.get('href'))

    return links

def scrape_mission_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="lxml")
    wikipedia_url = url
    toc = soup.find("div", {"class": "toc"})
    brief = toc.find_previous_sibling("p").text if (toc and toc.find_previous_sibling("p")) else ""

    infobox_table = soup.find('table', {"class": "infobox"})
    if infobox_table:
        caption = infobox_table.find('caption', {"class": "infobox-title"})
        name = caption.text if caption else ""
        type = infobox_table.find("th", text="Mission type").find_next_sibling("td").text if infobox_table.find("th", text="Mission type") else ""
        operator = infobox_table.find("th", text="Operator").find_next_sibling("td").text if infobox_table.find("th", text="Operator") else ""
        cospar_id = infobox_table.find("th", text="COSPAR ID").find_next_sibling("td").text if infobox_table.find("th", text="COSPAR ID") else ""
        satcat_no = infobox_table.find("th", text="SATCAT no.").find_next_sibling("td").text if infobox_table.find("th", text="SATCAT no.") else ""
        duration = infobox_table.find("th", text="Mission duration").find_next_sibling("td").text if infobox_table.find("th", text="Mission duration") else ""
        distance_traveled = infobox_table.find("th", text="Distance travelled").find_next_sibling("td").text if infobox_table.find("th", text="Distance travelled") else ""
        total_evas = infobox_table.find("th", text="EVAs").find_next_sibling("td").text if infobox_table.find("th", text="EVAs") else "0"
        total_eva_time = infobox_table.find("th", text="EVA duration").find_next_sibling("td").text if infobox_table.find("th", text="EVA duration") else "0"
        start_date = infobox_table.find("th", text="Launch date").find_next_sibling("td").text if infobox_table.find("th", text="Launch date") else ""
        launch_site = infobox_table.find("th", text="Launch site").find_next_sibling("td").text if infobox_table.find("th", text="Launch site") else ""
        end_date = infobox_table.find("th", text="Landing date").find_next_sibling("td").text if infobox_table.find("th", text="Landing date") else ""
        landing_site = infobox_table.find("th", text="Landing site").find_next_sibling("td").text if infobox_table.find("th", text="Landing site") else ""
        print(f"Mission: {name}")
        obj, created = Mission.objects.update_or_create(
            name=name,
            defaults={
                "wikipedia_url": wikipedia_url,
                "brief": remove_wikipedia_link(brief),
                "name" : remove_wikipedia_link(name),
                "type" : remove_wikipedia_link(type),
                "operator" : remove_wikipedia_link(operator),
                "cospar_id" : remove_wikipedia_link(cospar_id),
                "satcat_no" : remove_wikipedia_link(satcat_no),
                "duration" : remove_wikipedia_link(duration),
                "distance_traveled" : remove_wikipedia_link(distance_traveled),
                "total_evas" : remove_wikipedia_link(total_evas),
                "total_eva_time" : remove_wikipedia_link(total_eva_time),
                "start_date" : remove_wikipedia_link(start_date),
                "launch_site" : remove_wikipedia_link(launch_site),
                "end_date" : remove_wikipedia_link(end_date),
                "landing_site" : remove_wikipedia_link(landing_site),
            }
        )

        # download image
        image = infobox_table.find('img')
        if image:
            r = requests.get("https:"+image.get('src'))
            if r.status_code == requests.codes.ok:
                file_name = image.get('alt')
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

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Space Missions Scraper:'))
        url = "https://en.wikipedia.org/wiki/List_of_human_spaceflights"
        links = getMissionLinks(url)

        for mission_link in links:
            scrape_mission_info(mission_link)
