# -*- coding: utf-8 -*-
import os
import lxml.etree
import io
from . import pipeline_item
import core.docvert_exception


class GeneratePostConversionEditorFiles(pipeline_item.pipeline_stage):
    def stage(self, pipeline_value):
        return pipeline_value



