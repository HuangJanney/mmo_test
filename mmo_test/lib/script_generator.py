from lib.ai_model import predict_ui_action
from lib.airtest_base import *

# 根据AI预测结果生成Airtest脚本
def generate_airtest_script(image_paths):
    airtest_commands = []
    for image_path in image_paths:
        action = predict_ui_action(image_path)
        if action == 0:  # 假设0对应于点击操作
            airtest_commands.append(f'touch(Template(r"{image_path}"))')
        elif action == 1:  # 假设1对应于输入文本操作
            airtest_commands.append(f'text("your_text")')
        # 添加更多动作...

    return airtest_commands

# 将生成的指令写入Airtest脚本文件
def write_script_to_file(script, output_file):
    with open(output_file, 'w') as f:
        f.write("\n".join(script))

if __name__ == "__main__":
    image_paths = ['images/login_button.png', 'images/submit_button.png']
    script = generate_airtest_script(image_paths)
    write_script_to_file(script, 'tests/generated_script.air')
