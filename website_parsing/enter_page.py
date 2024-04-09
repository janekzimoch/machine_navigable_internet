

from browser_env.actions import execute_mouse_click

def enter_page(env, id: str):
    page = env.page
    obseration_processor = env.observation_handler.action_processor
    element_center = obseration_processor.get_element_center(id)
    
    execute_mouse_click(element_center[0], element_center[1], page)
    
    new_page_obs = env.observation_handler.text_processor.process(page, page.client)
    return new_page_obs



