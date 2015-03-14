#@PydevCodeAnalysisIgnore
import os
import sys

from panda3d.core import BitMask32
from panda3d.core import DynamicTextFont
from panda3d.core import Vec4

class Constants:

    CLIENT_VERSION = '1.00'
    BLACK = Vec4(0,0,0,0)
    WHITE = Vec4(1,1,1,0)
    HIGHLIGHT = Vec4(0,1,1,1)
    SERVER_IP = 'smurf.sfsu.edu'
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

    MSG_NONE                    = 0
    CMSG_AUTH                           = 1
    CMSG_REGISTER                       = 3
    CMSG_SEARCH_PRIVATE_GAMES           = 5
    CMSG_CURRENT_GAMES                  = 7
    CMSG_JOIN_PVE_WORLD                 = 9
    CMSG_JOIN_PVP_WORLD                 = 11
    CMSG_CREATE_NEW_PRIVATE_PVE_WORLD   = 13
    CMSG_CREATE_NEW_PRIVATE_PVP_WORLD   = 15
    CMSG_CREATE_NEW_PUBLIC_PVE_WORLD    = 17
    CMSG_CREATE_NEW_PUBLIC_PVP_WORLD    = 19
    CMSG_PASSWORD_PRIVATE_WORLD         = 21
    CMSG_START_GAME                     = 23
    CMSG_PVE_MODE_CHAT                  = 25
    CMSG_PVP_MODE_CHAT                  = 27
    CMSG_UNIVERSAL_CHAT                 = 29
    CMSG_WHISPERING_CHAT                = 31
    CMSG_WORLD_CHAT                     = 35
    CMSG_ADD_ANIMAL                     = 37
    CMSG_ADD_PLANT                      = 39
    CMSG_ANIMAL_INFO                    = 41
    CMSG_MOVE_ANIMAL                    = 43
    CMSG_RESEARCH_DISEASES              = 45
    CMSG_RESEARCH_WEATHER               = 47
    CMSG_SAVE_EXIT_GAME                 = 49
    CMSG_KICK_PLAYER_OUT                = 51
    CMSG_ACCEPT_ANIMAL                  = 53
    CMSG_VOTE_GAME_SCALE                = 55

    SMSG_AUTH                           = 2
    SMSG_REGISTER                       = 4
    SMSG_SEARCH_PRIVATE_GAMES           = 6
    SMSG_CURRENT_GAMES                  = 8
    SMSG_JOIN_PVE_WORLD                 = 10
    SMSG_JOIN_PVP_WORLD                 = 12
    SMSG_CREATE_NEW_PRIVATE_PVE_WORLD   = 14
    SMSG_CREATE_NEW_PRIVATE_PVP_WORLD   = 16
    SMSG_CREATE_NEW_PUBLIC_PVE_WORLD    = 18
    SMSG_CREATE_NEW_PUBLIC_PVP_WORLD    = 20
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

