from  manim import *
import numpy as np
class Scene1(Scene):
    def construct(self):
        #创建一个三角形（2，5）（1，3）（4，2）
        axes =  NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0},
            axis_config={"include_tip": True, "include_ticks": True},
        )
        x_label = axes.get_x_axis_label(MathTex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes.get_y_axis_label(MathTex("y").scale(1))
        o_label = Tex("o").next_to(axes.c2p(0, 0), DOWN+RIGHT, buff=0.2).scale(1)
        x_label.next_to(axes.c2p(7,0), DOWN, buff=0.3)
        y_label.next_to(axes.c2p(0,3.8), LEFT, buff=0.3)
        self.add(axes, x_label, y_label, o_label)
        p1 = np.array([0, 2, 0])
        p2 = np.array([3/2, 3, 0])
        p3 = np.array([2, 1, 0])
        triangle = Polygon(p1, p2, p3, color=BLUE, fill_opacity=0.8)
        #把三角形的点标黄
        point1 = Dot(p1, color=YELLOW)
        point2 = Dot(p2, color=YELLOW)
        point3 = Dot(p3, color=YELLOW)
        #动点p为p1和p2的中点
        
        
        dots = VGroup(point1, point2, point3)
        triangle1 = VGroup(triangle, point1, point2, point3)
        self.play(FadeIn(triangle1))
        self.wait(1)
        
        #动点p
        dot = Dot(p1, color=RED)
        #label = MathTex("P(0.75,2.5)", color=RED).next_to(dot, UP + LEFT, buff=0.2)
        label = MathTex("P(x,y)", color=RED).next_to(dot, UP + LEFT, buff=0.2)


        self.play(FadeIn(dot))
        dot_temp1 = Dot((1/5*p1 + 4/5*p2), color=RED)
        dot_temp2 = Dot((4/5*p1 + 1/5*p2), color=RED)
        dot_temp3 = Dot((1/2*p1 + 1/2*p2), color=RED)
        self.play(Transform(dot, dot_temp1))
        self.play(Transform(dot, dot_temp2))
        self.play(Transform(dot, dot_temp3))
        self.play(FadeIn(label))
        dotgro = VGroup(dot, label)


    
        
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
        dot_temp = dot.copy().flip(axis=line_end - line_start, about_point=line_start)
        #label_temp = label.copy().flip(axis=line_end - line_start, about_point=line_start)
        #计算出翻折后的p1和p2的中点坐标
        # 计算翻转后p1和p2的中点坐标，写成和上面p一样的形式方便后续处理
        def reflect_point(point, line_point, line_dir):
            d = line_dir / np.linalg.norm(line_dir)
            v = point - line_point
            proj = np.dot(v, d) * d
            perp = v - proj
            reflected = point - 2 * perp
            return reflected

        midpoint = 0.5 * (p1 + p2)
        reflected_midpoint = reflect_point(midpoint, line_start, line_end - line_start)
        dot_reflected = Dot(reflected_midpoint, color=RED)
        #label_reflected = MathTex(
        #    f"P({reflected_midpoint[0]:.2f},{reflected_midpoint[1]:.2f})", color=RED
        #).next_to(dot_reflected, DOWN + RIGHT, buff=0.2)
        label_reflected = MathTex(f"P(x',y')", color=RED).next_to(dot_reflected, DOWN + RIGHT, buff=0.2)
        dotgro_reflected = VGroup(dot_reflected, label_reflected)
        
        #label_temp = MathTex(f"P({})", color=RED).next_to(dot, DOWN + RIGHT, buff=0.2)
    
        self.play(Transform(triangle1, triangle1_mirrored),
                  Transform(dotgro, dotgro_reflected),
                  run_time=2, rate_func=smooth)
        self.play(FadeOut(mirror_line))
        self.wait(1)
        #将三角顺时针旋转90
        origin = np.array([0, 0, 0])
        point4 = Dot(origin, color=RED)
        self.play(FadeIn(point4))
        #计算出旋转后的点p标签
        dot_temp = dot.copy().rotate(angle=PI/2, about_point=origin)
        #label_temp = MathTex(f"P({-dot.get_center()[1]:.2f},{dot.get_center()[0]:.2f})", color=RED).next_to(dot_temp, UP + RIGHT, buff=0.2)
        label_temp = MathTex("P(x'',y'')", color=RED).next_to(dot_temp, UP + RIGHT, buff=0.2)
        dotgro_temp = VGroup(dot_temp, label_temp)#可以通过get——center()获取点的中心坐标无需进行多余计算

        self.play(Rotate(triangle1, angle=PI/2, about_point=np.array([0, 0, 0])),
                  Transform(dotgro, dotgro_temp),run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(point4))
        #让 标签单独消失
        self.play(FadeOut(label))
        p1 = np.array([-1, 1, 0])
        p2 = np.array([-2.5, 2, 0])
        dot_temp1 = Dot((1/5*p1 + 4/5*p2), color=RED)
        dot_temp2 = Dot((4/5*p1 + 1/5*p2), color=RED)
        dot_temp3 = Dot((1/2*dot_temp.get_center() + 1/2*dot.get_center()), color=RED)
        self.play(Transform(dot, dot_temp1))
        self.play(Transform(dot, dot_temp2))
        self.play(Transform(dot, dot_temp3))
        self.play(FadeOut(triangle1), FadeOut(point1), FadeOut(point2), FadeOut(point3),  FadeOut(dot))
        self.wait(1)


