# Constants

XPATH_OF_BUTTONS = ["//button[contains(.,\'Оставить только гласные\')]",
                     "//button[contains(.,\'Ну и ещё пробелы\')]",
                     "//button[contains(.,\'Оставить ещё и .,-!?\')]",
                    ]

XPATH_OF_BUTTONS_FROM_RIGHT_TO_LEFT = ["//button[contains(.,\'Оставить ещё и .,-!?\')]",
                                        "//button[contains(.,\'Ну и ещё пробелы\')]",
                                        "//button[contains(.,\'Оставить только гласные\')]",
                                        ]

# XPATH_OF_BUTTONS_FROM_RIGHT_TO_LEFT = ["//button[contains(.,\'Оставить ещё и .,-!?\')]",
#                                         "//button[contains(.,\'Ну и ещё пробелы\')]",
#                                         "//button[contains(.,\'Оставить только гласные\')]",
#                                         ]

INPUT_TEXT = [("Сменялись в детстве радугой дожди,\n"
               "Сияньем солнца — сумрачные тени.\n"
               "Но в зрелости не требуй и не жди\n"
               "Таких простых и скорых утешений.\n\n"
               "Самуил Яковлевич Маршак"),
              "рандом: оююВФЫВфбь лоюя,ю сфыббо!вф одфыыа,, ,одл;ы",
              "                                                   ",
              ]

OUTPUT_TEXT1 = [("еяиееауоои\n"
                 "ияеоауаыееи\n"
                 "оеоиееуиеи\n"
                 "аиоыиоыуееи\n\n"
                 "ауияоеиаа"),
                ("еяи ее ауо ои\n"
                 "ияе оа уаые еи\n"
                 "о еои е еу и е и\n"
                 "аи оы и оы уееи\n\n"
                 "ауи яоеи аа"),
                ("еяи ее ауо ои,\n"
                 "ияе оа уаые еи.\n"
                 "о еои е еу и е и\n"
                 "аи оы и оы уееи.\n\n"
                 "ауи яоеи аа"),
                ]

OUTPUT_TEXT2 = ["аооююыоюяюыооыыаоы",
                "ао оююы оюяю ыо оыыа оы",
                "ао оююы оюя,ю ыо! оыыа,, ,оы",
                ]

OUTPUT_TEXT3 = ["",
                "",
                "",
                ]

OUTPUT_TEXT = [OUTPUT_TEXT1, OUTPUT_TEXT2, OUTPUT_TEXT3]
