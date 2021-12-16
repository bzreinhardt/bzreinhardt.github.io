from md2py import md2py
from bs4 import BeautifulSoup
import mistune
import re
import pprint as pp
from varname import nameof
import argparse
import os
import shutil
import csv
import pdb

'''
TODO:
- Fix emdashes
- Actually use template variables
'''

#Variables
FULL_URL = "https://"
TITLE = "Shifting the impossible to the inevitable"
SUBTITLE = "A Private ARPA user manual"
DESCRIPTIVE_EMOJIS = "emojis"
HEADER_IMG_ALT_DESCRIPTION = "foobar"
# This might also be useful https://mistune.readthedocs.io/en/latest/guide.html
INDENT = "  "
VARIABLE_ONE = "a lovely bunch"
VARIABLE_TWO = "coconuts"
PUBLISH_DATE = "April 2021"


def generate_id_from_section_title(title):
    #TODO - need to check against existing
    lower_title=title.lower().strip()
    regex = re.compile('[^a-zA-Z0-9 \_]')
    return regex.sub("", lower_title.replace(" ", "_"))


def parse_personas(persona_file):
    '''Assumes a matrix with rows corresponding to each section
    and columns corresponding to personas'''
    sections = {}
    personas = []
    with open(persona_file) as f:
        reader = csv.reader(f, delimiter=',')
        for i, row in enumerate(reader):
            if i == 0:
                for persona in row[1:]:
                    personas.append(persona.replace(' ', '_'))
            else:
                sections[generate_id_from_section_title(row[0])] = list(map(int,row[1:]))
    return sections, personas

def parse_headers(content, header_lines=3):
    lines = content.split('\n')
    return '\n'.join(lines[header_lines:])
    '''
        if len(line.split(':')) > 1:
            variable = line.split(':')[0]
            value = ':'.join(line.split(':')[1:])
            if variable == 'Title':
                global TITLE
                TITLE = value
    '''


def convert_doc_markdown_to_normal_markdown(doc_markdown):
    '''
    Keep a running list of footnote reference locations along with their numbers
    once you find a reference to a foodnote with that number you add a pared
    footnote to the list
    '''
    lines = doc_markdown.split('/')
    all_footnotes = []
    incomplete_footnotes = {}
    absolute_position = 0
    new_lines = []
    for line in lines:
        if '<footnote>' in line.lower() or '<sidenote>' in line.low():
            number = int(re.findall(r'^\d+\.', line)[0][0:-1])
            content = line.split('>')[1:].join('>')

        position = 0
        footnotes = re.finditer(r'~\[\[.*?\)~', html)
        new_line = ''
        for footnote in footnotes:
            footnote_number = int(line[footnote.start()+3:footnote.start()+4])
            footnote_position = absolute_position + footnote.start()
            new_line = new_line + line[position:footnote.start()]
            position = footnote.end()
        new_line = new_line + line[position:]
        new_lines.append(new_line)
        # Adding a 1 to account for the addtion of newline characters when joining everything together
        absolute_position = absolute_position + len(new_line) + 1

def remove_comments(markdown):
    commented_text = re.finditer(r'\{.*?\}\{.*?\}', markdown)
    position = 0
    markdown_out = ''
    for comment in commented_text:
        text = markdown[comment.start():comment.end()]
        raw_text = re.findall(r'\{==.*?==\}', text)[0][3:-3]
        raw_comment = re.findall(r'\{>>.*?<<\}', text)[0][3:-3]
        timeless_comment = raw_comment[raw_comment.find(':')+4:]
        markdown_out = markdown_out + markdown[position:comment.start()]+raw_text
        position = comment.end()
    markdown_out = markdown_out + markdown[position:]
    return markdown_out



def fix_dashes(html):
    #-- becomes ndash
    #--- becomes mdash
    html = html.replace('---', '&mdash;')
    html = html.replace('--', '&ndash;')
    return html

def remove_first_header(html):
    soup = BeautifulSoup(html, features="html.parser")


def generate_section_list(html):
    section_list = []
    soup = BeautifulSoup(html, features="html.parser")
    h1s = soup.find_all('h1')
    for h1 in h1s:
        section_list.append(generate_id_from_section_title(h1.string))
    h2s = soup.find_all('h2')
    for h2 in h2s:
        section_list.append(generate_id_from_section_title(h2.string))
    h3s = soup.find_all('h3')
    for h3 in h3s:
        section_list.append(generate_id_from_section_title(h3.string))
    return section_list

def make_distillation_links_silent(html, start_id, stop_id):
    soup = BeautifulSoup(html, features="html.parser")

    section = soup.find(id=start_id)
    while section.get('id') != stop_id:
        for i, link in enumerate(section.find_all(class_="internal-link")):
            link['class'] = link['class'] + ['silent-link']
        section = section.nextSibling
        while not hasattr(section, 'get'):
            section = section.nextSibling
    return soup.prettify()

