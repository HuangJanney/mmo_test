from lib.ai_model import predict_ui_action
from lib.airtest_integration import start_app, touch, text, exists
import os

def generate_airtest_script(image_paths, output_file):
    airtest_commands = []
    
    # 添加初始化部分
    airtest_commands.append("start_app('your.app.package.name')")

    for image_path in image_paths:
        action = predict_ui_action(image_path)
        if action == 0:  # 假设0对应点击操作
            airtest_commands.append(f'touch(Template(r"{image_path}"))')
        elif action == 1:  # 假设1对应输入文本操作
            airtest_commands.append(f'text("your_text")')
        elif action == 2:  # 假设2对应滑动操作
            airtest_commands.append(f'swipe(Template(r"{image_path}"), vector(0, 0.5))')
        # 添加更多操作...

    # 添加断言部分
    airtest_commands.append('assert_exists(Template(r"images/home_screen.png"), "Home screen not found")')

    # 将生成的指令写入Airtest脚本文件
    with open(output_file, 'w') as f:
        f.write("\n".join(airtest_commands))

if __name__ == "__main__":
    image_paths = ['images/login_button.png', 'images/submit_button.png']
    generate_airtest_script(image_paths, 'tests/generated_script.air')
