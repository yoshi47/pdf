import PyPDF2

merger = PyPDF2.PdfFileMerger()

file = 'pdf-src/'

merger.append('第3回.pdf', pages=(0, 2))

merger.append('第3回.pdf', pages=(4, 23))

merger.write('sample.pdf')
merger.close()