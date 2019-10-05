from pyecharts import Map
from pyecharts.engine import create_default_environment
 
 
value = [155, 10, 66, 78, 33, 80, 190, 53, 49.6]
attr = [
    "福建", "山东", "北京", "上海", "甘肃", "新疆", "河南", "广西", "西藏"
    ]
#map = Map("name_map -> dict定义地图名称", width=1200, height=600)
map = Map("Map 结合 VisualMap 示例", width=1200, height=600)
map.add(
    "",     #name -> str图例名称
    attr,    #attr -> list属性名称
    value,    #value -> list属性所对应的值
    maptype="china",    #maptype -> str   地图类型。 从 v0.3.2+ 起，地图已经变为扩展包，支持全国省份，全国城市，全国区县，全球国家等地图 
    is_label_show=True,   #显示各区域名称
    #is_map_symbol_show=True,   #is_map_symbol_show -> bool  是否显示地图标记红点，默认为 True。
    is_map_symbol_show=False,    #设置 is_map_symbol_show=False 取消显示标记红点
    #is_roam -> bool/str 是否开启鼠标缩放和平移漫游。默认为 True 如果只想要开启缩放或者平移，可以设置成'scale'或者'move'。设置成 True 为都开启
    is_roam=True,
    #Visualmap 使用
    is_visualmap=True,
    visual_text_color="#000",
    
    #Note： 可以按右边的下载按钮将图片下载到本地，如果想要提供更多实用工具按钮，请在 add() 中设置 is_more_utils 为 True
    #is_more_utils=True
)
#map.render()#输出默认       render.html
map.render(path='./Map 结合 VisualMap 示例.html')
