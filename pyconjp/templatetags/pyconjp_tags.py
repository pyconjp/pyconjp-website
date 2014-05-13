from django import template

from biblion.models import Post

register = template.Library()


class LatestSectionPostsNode(template.Node):

    def __init__(self, section, context_var):
        self.section = template.Variable(section)
        self.context_var = context_var

    def render(self, context):
        try:
            section = self.section.resolve(context)
            posts = Post.objects.section(section, queryset=Post.objects.current())
            context[self.context_var] = posts
        except Exception:
            pass
        return u""


@register.tag
def latest_section_posts(parser, token):
    """
        {% latest_section_posts "articles" as latest_article_posts %}
    """
    bits = token.split_contents()
    return LatestSectionPostsNode(bits[1], bits[3])
