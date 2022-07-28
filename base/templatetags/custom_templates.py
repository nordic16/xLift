from django.template import Library, Node, TemplateSyntaxError

register = Library()

class RangeNode(Node):
    def __init__(self, num, context_name):
        self.num, self.context_name = num, context_name
    def render(self, context):
        context[self.context_name] = range(1, int(self.num + 1))
        return ""
        
@register.tag
def num_range(parser, token):
    """
    Takes a number and iterates and returns a range (list) that can be 
    iterated through in templates
    
    Syntax:
    {% num_range 5 as some_range %}
    
    {% for i in some_range %}
      {{ i }}: Something I want to repeat\n
    {% endfor %}
    
    Produces:
    0: Something I want to repeat 
    1: Something I want to repeat 
    2: Something I want to repeat 
    3: Something I want to repeat 
    4: Something I want to repeat
    """
    
    range_node = None
    
    try:
        fnctn, num, trash, context_name = token.split_contents()
        range_node = RangeNode(num, context_name)
        
    except ValueError:
        print("wtf")
    
    return range_node