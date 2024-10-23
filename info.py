from utils import global_utils
import logging
import cv2


# Gets all the possible information from the screen
# Mana to spend
# Cards in hand
# Active fields
# Available fields to play
def get_info(counter, screenshot, screenshot_dimensions, player_turn):
    # Logging information
    logging.info("---------------------------")
    logging.info("Picture: " + str(counter))

    # Log turn
    logging.info('* Turn: ' + str(player_turn))

    # cv2.waitKey(10)
    counter += 1
    return {
        'player_turn': player_turn,
        # 'my_hand_cards': my_hand_cards,
        # 'active_fields': active_fields,
        # 'player_played_cards': player_played_cards,
        'counter': counter
    }