def generate_internal_links(html):
    ''' Find back-to-back-single-bracket parts and link them to the appropriate section'''
    # This assumes that all internal link text have a space in front of them.
    links = re.finditer(r'.\[.*?\]\[.*?\]', html)
    position = 0
    new_html = ''
    section_list = generate_section_list(html)
    #pdb.set_trace()
    for link in links:
        #ignore image links
        if html[link.start():link.start()+1] == '!':
            continue
        all_text = html[link.start():link.end()]
        middle = all_text.find('][')
        # This is the text that you want to see
        text = html[link.start()+2:link.start()+middle]

        # This is the name of the section to link to
        section = html[link.start()+middle:link.end()-1]
        id = generate_id_from_section_title(section)
        #TODO - need to check against existing titles and if id is none, just remove brackets
        if id not in section_list:
            new_html=new_html+html[position:link.start()]+text
            position = link.end()
        else:
            a = '<a class="internal-link" href="#%s">%s</a>'%(id, text)
            new_html = new_html+html[position:link.start()]+a
            position = link.end()
    new_html = new_html+html[position:]
    #new_html = make_distillation_links_silent(new_html, 'preliminaries')
    return new_html

def add_id_to_headers(html):
    soup = BeautifulSoup(html, features="html.parser")
    for i in range (1,4):
        section_titles = soup.find_all('h%d'%i)
        for header in section_titles:
            title = header.text
            soup.find('h%d'%i, text=title)['id'] = generate_id_from_section_title(title)
    return(soup.prettify())

def bigfootify_footnotes(html):
    ''' converts mistune converted markdown footnotes to a format that works with bigfoot.js '''
    # modify footnote refs
    '''
    ref_links = re.finditer(r'<a href=\"#fn-', html)
    new_html = ''
    index = 0
    for link in ref_links:
        new_html = new_html + html[index:link.span[0]+3]
        new_html = new_html + 'rel="footnote" '
        index = link.span[0]+3
    new_html = new_html + html[index:]
    html = new_html
    '''
    soup = BeautifulSoup(html, features="html.parser")
    footnote_ref_links = soup.findAll('a', href=lambda x:x and x.startswith('#fn-'))
    for ref_link in footnote_ref_links:
        ref_link['rel'] = 'footnote'
    #remove class footnote from links
    footnote_links = soup.findAll('a', {'class':'footnote'})
    for link in footnote_links:
        link['class'] = 'footnote-link'
    footnote_list_items = soup.findAll('li', id=lambda x:x and x.startswith('fn-'))
    for list_item in footnote_list_items:
        list_item['class'] = 'footnote'
    return(soup.prettify())

def add_marginnotes(html):
    soup = BeautifulSoup(html, features="html.parser")
    footnotes = soup.findAll('li', {'class':'footnote'})
    sidenotes = []
    for footnote in footnotes:
        if footnote.text.strip().startswith('\\<sidenote'):
            id_num = footnote.get('id').split('-')[1]
            link = soup.find('sup', id='fnref-'+id_num)
            note_text = footnote.text.strip().replace('\\<sidenote>','')[:-3]
            marker = soup.new_tag('span')
            marker['class'] = 'MarginNoteMarker'
            note = soup.new_tag('span')
            note['class'] = 'marginnote'
            text = BeautifulSoup(note_text, features="html.parser")
            note.append(text)
            #note.string = note_text
            link.insert_before(note)
            note.insert_before(marker)
            footnote.decompose()
            link.decompose()
    return(soup.prettify())

def fix_bold(html):
    ''' replace <strong> with useful class '''
    html = html.replace('<strong>', '<span class="definition">' )
    html = html.replace('</strong>', '</span>')
    return html

def parse_images(html, assets_dir):
    # Find images
    # Grab measurements?
    # Do subtitle?
    image_refs = re.finditer(r' \[.*?\]\:.*?px.*?px', html)
    image_paths = {}
    position = 0
    new_html = ''
    for image in image_refs:
        image_text = html[image.start():image.end()]
        image_title = re.findall(r'\[.*?\]', image_text)[0][1:-1]
        image_name = re.findall(r'\]\:\ .*?\ ', image_text)[0][3:-1]
        image_path = os.path.join(assets_dir, image_name)
        image_paths[image_title] = image_path
        new_html = new_html + html[position:image.start()]
        position = image.end()
    new_html = new_html + html[position:]

    position = 0
    new_new_html = ''
    images = re.finditer(r'\!\[\]\[.*?\]', new_html)
    #pdb.set_trace()
    for image in images:
        image_name = new_html[image.start()+4:image.end()-1]
        image_path = image_paths[image_name]
        image_html = '<img src="/%s">'%image_path
        #print(image_name)
        #print(image_path)
        #remove image stuff and put in the html link to image
        new_new_html = new_new_html + new_html[position:image.start()]+image_html
        position = image.end()
    new_new_html = new_new_html + new_html[position:]
    soup = BeautifulSoup(new_new_html, features="html.parser")
    images = soup.findAll('img')
    for image in images:
        img = image
        parent = image.parent
        parent['class'] = 'image-paragraph'
    return soup.prettify()

