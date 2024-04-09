''' 
This script exposes single function: _get_clickable_components(page) 

This function is responsible for taking an existing page and enhancing its HTML/accessability_tree_text with a descritpion of:
- what does the button do? 
    - does it redirect to a new page? If yes, what page is it redirecting to?
    - does it modify existing page? If yes, what does it change? 
    - does it expand some setting window? If yes, what are those setting options? 
'''
import json
import os
import subprocess
import tempfile
from types import SimpleNamespace


from browser_env.envs import ScriptBrowserEnv
from agent.agent import construct_agent
from browser_env.trajectory import Trajectory
from browser_env.utils import StateInfo
from browser_env.auto_login import get_site_comb_from_filepath
from website_parsing.parse_page import parse_accessibility_tree
from website_parsing.enter_page import enter_page


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

if __name__ == "__main__":
    args_defaults = {
        "render": False,
        "slow_mo": 0,
        "action_set_tag": "id_accessibility_tree",
        "observation_type": "accessibility_tree",
        "current_viewport_only": True,
        "viewport_width": 1280,
        "viewport_height": 720,
        "save_trace_enabled": True,
        "sleep_after_execution": 0.0,
        "max_steps": 30,
        "agent_type": "prompt",
        "instruction_path": "agent/prompts/jsons/p_cot_id_actree_2s.json",
        "parsing_failure_th": 3,
        "repeating_action_failure_th": 3,
        "provider": "openai",
        "model": "gpt-3.5-turbo-0613",
        "mode": "chat",
        "temperature": 1.0,
        "top_p": 0.9,
        "context_length": 0,
        "max_tokens": 384,
        "stop_token": None,
        "max_retry": 1,
        "max_obs_length": 1920,
        "model_endpoint": "",
        "test_start_idx": 0,
        "test_end_idx": 1,
        "result_dir": "",
        "render_screenshot": True
    }
    args = SimpleNamespace(**args_defaults)

    agent = construct_agent(args)

    env = ScriptBrowserEnv(
        headless=not args.render,
        slow_mo=args.slow_mo,
        observation_type=args.observation_type,
        current_viewport_only=args.current_viewport_only,
        viewport_size={
            "width": args.viewport_width,
            "height": args.viewport_height,
        },
        save_trace_enabled=args.save_trace_enabled,
        sleep_after_execution=args.sleep_after_execution,
    )

    config_file = "/Users/janek/Coding/hacathons/ef/machine_navigable_internet/config_files/0.json"
    with open(config_file) as f:
        _c = json.load(f)
        intent = _c["intent"]
        task_id = _c["task_id"]
        # automatically login
        if _c["storage_state"]:
            cookie_file_name = os.path.basename(_c["storage_state"])
            comb = get_site_comb_from_filepath(cookie_file_name)
            temp_dir = tempfile.mkdtemp()
            # subprocess to renew the cookie
            subprocess.run(
                [
                    "python",
                    "browser_env/auto_login.py",
                    "--auth_folder",
                    temp_dir,
                    "--site_list",
                    *comb,
                ]
            )
            _c["storage_state"] = f"{temp_dir}/{cookie_file_name}"
            assert os.path.exists(_c["storage_state"])
            # update the config file
            config_file = f"{temp_dir}/{os.path.basename(config_file)}"
            with open(config_file, "w") as f:
                json.dump(_c, f)


    obs, info = env.reset(options={"config_file": config_file})
    # print("obs: ", obs)

    components = parse_accessibility_tree(obs['text'])
    def get_comp_id():
        for comp in components:
            if 'SALES' in comp['label']:
                return comp['id']
    id = get_comp_id()
    print('id: ', id, '  type: ', type(id))
    enter_page(env, str(id))

    # # print("info: ", info)

    # state_info: StateInfo = {"observation": obs, "info": info}
    # trajectory: Trajectory = []
    # trajectory.append(state_info)
    # meta_data = {"action_history": ["None"]}
    # try:
    #     action = agent.next_action(
    #         trajectory, intent, meta_data=meta_data
    #     )
    # except ValueError as e:
    #     print(f"ERROR: {str(e)}")

    # print("\n\naction: ", action)

    # obs, _, terminated, _, info = env.step(action)

    # print('\n\nNew Observation: ', obs)
    # # to execute a click we need to do env.step(action)
    # # which calls execute_action() and then execute_mouse_click()
    # # then we simply call get observation to get a new page



