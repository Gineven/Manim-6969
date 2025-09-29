from  manim import *
import numpy as np
from manim.utils.rate_functions import smooth, there_and_back
from colour import Color

class matrix_mtex:
    #输入数字list，返回mathtex矩阵
    def __init__(self,m,n,list):
        self.m = m
        self.n = n
        self.list = list
        self.mtex_matrix1 = self.create_matrix()

        # 添加黑色背景
        bg_rect = Rectangle(
            width=self.mtex_matrix1.width + 0.1,
            height=self.mtex_matrix1.height + 0.1,
            fill_color=BLACK,
            fill_opacity=0.6,  # 半透明
            stroke_width=0
        )
        self.mtex_matrix = VGroup(bg_rect, self.mtex_matrix1)

    def create_matrix(self):
        if len(self.list) == self.m*self.n:
            #创建矩阵
            matrix_str = r"\begin{bmatrix}"
            for i in range(self.m):
                row = " & ".join([str(self.list[i*self.n+j]) for j in range(self.n)])
                matrix_str += row 
                if i < self.m-1:
                    matrix_str += r" \\ "
            matrix_str += r"\end{bmatrix}"
            matrix = MathTex(matrix_str)
            return matrix
        else:
            raise ValueError("输入的列表长度与矩阵大小不匹配")

    def count_elements(self):
        """
        计算实际渲染的元素数量以及渲染出的行列数。
        :return: (元素数量, 行数, 列数)
        """
        element_count = 2  # 初始化为2，表示左右括号各占一个元素
        for num in self.list:
            if num < 0:
                element_count += 2  # 负数：数字和负号各占一个元素
            else:
                element_count += 1  # 正数：仅数字占一个元素
        return element_count, self.m, self.n
    
    def get_rendered_element_index(self, row, col):
        """
        根据矩阵的行列编号，返回 MathTex 渲染的元素编号。
        :param row: 行索引，从 0 开始
        :param col: 列索引，从 0 开始
        :return: 渲染的元素编号（从 0 开始）
        """
        if 0 <= row < self.m and 0 <= col < self.n:
            index = 1  # 左括号占第一个元素
            for i in range(self.m):
                for j in range(self.n):
                    if i == row and j == col:
                        return index
                    num = self.list[i * self.n + j]
                    index += 2 if num < 0 else 1  # 负数占两个元素（负号+数字），正数占一个元素
            raise ValueError("索引超出范围")
        else:
            raise IndexError("行列索引超出矩阵范围")

    def matrix_set_color(self, row, col, color):
        """
        设置指定位置元素的颜色。
        :param row: 行索引，从 0 开始
        :param col: 列索引，从 0 开始
        :param color: 颜色，可以是字符串或 RGB 元组
        """
        if 0 <= row < self.m and 0 <= col < self.n:
            if self.m < 3:
                index = 1
            else:
                index = 2  # 左括号占第一个元素 # 左括号占前两个元素
            # index = 1
            for i in range(self.m):
                for j in range(self.n):
                    if i == row and j == col:
                        num = self.list[i * self.n + j]
                        self.mtex_matrix1[0][index].set_color(color) if num >= 0 else self.mtex_matrix1[0][index:index+2].set_color(color)
                        return index
                    num = self.list[i * self.n + j]
                    index += 2 if num < 0 else 1  # 负数占两个元素（负号+数字），正数占一个元素
        raise IndexError("行列索引超出矩阵范围")

#带标签的向量元素
class labeled_vector(VGroup):
    def __init__(self, list1, color, scale_factor = 1, **kwargs):
        super().__init__(**kwargs)
        self.list = list1
        self.vector = Vector(self.list, color=color, tip_length=0.23)
        # self.label0 = MathTex(r"\begin{bmatrix}" + "\\\\".join(map(str, self.list)) + r"\end{bmatrix}", color=color).scale(scale_factor)
        label = matrix_mtex(len(self.list), 1, self.list)
        label.matrix_set_color(0, 0, color)
        label.matrix_set_color(1, 0, color)
        self.label = label.mtex_matrix.scale(scale_factor)

        self.label.next_to(self.vector.get_end(), self.label_direction(), buff=0.2)

        # self.add(self.vector, self.label)
        # self.add(self.label, self.vector)

    # 判断标签方向函数
    def label_direction(self):
        if self.list[0] == 0 :
            if self.list[1] > 0:
                return LEFT
            else:
                return RIGHT
        direction = self.list[0]*RIGHT + self.list[1]*UP
        return direction

    def set_color(self, color):
        self.vector.set_color(color)
        self.label.set_color(color)
        return self

