from . import promptsTranslateEN, color2rgb


# 菜单名
NODE_CLASS_MAPPINGS = {
    "LP-TranslateToEN": promptsTranslateEN.translatetoen,
    "LP-color2RGB"    : color2rgb.color2RGB
}
 

NODE_DISPLAY_NAME_MAPPINGS = {
    "LP-TranslateToEN": "Tranlate to English 👻",
    "LP-color2RGB"    : "Color to RGB 👻"
}


