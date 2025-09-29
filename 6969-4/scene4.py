from  manim import *
import numpy as np
from manim.utils.rate_functions import smooth, there_and_back
from colour import Color
class Scene4(Scene):
    def construct(self):
        axes =  NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={"stroke_opacity": 0.9},
            axis_config={"include_tip": False, "stroke_width": 0,"include_ticks": False},
        )
        axe_trans2 = axes.copy()
        axe_practice = axes.copy()
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
        equation_1 = MathTex(r"2\begin{bmatrix} -2\\ 1\end{bmatrix} + 1\begin{bmatrix} 1\\ 1\end{bmatrix} = \begin{bmatrix} -3\\ 3\end{bmatrix}",color=WHITE).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.2).scale(0.8)
        rect = Rectangle(
            width=equation_1.width + 0.4,
            height=equation_1.height + 0.4,
            fill_color=BLACK,
            fill_opacity=0,
            stroke_width=0
        ).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.2)
        self.add(rect)
        
        
       


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
        def transmf2111(p):
            return np.array([ -2*p[0]+1*p[1], 1*p[0]+1*p[1], p[2]])
        #矩阵变换
        vector_i_label_target = MathTex(r"\begin{bmatrix}-2\\ 1\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(-2, 1), LEFT, buff=0.2).scale(0.8)
        vector_j_label_target = MathTex(r"\begin{bmatrix}1\\ 1\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(1, 1), UP+RIGHT, buff=0.05).scale(0.8)
        vector_21_label_target = MathTex(r"\begin{bmatrix}-3\\ 3\end{bmatrix}",color=YELLOW).next_to(axes_4d_back.c2p(-3, 3), RIGHT, buff=0.5).scale(0.8)
        self.play(
            axes.animate.apply_function(transmf2111),
            Transform(vector_i, Vector((-2,1,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((1,1,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_21, Vector((-3,3,0),color=YELLOW,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_i_label, vector_i_label_target),
            Transform(vector_j_label, vector_j_label_target),
            Transform(vector_21_label, vector_21_label_target),
            run_time=2,
            rate_function=smooth
        )
        self.wait(2)

        vector_2i_trans = Vector((-4,2,0),color=RED,tip_length=0.2).set_stroke(width=3)
        vector_2i_trans_label = MathTex(r"2\begin{bmatrix}-2\\ 1\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(-4, 2), DOWN, buff=0.2).scale(0.8)  
        self.play(Transform(vector_i,vector_2i_trans),
                  Transform(vector_i_label, vector_2i_trans_label),
                    run_time=2
                  )
        self.wait(1)
        self.play(vector_j.animate.shift(4*LEFT+2*UP),
                  vector_j_label.animate.next_to(axes_4d_back.c2p(-3, 3), LEFT, buff=0.6).scale(1),
                  run_time=2)
        self.wait(2)
        #组合向量的同时保留标签 #矩阵
        equation_1 = MathTex(r"2\begin{bmatrix} 1\\ 0\end{bmatrix} + 1\begin{bmatrix} 0\\ 1\end{bmatrix} = \begin{bmatrix} 2\\ 1\end{bmatrix}",color=WHITE).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.2).scale(0.8)
        self.play(rect.animate.set_opacity(0.8),run_time=2)

        self.play(
            # Transform(vector_2i_label, VGroup(*equation_1[0][0:5])),
            vector_i_label.animate.move_to(VGroup(*equation_1[0][0:5]).get_center()),
            Write(equation_1[0][5]),
            run_time=2
        )
        self.wait(1)
        vector_j_label_new = MathTex(r"1\begin{bmatrix} 1\\ 1\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(-3,3), LEFT, buff=0.6).scale(0.8)
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
        self.play(
            FadeOut(vector_i, vector_j, vector_21, ),
            FadeOut(axes, axes_4d_back, x_label, y_label, o_label ),
            run_time=2
        )
        self.wait(2)

        group_equation = VGroup(vector_21_label, vector_i_label, vector_j_label, equation_1[0][5], equation_1[0][11])
        self.play(
            group_equation.animate.move_to(ORIGIN).scale(2),
            run_time=2
        )
        self.wait(2)

        matrix_empty = MathTex(r"\begin{bmatrix}  2\\ 1 \end{bmatrix}",color=BLUE).next_to(group_equation, LEFT, buff=1).scale(1.6)
        matrix_empty[0][1].set_opacity(0)
        matrix_empty[0][2].set_opacity(0)
        copy_vector_i_label = vector_i_label[0][0].copy()
        copy_vector_j_label = vector_j_label[0][0].copy()
        self.play(FadeIn(matrix_empty))
        self.play(
            copy_vector_i_label.animate.move_to(matrix_empty[0][1]).set_color(BLUE),
            vector_i_label[0][0].animate.set_color(BLUE),
            copy_vector_j_label.animate.move_to(matrix_empty[0][2]).set_color(BLUE),
            vector_j_label[0][0].animate.set_color(BLUE),
            run_time=2
        )
        self.wait(1)
        arrow_input = Arrow(start=matrix_empty.get_right(), end=group_equation.get_left(), buff=0.2, color=WHITE)
        arrow_output = Arrow(start=vector_j_label.get_right(), end=vector_21_label.get_left(), buff=0.2, color=WHITE)
        self.play(FadeIn(arrow_input), Transform(equation_1[0][11],arrow_output),run_time=2)



        self.wait(1)
        x_matrix_empty_label = MathTex(r"x",color=BLUE).scale(1.6).move_to(matrix_empty[0][1])
        y_matrix_empty_label = MathTex(r"y",color=BLUE).scale(1.6).move_to(matrix_empty[0][2])
        x_matrix_label = MathTex(r"x",color=BLUE).scale(1.6).move_to(vector_i_label[0][0])
        y_matrix_label = MathTex(r"y",color=BLUE).scale(1.6).move_to(vector_j_label[0][0])
        equation_21_label = MathTex(r"\begin{bmatrix} -2x+y\\ x+y \end{bmatrix}",color=YELLOW).next_to(arrow_output, RIGHT, buff=1).scale(1.6)

        self.play(
            Transform(copy_vector_i_label, x_matrix_empty_label),
            Transform(copy_vector_j_label, y_matrix_empty_label),
            Transform(vector_i_label[0][0], x_matrix_label),
            Transform(vector_j_label[0][0], y_matrix_label),
            Transform(vector_21_label, equation_21_label),
            run_time=2
        )

        self.wait(2)
        matrix_f21_11 = MathTex(r"\begin{bmatrix} -2 & 1\\ 1 & 1 \end{bmatrix}",color=WHITE).scale(1.6)
        matrix_f21_11[0][1].set_color(RED)
        matrix_f21_11[0][2].set_color(RED)
        matrix_f21_11[0][3].set_color(GREEN)
        matrix_f21_11[0][4].set_color(RED)
        matrix_f21_11[0][5].set_color(GREEN)

        self.play(
            FadeOut(matrix_empty,arrow_input, arrow_output,copy_vector_i_label, 
                    copy_vector_j_label, equation_1[0][5], equation_1[0][11],vector_21_label,
                    vector_i_label[0][0], vector_j_label[0][0],vector_i_label[0][5],vector_j_label[0][1]),
            run_time = 2,
            rate_functions = smooth 
        )
        self.wait(2)
        self.play(
            Transform(VGroup(*vector_i_label[0][1:5]), VGroup(matrix_f21_11[0][0],matrix_f21_11[0][1],matrix_f21_11[0][2],matrix_f21_11[0][4])),
            Transform(VGroup(*vector_j_label[0][2:5]), VGroup(matrix_f21_11[0][3],matrix_f21_11[0][5],matrix_f21_11[0][6])),
            run_time=2,
            rate_function=smooth
        )
        # self.play(FadeOut(vector_i_label[0][1],vector_i_label[0][2],vector_i_label[0][3],))
        self.wait(2)
        self.play(FadeOut(vector_i_label[0][1],vector_i_label[0][2],vector_i_label[0][3],vector_i_label[0][4],
                          vector_j_label[0][2],vector_j_label[0][3],vector_j_label[0][4],))
        self.wait(2)
        

        # 新的线性变换
        #首先映入坐标系
        #
        #第二次映入坐标系
        #
        #
        #
        self.play(FadeIn(axes_4d_back, x_label, y_label, o_label,axe_trans2), run_time=2)
        self.wait(1)
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
        Matrix_blackboard_2 = MathTex(r" \begin{bmatrix}-2&-1 \\-1&-1\end{bmatrix}",color=WHITE).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.5).scale(0.8)
        rect_blackboard_2 = Rectangle(
            width=Matrix_blackboard_2.width + 0.4,
            height=Matrix_blackboard_2.height + 0.4,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_width=0
        ).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.2)
        #定义了左边和右边的坐标的移动地点
        left_target = VGroup(Matrix_blackboard_2[0][1],Matrix_blackboard_2[0][2],Matrix_blackboard_2[0][5],Matrix_blackboard_2[0][6])
        right_target = VGroup(Matrix_blackboard_2[0][3],Matrix_blackboard_2[0][4],Matrix_blackboard_2[0][7],Matrix_blackboard_2[0][8])
        
        ####
        ###外部框架和黑色背景版一起出现
        framework_target = VGroup(rect_blackboard_2,Matrix_blackboard_2[0][0],Matrix_blackboard_2[0][9])
        
        #先设置了黑色的黑板


        #
        ##
        def trans01_f10(p):
            return np.array([ 0*p[0]-1*p[1], 1*p[0]+0*p[1], p[2]])
        def untrans01_f10(p):
            return np.array([ 0*p[0]+1*p[1], -1*p[0]+0*p[1], p[2]])
        #矩阵变换
        vector_i_label_target = MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(0, 1), LEFT, buff=0.2).scale(0.8)
        vector_j_label_target = MathTex(r"\begin{bmatrix}-1\\ 0\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(-1, 0), 0.4*LEFT+DOWN, buff=0.2).scale(0.8)
        self.play(
            axe_trans2.animate.apply_function(trans01_f10),
            Transform(vector_i, Vector((0,1,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((-1,0,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_i_label, vector_i_label_target),
            Transform(vector_j_label, vector_j_label_target),
            run_time=2,
            rate_function=smooth
        )
        self.wait(2)
        #移动向量到目标地点
        ##考虑整体封装函数？？？
        self.play(
            FadeIn(framework_target),
        )
        group_i = VGroup(vector_i_label[0][1].copy(),vector_i_label[0][2].copy())
        group_j = VGroup(vector_j_label[0][1].copy(),vector_j_label[0][2].copy(),vector_j_label[0][3].copy())
        self.play(
            group_i.animate.move_to(left_target),
        )
        self.play(
            group_j.animate.move_to(right_target),
        )
        self.wait(2)
        self.play(
            FadeOut(framework_target),FadeOut(group_i,group_j),run_time=2
        )
        #移动完成，并设置消失
        #考虑整体封装函数？？？
        #
        #恢复回去
        self.play(
            axe_trans2.animate.apply_function(untrans01_f10),
            Transform(vector_i, Vector((1,0,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((0,1,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_i_label, MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(1, 0), DOWN, buff=0.2).scale(0.8)),
            Transform(vector_j_label, MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(0, 1), LEFT, buff=0.2).scale(0.8)),
            run_time=2,
            rate_function=smooth
        )
        self.wait(2)


        #第二次线性变换
        def trans10_11(p):
            return np.array([ 1*p[0]+1*p[1], 0*p[0]+1*p[1], p[2]])
        def untrans10_11(p):
            return np.array([ p[0]-p[1], p[1], p[2]])
        #矩阵变换
        vector_i_label_target = MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(1, 0), DOWN, buff=0.2).scale(0.8)
        vector_j_label_target = MathTex(r"\begin{bmatrix}1\\ 1\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(1, 1), UP+RIGHT, buff=0.2).scale(0.8)
        self.play(
            axe_trans2.animate.apply_function(trans10_11),
            Transform(vector_i, Vector((1,0,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((1,1,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_i_label, vector_i_label_target),
            Transform(vector_j_label, vector_j_label_target),
            run_time=2,
            rate_function=smooth
        )
        self.wait(2)
        #移动向量到目标地点
        ##考虑整体封装函数？？？
        #考虑整体封装函数？？？
        self.play(
            FadeIn(framework_target),
        )
        group_i = VGroup(vector_i_label[0][1].copy(),vector_i_label[0][2].copy())
        group_j = VGroup(vector_j_label[0][2].copy(),vector_j_label[0][3].copy())
        self.play(
            group_i.animate.move_to(left_target),
        )
        self.play(
            group_j.animate.move_to(right_target),
        )
        self.wait(2)
        self.play(
            FadeOut(framework_target),FadeOut(group_i,group_j),run_time=2
        )
        #移动完成，并设置消失
        #考虑整体封装函数？？？
        #恢复回去
        self.play(
            axe_trans2.animate.apply_function(untrans10_11),
            Transform(vector_i, Vector((1,0,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((0,1,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_i_label, MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(1, 0), DOWN, buff=0.2).scale(0.8)),
            Transform(vector_j_label, MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(0, 1), LEFT, buff=0.2).scale(0.8)),
            run_time=2,
            rate_function=smooth
        )
        self.wait(2)

        #下一组矩阵计算
        def trans31_23(p):
            return np.array([ 3*p[0]+2*p[1], 1*p[0]+3*p[1], p[2]])
        def untrans31_23(p):
            return np.array([ 3/7*p[0]-2/7*p[1], -1/7*p[0]+3/7*p[1], p[2]])
        #矩阵变换
        vector_i_label_target = MathTex(r"\begin{bmatrix}3\\ 1\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(3, 1), UP+RIGHT, buff=0.2).scale(0.8)
        vector_j_label_target = MathTex(r"\begin{bmatrix}2\\ 3\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(2, 3), LEFT, buff=0.4).scale(0.8)
        self.play(
            axe_trans2.animate.apply_function(trans31_23),
            Transform(vector_i, Vector((3,1,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((2,3,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_i_label, vector_i_label_target),
            Transform(vector_j_label, vector_j_label_target),
            run_time=2,
            rate_function=smooth
        )
        self.wait(2)
        #移动向量到目标地点
        ##考虑整体封装函数？？？
        #考虑整体封装函数？？？
        self.play(
            FadeIn(framework_target),
        )
        group_i = VGroup(vector_i_label[0][1].copy(),vector_i_label[0][2].copy())
        group_j = VGroup(vector_j_label[0][2].copy(),vector_j_label[0][3].copy())
        self.play(
            group_i.animate.move_to(left_target),
        )
        self.play(
            group_j.animate.move_to(right_target),
        )
        self.wait(2)
        self.play(
            FadeOut(framework_target),FadeOut(group_i,group_j),run_time=2
        )
        #移动完成，并设置消失
        #考虑整体封装函数？？？
        #恢复回去
        self.play(
            axe_trans2.animate.apply_function(untrans31_23),
            Transform(vector_i, Vector((1,0,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((0,1,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_i_label, MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(1, 0), DOWN, buff=0.2).scale(0.8)),
            Transform(vector_j_label, MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(0, 1), LEFT, buff=0.2).scale(0.8)),
            run_time=2,
            rate_function=smooth
        )
        self.wait(2)

        self.play(
            FadeOut(vector_i, vector_j, ),
            FadeOut(axes_4d_back, x_label, y_label, o_label, vector_i_label, vector_j_label),
            FadeOut(axe_trans2),
            run_time=2
        )
        self.wait(1)


        #矩阵的计算，直接写矩阵的情况
        matrix01_f10 = MathTex(r"\begin{bmatrix} 0 & -1\\ 1 & 0 \end{bmatrix}",color=WHITE).scale(1.6)
        matrix10_11 = MathTex(r"\begin{bmatrix} 1 & 1\\ 0 & 1 \end{bmatrix}",color=WHITE).scale(1.6)
        matrix31_23 = MathTex(r"\begin{bmatrix} 3 & 2\\ 1 & 3 \end{bmatrix}",color=WHITE).scale(1.6)
        matrix01_f10[0][1].set_color(RED)
        matrix01_f10[0][2].set_color(GREEN)
        matrix01_f10[0][3].set_color(GREEN)
        matrix01_f10[0][4].set_color(RED)
        matrix01_f10[0][5].set_color(GREEN)

        matrix10_11[0][1].set_color(RED)
        matrix10_11[0][2].set_color(GREEN)
        matrix10_11[0][3].set_color(RED)
        matrix10_11[0][4].set_color(GREEN)

        matrix31_23[0][1].set_color(RED)
        matrix31_23[0][2].set_color(GREEN)
        matrix31_23[0][3].set_color(RED)
        matrix31_23[0][4].set_color(GREEN)

        self.play(Write(matrix01_f10), run_time=2)
        self.wait(1)
        self.play(FadeOut(matrix01_f10))
        self.wait(1)
        self.play(Write(matrix10_11), run_time=2)
        self.wait(1)
        self.play(FadeOut(matrix10_11))
        self.wait(1)
        self.play(Write(matrix31_23), run_time=2)
        self.wait(1)
        self.play(FadeOut(matrix31_23))
        self.wait(2)


        #矩阵乘法的板书
        #写矩阵
        matrix_f21_11 = MathTex(r"\begin{bmatrix} -2 & 1\\ 1 & 1 \end{bmatrix}",color=WHITE).scale(1.6)
        xy_label = MathTex(r"\begin{bmatrix} x\\ y \end{bmatrix}",color=BLUE).scale(1.6).next_to(matrix_f21_11, RIGHT, buff=0.2)
        matrix_f21_11[0][1].set_color(RED)
        matrix_f21_11[0][2].set_color(RED)
        matrix_f21_11[0][3].set_color(GREEN)
        matrix_f21_11[0][4].set_color(RED)
        matrix_f21_11[0][5].set_color(GREEN)
        group = VGroup(matrix_f21_11, xy_label)
        group.shift(UP*1.5+LEFT*0.5)
        self.play(Write(matrix_f21_11), Write(xy_label), run_time=2)
        self.wait(2)

        equation_end = MathTex(r"x\begin{bmatrix} -2\\ 1\end{bmatrix} + y\begin{bmatrix} 1\\ 1\end{bmatrix} = \begin{bmatrix} -2x+1y\\ 1x+1y\end{bmatrix}",color=WHITE).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.2).scale(1.6)
        equation_end.set_opacity(0)
        # self.play(Write(equation_end), run_time=2)
        self.wait(2)
        groupf21 = VGroup(matrix_f21_11[0][1].copy(),matrix_f21_11[0][2].copy(),matrix_f21_11[0][4].copy())
        targetf21 = VGroup(equation_end[0][2],equation_end[0][3],equation_end[0][4])
        x_label_temp = xy_label[0][1].copy()
        y_label_temp = xy_label[0][2].copy()
        self.play(x_label_temp.animate.move_to(equation_end[0][0]),
                  groupf21.animate.move_to(targetf21),
                  equation_end[0][1].animate.set_opacity(1),
                  equation_end[0][5].animate.set_opacity(1),
                    run_time=2
                  )
        self.wait(1)
        group11 = VGroup(matrix_f21_11[0][3].copy(),matrix_f21_11[0][5].copy())
        target11 = VGroup(equation_end[0][9],equation_end[0][10])
        
        self.play(y_label_temp.animate.move_to(equation_end[0][7]),
                  group11.animate.move_to(target11),
                  equation_end[0][8].animate.set_opacity(1),
                  equation_end[0][11].animate.set_opacity(1),
                    run_time=2
                  )
        self.wait(1)
        self.play(
            equation_end[0][6].animate.set_opacity(1),
            equation_end[0][12].animate.set_opacity(1),
            equation_end[0][13].animate.set_opacity(1),
            equation_end[0][25].animate.set_opacity(1),
            run_time=2

        )

        #设置公式颜色
        equation_end[0][14].set_color(RED).set_opacity(1)
        equation_end[0][15].set_color(RED).set_opacity(1)
        equation_end[0][16].set_color(BLUE).set_opacity(1)
        equation_end[0][17].set_color(WHITE).set_opacity(1)
        equation_end[0][18].set_color(GREEN).set_opacity(1)
        equation_end[0][19].set_color(BLUE).set_opacity(1)
        equation_end[0][20].set_color(RED).set_opacity(1)
        equation_end[0][21].set_color(BLUE).set_opacity(1)
        equation_end[0][22].set_color(WHITE).set_opacity(1)
        equation_end[0][23].set_color(GREEN).set_opacity(1)
        equation_end[0][24].set_color(BLUE).set_opacity(1)
        group_equation_end = VGroup(equation_end[0][14:25])
        self.play(Write(group_equation_end), run_time=2)
        self.wait(3)

        self.play(
            FadeOut(equation_end, matrix_f21_11, xy_label,group11,groupf21,x_label_temp,y_label_temp)
        )
        self.wait(2)

        #线性变换 练习部分
        ###
        ###
        ###第三次映入坐标系
        ###

        self.play(FadeIn(axes_4d_back, x_label, y_label, o_label,axe_practice), run_time=2)
        self.wait(1)
        vector_i = Vector((1,0,0),color=RED,tip_length=0.2)
        vector_i_label = MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(1, 0), DOWN, buff=0.2).scale(0.8)
        vector_j = Vector((0,1,0),color=GREEN,tip_length=0.2)
        vector_j_label = MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(0, 1), LEFT, buff=0.2).scale(0.8)
        vector_i.set_stroke(width=3)
        vector_j.set_stroke(width=3)
        self.play(FadeIn(vector_i,vector_j)
                  ,run_time=2
                  )
        self.wait(2)

        ###
        ###
        ###第三块小黑板把数据拿走到变换中去

        Matrix_blackboard_3_1 = MathTex(r" \begin{bmatrix}0&1 \\1&0\end{bmatrix}",color=WHITE).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.5).scale(1)
        rect_blackboard_3 = Rectangle(
            width=Matrix_blackboard_3_1.width + 0.4,
            height=Matrix_blackboard_3_1.height + 0.4,
            fill_color=BLACK,
            fill_opacity=0.8,
            stroke_width=0
        ).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.2)
        Matrix_blackboard_3_1[0][1].set_color(RED)
        Matrix_blackboard_3_1[0][2].set_color(GREEN)
        Matrix_blackboard_3_1[0][3].set_color(RED)
        Matrix_blackboard_3_1[0][4].set_color(GREEN)

        #定义了左边和右边的坐标的移动起始点
        left_origin = VGroup(Matrix_blackboard_3_1[0][1],Matrix_blackboard_3_1[0][3]).copy()
        right_origin = VGroup(Matrix_blackboard_3_1[0][2],Matrix_blackboard_3_1[0][4]).copy()
        framework_origin_i = VGroup(Matrix_blackboard_3_1[0][0],Matrix_blackboard_3_1[0][5]).copy()
        framework_origin_j = VGroup(Matrix_blackboard_3_1[0][0],Matrix_blackboard_3_1[0][5]).copy()

        ####
        ###外部框架和黑色背景版一起出现
        self.play(FadeIn(rect_blackboard_3))
        self.play(FadeIn(Matrix_blackboard_3_1))
        #先设置了黑色的黑板
        self.wait(2)

        ##
        ##
        def trans01_10(p):
            return np.array([ 0*p[0]+1*p[1], 1*p[0]+0*p[1], p[2]])
        
        self.play(
            axe_practice.animate.apply_function(trans01_10),
            Transform(vector_i, Vector((0,1,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((1,0,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            #Transform(vector_i_label, MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(1, 0), DOWN, buff=0.2).scale(0.8)),
            #Transform(vector_j_label, MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(0, 1), LEFT, buff=0.2).scale(0.8)),
            run_time=2,
            rate_function=smooth
        )
        i_label_temp = MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(0, 1),LEFT,buff=0.2).scale(1)
        i_framework_group = VGroup(i_label_temp[0][0],i_label_temp[0][3])
        j_label_temp = MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(1, 0),DOWN,buff=0.2).scale(1)
        j_framework_group = VGroup(j_label_temp[0][0],j_label_temp[0][3])
        self.play(
            left_origin.animate.move_to(i_label_temp),
            Transform(framework_origin_i,i_framework_group)

        )
        self.play(
            right_origin.animate.move_to(j_label_temp),
            Transform(framework_origin_j,j_framework_group),
            run_time = 2
        )
        self.wait(2)
        self.play(FadeOut(rect_blackboard_3,Matrix_blackboard_3_1),FadeOut(left_origin,right_origin),FadeOut(framework_origin_i,framework_origin_j))
        self.wait(1)
        #还原变换
        self.play(
            axe_practice.animate.apply_function(trans01_10),
            Transform(vector_i, Vector((1,0,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((0,1,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            #Transform(vector_i_label, MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(1, 0), DOWN, buff=0.2).scale(0.8)),
            #Transform(vector_j_label, MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(0, 1), LEFT, buff=0.2).scale(0.8)),
            run_time=2,
            rate_function=smooth
        )
        self.wait(2)
        
        def trans_f11_23(p):
            return np.array([ -1*p[0]+2*p[1], 1*p[0]+3*p[1], p[2]])
        Matrix_blackboard_3_2 = MathTex(r" \begin{bmatrix}-1&2 \\1&3\end{bmatrix}",color=WHITE).next_to(axes_4d_back.c2p(0, -1), DOWN, buff=0.5).scale(1)
        Matrix_blackboard_3_2[0][1].set_color(RED)
        Matrix_blackboard_3_2[0][2].set_color(RED)
        Matrix_blackboard_3_2[0][3].set_color(GREEN)
        Matrix_blackboard_3_2[0][4].set_color(RED)
        Matrix_blackboard_3_2[0][5].set_color(GREEN)
        self.play(FadeIn(rect_blackboard_3))
        self.play(FadeIn(Matrix_blackboard_3_2))
        #定义了左边和右边的坐标的移动起始点
        left_origin = VGroup(Matrix_blackboard_3_2[0][0],Matrix_blackboard_3_2[0][1],Matrix_blackboard_3_2[0][2],Matrix_blackboard_3_2[0][4],Matrix_blackboard_3_2[0][6]).copy()
        left_origin = VGroup(Matrix_blackboard_3_2[0][1],Matrix_blackboard_3_2[0][2],Matrix_blackboard_3_2[0][4]).copy()

        right_origin = VGroup(Matrix_blackboard_3_2[0][0],Matrix_blackboard_3_2[0][3],Matrix_blackboard_3_2[0][5],Matrix_blackboard_3_2[0][6]).copy()
        right_origin = VGroup(Matrix_blackboard_3_2[0][3],Matrix_blackboard_3_2[0][5]).copy()
        framework_origin_i = VGroup(Matrix_blackboard_3_2[0][0],Matrix_blackboard_3_2[0][6]).copy()
        framework_origin_j = VGroup(Matrix_blackboard_3_2[0][0],Matrix_blackboard_3_2[0][6]).copy()
        #先设置了黑色的黑板
        self.wait(2)



        self.play(
            axe_practice.animate.apply_function(trans_f11_23),
            Transform(vector_i, Vector((-1,1,0),color=RED,tip_length=0.2).set_stroke(width=3)),
            Transform(vector_j, Vector((2,3,0),color=GREEN,tip_length=0.2).set_stroke(width=3)),
            #Transform(vector_i_label, MathTex(r"\begin{bmatrix}0\\ 1\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(1, 0), DOWN, buff=0.2).scale(0.8)),
            #Transform(vector_j_label, MathTex(r"\begin{bmatrix}1\\ 0\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(0, 1), LEFT, buff=0.2).scale(0.8)),
            run_time=2,
            rate_function=smooth
        )
        i_label_temp = MathTex(r"\begin{bmatrix}-1\\ 1\end{bmatrix}",color=RED).next_to(axes_4d_back.c2p(-1, 1),LEFT,buff=0.2).scale(1)
        # i_label_temp[0][0].set_color(WHITE)
        # i_label_temp[0][4].set_color(WHITE)
        i_framework_group = VGroup(i_label_temp[0][0],i_label_temp[0][4])
        j_label_temp = MathTex(r"\begin{bmatrix}2\\ 3\end{bmatrix}",color=GREEN).next_to(axes_4d_back.c2p(2, 3),RIGHT,buff=0.2).scale(1)
        # j_label_temp[0][0].set_color(WHITE)
        # j_label_temp[0][3].set_color(WHITE)
        j_framework_group = VGroup(j_label_temp[0][0],j_label_temp[0][3])
        self.play(
            left_origin.animate.move_to(i_label_temp),
            Transform(framework_origin_i,i_framework_group)
        )
        self.play(
            right_origin.animate.move_to(j_label_temp),
            Transform(framework_origin_j,j_framework_group)
        )
        
        self.wait(2)

        




        