# 二维线性变换类
class LinearTransform2D(VGroup):
    def __init__(self, list1, **kwargs):
        super().__init__(**kwargs)
        self.list = list1
        # self.add(self.create_transformed_grid())

        self.vec_i = labeled_vector([1, 0], color=RED)
        self.vec_j = labeled_vector([0, 1], color=GREEN)

        #变换向量
        self.transformed_vec_i = labeled_vector([self.list[0],self.list[2]], color=RED)
        self.transformed_vec_j = labeled_vector([self.list[1], self.list[3]], color=GREEN)

        # self.add(self.vec_i.vector, self.vec_j.vector)
        # self.add(self.vec_i.label, self.vec_j.label)

    # 创建背景网格
    def background_grid(self):
        axes_4d_back = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
            "stroke_opacity": 0.5,
            "stroke_color": GREY
            },
            faded_line_ratio=2,

            axis_config={
            "include_tip": True,

              # 显示箭头
            "include_ticks":True
            }
        )
        x_label = axes_4d_back.get_x_axis_label(MathTex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes_4d_back.get_y_axis_label(MathTex("y").scale(1))
        o_label = Tex("o").next_to(axes_4d_back.c2p(0, 0), DOWN+RIGHT, buff=0.2).scale(1)
        x_label.next_to(axes_4d_back.c2p(6.5,0), DOWN, buff=0.3)
        y_label.next_to(axes_4d_back.c2p(0,3.5), LEFT, buff=0.3)
        grid_group = VGroup(axes_4d_back, x_label, y_label, o_label)
        return grid_group

    # 创建网格
    def create_grids(self):
        grid = NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={"stroke_opacity": 0.8},
            axis_config={"include_tip": False, "stroke_width": 1,"include_ticks": False},
        )
        
        return grid
    
    # 线性变换函数 
    def linear_transform_func2d(self,p):
        return np.array(self.list[0]*p[0]+self.list[1]*p[1],self.list[2]*p[0]+self.list[1])
    
    # def linear_transform(self):

class TestMatrix(Scene):
    def construct(self):
        matrix = matrix_mtex(3, 3, [1, 2, 3, -1, 2, -5, 2, 3, 1])
        # matrix.set_color(1, 2, RED)
        matrix.get_rendered_element_index(1, 2)

        for i in range(3):
            matrix.matrix_set_color(i, 0, RED)
            matrix.matrix_set_color(i, 1, GREEN)
            matrix.matrix_set_color(i, 2, BLUE)

        # self.add(matrix.mtex_matrix[0])
        self.play(Write(matrix.mtex_matrix[1].scale(1.5)),run_time=2)
        self.wait(1)
        self.play(FadeOut(matrix.mtex_matrix))

