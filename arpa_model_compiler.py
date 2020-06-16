import re
import argparse

useful_classes = {
    'c0':'quote',
    'c3':'note_to_reader',
    'c22':'footnote',
    'c13':'bold',
    'c44':'quote',
    'c20':'quote',
    'c5':'emphasis',
    'c2':'link',
    'c57':'bold2',
    'c64':'tiny',
    'showbutton':'showbutton',
    'BodyColumn':'BodyColumn'
}

things_to_add_to_body = {
    'max-width': '550px',
    'line-height': '27px',
    'margin-top':'0px',
    'margin-bottom':'22px',
    'position':'relative',
    'padding-left':'32px',
    'padding-right':'32px'
}

def get_span(text):
    span =  re.findall(r'<span.*>(.+?)</span>',text)
    if len(span) == 0:
        return ""
    else:
        return span[0].strip()

def get_id(text):
    id =  re.findall(r'id=\"(.+?)\"',text)
    if len(id) == 0:
        return ""
    else:
        return id[0].strip()

def get_level(text):
    level = re.findall(r'<h(.+?)\ ',text)
    if len(level)==0:
        return ""
    else:
        return level[0]

def remove_outline(lines):
    skip = False
    lines_out = []
    for line in lines:
        if 'Outline' in line:
            skip = True
        if skip is True and "Distillation" in line:
            skip = False
        if not skip:
            lines_out.append(line)
    return lines_out

def convert_footnote_ref(line):
    footnote_num =  int(re.findall(r'ftnt(.+?)\"',line)[0])
    line = line.replace('<sup ><a href="#ftnt%d" id="ftnt_ref%d">[%d]</a></sup>'%(footnote_num, footnote_num, footnote_num),
        '<a id="footnote_source_%d" href="#footnote_%d"><sup class="mark">[%d]</sup></a>'%(footnote_num, footnote_num, footnote_num))
    line = line.replace('<sup class="c6 c11"><a href="#ftnt%d" id="ftnt_ref%d">[%d]</a></sup>'%(footnote_num, footnote_num, footnote_num),
        '<a id="footnote_source_%d" href="#footnote_%d"><sup class="mark">[%d]</sup></a>'%(footnote_num, footnote_num, footnote_num))
    line = line.replace('<sup class="link"><a href="#ftnt%d" id="ftnt_ref%d">[%d]</a></sup>'%(footnote_num, footnote_num, footnote_num),
    '<a id="footnote_source_%d" href="#footnote_%d"><sup class="mark">[%d]</sup></a>'%(footnote_num, footnote_num, footnote_num))


    return line
    #<sup ><a href="#ftnt13" id="ftnt_ref13">[13]</a></sup>
    #<a id="footnote_source_1" href="#footnote_1"><sup class="mark" style="font-size: 115%">[1]</sup></a>

def convert_footnote(line):
    footnote_num =  int(re.findall(r'id=\"ftnt(.+?)\"',line)[0])
    line=line.replace('<p class="footnote"><a href="#ftnt_ref%d" id="ftnt%d">[%d]</a>'%(footnote_num, footnote_num, footnote_num),
        '<a id="footnote_%d"></a><span >'%footnote_num)
    line=line.replace('<p ><a href="#ftnt_ref%d" id="ftnt%d">[%d]</a>'%(footnote_num, footnote_num, footnote_num),
        '<a id="footnote_%d"></a><span >'%footnote_num)

    #<p class="footnote"><a href="#ftnt_ref1" id="ftnt1">[1]</a>

    #<a id="footnote_1"></a><span >
    return line, footnote_num



def create_sitelist(lines):
    headers = []
    type = []
    ids = []
    current_h1 = ""
    current_h2 = ""
    indent = '  '
    for line in lines:
        if "<h" in line:
            level = get_level(line)
            span = get_span(line)
            id = get_id(line)
            if level.isdigit() and span and id and int(level) < 4:
                type.append(int(level))
                headers.append(span)
                ids.append(id)
    out = []
    out.append(2*indent+'<div class="SiteMenu">')
    out.append(3*indent+'<ul class="EssayList">')
    out.append(4*indent+'<ul class="TableOfContents">')
    open_classes = []
    for i,header in enumerate(headers):
        out.append('<li class="H%d ">'%type[i])
        out.append('<a href="#%s">'%ids[i] + header +'</a>')
        if i+1 < len(headers):
            if type[i+1] == type[i]:
                out.append('</li>')
            elif type[i+1] < type[i]:
                out.append('</li>')
                while open_classes[-1] >= type[i+1]:
                    out.append('</ul>')
                    out.append('</li>')
                    open_classes.pop()
            else:
                out.append('<ul>')
                open_classes.append(type[i])
        else:
            out.append('</li>')
            while len(open_classes) > 0:
                out.append('</ul>')
                out.append('</li>')
                open_classes.pop()
    out.append(4*indent+'</ul>')
    out.append(3*indent+'</ul>')
    out.append(2*indent+'</div>')
    return out

