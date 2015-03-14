import os
import sys

from panda3d.core import BitMask32, DynamicTextFont, Vec4

class Constants:

    CLIENT_VERSION = '1.00'
    BLACK = Vec4(0,0,0,0)
    WHITE = Vec4(1,1,1,0)
    HIGHLIGHT = Vec4(0,1,1,1)
    #SERVER_IP = 'smurf.sfsu.edu'
#    SERVER_IP = '130.212.135.127'
    SERVER_IP = '192.168.2.2'
    SERVER_PORT = 9090
    MYDIR = os.path.abspath(os.path.dirname(sys.argv[0])) + '/'
    DATABASE = MYDIR + 'db/SeriousGames.db'
    USERNAME = 'username'
    PASSWORD = 'password'
    DEBUG = True

    RANDOM_ID = 2000
    MAX_ITEM_COUNT = 1000
    MAX_MONEY = 1000000000

    FONT_TYPE_01 = DynamicTextFont('models/fonts/arial.ttf')
    FONT_TYPE_02 = DynamicTextFont('models/fonts/coopbl.ttf')
    FONT_TYPE_02.setOutline((0, 0, 0, 1), 0.5, 0.3)

    BAR_COLOR = (0, 0, 0, 0.3)

#    BG_COLOR = (0.55, 0.11, 0.11, 0.95)
    BG_COLOR = (0.33, 0.42, 0.18, 0.95)