class LinearTransformExample(Scene):
    def linear_transform(self,list1,start=False):
        linear_transform = LinearTransform2D(list1)
        grid = linear_transform.create_grids()
        grid_copy = grid.copy()

        background = linear_transform.background_grid()
        # Vectors = VGroup(linear_transform.vec_i, linear_transform.vec_j)
        Vectors = VGroup(linear_transform.vec_i.vector, linear_transform.vec_j.vector, linear_transform.vec_i.label, linear_transform.vec_j.label)
        Vectors_copy = Vectors.copy()

        TransformedVectors = VGroup(linear_transform.transformed_vec_i.vector, linear_transform.transformed_vec_j.vector, linear_transform.transformed_vec_i.label, linear_transform.transformed_vec_j.label)
    
        self.add(background)
        if start:
            self.play(FadeIn(grid),run_time=2)
        else:
            self.add(grid)

        self.add(Vectors)
        self.wait(1)

        self.play(
            grid.animate.apply_matrix([[list1[0], list1[1]], [list1[2], list1[3]]]),
            Transform(Vectors, TransformedVectors),
            run_time=3,
        )
        self.wait(2)

        self.play(
            Transform(grid, grid_copy),
            Transform(Vectors, Vectors_copy),
        )
        self.wait(2)

        # 清除元素
        self.play(FadeOut(grid),FadeOut(background),FadeOut(Vectors))

    # 有小黑板的变换
    def linear_transform_matrix_blackboard(self,list1,start=False):
        linear_transform = LinearTransform2D(list1)
        grid = linear_transform.create_grids()
        grid_copy = grid.copy()

        background = linear_transform.background_grid()
        # Vectors = VGroup(linear_transform.vec_i, linear_transform.vec_j)
        Vectors = VGroup(linear_transform.vec_i.vector, linear_transform.vec_j.vector, linear_transform.vec_i.label, linear_transform.vec_j.label)
        Vectors_copy = Vectors.copy()

        TransformedVectors = VGroup(linear_transform.transformed_vec_i.vector, linear_transform.transformed_vec_j.vector, linear_transform.transformed_vec_i.label, linear_transform.transformed_vec_j.label)
    
        self.add(background)
        if start:
            self.play(FadeIn(grid),run_time=2)
        else:
            self.add(grid)

        self.add(Vectors)
        self.wait(1)

        self.play(
            grid.animate.apply_matrix([[list1[0], list1[1]], [list1[2], list1[3]]]),
            Transform(Vectors, TransformedVectors),
            run_time=3,
        )
        self.wait(2)

        # 向量移动到中间小黑板
        matrix = matrix_mtex(2, 2, list1)
        # matrix = matrix0.mtex_matrix
        # matrix.set_color(0, 0, RED)
        for i in range(2):
            matrix.matrix_set_color(i, 0, RED)
            matrix.matrix_set_color(i, 1, GREEN)
        # 中间靠下
        matrix1 = matrix.mtex_matrix.move_to(1.5*DOWN).scale(1.5)
        # self.play(
        #     Write(matrix1)
        # )

        i_position = matrix1[0].get_center()
        j_position = matrix1[0].get_center()

        self.play(
            linear_transform.vec_i.label.animate.move_to(i_position+0.5*LEFT).scale(1.5)
        )

        self.play(
            linear_transform.vec_j.label.animate.move_to(j_position+0.5*RIGHT).scale(1.5)
        )

        leni = len(linear_transform.vec_i.label[1][0])
        lenj = len(linear_transform.vec_j.label[1][0])

        # self.play(
        #     linear_transform.vec_i.label[1][0][0:leni-1].animate.move_to(LEFT).scale(1.5)
        # )

        # self.play(
        #     Transform(VGroup(linear_transform.vec_i.label[1][0][0:leni-1], linear_transform.vec_j.label[1][0][1:lenj]),matrix1[1]),
        # )
        self.play(
            FadeOut(VGroup(linear_transform.vec_i.label[1][0][leni-1], linear_transform.vec_j.label[1][0][0])),
        )

        self.wait(2)

        self.play(
            Transform(grid, grid_copy),
            Transform(Vectors, Vectors_copy),
        )
        self.wait(2)

        # 清除元素
        self.play(FadeOut(grid),FadeOut(background),FadeOut(Vectors))

    def construct(self):
        # 出现网格
        list1 = [1, -2, 2, 1]
        self.linear_transform(list1,start=True)

        list2 = [2, 1, 1, 0]
        self.linear_transform(list2)

        list3 = [1, -1, 2, -2]
        self.linear_transform(list3)
        list1 = [1, -2, 2, 1]
        self.linear_transform_matrix_blackboard(list1)

        list2 = [2, 1, 1, 0]
        self.linear_transform_matrix_blackboard(list2)

        list3 = [1, -1, 2, -2]
        self.linear_transform_matrix_blackboard(list3)

