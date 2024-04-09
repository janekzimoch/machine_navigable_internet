import re

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