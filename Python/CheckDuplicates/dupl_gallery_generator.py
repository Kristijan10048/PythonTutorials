# Importing BeautifulSoup class from the bs4 module
from bs4 import BeautifulSoup


class CAppHtmlGallery:
    def write_html_file(self, s_path: str, o_soup: object) -> None:
        with open("output1.html", "w") as file:
            file.write(str(o_soup))

    def parse_html_gallery(self):
        # Opening the html file
        html_file = open(r'D:\Repository\PythonTutorials\Python\CheckDuplicates\google-image-layout\template.html', "r")

        # Reading the file
        html_template = html_file.read()

        # Creating a BeautifulSoup object and specifying the parser
        o_soup = BeautifulSoup(html_template, 'html.parser')

        for tag in o_soup.find_all('div'):
            # Printing the name, and text of p tag
            # print(f'{tag.name}: {tag.text}')
            if tag.get('id') == 'imgs':
                new_img = o_soup.new_tag('img', src=r'Z:\kris\Photos\Cannon backup\back up\170_2508\IMG_2761.JPG',
                                         width=300, height=300)
                tag.append(new_img)

        # write modified template to a file
        self.write_html_file(s_path='.', o_soup=o_soup)
