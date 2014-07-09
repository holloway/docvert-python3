# -*- coding: utf-8 -*-
import zipfile
import io

class types(object):
    oasis_open_document = "oasis_open_document (any version)"
    pdf = "portable document format (any version)"
    xml = "xml"
    html = "html"
    exception = "exception"
    unknown_type = "unknown file type"

def detect_document_type(data):
    if isinstance(data, Exception):
        return types.exception
    if isinstance(data, str):
        data = io.BytesIO(data)

    # 1. Sniff for OpenDocument
    try:
        magic_bytes_open_document = 'PK'
        data.seek(0)
        first_bytes = data.read(len(magic_bytes_open_document)).decode('latin-1')
        if first_bytes == magic_bytes_open_document: # Ok it's a ZIP but...
            archive = zipfile.ZipFile(data)
            if 'mimetype' in archive.namelist() and archive.read('mimetype').decode('utf-8') == 'application/vnd.oasis.opendocument.text': # ...if it doesn't have these files it's not an OpenDocument
                return types.oasis_open_document
    except UnicodeDecodeError as e:
        pass
    except Exception as e:
        print(e)
    # 2. Sniff for PDF
    try:
        magic_bytes_pdf = '%PDF'
        data.seek(0)
        first_bytes = data.read(len(magic_bytes_pdf)).decode('latin-1')
        if first_bytes == magic_bytes_pdf:
            return types.pdf
    except UnicodeDecodeError as e:
        pass
    except Exception as e:
        print(e)
    # 3. Sniff for HTML and XML
    data.seek(0)
    try:
        first_bytes = data.read(200).decode('latin-1') #200 bytes in, because sometimes there's a really long doctype
        #print first_bytes
        data.seek(0)
        if first_bytes.count("<html") > 0:
            return types.html
        if first_bytes.count("<?xml") > 0:
            return types.xml
    except UnicodeDecodeError as e:
        pass
    except Exception as e:
        print(e)
   
    return types.unknown_type
