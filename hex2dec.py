class AnyType(str):
    """A special type that can be connected to any other types. Credit to pythongosssss"""

    def __ne__(self, __value: object) -> bool:
        return False

any_type = AnyType("*")

# ---------------------------------------------------------------


class hex2dec:
    # @乐皮ai 2024-09-10

    @classmethod
    def INPUT_TYPES(s):  
    
        return {
            "required": {
                "colorhex": ("STRING", {"forceInput": True}),
            },        
            }

    RETURN_TYPES = (any_type,  )
    RETURN_NAMES = ("decimal_value",  )    
    FUNCTION = "convertcolor"

    CATEGORY = "MiniTools"
    

    def convertcolor(self, colorhex):

        if isinstance(colorhex, tuple):  

            # (255,2,1) 转换成十进制
            tulpeSn = list(colorhex)
            strings = [part for part in tulpeSn[:3]]
            R, G, B, = strings + [""] * (3 - len(strings))
            decimal_value = (R * 256**2) + (G * 256) + B    
            print(decimal_value,)         

        else: 
            # 如果传的是16进制，如#fff000
            hex_color_hash = colorhex.lstrip('#')
            decimal_value = int(hex_color_hash, 16)


        return (decimal_value,)
            


