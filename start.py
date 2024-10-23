from utils import android_connection, global_utils
import logging
import info
import time
import config
import clear_tmp
import os

def click_possible_button(screenshot):
    possible_buttons_folder = os.path.join(config.project_path, 'images', 'possible')
    
    for filename in os.listdir(possible_buttons_folder):
        file_path = os.path.join(possible_buttons_folder, filename)
        global_utils.find_and_click(file_path, screenshot)
    
    return


def click_play_button(screenshot,screenshot_dimensions):

    if(global_utils.find_and_click(config.project_path+'\\images\\play_button.png', screenshot)):
        time.sleep(20)
        
    global_utils.find_and_click(
        config.project_path+'\\images\\next_button.png', screenshot)
    
    global_utils.find_and_click(
        config.project_path+'\\images\\turns\\collect_rewards.png', screenshot)
    
    return 

def main(turns):
    
    counter = 0
    
    while 1:
        
        global_utils.click([100, 1500])
        
        time.sleep(3)
        
        screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
        
        start = global_utils.end_timer()
        
        # global_utils.find_and_click(config.project_path+'\\images\\accept.png', screenshot)
        
        if(global_utils.find_and_click(config.project_path+'\\images\\challenge.png', screenshot)):
            time.sleep(3)
            screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
            global_utils.find_and_click(config.project_path+'\\images\\record.png', screenshot)
            
            screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
            global_utils.find_and_click(config.project_path+'\\images\\adopt.png', screenshot)
            
            screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
            global_utils.find_and_click(config.project_path+'\\images\\accept.png', screenshot)
            
            screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
            global_utils.find_and_click(config.project_path+'\\images\\auto_challenge.png', screenshot)
            
            # screenshot = global_utils.take_screenshot("tmp\\"+str(counter)+".png")
            # global_utils.find_and_click(config.project_path+'\\images\\afk.png', screenshot)
            # global_utils.find_and_click(config.project_path+'\\images\\accept.png', screenshot)
            time.sleep(3)
            global_utils.click([130, 1050])
            
        
        end = global_utils.end_timer()
        global_utils.log_time_elapsed(
            "get_time", end-start)

        # click_possible_button(screenshot)
        
        counter += 1
        if counter > 100:
            counter = 0
            clear_tmp.clear()

if __name__ == "__main__":
    
    logging.basicConfig(filename=config.project_path+'\\log.txt', filemode='w', format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())

    android_connection.connect()
    
    main(6)