#    CMSG_AUTH                   = 1
#    SMSG_AUTH_RESPONSE          = 2
#    CMSG_MSG                    = 3
#    SMSG_MSG                    = 4
#    CMSG_DISCONNECT             = 5
#    SMSG_DISCONNECT             = 6
#    CMSG_MOVE                   = 7
#    SMSG_MOVE                   = 8
#    SMSG_REMOVE_USER            = 9
#    SMSG_CREATE                 = 10
#
#    CMSG_HEARTBEAT              = 12
#
#    CMSG_GLOBAL_CHAT            = 14
#    SMSG_GLOBAL_CHAT            = 15
#    CMSG_PRIVATE_CHAT           = 16
#    SMSG_PRIVATE_CHAT           = 17
#    CMSG_ITEM_USE               = 18
#    SMSG_ITEM_USE               = 19
#    CMSG_EQUIPMENTS             = 20
#    SMSG_EQUIPMENTS             = 21
#
#    SMSG_EQUIPMENT_ADD          = 23
#    CMSG_EQUIPMENT_REMOVE       = 24
#    SMSG_EQUIPMENT_REMOVE       = 25
#
#    SMSG_ITEM_EFFECT            = 27
#    CMSG_NPC_TALK               = 28
#    SMSG_NPC_TALK               = 29
#    CMSG_NPC_BUY                = 30
#    SMSG_NPC_BUY                = 31
#    CMSG_NPC_SELL               = 32
#    SMSG_NPC_SELL               = 33
#    CMSG_ANSWER                 = 34
#    SMSG_ANSWER                 = 35
#    CMSG_HOTKEYS                = 36
#    SMSG_HOTKEYS                = 37
#    CMSG_HOTKEY_ADD             = 38
#    SMSG_HOTKEY_ADD             = 39
#    CMSG_HOTKEY_REMOVE          = 40
#    SMSG_HOTKEY_REMOVE          = 41
#    CMSG_HOTKEY_SET             = 42
#    SMSG_HOTKEY_SET             = 43
#    CMSG_REGISTER               = 44
#    SMSG_REGISTER               = 45
#    CMSG_BUGS                   = 46
#    SMSG_SPAWN_BUG              = 47
#    CMSG_MAP                    = 48
#
#    SMSG_VIEW_REMOVE            = 51
#
#    SMSG_VIEW_SET               = 53
#    CMSG_MAP_CHANGE             = 54
#    SMSG_MAP_CHANGE             = 55
    
    
#    CMSG_BUDDIES                = 56
#    SMSG_BUDDIES                = 57
#    CMSG_BUDDY_ADD              = 58
#    SMSG_BUDDY_ADD              = 59
#    CMSG_BUDDY_ACCEPT           = 60
#    SMSG_BUDDY_ACCEPT           = 61
#    CMSG_BUDDY_REMOVE           = 62
#    SMSG_BUDDY_REMOVE           = 63
#    CMSG_ANIMATION              = 64
#    SMSG_ANIMATION              = 65
#    CMSG_PARTY_CHAT             = 66
#    SMSG_PARTY_CHAT             = 67
#    CMSG_PUBLIC_CHAT            = 68
#    SMSG_PUBLIC_CHAT            = 69
#    CMSG_PARTY                  = 70
#    SMSG_PARTY                  = 71
#    CMSG_PARTY_ADD              = 72
#    SMSG_PARTY_ADD              = 73
#    CMSG_PARTY_REMOVE           = 74
#    SMSG_PARTY_REMOVE           = 75
#    CMSG_PARTY_ACCEPT           = 76
#    SMSG_PARTY_ACCEPT           = 77
#    CMSG_PARTY_LEADER           = 78
#    SMSG_PARTY_LEADER           = 79
#    CMSG_PARTY_SHARE            = 80
#    SMSG_PARTY_SHARE            = 81
#
#    SMSG_DEAD                   = 83
#    CMSG_INVENTORY              = 84
#    SMSG_INVENTORY              = 85
#
#    SMSG_INVENTORY_ADD          = 87
#    CMSG_INVENTORY_REMOVE       = 88
#    SMSG_INVENTORY_REMOVE       = 89
#    CMSG_INVENTORY_SET          = 90
#    SMSG_INVENTORY_SET          = 91
#    CMSG_REGISTER_BUG           = 92
#
#    SMSG_CREATE_BUG             = 95
#
#    SMSG_QUESTION               = 97
#    CMSG_BATTLE_ADD             = 98
#    SMSG_BATTLE_ADD             = 99
#    CMSG_BATTLE_END             = 100
#
#    CMSG_ATTACK                 = 102
#    SMSG_ATTACK                 = 103
#
#    SMSG_BATTLE_REMOVE          = 105
#    CMSG_JUMP                   = 106
#    SMSG_JUMP                   = 107
#
#    SMSG_MONEY                  = 109
#
#    SMSG_CREATE_NPC             = 111
#    CMSG_RESPAWN                = 112
#    SMSG_RESPAWN                = 113
#
#    SMSG_PARTY_UPDATE           = 115
#
#    SMSG_PARTY_ONLINE           = 117
#    CMSG_PARTY_DESTROY          = 118
#    SMSG_PARTY_DESTROY          = 119
#    CMSG_BATTLE_START           = 120
#    SMSG_BATTLE_START           = 121
#    CMSG_BATTLE_SET             = 122
#    SMSG_BATTLE_SET             = 123
#
#    SMSG_ELIMINATE_CHOICES      = 125
#
#    SMSG_ATTRIBUTE_UPDATE       = 127
#    CMSG_BOARD_DICE             = 128
#    SMSG_BOARD_DICE             = 129
#
#    SMSG_MODE_START             = 131
#    CMSG_MODE_END               = 132
#    SMSG_MODE_END               = 133
#
#    SMSG_BOARD_MOVE             = 135
#
#    SMSG_BOARD_PLAYER_TURN      = 137
#    CMSG_BOARD_ANSWER           = 138
#    SMSG_BOARD_ANSWER           = 139
#    CMSG_BOARD_QUESTION         = 140
#    SMSG_BOARD_QUESTION         = 141
#    CMSG_MODE_READY             = 142
#    SMSG_MODE_READY             = 143
#
#    SMSG_BOARD_TIME             = 145
#
#    SMSG_BOARD                  = 147
#
#    SMSG_BOARD_WINNER           = 149
#
#    SMSG_EXPERIENCE             = 151
#
#    SMSG_LEVEL                  = 153
#
#    SMSG_BOARD_END_TURN         = 155
#
#    SMSG_BUDDY_ONLINE           = 157
#
#    SMSG_SURVIVAL_MODE          = 159
#
#    SMSG_SURVIVAL_TIME          = 161
#
#    SMSG_CREATE_MAP             = 163
#
#    SMSG_REMOVE_MAP             = 165
#    CMSG_MODE_LEAVE             = 166
#    SMSG_MODE_LEAVE             = 167
#
#    SMSG_SURVIVAL_WAVE          = 169
#    CMSG_BOARD_MOVE_SET         = 170
#
#    SMSG_BOARD_LOCATION         = 173
#    CMSG_TRADE                  = 174
#    SMSG_TRADE                  = 175
#    CMSG_TRADE_ACCEPT           = 176
#    SMSG_TRADE_ACCEPT           = 177
#    CMSG_TRADE_CONFIRM          = 178
#    SMSG_TRADE_CONFIRM          = 179
#    CMSG_TRADE_SET              = 180
#    SMSG_TRADE_SET              = 181
#    CMSG_TRADE_REMOVE           = 182
#    SMSG_TRADE_REMOVE           = 183
#    CMSG_QUESTION_COMMENT       = 184
#    SMSG_QUESTION_COMMENT       = 185
#
#    SMSG_QUESTION_RATIO         = 187
#    CMSG_DUEL                   = 188
#    SMSG_DUEL                   = 189
#    CMSG_DUEL_ACCEPT            = 190
#    SMSG_DUEL_ACCEPT            = 191
#
#    SMSG_DUEL_START             = 193
#
#    SMSG_DUEL_END               = 195
#    CMSG_DUEL_TOPICS            = 196
#    SMSG_DUEL_TOPICS            = 197
#    CMSG_DUEL_ANSWER            = 198
#    SMSG_DUEL_ANSWER            = 199
#    CMSG_TARGET_SET             = 200
#    SMSG_TARGET_SET             = 201
#    CMSG_TARGET_REMOVE          = 202
#    SMSG_TARGET_REMOVE          = 203
#
#    SMSG_UPDATE_HEALTH          = 205
#
#    SMSG_QUESTION_LOG           = 207
#
#    SMSG_HEALTH                 = 209
#
#    SMSG_BATTLE_TIME            = 211
#
#    SMSG_QUESTION_HINT          = 213
#
#    SMSG_UPDATE_ATTACK_POWER    = 215
#
#    SMSG_UPDATE_DEFENSE         = 217
#
#    SMSG_UPDATE_POSITION        = 219
#
#    SMSG_CODE_GAME              = 221
#
#    SMSG_CODE_QUESTION          = 223
#    CMSG_CODE_CHECK             = 224
#    SMSG_CODE_CHECK             = 225
#    CMSG_LEADERBOARD_FETCH      = 226
#    SMSG_LEADERBOARD_FETCH      = 227
#    CMSG_LEADERBOARD_PLAYER     = 228
#    SMSG_LEADERBOARD_PLAYER     = 229
#
#    SMSG_TOP_DOWN               = 231
#
#    SMSG_TOP_DOWN_CREATE        = 233
#    CMSG_TOP_DOWN_MOVE          = 234
#    SMSG_TOP_DOWN_MOVE          = 235
#    CMSG_TOP_DOWN_SET           = 236
#    SMSG_TOP_DOWN_SET           = 237
#
#    SMSG_TOP_DOWN_QUESTION      = 239
#
#    SMSG_TOP_DOWN_COMPLETE      = 241
#
#    SMSG_TOP_DOWN_CLEAR         = 243
#
#    SMSG_VARIABLES              = 245
#
#    SMSG_VAR_GAME_QUESTION      = 247
#
#    SMSG_VAR_GAME_INSTR_SET     = 249
#
#    SMSG_VAR_GAME_LEVEL         = 251
#
#    CMSG_VAR_GAME_SET           = 252
#    SMSG_VAR_GAME_SET           = 253
#
#    SMSG_VAR_GAME_COMPLETE      = 255
#
#    SMSG_VAR_GAME_CLEAR         = 257
#
#    SMSG_VAR_GAME_END           = 259
#
#    SMSG_VAR_GAME_REMOVE        = 261
#
#    SMSG_VAR_GAME_POINTS        = 263
#    
#    SMSG_LOBBY                  = 265
#
#    CMSG_LOBBY_JOIN             = 266
#    SMSG_LOBBY_JOIN             = 267
#    CMSG_LOBBY_LEAVE            = 268
#    SMSG_LOBBY_LEAVE            = 269
#
#    SMSG_LOBBY_CLOSE            = 271
#
#    SMSG_LOBBY_START            = 273
#
#    SMSG_LOBBY_CANCEL           = 275
#    CMSG_LOBBY_FETCH            = 276
#    SMSG_LOBBY_FETCH            = 277
#    CMSG_VAR_GAME_VALUE_SET     = 278
#    SMSG_VAR_GAME_VALUE_SET     = 279
#
#    SMSG_VAR_GAME_TURN          = 281
#
#    SMSG_TOP_DOWN_POINTS        = 283

