import json
import requests
import pytest


#企业标签库接口测试
from service.tag import Tag

class TestTag():

    def setup_class(self):
        # 初始化Tag
        self.tag = Tag()
        # 拿到token
        self.tag.get_token()

    def test_tag_list(self):
        # 获取新列表 进行校验
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

    #参数化
    @pytest.mark.parametrize("group_name,tag_names",[
        ["group_demo_leemandy2",[{'name': 'tag_demo_leemandy2'}]],
        ["group_demo_leemandy2",[{'name': 'tag_demo_leemandy2'}]],
        ["group_demo_leemandy2",[{'name': 'tag_demo_leemandy2'},{'name': 'tag_demo_leemandy3'}]],

    ])
    def test_tag_add(self,group_name,tag_names):
        #增加标签组
        r= self.tag.add(group_name, tag_names)
        assert r.status_code == 200

        #python列表表达式
        #校验 找taggroup下面有没有新建的groupname
        group=[group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        #校验 找taggroup下tag下的name是不是我刚刚新建的
        tags=[{'name':tag['name']} for tag in group['tag'] if tag['name']]
        print(group)
        print(tags)
        assert group['group_name'] == group_name
        assert tags == tag_names


    #tagname超过31个字符回会报错
    def test_tag_fail(self):
        pass

    @pytest.mark.parametrize("",[
        #删除单个标签
        #删除多个标签
        #删除不存在的标签
        #删除标签组
    ]

    )
    def test_tag_delete(self,group_id,tag_id):
        self.tag.delete()
