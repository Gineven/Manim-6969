from  manim import *
import numpy as np
from manim.utils.rate_functions import smooth, there_and_back
from colour import Color
class Scene3(Scene):
    def construct(self):
        axes =  NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={"stroke_opacity": 0.6},
            axis_config={"include_tip": False, "stroke_width": 0,"include_ticks": False},
        )
        axe_trans = axes.copy()
        axes_4d_back = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
            "stroke_opacity": 0.3,
            "stroke_color": GREY
            },
            axis_config={
            "include_tip": True,

              # 显示箭头
            "include_ticks":True
            }
        )
        x_label = axes.get_x_axis_label(MathTex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes.get_y_axis_label(MathTex("y").scale(1))
        o_label = Tex("o").next_to(axes.c2p(0, 0), DOWN+RIGHT, buff=0.2).scale(1)
        x_label.next_to(axes_4d_back.c2p(6.5,0), DOWN, buff=0.3)
        y_label.next_to(axes_4d_back.c2p(0,3.5), LEFT, buff=0.3)
        self.add( x_label, y_label, o_label,axes_4d_back,axes,)
        self.wait(1)
        #向量万花筒
        l_vector = []
        for i in range(3,-5,-1):
            for j in range(-7,7,1):
                vector = Vector(np.array([j+0.5,i+0.5,0]))
                vector.set_color(Color(hue=(j + 7) / 14 * 0.5 + 0.5, saturation=0.7, luminance=0.6))
                # hue=(j + 7) / 14 * 0.5 + 0.5
                # 计算颜色的色调值，范围在0到1之间
                l_vector.append(vector)

        #与之对应的点阵
        l = []
        for i in range(3,-5,-1):
            for j in range(-7,7,1):
                dot = Dot(np.array([j+0.5,i+0.5,0])).scale(0.6)
                dot.set_color(Color(hue=(j + 7) / 14 * 0.5 + 0.5, saturation=0.7, luminance=0.6))
                # hue=(j + 7) / 14 * 0.5 + 0.5
                # 计算颜色的色调值，范围在0到1之间
                l.append(dot)
        #移动后的点阵
        l1 = []
        for i in range(3,-5,-1):
            for j in range(-7,7,1):
                dot = Dot(np.array([3*(j+0.5)+2*(i+0.5),(j+0.5)+2*(i+0.5),0])).scale(0.8)
                dot.set_color(Color(hue=(j + 7) / 14 * 0.5 + 0.5, saturation=0.7, luminance=0.6))
                # hue=(j + 7) / 14 * 0.5 + 0.5
                # 计算颜色的色调值，范围在0到1之间
                l1.append(dot)    
        #淡入点阵，再变换为向量
        self.play(FadeIn(*l_vector), run_time=1, rate_functions=there_and_back)
        # FadeIn(*l) 会使得所有的点同时淡入
        # run_time=1 表示动画持续时间为 1 秒
        self.wait(1)
        self.play(
            Transform(VGroup(*l_vector), VGroup(*l)),
            run_time=3,
            rate_function=smooth
        )
        self.wait(2)
        
        self.play(
            Transform(VGroup(*l_vector), VGroup(*l1)),
            run_time=3,
            rate_function=smooth
        )
        self.play(FadeOut(*l_vector), run_time=1, rate_functions=there_and_back)
        self.wait(3)
        #生成不同的向量加法
        #唤出小黑板
        equation_1 = MathTex(r"2\begin{bmatrix} 1\\ 0\end{bmatrix} + 1\begin{bmatrix} 0\\ 1\end{bmatrix} = \begin{bmatrix} 2\\ 1\end{bmatrix}",color=WHITE).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.2).scale(0.8)
        rect = Rectangle(
            width=equation_1.width + 0.4,
            height=equation_1.height + 0.4,
            fill_color=BLACK,
            fill_opacity=0,
            stroke_width=0
        ).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.2)
        self.add(rect)
        #设置小黑板透明度

        vector_21 = Vector((2,1,0),color=YELLOW,tip_length=0.2)
        vector_21_label = MathTex(r"\begin{bmatrix}2\\ 1\end{bmatrix}",color=YELLOW).next_to(axes_4d_back.c2p(2, 1), UP+RIGHT, buff=0.2).scale(0.8)
        vector_21.set_stroke(width=3)
        vector_21.set_tip_length(0.01)
        self.play(FadeIn(vector_21,vector_21_label)
                  )
        self.wait(2)
        # self.play(FadeOut(vector_21,vector_21_label))

        vector_i = Vector((1,0,0),color=RED,tip_length=0.2)
        vector_i_label = MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(1, 0), DOWN, buff=0.2).scale(0.8)
        vector_j = Vector((0,1,0),color=GREEN,tip_length=0.2)
        vector_j_label = MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(0, 1), LEFT, buff=0.2).scale(0.8)
        vector_i.set_stroke(width=3)
        vector_j.set_stroke(width=3)
        self.play(FadeIn(vector_i,vector_i_label,vector_j,vector_j_label)
                  ,run_time=2
                  )
        self.wait(2)
        
        vector_2i = Vector((2,0,0),color=RED,tip_length=0.2)
        vector_2i.set_stroke(width=3)

        vector_2i_label = MathTex(r"2\begin{bmatrix} 1\\ 0\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(2, 0), LEFT+DOWN, buff=0.2).scale(0.8)
        self.play(Transform(vector_i,vector_2i),Transform(vector_i_label,vector_2i_label),run_time=2)
        self.wait(1)
        self.play(vector_j.animate.move_to(axes_4d_back.c2p(2,0.5)),
                  vector_j_label.animate.next_to(axes_4d_back.c2p(2, 0.5), RIGHT, buff=0.2).scale(1),
                  run_time=2)
        self.wait(1)
        #组合向量的同时保留标签 #矩阵


        #矩阵计算
        equation_1 = MathTex(r"2\begin{bmatrix} 1\\ 0\end{bmatrix} + 1\begin{bmatrix} 0\\ 1\end{bmatrix} = \begin{bmatrix} 2\\ 1\end{bmatrix}",color=WHITE).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.2).scale(0.8)
        
        self.play(rect.animate.set_opacity(0.8),run_time=2)
        # self.play(Write(equation_1),run_time=2)
        # self.play(FadeOut(*equation_1[0][0:5]))
        self.play(
            # Transform(vector_2i_label, VGroup(*equation_1[0][0:5])),
            vector_i_label.animate.move_to(VGroup(*equation_1[0][0:5]).get_center()),
            Write(equation_1[0][5]),
            run_time=2
        )
        self.wait(1)
        vector_j_label_new = MathTex(r"1\begin{bmatrix} 0\\ 1\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(2,0.5), RIGHT, buff=0.2).scale(0.8)
        self.play(Transform(vector_j_label,vector_j_label_new),run_time=1)
        self.play(
            # Transform(vector_j_label, VGroup(*equation_1[0][6:11])),
            vector_j_label.animate.move_to(VGroup(*equation_1[0][6:11]).get_center()),
            Write(equation_1[0][11]),
            run_time=2
        )
        self.wait(1)
        self.play(
            # Transform(vector_21_label, VGroup(*equation_1[0][12:16])),
            vector_21_label.animate.move_to(VGroup(*equation_1[0][12:16]).get_center()),
            run_time=2
        )
        
        self.wait(2)
