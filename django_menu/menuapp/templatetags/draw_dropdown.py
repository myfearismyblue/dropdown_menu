from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def is_checked(context, node):
    """
    Finds node url in a context path_name. Returns 'checked' parameter for <input> tag if found,
    else recurently looks up at children's urls.
    """
    url = node.get_url()
    # if the toplevel node url in a context path_name then it's should be checked
    if url in context.request.get_full_path():
        return 'checked'
    # if not, then look at it's children if they are exist
    if node.nodes.all():
        for n in node.nodes.all():
            res = is_checked(context, n)
            if res is not None:
                return 'checked'


@register.inclusion_tag('template_tags/dropdown.html', takes_context=True)
def draw_dropdown(context, node):
    return {'node': node}


