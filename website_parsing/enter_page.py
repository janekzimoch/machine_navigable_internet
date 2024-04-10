

from browser_env.actions import execute_mouse_click

def enter_page(env, id: str):
    page = env.page
    obseration_processor = env.observation_handler.action_processor
    element_center = obseration_processor.get_element_center(id)
    
    execute_mouse_click(element_center[0], element_center[1], page)
    
    new_page_obs = env.observation_handler.text_processor.process(page, page.client)
    return new_page_obs


def compare_components(old_components, new_components):
    # Convert old components list to a dictionary for faster access
    old_components_dict = {comp['type'] + '_' + comp['label']: comp for comp in old_components}
    changes = []

    for new_comp in new_components:
        label = new_comp['label']
        new_children_ids = new_comp['children_id']
        
        # Check if the component exists in the old components by label
        if label in old_components_dict:
            old_children_ids = old_components_dict[label]['children_id']
            # Check if children_id lists are different
            if set(new_children_ids) != set(old_children_ids):
                changes.append({'label': label, 'old_children_id': old_children_ids, 'new_children_id': new_children_ids})
        else:
            # Component is new
            changes.append({'label': label, 'old_children_id': [], 'new_children_id': new_children_ids})

    return changes


def get_page_diff(prev_components, new_components) -> str:
    diff = compare_components(prev_components, new_components)
    print(diff)
    page_diff = ''
    return page_diff

