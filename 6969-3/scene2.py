from  manim import *
import numpy as np
from manim.utils.rate_functions import smooth, there_and_back
from colour import Color
class Scene2(Scene):
    def construct(self):
        #创建一个三角形（2，5）（1，3）（4，2）
        axes =  NumberPlane(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            background_line_style={"stroke_opacity": 0.3},
            axis_config={"include_tip": False, "stroke_width": 0,"include_ticks": False},
        )
        axesvec = axes.copy()
        axesvector = axes.copy()
        axestrans = axes.copy()
        axestrans2 = axes.copy()
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
        x_label.next_to(axes.c2p(7,0), DOWN, buff=0.3)
        y_label.next_to(axes.c2p(0,3.8), LEFT, buff=0.3)
        self.add(axes_4d_back)
        self.play(FadeIn(axes, x_label, y_label, o_label))
        p1 = np.array([0, 2, 0])
        p2 = np.array([3/2, 3, 0])
        p3 = np.array([2, 1, 0])
        triangle = Polygon(p1, p2, p3, color=BLUE, fill_opacity=0.8)
        #把三角形的点标黄
        point1 = Dot(p1, color=YELLOW)
        point2 = Dot(p2, color=YELLOW)
        point3 = Dot(p3, color=YELLOW)
        dots = VGroup(point1, point2, point3)
        triangle1 = VGroup(triangle, point1, point2, point3)
        triangle_to_transform = triangle1.copy()
        
        self.play(FadeIn(triangle1))
        self.wait(1)
        #让三角形沿着y=x+1直线翻转
        # 定义y=x+1直线的两个点
        line_start = np.array([-5, -4, 0])
        line_end = np.array([3, 4, 0])
        mirror_line = Line(line_start, line_end, color=RED)
        self.play(Create(mirror_line))
        self.wait(0.5)

        # 沿着y=x+1直线翻折三角形
        triangle1_mirrored = triangle1.copy().flip(axis=line_end - line_start, about_point=line_start)
        axes_mirrored = axes.copy().flip(axis=line_end - line_start, about_point=line_start)
        self.play(Transform(triangle1, triangle1_mirrored),Transform(axes, axes_mirrored), run_time=1.5, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(mirror_line))
        self.wait(1)
        #将三角顺时针旋转90
        origin = np.array([0, 0, 0])
        point4 = Dot(origin, color=RED)
        self.play(FadeIn(point4))
        self.play(Rotate(triangle1, angle=PI/2, about_point=np.array([0, 0, 0])),Rotate(axes, angle=PI/2, about_point=np.array([0, 0, 0])),run_time=1.5, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(triangle1), FadeOut(point1), FadeOut(point2), FadeOut(point3), FadeOut(point4))
        self.play(FadeOut(axes))
        self.wait(2)


        l = []
        for i in range(4,-5,-1):
            for j in range(-6,7):
                dot = Dot(np.array([j,i,0]))
                dot.set_color(Color(hue=(j + 7) / 14 * 0.5 + 0.5, saturation=0.7, luminance=0.6))
                # hue=(j + 7) / 14 * 0.5 + 0.5
                # 计算颜色的色调值，范围在0到1之间
                l.append(dot)
        self.play(FadeIn(*l), run_time=1, rate_functions=there_and_back)
        # FadeIn(*l) 会使得所有的点同时淡入
        # run_time=1 表示动画持续时间为 1 秒
        # rate_functions=there_and_back 会使得动画先向一个方向移动，然后再回到原来的位置
        self.play(FadeOut(*l), run_time=1, rate_functions=there_and_back)
        self.wait(3)

        vectora = Vector((3,1,0), color=BLUE)
        vectori = Vector((1,0,0), color=MAROON_B)
        vector3i = Vector((3,0,0), color=MAROON_B)
        vectorj = Vector((0,1,0), color=PURPLE_A)
        self.play(FadeIn(vectora),FadeIn(axesvec))
        self.wait(1)
        self.play(FadeIn(vectori))
        self.play(Transform(vectori, vector3i), run_time=1, rate_functions=smooth)
        self.wait(1)
        self.play(FadeIn(vectorj))
        self.wait(1)
        self.play(vectorj.animate.shift(RIGHT*3), run_time=1, rate_functions=smooth)
        self.wait(1)
        p31 = Dot(np.array([3,1,0]), color=BLUE)
        #label31 = MathTex("(3,1)", color=YELLOW).next_to(p31, UP + RIGHT, buff=0.1)

        self.play(FadeOut(vectori), FadeOut(vectorj))
        self.play(Transform(vectora, p31), run_time=1.5, rate_functions=smooth)
        self.wait(2)
        p32 = Dot(np.array([3,2,0]), color=BLUE)
        p12 = Dot(np.array([1,2,0]), color=BLUE)
        p23 = Dot(np.array([2,3,0]), color=BLUE)
        # label32 = MathTex("(3,2)",color=YELLOW).next_to(p32, UP + RIGHT, buff=0.1)
        # label12 = MathTex("(1,2)",color=YELLOW).next_to(p12, DOWN + LEFT, buff=0.1)
        # label23 = MathTex("(2,3)",color=YELLOW).next_to(p23, UP + RIGHT, buff=0.1)
        # vector12to23 = Vector((1,1,0), color=BLUE).shift(RIGHT*1+UP*2)
        self.play(axesvec.animate.shift(UP),ReplacementTransform(vectora,p32), run_time=1.5, rate_functions=smooth)
        self.wait(1)
        self.play(Transform(p32, p12),axesvec.animate.shift(LEFT*2),run_time=1.5, rate_functions=smooth)
        self.wait(1)
        # self.play(FadeIn(vector12to23))
        # self.wait(1)
        group12to23 = VGroup(p32)
        group23 = VGroup(p23)
        self.play(Transform(group12to23, group23),axesvec.animate.shift(UP+RIGHT),run_time=1.5, rate_functions=smooth)
        self.wait(1)
        self.play(FadeOut(group12to23), FadeOut(group23),FadeOut(axesvec))
        self.wait(2)




        #向量三角形的翻转
        vectora_new = Vector((3,1,0), color=BLUE)
        self.play(FadeIn(vectora_new),FadeIn(vectori),FadeIn(vectorj),FadeIn(axesvector))
        groupvectors = VGroup(vectora_new,vectori,vectorj,axesvector)
        line_start = np.array([-4, -4, 0])
        line_end = np.array([4, 4, 0])
        mirror_line = Line(line_start, line_end, color=RED)
        self.play(Create(mirror_line))
        self.wait(0.5)
        self.play(Transform(groupvectors, groupvectors.copy().flip(axis=line_end - line_start, about_point=line_start)), run_time=1.5, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(mirror_line))
        self.wait(1)
        dot_temp = Dot(np.array([0,0,0]), color=RED)
        self.play(FadeIn(dot_temp))
        self.play(Rotate(groupvectors, angle=PI/2, about_point=np.array([0, 0, 0])), run_time=1.5, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(groupvectors), FadeOut(dot_temp))



        #线性变换
        vectori_new = Vector((1,0,0), color=MAROON_B)
        vectorj_new = Vector((0,1,0), color=PURPLE_A)
        i_label = MathTex(r"\vec{i}",color=MAROON_B).next_to(axestrans.c2p(1, 0), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        j_label = MathTex(r"\vec{j}",color=PURPLE_A).next_to(axestrans.c2p(0, 1), DOWN + LEFT, buff=0.2).scale(1)
        self.play(FadeIn(vectori_new),FadeIn(vectorj_new),FadeIn(i_label),FadeIn(j_label),FadeIn(axestrans))
        def tranl1(p):
    # 返回一个新的坐标向量，x 和 y 坐标根据比例进行缩放
            #return np.array([ -2*p[1]+p[0], 3*p[0], p[2]])  # 假设是三维空间（或者如果是二维，只返回前两个值）
        #将底色的
            return np.array([ 3*p[1]+p[0], -2*p[0], p[2]])# x-> x -2y y-> 3x
        def ros(p):#旋转函数
    # 返回一个新的坐标向量，x 和 y 坐标根据比例进行缩放
            #return np.array([ -2*p[1]+p[0], 3*p[0], p[2]])  # 假设是三维空间（或者如果是二维，只返回前两个值）
        #将底色的
            return np.array([ -1*p[1], p[0], p[2]])# x-> y y-> -x
        def unros(p):#反向旋转函数
            return np.array([ p[1], -p[0], p[2]])# x-> x -2y y-> 3x
        def transform1(p):#翻折函数
            return np.array([ p[1], p[0], p[2]])# x-> x -2y y-> 3x
        def transform2(p):
            return np.array([ p[0]-2*p[1], 2*p[0]-4*p[1], p[2]])
        
        def trans1011(p):
            return np.array([ p[0]+p[1], p[1], p[2]])
        def untrans1011(p):
            return np.array([ p[0]-p[1], p[1], p[2]])
        def trans3123(p):
            return np.array([ 3*p[0]+2*p[1], p[0]+3*p[1], p[2]])
        def untrans3123(p):
            return np.array([ 3/7*p[0]-2/7*p[1], -1/7*p[0]+3/7*p[1], p[2]])
        def transmf2213(p):
            return np.array([ -2*p[0]+1*p[1], 2*p[0]+3*p[1], p[2]])
        def untransmf2213(p):
            return np.array([ -3/8*p[0]+1/8*p[1], 1/4*p[0]+1/4*p[1], p[2]])

        vectori = Vector((1,0,0), color=MAROON_B)
        vectori.apply_function(ros).set_tip_length(0.2)
        vectorj = Vector((0,1,0), color=PURPLE_A)
        vectorj.apply_function(ros).set_tip_length(0.2)
        #建立副本获取位置的方法 保证实时移动且不旋转
        #第一次旋转
        self.play(axestrans.animate.apply_function(ros),
                    vectori_new.animate.apply_function(ros).set_tip_length(0.2),
                    vectorj_new.animate.apply_function(ros).set_tip_length(0.2),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        vectorj.apply_function(unros).set_tip_length(0.2)
        vectori.apply_function(unros).set_tip_length(0.2)
        #旋转回来
        self.play(axestrans.animate.apply_function(unros),
                    vectori_new.animate.apply_function(unros).set_tip_length(0.2),
                    vectorj_new.animate.apply_function(unros).set_tip_length(0.2),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        #翻折变换
        vectorj.apply_function(transform1).set_tip_length(0.2)
        vectori.apply_function(transform1).set_tip_length(0.2)

        self.play(axestrans.animate.apply_function(transform1),
                    vectori_new.animate.apply_function(transform1).set_tip_length(0.2),
                    vectorj_new.animate.apply_function(transform1).set_tip_length(0.2),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        #二次翻折恢复
        vectorj.apply_function(transform1).set_tip_length(0.2)
        vectori.apply_function(transform1).set_tip_length(0.2)

        self.play(axestrans.animate.apply_function(transform1),
                    vectori_new.animate.apply_function(transform1).set_tip_length(0.2),
                    vectorj_new.animate.apply_function(transform1).set_tip_length(0.2),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        #基向量 （1,0）（1,1）     （3,1） （2,3）     （-2,2）（1,3） 三组
        #第一组
        vectorj.apply_function(trans1011).set_tip_length(0.2)
        vectori.apply_function(trans1011).set_tip_length(0.2)

        self.play(axestrans.animate.apply_function(trans1011),
                    Transform(vectori_new, Vector(vectori.get_end(), color=MAROON_B).set_tip_length(0.2)),
                    Transform(vectorj_new, Vector(vectorj.get_end(), color=PURPLE_A).set_tip_length(0.2)),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        vectorj.apply_function(untrans1011).set_tip_length(0.2)
        vectori.apply_function(untrans1011).set_tip_length(0.2)
        #恢复
        self.play(axestrans.animate.apply_function(untrans1011),
                    Transform(vectori_new, Vector(vectori.get_end(), color=MAROON_B).set_tip_length(0.2)),
                    Transform(vectorj_new, Vector(vectorj.get_end(), color=PURPLE_A).set_tip_length(0.2)),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), DOWN + LEFT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        #第二组
        vectorj.apply_function(trans3123).set_tip_length(0.2)
        vectori.apply_function(trans3123).set_tip_length(0.2)
        self.play(axestrans.animate.apply_function(trans3123),
                    Transform(vectori_new, Vector(vectori.get_end(), color=MAROON_B).set_tip_length(0.2)),
                    Transform(vectorj_new, Vector(vectorj.get_end(), color=PURPLE_A).set_tip_length(0.2)),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        vectorj.apply_function(untrans3123).set_tip_length(0.2)
        vectori.apply_function(untrans3123).set_tip_length(0.2)
        #恢复
        self.play(axestrans.animate.apply_function(untrans3123),
                    Transform(vectori_new, Vector(vectori.get_end(), color=MAROON_B).set_tip_length(0.2)),
                    Transform(vectorj_new, Vector(vectorj.get_end(), color=PURPLE_A).set_tip_length(0.2)),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)


        #第三组
        vectorj.apply_function(transmf2213).set_tip_length(0.2)
        vectori.apply_function(transmf2213).set_tip_length(0.2)
        self.play(axestrans.animate.apply_function(transmf2213),
                    Transform(vectori_new, Vector(vectori.get_end(), color=MAROON_B).set_tip_length(0.2)),
                    Transform(vectorj_new, Vector(vectorj.get_end(), color=PURPLE_A).set_tip_length(0.2)),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        vectorj.apply_function(untransmf2213).set_tip_length(0.2)
        vectori.apply_function(untransmf2213).set_tip_length(0.2)
        #恢复
        self.play(axestrans.animate.apply_function(untransmf2213),
                    Transform(vectori_new, Vector(vectori.get_end(), color=MAROON_B).set_tip_length(0.2)),
                    Transform(vectorj_new, Vector(vectorj.get_end(), color=PURPLE_A).set_tip_length(0.2)),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)


        #第二次线性变换压扁
        vectorj.apply_function(transform2).set_tip_length(0.2)
        vectori.apply_function(transform2).set_tip_length(0.2)
        axes_trans_temp = axestrans.copy()
        self.play(axestrans.animate.apply_function(transform2),
                    Transform(vectori_new, Vector(vectori.get_end(), color=MAROON_B).set_tip_length(0.2)),
                    Transform(vectorj_new, Vector(vectorj.get_end(), color=PURPLE_A).set_tip_length(0.2)),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(2)
        #恢复
        a = axes_trans_temp.c2p(1,0)
        b = axes_trans_temp.c2p(0,1)
        self.play(
            Transform(axestrans,axes_trans_temp),
            Transform(vectori_new, Vector((1,0,0), color=MAROON_B).set_tip_length(0.2)),
            Transform(vectorj_new, Vector((0,1,0), color=PURPLE_A).set_tip_length(0.2)),
            Transform(i_label, i_label.copy().next_to(a, DOWN + LEFT, buff=0.2).scale(1)),
            Transform(j_label, j_label.copy().next_to(b, DOWN + LEFT, buff=0.2).scale(1)),
            run_time=2, rate_func=smooth
        )


        #先翻折再旋转
        vectori = Vector((1,0,0), color=MAROON_B)
        vectorj = Vector((0,1,0), color=PURPLE_A)
        vectorj.apply_function(transform1).set_tip_length(0.2)
        vectori.apply_function(transform1).set_tip_length(0.2)
        self.play(axestrans.animate.apply_function(transform1),
                    Transform(vectori_new, Vector(vectori.get_end(), color=MAROON_B).set_tip_length(0.2)),
                    Transform(vectorj_new, Vector(vectorj.get_end(), color=PURPLE_A).set_tip_length(0.2)),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(1)
        vectorj.apply_function(ros).set_tip_length(0.2)
        vectori.apply_function(ros).set_tip_length(0.2)
        axes_trans_temp = axestrans.copy()
        self.play(axestrans.animate.apply_function(ros),
                    Transform(vectori_new, Vector(vectori.get_end(), color=MAROON_B).set_tip_length(0.2)),
                    Transform(vectorj_new, Vector(vectorj.get_end(), color=PURPLE_A).set_tip_length(0.2)),
                    Transform(i_label, i_label.copy().next_to(vectori.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                    Transform(j_label, j_label.copy().next_to(vectorj.get_end(), UP+RIGHT, buff=0.2).scale(1)),
                  run_time=2, rate_func=smooth)
        self.wait(2)


        #消失向量ij和label
        self.play(FadeOut(axestrans),FadeOut(vectori_new),FadeOut(vectorj_new),FadeOut(i_label),FadeOut(j_label))
        self.wait(2)


        


        #三角形变换 加黄点 加y=x+1 红色直线翻折后平移再消失红色
        line_start = np.array([-7, -6, 0])
        line_end = np.array([5, 6, 0])
        mirror_line = Line(line_start, line_end, color=RED)
        self.play(FadeIn(axestrans2),FadeIn(mirror_line))
        self.play(FadeIn(triangle_to_transform))
        self.wait(1)
        
        transgroup = VGroup(triangle_to_transform, axestrans2)
        self.play(transgroup.animate.shift(DOWN),mirror_line.animate.shift(DOWN),rate_functions=smooth, run_time=1.5)
        self.wait(1)
        self.play(transgroup.animate.apply_function(transform1), run_time=1.5, rate_functions=smooth)
        self.wait(1)
        self.play(transgroup.animate.shift(UP),mirror_line.animate.shift(UP), run_time=1.5, rate_functions=smooth)
        dot_temp = Dot(np.array([0,0,0]), color=RED)
        self.play(FadeOut(mirror_line), FadeIn(dot_temp))
        self.wait(1)
        self.play(transgroup.animate.apply_function(ros), run_time=1.5, rate_functions=smooth)
        self.wait(1)
        self.play(FadeOut(transgroup), FadeOut(dot_temp))
        self.wait(1)

        self.play(FadeOut(axes_4d_back),FadeOut(x_label),FadeOut(y_label),FadeOut(o_label))
        self.wait(2)

        

        