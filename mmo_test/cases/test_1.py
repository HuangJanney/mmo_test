# -*- encoding=utf8 -*-
__author__ = "Janney"

from airtest.core.api import *

auto_setup(__file__)

# 启动应用
start_app("your.app.package.name")

# 点击登录按钮
touch(Template(r"images/login_button.png"))

# 输入用户名
text("your_username")

# 点击提交按钮
touch(Template(r"images/submit_button.png"))

# 断言：检查是否进入主页
assert_exists(Template(r"images/home_screen.png"), "Home screen not found")
