import os
import sys

from panda3d.core import BitMask32
from panda3d.core import DynamicTextFont
from panda3d.core import Vec4

class Constants:

    CLIENT_VERSION = '1.32'
    BLACK = Vec4(0,0,0,0)
    WHITE = Vec4(1,1,1,0)
    HIGHLIGHT = Vec4(0,1,1,1)
#    SERVER_IP = 'smurf.sfsu.edu'
    SERVER_PORT = 9252
    SERVER_IP = 'localhost'
#    SERVER_PORT = 9090
    MYDIR = os.path.abspath(os.path.dirname(sys.argv[0])) + '/'
    DATABASE = MYDIR + 'db/SeriousGames.db'
    USERNAME = 'username'
    PASSWORD = 'password'
    DEBUG = False

    USER_ID = -1
    AVATAR_ID = -1

    LOD_FAR = 50
    LOD_NEAR = 3
    
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
    TEXT_D_COLOR = (0.5, 0.5, 0.5, 1)
    TEXT_SHADOW_COLOR = (0, 0, 0, 0.5)
    LEADER_NAME_COLOR = (1, 1, 0, 1)

    TEXT_TYPE_CRITICAL = (0.8, 0.5, 0, 1)
    TEXT_TYPE_DAMAGE = (0.8, 0.2, 0.2, 1)
    TEXT_TYPE_DEATH = (0.4, 0.4, 0.4, 1)
    TEXT_TYPE_BIRTH = (0.2, 0.8, 0.2, 1)
    TEXT_TYPE_EXPERIENCE = (0.2, 0.8, 0.2, 1)
    TEXT_TYPE_HEALTH = (0.2, 0.8, 0.2, 1)
    TEXT_TYPE_LEVEL_UP = (1, 1, 0.2, 1)
    TEXT_TYPE_MONEY = (1, 1, 0.2, 1)

    REWARD_TYPE_XP = 0
    REWARD_TYPE_MONEY = 1

    NO_MASK = BitMask32(0x0)            # 0000 0000
    GROUND_MASK = BitMask32(0x1)        # 0000 0001
    WALL_MASK = BitMask32(0x2)          # 0000 0010
    GNDWALL_MASK = BitMask32(0x3)       # 0000 0011
    CLICKABLE_MASK = BitMask32(0x4)     # 0000 0100
    MOUSE_CLICK_MASK = BitMask32(0x15)  # 0000 0101
    CAM_TARGET_MASK = BitMask32(0x8)    # 0000 1000
    ZONE_MASK = BitMask32(0x10)         # 0001 0000

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
    CMSG_AUTH                           = 101
    SMSG_AUTH                           = 201
    CMSG_REGISTER                       = 102
    SMSG_REGISTER                       = 202
    CMSG_SEARCH_PRIVATE_WORLD           = 103
    SMSG_SEARCH_PRIVATE_WORLD           = 203
    CMSG_JOIN_PVE_WORLD                 = 104
    SMSG_JOIN_PVE_WORLD                 = 204
    CMSG_JOIN_PVP_WORLD                 = 105
    SMSG_JOIN_PVP_WORLD                 = 205
    CMSG_CREATE_NEW_WORLD               = 106
    SMSG_CREATE_NEW_WORLD               = 206
    CMSG_SEE_PVE_ONLINE_PLAYERS         = 107
    SMSG_SEE_PVE_ONLINE_PLAYERS         = 207
    CMSG_SEE_PVP_ONLINE_PLAYERS         = 108
    SMSG_SEE_PVP_ONLINE_PLAYERS         = 208
    CMSG_CHANGE_AVATAR_TYPE             = 109
    SMSG_CHANGE_AVATAR_TYPE             = 209
    CMSG_PASSWORD_PRIVATE_WORLD         = 110
    SMSG_PASSWORD_PRIVATE_WORLD         = 210
    CMSG_START_GAME                     = 111
    SMSG_START_GAME                     = 211
    CMSG_CHAT                           = 112
    SMSG_CHAT                           = 212
    CMSG_HEARTBEAT                      = 113
    SMSG_HEARTBEAT                      = 213
    CMSG_BUY_ANIMAL                     = 114
    SMSG_BUY_ANIMAL                     = 214
    CMSG_BUY_PLANT                      = 115
    SMSG_BUY_PLANT                      = 215
    CMSG_MOVE_ANIMAL                    = 116
    SMSG_MOVE_ANIMAL                    = 216
    CMSG_RESEARCH_DISEASES              = 117
    SMSG_RESEARCH_DISEASES              = 217
    CMSG_RESEARCH_WEATHER               = 118
    SMSG_RESEARCH_WEATHER               = 218
    CMSG_SAVE_EXIT_GAME                 = 119
    SMSG_SAVE_EXIT_GAME                 = 219
    CMSG_VOTE_GAME_SCALE                = 120
    SMSG_VOTE_GAME_SCALE                = 220
    CMSG_KICK_PLAYER_PVP_LOBBY          = 121
    SMSG_KICK_PLAYER_PVP_LOBBY          = 221
    CMSG_ACCEPT_ANIMAL                  = 122
    SMSG_ACCEPT_ANIMAL                  = 222
    CMSG_START_TO_READY_GAME            = 123
    SMSG_START_TO_READY_GAME            = 223
    CMSG_READY                          = 124
    SMSG_READY                          = 224
    CMSG_CANCEL_TO_JOIN_GAME            = 125
    SMSG_CANCEL_TO_JOIN_GAME            = 225
    CMSG_CHANGE_TEAM_PVP                = 126
    SMSG_CHANGE_TEAM_PVP                = 226
    CMSG_GETPVEWORLDS                   = 127
    SMSG_GETPVEWORLDS                   = 227
    CMSG_GETPVPWORLDS                   = 128
    SMSG_GETPVPWORLDS                   = 228
    CMSG_SEEONLINEPLAYERS               = 129
    SMSG_SEEONLINEPLAYERS               = 229
    CMSG_UPDATE_ANIMAL_TARGET           = 130
    SMSG_UPDATE_ANIMAL_TARGET           = 230
    CMSG_UPDATE_ANIMAL_COORS            = 131
    SMSG_UPDATE_ANIMAL_COORS            = 231
    CMSG_UPDATEENVIRONMENT              = 132
    SMSG_UPDATEENVIRONMENT              = 232
    CMSG_REQUESTWATERSOURCES            = 133
    SMSG_REQUESTWATERSOURCES            = 233
    CMSG_SHOP_LIST_ANIMAL               = 134
    SMSG_SHOP_LIST_ANIMAL               = 234
    CMSG_SHOP_LIST_PLANT                = 135
    SMSG_SHOP_LIST_PLANT                = 235
    CMSG_ALL_AVATAR_INFO                = 136
    SMSG_ALL_AVATAR_INFO                = 236
    CMSG_GET_PLAYER_WORLDS              = 137
    SMSG_GET_PLAYER_WORLDS              = 237
    CMSG_PLACE_SPECIES                  = 138
    SMSG_PLACE_SPECIES                  = 238
    CMSG_CHANGE_PARAMETERS              = 141
    SMSG_CHANGE_PARAMETERS              = 241
    CMSG_LEAVE_WORLD                    = 142
    SMSG_LEAVE_WORLD                    = 242
    CMSG_STATISTICS                     = 143
    SMSG_STATISTICS                     = 243
    CMSG_PARAMS                         = 144
    SMSG_PARAMS                         = 244
    CMSG_RESTART                        = 145
    SMSG_RESTART                        = 245
    CMSG_GIVE_SPECIES                   = 146
    SMSG_GIVE_SPECIES                   = 246
    CMSG_CHANGE_FUNCTIONAL_PARAMETERS   = 147
    SMSG_CHANGE_FUNCTIONAL_PARAMETERS   = 247
    CMSG_HIGH_SCORE                     = 148
    SMSG_HIGH_SCORE                     = 248
    CMSG_GET_FUNCTIONAL_PARAMETERS      = 149
    SMSG_GET_FUNCTIONAL_PARAMETERS      = 249
    CMSG_CHART_BIOMASS                  = 150
    SMSG_CHART_BIOMASS                  = 250
    CMSG_DELETE_WORLD                   = 151
    SMSG_DELETE_WORLD                   = 251

    ################################################################
    #CODES FOR RESPONSE CLASSES FROM SERVER (WITHOUT REQUEST)
    ################################################################
    SMSG_BIRTH_ANIMAL                   = 301
    SMSG_BIRTH_PLANT                    = 302
    SMSG_RESPONSE_GET_ENVIRONMENT       = 303
    SMSG_CURE_ANIMAL_DISEASE            = 304
    SMSG_CURE_PLANT_DISEASE             = 305
    SMSG_UPDATE_ANIMAL_BIOMASS          = 306
    SMSG_UPDATE_PLANT_BIOMASS           = 307
    SMSG_UPDATE_ANIMAL_NO_WATER_COUNT   = 308
    SMSG_UPDATE_PLANT_NO_WATER_COUNT    = 309
    SMSG_UPDATE_ANIMAL_ZONE             = 310
    SMSG_UPDATE_ANIMAL_OWNER            = 311
    SMSG_UPDATE_PLANT_NO_LIGHT_COUNT    = 312
    SMSG_KILL_ANIMAL                    = 313
    SMSG_KILL_PLANT                     = 314
    SMSG_UPDATE_WATER_SOURCE            = 315
    SMSG_UPDATE_TIME                    = 316
    SMSG_WEATHER_PREDICTION             = 317
    SMSG_UPDATE_AVG_GAME_SCALE          = 318
    SMSG_UPDATE_XP                      = 319
    SMSG_UPDATE_GOLD                    = 320
    SMSG_UPDATE_ENV_SCORE               = 321
    SMSG_SET_USER_PRIMARY_AVATAR        = 322
    SMSG_REVEAL_ANIMAL_DISEASE          = 323
    SMSG_REVEAL_PLANT_DISEASE           = 324
    SMSG_UPDATE_GAME_SCALE_TIME         = 325
    SMSG_UPDATE_ONLINE_PLAYERS          = 326
    SMSG_UPDATE_LEVEL                   = 327
    SMSG_DRINK_WATER                    = 328
    SMSG_CREATE_ENV                     = 329
    SMSG_TARGET_REWARD                  = 330
    SMSG_SHOP_UNLOCK                    = 331

    ###########################################################

    PENDING_PVP_OBJ                     = 210

    CMSG_SHOP_LIST_ANIMAL_GAMESTATE     = 229
    CMSG_SHOP_LIST_PLANT_GAMESTATE      = 231


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
    LISTENER_CREATE_NEW_GAME_RESPONSE   = "listener_create_new_game_response"
    LISTENER_CREATE_NEW_WORLD_RESPONSE  = "listener_create_new_world_response"
    PENDING_KICK_PLAYER_PVP_LOBBY       = "pending_kick_player_pvp_lobby"

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
    CMSG_WHISPER_CHAT           = 80
    SMSG_WHISPER_CHAT           = 81
    
    
    CHAT_BUTTON_COLOR           =(0, 0, 0, 0.2)
    CHAT_BUTTON_FOCUS           =(1, 1, 1, 0.3)


    ZONE_SIZE = 512
    ENVIRONMENT_SIZE = 512 * 3

    T_NIGHT     = 0
    T_DAWN      = 1
    T_MORNING   = 2
    T_DAY       = 3
    T_EVENING   = 4
    T_DUSK      = 5

    ######################## Event Names ###################################
    WORLD_TYPE   = 300
    WORLD_NAME   = 301
    OWN_AVATARID = 302
    PENDING_WORLD_LOBBY_OBJ     =303

    PARAMETER_K     = 0
    PARAMETER_R     = 1
    PARAMETER_X     = 2
    PARAMETER_X_A   = 3
    PARAMETER_E     = 4
    PARAMETER_D     = 5
    PARAMETER_Q     = 6
    PARAMETER_A     = 7

    ORGANISM_TYPE_ANIMAL    = 0
    ORGANISM_TYPE_PLANT     = 1

    LIFE_STATUS_DEAD    = 0
    LIFE_STATUS_DYING   = 1
    LIFE_STATUS_ALIVE   = 3