#    SMSG_TOP_DOWN_LEVEL         = 285
#    CMSG_GAME_INFO              = 286
#    SMSG_GAME_INFO              = 287
#    CMSG_DOWNLOAD               = 288
#    SMSG_DOWNLOAD               = 289

    ITEM_HEAL                   = 1
    ITEM_HEAL_P                 = 2
    ITEM_MAX_HEALTH             = 3
    ITEM_MAX_HEALTH_P           = 4
    ITEM_MOVE_SPEED             = 5
    ITEM_MOVE_SPEED_P           = 6
    ITEM_DEFENSE                = 7
    ITEM_DEFENSE_P              = 8
    ITEM_MONEY                  = 9
    ITEM_MONEY_P                = 10
    ITEM_EXPERIENCE             = 11
    ITEM_EXPERIENCE_P           = 12
    ITEM_RETURN                 = 13
    ITEM_ELIMINATE_CHOICES      = 14
    ITEM_RANDOM_ITEM            = 15
    ITEM_ATTACK_TIME            = 16
    ITEM_HINT                   = 17

    ATTRIBUTE_HEALTH            = 1
    ATTRIBUTE_MAX_HEALTH        = 2
    ATTRIBUTE_MOVE_SPEED        = 3
    ATTRIBUTE_DEFENSE           = 4
    ATTRIBUTE_ATTACK_MIN        = 5
    ATTRIBUTE_ATTACK_MAX        = 6
    ATTRIBUTE_ATTACK_DELAY      = 7
    ATTRIBUTE_ATTACK_RANGE      = 8
    ATTRIBUTE_SCALE             = 9
    ATTRIBUTE_LEVEL             = 10
    ATTRIBUTE_EXPERIENCE        = 11
    ATTRIBUTE_MONEY             = 12

    BOARD_NONE                  = 0
    BOARD_NORTH                 = 1
    BOARD_EAST                  = 2
    BOARD_SOUTH                 = 3
    BOARD_WEST                  = 4

    BOARD_START                 = 0
    BOARD_END                   = 1
    BOARD_REGULAR               = 2
    BOARD_BONUS                 = 3
    BOARD_BLACKHOLE             = 4
    BOARD_GOLD                  = 5

    BOARD_MODE_REGULAR          = 0
    BOARD_MODE_RACE             = 1

    G_MODE_BOARD                = 1
    G_MODE_SURVIVAL             = 2
    G_MODE_CODING               = 3
    G_MODE_TOP_DOWN             = 4
    G_MODE_VARIABLES            = 5

    G_TYPE_BOARD_VERSUS         = 0
    G_TYPE_SURVIVAL_SOLO        = 0
    G_TYPE_SURVIVAL_COOP        = 1
    G_TYPE_CODING_SOLO          = 0
    G_TYPE_CODING_COOP          = 1
    G_TYPE_CODING_VERSUS        = 2
    G_TYPE_TOP_DOWN_SOLO        = 0
    G_TYPE_TOP_DOWN_COOP        = 1
    G_TYPE_TOP_DOWN_VERSUS      = 2
    G_TYPE_VARIABLES_SOLO       = 0
    G_TYPE_VARIABLES_COOP       = 1
    G_TYPE_VARIABLES_VERSUS     = 2
############## Chat related constants#####################

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