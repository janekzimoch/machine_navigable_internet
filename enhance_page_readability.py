''' 
This script exposes single function: _get_clickable_components(page) 

This function is responsible for taking an existing page and enhancing its HTML/accessability_tree_text with a descritpion of:
- what does the button do? 
    - does it redirect to a new page? If yes, what page is it redirecting to?
    - does it modify existing page? If yes, what does it change? 
    - does it expand some setting window? If yes, what are those setting options? 
'''

def modify_current_page(page):
    ''' itterate through all clickable components and for each, idenitfy it's purpose.
    then enhance current page with those descriptions '''
    enhanced_page = page
    clickable_components = _get_clickable_components(page)
    for comp in clickable_components:
        child_page = _click_button(comp)
        child_summary = _summarise_page(child_page)
        enhanced_page = _enhance_comp_description(child_summary)
    enhanced_page = None
    return enhanced_page

def _click_button(component):
    ''' click button component to retrive page it routes to. '''
    page = None
    return page

def _summarise_page(page):
    ''' given html/accesability_tree page, output descritpion of what's page's purpose. '''
    page_summary = ""
    return page_summary

def _get_clickable_components(page):
    return []

def _enhance_comp_description(component, child_description):
    enhanced_page = None
    return enhanced_page