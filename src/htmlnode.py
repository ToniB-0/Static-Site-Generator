
class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
        
        
    def to_html(self):
        raise NotImplementedError("Child/subclasses should implement this method")
    
    def props_to_html(self):
        if not self.props:
            return ''
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())



    def __repr__(self):
        return (
            f"HTMLNode(tag={self.tag}, "
            f"value={self.value}, "
            f"children={self.children}, "
            f"props={self.props})"
        )


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=[], props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf nodes must have a value")    
    
        if self.tag is None:
            return self.value
        
        attrs = self.props_to_html()
        attrs_part = f" {attrs}" if attrs else ""

        # return the HTML string
        return f"<{self.tag}{attrs_part}>{self.value}</{self.tag}>"



class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
     

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if not self.children:
            raise ValueError("Parent nodes must have children")

        # Convert all children to HTML and join them
        children_html = ''.join(child.to_html() for child in self.children)
        
        # Build the HTML with props and children
        attrs = self.props_to_html()
        attrs_part = f" {attrs}" if attrs else ""
        return f"<{self.tag}{attrs_part}>{children_html}</{self.tag}>"
