import random

# 中文数字映射
chinese_numbers = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']


# 生成对称且带有一个不同字符的矩阵
def generate_matrix(rows=9, cols=9):
    base_char = '辏'
    special_char = '鞅'
    matrix = [[base_char] * cols for _ in range(rows)]
    # 确保矩阵对称
    for i in range(rows):
        for j in range(i, cols):
            matrix[j][i] = matrix[i][j]
    # 随机选择一个位置放置不同字符
    diff_row = random.randint(0, rows - 1)
    diff_col = random.randint(0, cols - 1)
    matrix[diff_row][diff_col] = special_char
    # 保持对称
    matrix[diff_col][diff_row] = special_char
    return matrix


# 打印矩阵，使用中文数字表示行号和列号
def print_matrix(matrix):
    col_num = len(matrix[0])
    # 打印列数头部
    col_header = " " + "  ".join([chinese_numbers[i + 1] for i in range(col_num)])
    print(f"{chinese_numbers[0]} |{col_header}")
    # 打印分隔线
    print("  " + "——" * (len(col_header)))
    for i, row in enumerate(matrix, start=1):
        row_str = "  ".join(row)
        print(f"{chinese_numbers[i]} | {row_str}")


# 主游戏函数
def play_game():
    matrix = generate_matrix()
    print("矩阵:")
    print_matrix(matrix)

    while True:
        try:
            row_input = input("请输入不同字符所在的行（如 一），输入 '退出' 结束游戏: ")
            if row_input == '退出':
                print("游戏结束。")
                break
            col_input = input("请输入不同字符所在的列（如 一）: ")

            row_answer = chinese_numbers.index(row_input) - 1
            col_answer = chinese_numbers.index(col_input) - 1

            # 找出实际不同字符的位置
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if matrix[i][j] != '辏':
                        correct_row = i
                        correct_col = j
                        break

            if row_answer == correct_row and col_answer == correct_col:
                print("恭喜你，回答正确！")
                break
            else:
                print("回答错误，请再试一次。")
        except ValueError:
            print("输入无效，请输入正确的中文数字或 '退出'。")


if __name__ == "__main__":
    play_game()


