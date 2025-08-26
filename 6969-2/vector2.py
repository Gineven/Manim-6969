from manim import *

class Vector3DExample(ThreeDScene):
    def construct(self):
        # 创建三维坐标轴
        axes = ThreeDAxes(
            y_length=10,
            x_length=14,
            z_length=6,
            axis_config={
                "include_ticks" : False
            }
        )
        
        
        # 添加xyz轴标签
        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y"))
        z_label = axes.get_z_axis_label(Tex("z"))

        # 让y轴标签顺时针旋转90度
        y_label.rotate(-PI / 2)

        
        # 创建向量 (2, 2, 2)
        vector = Vector(
            [2, 2, 0],
            color=RED,
            tip_length=0.2,  # 默认是0.35，减小这个值箭头会变小
        )


        #拉伸向量
        vector_a = Vector(
            [2,2,2],
            color = RED,
            tip_length = 0.2
        )
        vector_b = Vector(
            [4,4,4],
            color = RED,
            tip_length = 0.2
        )
        vector_c = Vector(
            [2,3,4],
            color = RED,
            tip_length = 0.2
        )
        vector_d = Vector(
            [5,0,2],
            color = RED,
            tip_length = 0.2
        )
        vector_e = Vector(
            [2,2,0],
            color = RED,
            tip_length = 0.2
        )
        
        vector_label = MathTex(r"\vec{v} = (2, 2)", color=RED)
        vector_label.next_to(vector.get_end(), UP + RIGHT, buff=0.1)
        
        # 添加坐标轴和向量
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        # 依次平滑地创建坐标轴和标签
        self.play(FadeIn(axes), run_time=2, rate_func=smooth)
        self.play(Write(x_label), Write(y_label), Write(z_label), run_time=2, rate_func=smooth)
        

        self.play(GrowArrow(vector), run_time=2)
        self.play(ReplacementTransform(vector,vector_a),run_time=1,rate_func=smooth)
        self.play(ReplacementTransform(vector_a,vector_b),run_time=1,rate_func=smooth)
        self.play(ReplacementTransform(vector_b,vector_c),run_time=1,rate_func=smooth)
        self.play(ReplacementTransform(vector_c,vector_d),run_time=1,rate_func=smooth)
        self.play(ReplacementTransform(vector_d,vector_e),run_time=1,rate_func=smooth)
        # 设置初始视角（可以调整方便观察三维结构）
        self.wait(2)
        
        # 移动视角，只观察x-y平面
        # 也就是视角正对z轴，phi=0度（俯视）
        self.move_camera(phi=0 * DEGREES, theta=-90 * DEGREES)
        # ThreeDAxes does not support set_y_range animation; to change range, recreate axes if needed
        self.wait(2)
        axes2D = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE,
                "stroke_width": 1.5,
                "stroke_opacity": 0.3
            },
            
        )
        self.play(FadeOut(axes),FadeOut(z_label) 
                  ,FadeIn(axes2D), FadeIn(vector_label),run_time=2)
        self.wait(2)


        vector2 = Vector(
            direction=[2, 1, 0],
            color=BLUE,
            tip_length = 0.2
        )
        vector2_label = MathTex(r"\vec{u} = (2, 1)", color=BLUE).next_to(vector2.get_end(), UP + RIGHT, buff=0.1)

        self.play(
            GrowArrow(vector2),
            Write(vector2_label),
            run_time=2
        )

        #去标签
        self.play(FadeOut(vector_label),FadeOut(vector2_label,run_time=2))
        self.play(vector2.animate.shift(UP*2+RIGHT*2))

        #向量加法
        vector3 = Vector(
            direction=[4, 3, 0],
            color=PURPLE,
            tip_length = 0.2
        )
        vector3_label = MathTex(r"\vec{c} = (4, 3)", color=PURPLE)
        vector3_label.next_to(vector3.get_end(), UP + RIGHT, buff=0.1)
        group1 = VGroup(vector2,vector_e)
        group2 = VGroup(vector3, vector3_label)
        self.play(ReplacementTransform(group1,vector3),run_time=2)
        self.play(Write(vector3_label))
        self.wait( )
        #self.play(FadeOut(group1),FadeIn(group2),run_time=2)
