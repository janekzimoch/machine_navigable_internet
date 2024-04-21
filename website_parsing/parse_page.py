import re
from dataclasses import dataclass

@dataclass
class Component:
    id: str
    tag: str
    attrs: dict
    description: str = ""


def parse_html_line(line: str) -> Component:
    ' splits a string of an html into Component object '
    pattern = re.compile(r'\[(\d+)\]\s*<(\w+)(.*?)>')
    
    match = pattern.search(line)
    if not match: 
        return None

    id = match.group(1)
    tag = match.group(2)
    attrs_str = match.group(3).strip()

    attrs_pattern = re.compile(r'(\w+)="([^"]*)"')
    attrs = dict(attrs_pattern.findall(attrs_str))

    return Component(id=id, tag=tag, attrs=attrs)


def is_clickable(component: Component) -> bool:
    if component is None:
        return None
    if component.tag in ['A', 'BUTTON'] or 'onclick' in component.attrs:
        return True
    else:
        return False


def parse_html(html: str) -> list[Component]:
    ' extract clickable components from an html '
    lines = html.split('\n')
    clickable_components = []
    for line in lines:
        comp = parse_html_line(line)
        if is_clickable(comp):
            clickable_components.append(comp)
    return clickable_components


def parse_accessibility_tree(tree):
    # Split the input string into lines
    lines = tree.strip().split('\n')
    components = []

    # Helper function to parse misc info
    def parse_misc(info_str):
        if not info_str:
            return None
        # Match key-value pairs where the key is followed by a colon and the value can contain spaces
        pattern = re.compile(r'(\w+):\s*([^:]+)(?=\s+\w+:|$)')
        misc = dict(pattern.findall(info_str))
        return misc if misc else None

    # Parse each line
    for line in lines:
        # Using regex to extract id, type, label and misc if available
        match = re.match(r'\s*\[(\d+)\]\s+(\w+)\s*\'(.*?)\'\s*(.*)', line)
        if match:
            component_id, component_type, label, misc_str = match.groups()
            # Extract misc info as a dictionary
            misc = parse_misc(misc_str)
            depth = line.count('\t')

            # Prepare the component dictionary
            component = {
                'id': int(component_id),
                'type': component_type,
                'label': label,
                'misc': misc,
                'depth': depth,
                'children_id': []
            }
            # Append to components list
            components.append(component)

    # Then, when determining parent-child relationships
    for i, component in enumerate(components):
        if i > 0:  # Skip the first element as it does not have a parent
            depth = component['depth']
            # Traverse backwards to find parent
            for parent in reversed(components[:i]):
                parent_depth = parent['depth']
                if parent_depth < depth:
                    parent['children_id'].append(component['id'])
                    break

    return components