def format_footnotes(content):
    ''' pre-html-ize formatting in the foodnotes '''
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if line.startswith('[^fn'):
            split_line = line.split(':')
            line_content=':'.join(split_line[1:])
            htmlized_line_content = mistune.markdown(line_content)[3:-5]
            line = ':'.join([split_line[0],htmlized_line_content])
        new_lines.append(line)
    return '\n'.join(new_lines)

def add_personas(html, persona_path):
    sections, personas = parse_personas(persona_path)
    soup = BeautifulSoup(html, features="html.parser")
    # Add persona clearing button
    new_tag = soup.new_tag("a")
    new_tag.string = "chart your own adventure"
    new_tag['class'] = ['clear_persona']
    soup.find_all(text=re.compile(r'.*?chart your own adventure.*?'))[0].replace_with(new_tag)
    for section in sections:
        headers = soup.findAll(id=section)
        if len(headers) is not 1:
            print("adding personas and got weird number of headers (%d) with id %s"%(len(headers),section))
            continue
        header = headers[0]
        for i, persona in enumerate(personas):
            if sections[section][i]:
                if header.get('class'):
                    header['class'] = header.get('class') + [persona]
                else:
                    header['class'] = [persona]
    for persona in personas:
        for elem in soup(text=re.compile(r'.*?%s.*?'%persona.replace('_',' '))):
            if elem.parent.get('class'):
                elem.parent['class'] = elem.parent.get('class') + ['persona_button']
            else:
                elem.parent['class'] = ['persona_button']
            elem.parent.name = 'a'
    return soup.prettify()



def parse_markdown(content, upgrade_headers=True,
                            add_ids=True,
                            footnotes=True,
                            add_links=True,
                            marginnotes=True,
                            dashes=True,
                            assets_dir=None,
                            persona_path=None):
    '''
    Need to decide wether to do a monolilith or disprse thing
    In addition to the sections and content, need to
    - generate hrefs
    - replace [[Links]] with <a href="link">links</a>


    assumptions
    - content has only one h1
    '''
    content = parse_headers(content)
    content = remove_comments(content)
    content = format_footnotes(content)

    html = mistune.markdown(content)
    h1_sections = re.finditer(r'<h1>.*?</h1>', html)
    '''
    for i, section in enumerate(h1_sections):
        if i > 0:
            print("Weird, the parsed markdown seems to have more than one h1 section")
            continue
        title = content[section.start()+5:section.end()-5]
        if upgrade_headers:
            html = html[0:section.start()] + html[section.end():]
            for j in range(2,4):
                html = html.replace('h%d>'%j,'h%d>'%(j-1))
    '''
    section_list = generate_section_list(html)
    if add_ids:
        html = add_id_to_headers(html)
    if footnotes:
        html = bigfootify_footnotes(html)
    if add_links:
        html = generate_internal_links(html)
    if marginnotes:
        html = add_marginnotes(html)
    if dashes:
        html = fix_dashes(html)
    if assets_dir:
        html = parse_images(html, assets_dir)
    if persona_path:
        html = add_personas(html, persona_path)
    html = fix_bold(html)
    return html


def create_table_of_contents(content, persona_path=None):
    '''
      <li class="H1 ">
        <ul>
            <li class="H2 ">
                <a href="#h2-href">H2 TITLE</a>
                    <ul>
                        <li class="H3">
                            <a href="#h3-href">H3 TITLE</a>
                        </li>
                        ...
                    </ul>
            </li>
            ...
        </ul>
    </li>
    '''
    if persona_path:
        sections, personas = parse_personas(persona_path)

    html = mistune.markdown(content)
    soup = BeautifulSoup(html, features="html.parser")
    lines = ['<li id="tracker">',\
                '<a href="">',
                    '',
                '</a',
             '</li>',
             '<li class="H1">',
             INDENT+'<ul>']
    indent_level = 2
    last_header = None
    section_list = []
    for child in soup:
        if not hasattr(child, 'getText'):
            continue
        header_personas = []
        if persona_path:
            for i, persona in enumerate(personas):
                if generate_id_from_section_title(child.getText()) in sections and sections[generate_id_from_section_title(child.getText())][i]:
                    header_personas.append(persona)
        #if child.name == 'h1':
        #    last_header = 'h1'
        if child.name == 'h1':
            # do h2 stuff
            if last_header == 'h1':
                lines.pop()
            if last_header == 'h2':
                lines.append(4*INDENT+'</ul>')
                lines.append(2*INDENT+'</li>')
            lines.append(2*INDENT+'<li class="H2">')
            lines.append(3*INDENT+'<div class="toc %s">'%" ".join(header_personas))
            lines.append(3*INDENT+'<a href="#%s">%s</a>'%(generate_id_from_section_title(child.getText()), child.getText()))
            lines.append(3*INDENT+'</div>')
            lines.append(4*INDENT+'<ul class="toc_ul">')
            last_header = 'h1'
        elif child.name == 'h2':
            lines.append(5*INDENT+'<li class="H3">')
            lines.append(6*INDENT+'<div class="toc %s">'%" ".join(header_personas))
            lines.append(6*INDENT+'<a href="#%s">%s</a>'%(generate_id_from_section_title(child.getText()), child.getText()))
            lines.append(6*INDENT+'</div>')
            lines.append(5*INDENT+'</li>')
            last_header = 'h2'
        else:
            continue
    lines.append(INDENT+'</ul>')
    lines.append('</li>')
    return '\n'.join(lines)

