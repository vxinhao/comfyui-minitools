import requests
import random
from hashlib import md5


# 百度翻译api 免费申请地址：https://api.fanyi.baidu.com/

# ----------需要修改成自己的appid和密钥------------
appid = 'xxxxxx'  # appid

secretKey = 'xxxxx'  # 密钥 
#------------------------------------------------

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


class translatetoen:
    @classmethod
      
    def INPUT_TYPES(s):
    # 定义一个字典并返回
        return {
            # 定义一个名为"required"的字典
            "required": {
                # 定义一个名为"prompt_text"的元组，包含两个元素
                "prompt_text": (
                    # 第一个元素为字符串类型，值为"STRING"
                    "STRING",
                    # 第二个元素为字典类型，包含两个键值对
                    {
                        # 键为"multiline"，值为True，表示支持多行输入
                        "multiline": True,
                        # 键为"default"，值为"杰作，高清画质"，表示默认输入值为"杰作，高清画质"
                        "default": "杰作，高清画质"
                    }
                ),
            }
        }


    
    RETURN_TYPES = ("STRING",)
    FUNCTION = "TranslateFun"
    CATEGORY = "MiniTools"

    def TranslateFun(self,prompt_text,appid=appid,secretkey=secretKey):
        # 百度翻译api
        fanyiser = 'https://api.fanyi.baidu.com'
        apiurl = '/api/trans/vip/translate'
        url = fanyiser + apiurl
        salt = random.randint(32768, 65536)
        sign = make_md5(appid + prompt_text + str(salt) + secretkey)
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'appid': appid, 'q': prompt_text, 'from': 'zh', 'to': 'en', 'salt': salt, 'sign': sign}
        response = requests.post(url, params=payload, headers=headers)
        result = response.json()

        text = result['trans_result'][0]['dst']
        
        return (text,)
    



