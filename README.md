# comfyui-minitools
comfyui小工具集，避免节点冗余，看有没时间持续更新吧~
alltools中均为独立节点，可按需下载安装。

安装方法：

方案一、下载allTools目录中的文件到comfyui/custom_nodes/，重启comfyui即可，推荐；

方案二、git clone命令克隆本项目，即可完成所有节点的安装，不太推荐。

1、color2rgb 用于配合[comfyui layer style](https://github.com/chflame163/ComfyUI_LayerStyle)中颜色选择器节点，转换成RGB，且分别输出R、G、B值
![image](https://github.com/vxinhao/comfyui-minitools/assets/50534209/87b18e32-b7f8-4c5a-a4d5-f8166943e68e)

2、promptsTranslateEN 提示词翻译节点，将输入的内容转换成英文，用的百度翻译api，所以需要实现准备好appid（可在百度翻译官方免费申请）
节点演示：
![image](https://github.com/vxinhao/comfyui-minitool/assets/50534209/d3f08259-a2ef-4b0b-85df-fb5ef9f32e01)
