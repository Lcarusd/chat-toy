from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# 初始化聊天机器人
momo = ChatBot(
    'Momo',
    storage_adapter='chatterbot.storage.MongoDatabaseAdapter',  # 使用mongo存储数据
    logic_adapters=[  # 指定逻辑处理模块
        "chatterbot.logic.BestMatch",
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",
    ],
    input_adapter='chatterbot.input.VariableInputTypeAdapter',
    output_adapter='chatterbot.output.OutputAdapter',
    database='chatterbot',  # 指定数据库
    read_only=True
)


# 读取.conv 数据文件，因为我服务器配置较低，所以选择了一个内容较少的文件
# 这个函数是一个生成器
def read_conv(filename='./data/dgk_lost_conv/results/prisonb.conv'):
    with open(filename, 'rt') as f:
        conv = []
        # 逐行读取
        for line in f:
            _line = line.replace('\n', '').strip()  # 预处理字符串 去掉首位空格
            if _line == 'E':  # 如果是分隔符 表示对话结束 返回对话列表
                yield conv
                conv = []  # 重置对话列表
            else:  # 不是分隔符则将内容加入对话列表
                c = _line.split()[-1]  # 其实这里如果对话中包含空格 对话数据会不完整，应该只去掉M和开头的空格
                conv.append(c)


def traine_momo():
    for conv in read_conv():
        print(conv)
        momo.set_trainer(ListTrainer)  # 指定训练方式
        momo.train(conv)  # 训练数据


def main():
    traine_momo()


if __name__ == '__main__':
    main()
