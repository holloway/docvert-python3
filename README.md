<p align="center">
<img src="logo.gif" alt="Docvert">
</p>


Converts Word Processor office files (e.g. .DOC files) to OpenDocument, DocBook, and structured HTML.

This is Docvert for Python 3. It is beta quality. To find Docvert for Python 2.x see http://github.com/holloway/docvert/

Web Service
-----------

    python3 ./docvert-web.py [-p PORT] [-H host]

Command Line
------------

    python3 ./docvert-cli.py

    usage: docvert-cli.py [-h] [--version] --pipeline PIPELINE
        [--response {auto,path,stdout}]
        [--autopipeline {Break up over Heading 1.default,Nothing one long page}]
        [--url URL]
        [--list-pipelines]
        [--pipelinetype {tests,auto_pipelines,pipelines}]
        infile [infile ...]

Community
---------

http://lists.catalyst.net.nz/mailman/listinfo/docvert

Requirements
------------

    Python 3
    libreoffice
    python3-uno
    python-lxml
    python-imaging
    pdf2svg
    librsvg2-2
    
Quickstart Guide
----------------

    sudo apt-get install libreoffice python3-uno python-lxml python3-imaging pdf2svg librsvg2-2

    /usr/bin/soffice --headless --norestore --nologo --norestore --nofirststartwizard --accept="socket,port=2002;urp;"

then in another terminal

    cd ~

    git clone git://github.com/holloway/docvert-python3.git

    cd docvert-python3

    python3 ./docvert-web.py

and browse to http://localhost:8080


LICENCE
-------
Released under the GPL3 see LICENCE


