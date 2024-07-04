class AnyType(str):
    """A special type that can be connected to any other types. Credit to pythongosssss"""

    def __ne__(self, __value: object) -> bool:
        return False

any_type = AnyType("*")

# ---------------------------------------------------------------


class color2RGB:
    # @乐皮ai 2024-05-09

    @classmethod
    def INPUT_TYPES(s):  
    
        return {
            "required": {
                "colorDEC": ("STRING", {"forceInput": True}),
            },        
            }

    RETURN_TYPES = (any_type, any_type, any_type,  )
    RETURN_NAMES = ("R", "G", "B",  )    
    FUNCTION = "split"

    CATEGORY = "MiniTools"

    def split(self, colorDEC):


        tulpeSn = list(colorDEC)
        strings = [part for part in tulpeSn[:3]]
        R, G, B, = strings + [""] * (3 - len(strings))          

        return (R, G, B, )





