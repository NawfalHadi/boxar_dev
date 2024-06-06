class Config:
    # Window settings
    WINDOW_SIZE = (800, 600)
    WINDOW_TITLE = "Training and Match Game"

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (128, 128, 128)  # Add more colors as needed

    # Button settings
    BUTTON_FONT_SIZE = 36
    BUTTON_TEXT_COLOR = BLACK
    BUTTON_NORMAL_COLOR = GREY
    BUTTON_HOVER_COLOR = BLACK

    MENUS = {
        "tutorial": {"pos": (50, 50), "size": (200, 50), "label": "Tutorial"},
        "shadow_box": {"pos": (50, 120), "size": (200, 50), "label": "Shadow Box"},
        "pad_works": {"pos": (50, 190), "size": (200, 50), "label": "Pad Works"},
        "play_vs_bot": {"pos": (50, 260), "size": (200, 50), "label": "Play vs Bot"}
    }

    FOOTER_SIZE = 100

    