def create_variable_dict(variable_list):
    variable_dict = {}
    for var in variable_list:
        variable_dict[nameof(var)] = var
    return variable_dict

def get_variable(variable_name, variables=None):
    ''' Get a variable value based on a text name. For now assuming variables are in a dictionary with the keys as names '''
    try:
        var = eval(variable_name)
    except:
        print('could not find variable %s'%variable_name)
        return None
    return var

def insert_variables_into_text(text, variable_list = None):
    '''Very hacky: This assumes variables are global variables'''
    new_text = ''
    position = 0
    variables = re.finditer(r'{{(.*?)}}', text)
    for var in variables:
        new_text = new_text + text[position:var.start()]
        variable_name = text[var.start()+2:var.end()-2]
        variable = get_variable(variable_name)
        if variable:
            new_text = new_text + variable
        position = var.end()
    new_text = new_text + text[position:]
    return new_text

def test_insert_variables_into_text():
    variables = [VARIABLE_ONE, VARIABLE_TWO]
    text = "This is {{VARIABLE_ONE}} of {{VARIABLE_TWO}}"
    new_text = insert_variables_into_text(text, variables)
    print ("Result of insert variable test:")
    print(new_text)


def main(structure, head, content, assets_dir=None, persona_path=None):
    global HEAD
    HEAD = head
    global TABLE_OF_CONTENTS
    TABLE_OF_CONTENTS = create_table_of_contents(content, persona_path=persona_path)
    global ESSAY_BODY
    ESSAY_BODY = parse_markdown(content, assets_dir=assets_dir, persona_path=persona_path)
    HEAD = insert_variables_into_text(HEAD)
    out = insert_variables_into_text(structure)
    return out

def move_images(content_dir, root_dir, assets_directory_from_root):
    ''' copy images that get exported scriviner '''
    assets_dir = os.path.join(root_dir, assets_directory_from_root)
    for file in os.listdir(content_dir):
        if not file.endswith('md'):
            shutil.copy(os.path.join(content_dir, file), os.path.join(assets_dir, file))
    return 0






if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', default='/Users/zaaron/Dropbox/Projects/Personal Website/')
    parser.add_argument('--assets', default='assets/parpa')
    parser.add_argument('--test_insert_variables', action="store_true")
    parser.add_argument('--structure', default='html-chunks/structure.html')
    parser.add_argument('--head', default='html-chunks/head.html')
    parser.add_argument('--content', default='content/scriviner_test_markdown/scriviner_test_markdown.md')
    parser.add_argument('--out', default='out.html')
    parser.add_argument('--personas', default='content/persona_paths.csv')
    parsed_args = vars(parser.parse_args())

    if parsed_args.get("test_insert_variables"):
        test_insert_variables_into_text()
    else:
        content_path = os.path.abspath(parsed_args.get('content'))
        content_dir = os.path.dirname(content_path)
        root_dir = os.path.abspath(parsed_args.get('root'))
        assets_directory_from_root = parsed_args.get('assets')
        structure_path = os.path.abspath(parsed_args.get('structure'))
        head_path = os.path.abspath(parsed_args.get('head'))
        out_path = os.path.abspath(parsed_args.get('out'))
        persona_path = os.path.abspath(parsed_args.get('personas'))
        move_images(content_dir, root_dir, assets_directory_from_root)
        with open(structure_path, 'r') as f:
            structure = f.read()
        with open(head_path, 'r') as f:
            head = f.read()
        with open(content_path, 'r') as f:
            content = f.read()
        out = main(structure, head, content, assets_dir=assets_directory_from_root, persona_path=persona_path)
        with open(out_path, 'w') as f:
            f.write(out)