def create_sidebar_nav(lines):
    out = []
    out.append('<div class="MobileNav Scrolled">')
    out.append('    <div class="LeftItems">')
    out.append('      <div class="CurrentSectionLabel">')
    out.append('        <p class="Section">')
    out.append('          <span id="current_section_label">ARPA Model</span>')
    out.append('        </p>')
    out.append('      </div>')
    out.append('    </div>')
    out.append('    <div class="RightItems">')
    out.append('      <div id="toc" class="MobileSiteList">')
    out = out + create_sitelist(lines)
    out.append('     </div>')
    out.append('      <div class="MenuButton">')
    out.append('        <button class="IconButton" onclick="toggleVisibility()">')
    out.append('          <svg width="25" height="23" viewBox="0 0 25 23" fill="none">')
    out.append('            <title></title>')
    out.append('            <line x1="5.5" y1="1.5" x2="24.5" y2="1.5" stroke="#BBBBBB" stroke-linecap="round"></line>')
    out.append('            <circle cx="1.5" cy="1.5" r="1.5" fill="#BBBBBB"></circle>')
    out.append('            <line x1="5.5" y1="16.5" x2="24.5" y2="16.5" stroke="#BBBBBB" stroke-linecap="round"></line>')
    out.append('            <circle cx="1.5" cy="16.5" r="1.5" fill="#BBBBBB"></circle>')
    out.append('            <line x1="9.5" y1="6.5" x2="24.5" y2="6.5" stroke="#BBBBBB" stroke-linecap="round"></line>')
    out.append('            <circle cx="5.5" cy="6.5" r="1.5" fill="#BBBBBB"></circle>')
    out.append('            <line x1="9.5" y1="21.5" x2="24.5" y2="21.5" stroke="#BBBBBB" stroke-linecap="round"></line>')
    out.append('            <circle cx="5.5" cy="21.5" r="1.5" fill="#BBBBBB"></circle>')
    out.append('            <line x1="9.5" y1="11.5" x2="24.5" y2="11.5" stroke="#BBBBBB" stroke-linecap="round"></line>')
    out.append('            <path d="M7 11.5C7 12.3284 6.32843 13 5.5 13C4.67157 13 4 12.3284 4 11.5C4 10.6716 4.67157 10 5.5 10C6.32843 10 7 10.6716 7 11.5Z" fill="#BBBBBB"></path>')
    out.append('          </svg>')
    out.append('        </button>')
    out.append('      </div>')
    out.append('    </div>')
    out.append('  </div>')
    return out

def create_desktop_sidebar(lines):
    out = []
    indent = '  '
    out.append(indent+'<div class="DesktopSidebarContainer">')
    out = out + create_sitelist(lines)
    out.append('</div>')
    return out

def create_navbar(lines):
    out = []
    out.append('<div id="NavContainer">')
    out = out + create_desktop_sidebar(lines)
    out = out + create_sidebar_nav(lines)
    out.append('</div>')
    return out



def append_body_styles(out):
    out.append("<style>")
    out.append('.BodyColumn {')
    for thing in things_to_add_to_body:
        out.append(thing + ":" + things_to_add_to_body[thing] + ";")
    out.append("}")
    out.append("</style>")
    return out

def clean_classes(lines):
    out = []
    for line in lines:
        # Replace classes with useful classes
        matches=re.finditer(r'class=\"(.+?)\"',line)
        for match in matches:
            classes = match.group(1).split(" ")
            for c in classes:
                if c in useful_classes:
                    line = line.replace(c, useful_classes[c])
                else:
                    line = line.replace(c, "")
        line = line.replace('class=""','')
        line = line.replace('class=" "','')
        line = line.replace('class="  "','')
        line = line.replace('class=" 8"','')
        out.append(line)
    return out

def remove_styles(lines):
    out = []
    skip = False
    for line in lines:
        if '<style' in line:
            skip = True
        elif '</style' in line:
            skip = False
            continue
        if skip is True:
            continue
        out.append(line)
    return out

def convert_footnotes(lines):
    footnote = 0
    first_footnote = True
    out = []
    for line in lines:
        if 'id="ftnt_ref' in line:
            line = convert_footnote_ref(line)
        #footnote line
        if 'href="#ftnt_ref' in line:
            out.pop()
            if first_footnote:
                out.append('<ol id="footnotes">')
                first_footnote = False
            out.append('<li class="footnote">')
            line, footnote_num = convert_footnote(line)
            footnote=footnote_num
        if footnote > 0:
            line=line.replace('</p>','')
        if footnote > 0 and '</div>' in line:
            out.append('<a href="#footnote_source_%d">↩</a>'%(footnote))
            line = '</li>'
            footnote = 0
        out.append(line)
    return out

def add_internal_links(lines):
    out = []
    for line in lines:
        if 'href="#' in line:
            line = line.replace('href="#', 'class="internal-link" href="#')
        out.append(line)
    return out

def fix_distillation_headers(lines):
    out = []
    distillation = False
    for line in lines:
        if 'h3' in line and 'Metadiscussion' in line:
            print('metadiscussion')
            line = line.replace('h3', 'h2')
            print(line)
        if 'h2' in line and distillation:
            distillation = False
        if 'h2' in line and 'Distillation' in line:
            distillation = True
        if distillation and '<p ><span ><a class="internal-link"' in line:
            line = line.replace('<p ><span ><a class="internal-link"',
                         '<p ><span ><a class="internal-link distillationHeader"')
        out.append(line)
    return out

