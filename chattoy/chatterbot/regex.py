#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


class Regex(object):
    def strip_var(m):
        """
        strip useless tag in vars. Like this:
        from:
            `<w:t>{{</w:t>
            </w:r>
            <w:r w:rsidR="001A7474">
                <w:t xml:space="preserve"> i</w:t>
            </w:r>
            <w:r>
                <w:rPr>
                    <w:rFonts w:hint="eastAsia"/>
                </w:rPr>
            <w:t>tem}}</w:t>`
        to:
            `<w:t>{{ item}}</w:t>`
        """
        txt = m.group()
        start = m.groups()[0]
        end = m.groups()[1]
        wrs = re.findall('<w:t[^>]*>.*?</w:t>', txt)  # tag with text
        return start + ''.join([re.sub('<[^>]*?>', '', i)
                                for i in wrs]) + end  # replace tag

    def tag(name='', reserve=False):
        if reserve:
            return r'(<%s[^>]*?>)' % name
        else:
            return r'<%s[^>]*?>' % name

    def tag_end(name='', reserve=False):
        if reserve:
            return r'(</%s>)' % name
        else:
            return r'</%s>' % name

    REGX_TABLE = [
        # join the splited {{ or {%
        (r"{(" + tag() + r"[\s\r\n]*)+({|%)", r"{\2"),
        (r"}(" + tag() + r"[\s\r\n]*)+(%|})", r"}\2"),
        # replace logic control :
        (
            r"(" + tag("w:t") + ")[^<]*" + "{%" + "[^<}]*?(" + tag_end("w:t") +
            ")"  # tag with "{%"
            r".*?"  # content in {% and %}
            r"" + tag("w:t") + "[^<{]*?" + "%}" + "[^<]*" + tag_end("w:t") +
            ""  # tag with "%}"
            ,
            strip_var),
        # replace vars :
        (
            r"(" + tag("w:t") + ")[^<]*" + "{{" + "[^<}]*?(" + tag_end("w:t") +
            ")"  # tag with "{{"
            r".*?"  # content in {{ and }}
            r"" + tag("w:t") + "[^<{]*?" + "}}" + "[^<]*" + tag_end("w:t") +
            ""  # tag with "}}"
            ,
            strip_var),
    ]

    def format_jinja_template(txt):
        for regx, rep in REGX_TABLE:
            txt = re.sub(regx, rep, txt, flags=re.DOTALL)
        return txt

    def format_jinja_template_file(input_file, output_file):
        txt = open(input_file, 'r').read()
        txt = format_jinja_template(txt)
        open(output_file, 'w').write(txt)
        return output_file
