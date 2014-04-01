# -*- coding: utf-8 -*-
import lxml.etree
from . import pipeline_item
import core.docvert_exception
import core.docvert_xml

class GetPreface(pipeline_item.pipeline_stage):
    def stage(self, pipeline_value):
        params = dict(
            loopDepth = 0,
            process = self.attributes['process'],
            customFilenameIndex = 'index.html',
            customFilenameSection = 'section#.html'
        )
        xslt_path = self.resolve_pipeline_resource('internal://each-page.xsl')
        return core.docvert_xml.transform(pipeline_value, xslt_path, params)


