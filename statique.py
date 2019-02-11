# coding=UTF-8
import click
import markdown2

@click.command()
@click.option('-i',"--input-file","in_file", default='', help='chemin du fichier à convertir.')
@click.option("-o","--output-directory","out_directory", default='', help = 'Chemin du fichier de sortie')

def convertir (in_file, out_directory):
        file = in_file
        out = out_directory
        html_head = ('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Titre</title>\n</head>\n<body>\n')
        html_foot = "</body>\n</html>"
        html_mark = markdown2.markdown_path(file)
        html = html_head + html_mark + html_foot
        open(out + ".html", "w+", encoding="UTF-8").write(html)


if __name__ == '__main__':
    convertir()