def remove_blank_lines(lines):
    out = []
    for line in lines:
        if len(re.findall('<span[^>]*></span>3nnrp1l5173', line)) > 0:
            print("removing line")
            print(line)
        else:
            out.append(line)
    return out

def fix_google_links(lines):
    out = []
    for line in lines:
        if 'https://www.google.com/url?q=' in line:
            line = line.replace('https://www.google.com/url?q=','')
        out.append(line)
    return out


def create_legible_headers(lines):
    intermediate_lines = []
    headers = {}
    distillation = False

    for line in lines:
        if 'h2' in line and distillation:
            distillation = False
        if 'id="h.' in line:
            id = re.findall(r'id=\"(.+?)\"',line)[0]
            text = re.findall(r'<span.*>(.+?)</span>',line)
            if len(text) == 0:
                print("no span on this line:")
                print(line)
                text=""
            else:
                text = text[0]
            new_header = text.strip().lower().replace(" ","_")
            if distillation:
                new_header = new_header + "_mini"
            line = line.replace(id, new_header)
            headers[id] = new_header
        intermediate_lines.append(line)

        if 'h2' in line and 'Distillation' in line:
            distillation = True
    out = []
    for line in intermediate_lines:
        if 'href="#h.' in line:
            id = re.findall(r'href=\"#(.+?)\"',line)[0]
            if id in headers:
                new_header = headers[id]
                line = line.replace(id, new_header)
            else:
                print("could not find id:%s"%id)
        out.append(line)
    return out

def create_license():
    out = []
    out.append('<h3>License</h3>')
    out.append('<p>')
    out.append('This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative')
    out.append('Commons Attribution 4.0 International License</a>.  This')
    out.append('means you’re free to copy, share, and build on the work,')
    out.append('provided you attribute it appropriately.  Please click on')
    out.append('the following license link for details: <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative')
    out.append('Commons License" style="border-width: 0; height: 21px;" src="https://i.creativecommons.org/l/by/4.0/88x31.png"></a>')
    out.append('</p>')
    return out


def main_old():
    with open("ARPAModelMaster.html") as f:
        content = f.read()
    lines = content.split("\n")
    lines = remove_outline(lines)
    lines = remove_blank_lines(lines)
    lines = clean_classes(lines)
    lines = remove_styles(lines)
    lines = convert_footnotes(lines)
    lines = add_internal_links(lines)
    lines = fix_distillation_headers(lines)
    lines = create_legible_headers(lines)
    lines = fix_google_links(lines)
    out = []
    first_header = True
    footnote = 0
    first_footnote = True
    for line in lines:

        if '<h1' in line and first_header is True:
            out.append('<div id="EssayContents">')
            out.append('<div id="EssayContentsInner" >')
            out.append('<div class="BodyColumn">')
            out.append(line)
            first_header = False
        elif '<body' in line:
            out.append('<link rel="stylesheet" href="/css/arpa.css">')
            out.append('<link rel="stylesheet" href="/css/SiteMenu.css">')
            out.append('<link rel="stylesheet" href="/css/NavBar.css">')
            out.append('<link rel="stylesheet" href="/css/MobileNav.css">')
            out.append(line)
            out = out + create_navbar(lines)
        elif '</body' in line:
            out.append('</ol>')
            out = out + create_license()
            out.append('</div>')
            out.append('</div>')
            out.append('<div id="footnotediv" class="concealed popup"></div>')
            out.append(line)
            out.append('<script type="text/javascript" src="/js/fancy-popups.js" ></script>')
            out.append('<script type="text/javascript" src="/js/table-of-contents.js" ></script>')
            out.append('<script type="text/javascript" src="/js/mobile-control.js" ></script>')
        else:
            out.append(line)
    with open("arpa_model.html", 'w') as f:
        f.write("\n".join(out))

def updgrad_headers(lines):
    out = []
    for line in lines:
        if line.strip().startswith('<h2 '):
            line=line.replace('<h2','<h1')
        if line.strip().startswith('<h3 '):
            line=line.replace('<h3','<h2')
        if line.strip().startswith('<h4 '):
            line=line.replace('<h4','<h2')
        if 'class="H2' in line:
            line=line.replace('H2','H1')
        if 'class="H3' in line:
            line=line.replace('H3','H2')
        if 'class="H4' in line:
            line=line.replace('H4','H3')
        out.append(line)
    return out



def main():
    with open("arpa_model.html.backup") as f:
        content = f.read()
    lines = content.split("\n")
    out = updgrad_headers(lines)
    with open("arpa_model.html", 'w') as f:
        f.write("\n".join(out))




if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--test', action="store_true")
    parsed_args = vars(parser.parse_args())
    if parsed_args.get("test"):
        with open("ARPAModelMaster.html") as f:
            content = f.read()
        out=create_toc(content)
        with open("test_toc.html", 'w') as f:
            f.write("\n".join(out))
    else:
        main()
