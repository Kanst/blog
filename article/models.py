# -*- coding: utf-8 -*-
from django.db import models
from markdown import markdown
import markdown
from markitup.fields import MarkupField
# Create your models here.
from tagging.fields import TagField
from tagging.models import Tag
class Article(models.Model):
    title = models.CharField('название', max_length=100)
    slug = models.SlugField()
    text = MarkupField()
    add_date = models.DateTimeField('дата добавления', null=True, auto_now_add=True)
    
    res_date = models.DateTimeField('дата последнего изменения', null=True, auto_now=True)
    pub_date = models.DateTimeField('дата публикации', null=True, blank = True)
    tags = TagField()
    def __unicode__(self):
        return self.title


    def get_tags(self):
        return Tag.objects.get_for_object(self) 


def makeExtension(configs=None):
    return CardsExtension(configs=configs)

class CardsExtension(markdown.Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('split_blockquotes', SplitBlockquotes(md), '_begin')
        md.treeprocessors.add('mark_blockquotes', MarkBlockquotes(md), '_begin')
        md.postprocessors.add('replace_marker_tags', ReplaceMarkerTags(md), '_end')

class SplitBlockquotes(markdown.preprocessors.Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            if line.startswith('>') and not line.endswith('  '):
                new_line = line + '\n\n' + BLOCKQUOTE_SPLITTER + '\n\n'
            else:
                new_line = line
            new_lines.append(new_line)
        return new_lines


class MarkBlockquotes(markdown.treeprocessors.Treeprocessor):
    def run(self, root):
        for bq in root.findall('blockquote'):
            for elem in bq.iter():
                if elem.text and elem.text.find('<ok>') != -1:
                    bq.set('class', 'state_ok')
                    break
                if elem.text and elem.text.find('<error>') != -1:
                    bq.set('class', 'state_error')
                    break  

class ReplaceMarkerTags(markdown.postprocessors.Postprocessor):
    def run(self, text):
        text = re.sub('<ok>', u'<span class="state_ok_item">', text)
        text = re.sub('<error>', u'<span class="state_error_item">', text)
        text = re.sub('<example>', u'<span class="example">', text)
        text = re.sub('</ok>|</error>|</example>', u'</span>', text)
        text = re.sub('<p>' + BLOCKQUOTE_SPLITTER + '</p>', u'', text)
        return text