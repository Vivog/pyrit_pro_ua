import re
import pathlib
import tkinter
from pathlib import Path
from tkinter import messagebox as mb
root = tkinter.Tk()
root.withdraw()
try:
    path_xml = list(Path(pathlib.Path.cwd()).glob('*.xml'))[0]
    in_f = open(path_xml, 'r')
    data = in_f.readlines()
    in_f.close()
    pr1_str = str('<?xml-stylesheet type=\'text/xsl\' href=\'protocol1_UA.xsl\'?>')
    pr2_str = str('<?xml-stylesheet type=\'text/xsl\' href=\'protocol2_UA.xsl\'?>')
    if 'protocol1_UA.xsl' in data[1]:
        data[1] = data[1].replace(pr1_str, pr2_str)
        numbs = [re.findall(r'"\d\d\d.\d"', i) for i in data]


        def pyrit(elm):
            t = -16.6693 + 1.0801 * float(elm.strip(r'"'))
            return str(round(t, 1))


        n = [i for i in numbs if len(i) != 0]
        d = [j.strip('"') for i in n for j in i]
        print(n)
        print(d)
        new_d = list(map(pyrit, d))
        print(new_d)
        for i in range(0, len(data)):
            # print(i)
            for j in range(0, len(d)):
                if d[j] in data[i]:
                    data[i] = data[i].replace(d[j], new_d[j])

        path_xml_out = path_xml.name.replace(path_xml.suffix, '_OBR.xml')
        out_f = open(path_xml_out, 'w')
        out_f.writelines(data)
        out_f.close()
    else:
        mb._show('Шаблон протокола', "Использован не верный шаблон протокола\n\nПримените protocol1_UA")
except:
    mb._show('Файл протокола', "Файл протокола отсутствует.\nПоместите файл протокола в данную директорию")