#    BG_COLOR = (0.18, 0.18, 0.31, 0.95)

    BG_COLOR_LIGHT = (0.33, 0.42, 0.18, 0.65)

    TEXT_COLOR = (1, 1, 1, 1)
    TEXT_D_COLOR = (0.75, 0.75, 0.75, 1)
    TEXT_SHADOW_COLOR = (0, 0, 0, 0.5)
    LEADER_NAME_COLOR = (1, 1, 0, 1)

    TEXT_TYPE_CRITICAL = (0.8, 0.5, 0, 1)
    TEXT_TYPE_DAMAGE = (0.8, 0.2, 0.2, 1)
    TEXT_TYPE_DEATH = (0.4, 0.4, 0.4, 1)
    TEXT_TYPE_EXPERIENCE = (0.2, 0.8, 0.2, 1)
    TEXT_TYPE_HEALTH = (0.2, 0.8, 0.2, 1)
    TEXT_TYPE_LEVEL_UP = (1, 1, 0.2, 1)
    TEXT_TYPE_MONEY = (1, 1, 0.2, 1)

    NO_MASK = BitMask32(0x0)            # 0000 0000
    GROUND_MASK = BitMask32(0x1)        # 0000 0001
    WALL_MASK = BitMask32(0x2)          # 0000 0010
    GNDWALL_MASK = BitMask32(0x3)       # 0000 0011
    CLICKABLE_MASK = BitMask32(0x4)     # 0000 0100
    MOUSE_CLICK_MASK = BitMask32(0x5)   # 0000 0101
    CAM_TARGET_MASK = BitMask32(0x8)    # 0000 1000

    MISC_INVENTORY              = 0
    MISC_EQUIPMENT              = 1
    MISC_HOTKEY                 = 2
    MISC_SHOP                   = 3
    MISC_TRADE                  = 4

    HOTKEY_ITEM                 = 0
    HOTKEY_SKILL                = 1

    NPC_TYPE_REGULAR            = 0
    NPC_TYPE_SHOP               = 1
    NPC_TYPE_WARP               = 2

    UNIT_TYPE_CHAR              = 0
    UNIT_TYPE_BUG               = 1
    UNIT_TYPE_NPC               = 2
    UNIT_TYPE_TILE              = 3
    UNIT_TYPE_NODE              = 4

    MODE_TYPE_BOARD_GAME        = 0
    MODE_TYPE_SURVIVAL          = 1
    MODE_TYPE_CODING            = 2
    MODE_TYPE_TOP_DOWN          = 3
    MODE_TYPE_VARIABLES         = 4
    MODE_TYPE_CONTROL_FLOW      = 5

    ITEM_TYPE_CONSUMABLE        = 0
    ITEM_TYPE_NON_CONSUMABLE    = 1
    ITEM_TYPE_ARMOR             = 2
    ITEM_TYPE_WEAPON            = 3

    ITEM_SLOT_HEAD_TOP          = 1
    ITEM_SLOT_HEAD_MID          = 2
    ITEM_SLOT_HEAD_BOTTOM       = 3
    ITEM_SLOT_BODY_TOP          = 4
    ITEM_SLOT_MAIN_HAND         = 5
    ITEM_SLOT_OFF_HAND          = 6
    ITEM_SLOT_BODY_MID          = 7
    ITEM_SLOT_BODY_BOTTOM       = 8
    ITEM_SLOT_SHOE              = 9
    ITEM_SLOT_ACCESSORY         = 10

    MSG_NONE                            = 0
    CMSG_AUTH                           = 1
    CMSG_REGISTER                       = 3
    CMSG_SEARCH_PRIVATE_WORLD           = 5
    CMSG_CURRENT_GAMES                  = 7
    CMSG_JOIN_PVE_WORLD                 = 9
    CMSG_JOIN_PVP_WORLD                 = 11
    CMSG_CREATE_NEW_WORLD               = 13
    CMSG_SEE_PVE_ONLINE_PLAYERS         = 15
    CMSG_SEE_PVP_ONLINE_PLAYERS         = 17
    
    
    CMSG_PASSWORD_PRIVATE_WORLD         = 21
    CMSG_START_GAME                     = 23
    CMSG_PVE_MODE_CHAT                  = 25
    CMSG_PVP_MODE_CHAT                  = 27
    CMSG_UNIVERSAL_CHAT                 = 29
    CMSG_WHISPERING_CHAT                = 31
    CMSG_WORLD_CHAT                     = 33
    CMSG_ADD_ANIMAL                     = 35
    CMSG_ADD_PLANT                      = 37
    CMSG_ANIMAL_INFO                    = 39
    CMSG_MOVE_ANIMAL                    = 41
    CMSG_RESEARCH_DISEASES              = 43
    CMSG_RESEARCH_WEATHER               = 45
    CMSG_SAVE_EXIT_GAME                 = 47
    CMSG_KICK_PLAYER_OUT                = 49
    CMSG_ACCEPT_ANIMAL                  = 51
    CMSG_VOTE_GAME_SCALE                = 53
    CMSG_START_TO_READY_GAME            = 55
    CMSG_READY                          = 57
    CMSG_CANCEL_TO_JOIN_GAME            = 59

    CMSG_GETPVEWORLDS                   = 201
    CMSG_GETPVPWORLDS                   = 203
    CMSG_SEEONLINEPLAYERS               = 205
    CMSG_UPDATEENVIRONMENT              = 207

    SMSG_AUTH                           = 2
    SMSG_REGISTER                       = 4
    SMSG_SEARCH_PRIVATE_WORLD           = 6
    SMSG_CURRENT_GAMES                  = 8
    SMSG_JOIN_PVE_WORLD                 = 10
    SMSG_JOIN_PVP_WORLD                 = 12
    SMSG_CREATE_NEW_WORLD               = 14
    SMSG_SEE_PVE_ONLINE_PLAYERS         = 16
    SMSG_SEE_PVP_ONLINE_PLAYERS         = 18
    
    SMSG_PASSWORD_PRIVATE_WORLD         = 22
    SMSG_START_GAME                     = 24
    SMSG_PVE_MODE_CHAT                  = 26
    SMSG_PVP_MODE_CHAT                  = 28
    SMSG_UNIVERSAL_CHAT                 = 30
    SMSG_WHISPERING_CHAT                = 32
    SMSG_WORLD_CHAT                     = 34
    SMSG_ADD_ANIMAL                     = 36
    SMSG_ADD_PLANT                      = 38
    SMSG_ANIMAL_INFO                    = 40
    SMSG_MOVE_ANIMAL                    = 42
    SMSG_RESEARCH_DISEASES              = 44
    SMSG_RESEARCH_WEATHER               = 46
    SMSG_SAVE_EXIT_GAME                 = 48
    SMSG_KICK_PLAYER_OUT                = 50
    SMSG_ACCEPT_ANIMAL                  = 52
    SMSG_VOTE_GAME_SCALE                = 54
    SMSG_START_TO_READY_GAME            = 56
    SMSG_READY                          = 58
    SMSG_CANCEL_TO_JOIN_GAME            = 60

    SMSG_GETPVEWORLDS                   = 202
    SMSG_GETPVPWORLDS                   = 204
    SMSG_SEEONLINEPLAYERS               = 206
    SMSG_UPDATEENVIRONMENT              = 208

    UPDATE_PVE_ONLINE_PLAYERS           = "update_pve_online_players"
    UPDATE_PVP_ONLINE_PLAYERS           = "update_pvp_online_players"
    UPDATE_MAIN_ONLINE_PLAYERS          = "update_main_online_players"
    UPDATE_JOINPVEWORLD                 = "update_join_pve_world"
    UPDATE_JOINPVPWORLD                 = "update_join_pvp_world"

    LISTENER_LOGIN_2D                   = "listener_login_2d"
    LISTENER_PVP_2D                     = "listener_pvp_2d"
    LISTENER_PVP_ONLINE_PLAYERS         = "listener_pvp_online_players"
    LISTENER_PVP_REQUEST_ONLINE_PLAYER  = "listener_pvp_request_online_player"
    LISTENER_JOINPVPWORLD               = "listener_join_pvp_world"
    
    LISTENER_PVE_2D                     = "listener_pve_2d"
    LISTENER_PVE_ONLINE_PLAYERS         = "listener_pve_online_players"
    LISTENER_PVE_REQUEST_ONLINE_PLAYER  = "listener_pve_request_online_player"
    LISTENER_JOINPVEWORLD               = "listener_join_pvp_world"
    LISTENER_SEARCH_RESULT              = "listener_search_result"
    LISTENER_SEARCH_RESPONSE            = "listener_search_response"
    LISTENER_CREATE_NEW_WORLD_RESPONSE  = 'listener_create_new_world_response'
    LISTENER_CREATE_NEW_WORLD_RECEIVER  = 'listener_create_new_world_receiver'
    LISTENER_WORLD_LOBBY_INFO           = 'listener_world_lobby_info'
    LISTENER_CREATE_NEW_GAME_RESPONSE   = 'listener_create_new_game_response'
    LISTENER_GAME_LOBBY_RESPONSE        = 'listener_game_lobby_response'
    
    
    CMSG_PVPGAME_CHAT           = 68
    SMSG_PVPGAME_CHAT           = 69
    CMSG_PVEGAME_CHAT           = 70
    SMSG_PVEGAME_CHAT           = 71
    CMSG_UNIVERSAL_CHAT         = 72
    SMSG_UNIVERSAL_CHAT         = 73
    CMSG_PVPWORLD_CHAT          = 74
    SMSG_PVPWORLD_CHAT          = 75
    CMSG_PVEWORLD_CHAT          = 76
    SMSG_PVEWORLD_CHAT          = 77
    CMSG_TEAM_CHAT              = 78
    SMSG_TEAM_CHAT              = 79 
    
    CHAT_BUTTON_COLOR           =(0, 0, 0, 0.2)
    CHAT_BUTTON_FOCUS           =(1, 1, 1, 0.3)

