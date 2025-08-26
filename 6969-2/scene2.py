from  manim import *
class VectorOperationsScene(Scene):
    def construct(self):
        # 创建第一个坐标系（用于展示向量数乘）
        axes_left = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0},
            axis_config={"include_tip": True, "include_ticks": False},
        ).shift(LEFT * 4)  # 将第一个坐标系移动到左边

        # 创建第二个坐标系（用于展示向量加法）
        axes_right = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            background_line_style={"stroke_opacity": 0},
            axis_config={"include_tip": True, "include_ticks": False},
        ).shift(RIGHT * 4)  # 将第二个坐标系移动到右边


        axes =  NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.3},
            axis_config={"include_tip": True, "include_ticks": False},
        ) 
        axes_temp =  NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0},
            axis_config={"include_tip": True, "include_ticks": False},
        )



        vector1_left = Vector(
            [1, 1, 0],
            color=BLUE,
            tip_length=0.2
        ).shift(LEFT*4) 
        vector1_scale_left = Vector(
            [2.5, 2.5, 0],
            color=BLUE,
            tip_length=0.2
        ).shift(LEFT*4)  
        vector_a_right = Vector(
            [1.5, 0.7, 0],
            color=BLUE,
            tip_length=0.2
        ).shift(RIGHT*4)
        vector_b_right = Vector(
            [0.7, 1.5, 0],
            color=YELLOW,
            tip_length=0.2
        ).shift(RIGHT*4).shift(RIGHT*1.5+UP*0.7)
        vector_c_right = Vector(
            [2.2, 2.2, 0],
            color=GREEN,
            tip_length=0.2
        ).shift(RIGHT*4)
        
        self.play(FadeIn(vector1_left),FadeIn(vector_a_right),FadeIn(vector_b_right)
                  ,run_time=2,rate_func=smooth)
        self.wait(1)
        self.play(FadeIn(vector1_scale_left),FadeIn(vector_c_right)
                  ,run_time = 1)
        self.wait(2)
        group1 = VGroup(vector1_left,vector1_scale_left)
        gropu2 = VGroup(vector_a_right,vector_b_right,vector_c_right)
        group3 = VGroup(gropu2,group1)
        self.play(FadeOut(group1),FadeOut(gropu2),FadeIn(axes),rate_func=smooth,run_time=3)
        x_label = axes.get_x_axis_label(Tex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes.get_y_axis_label(Tex("y").scale(1))
        o_label = Tex("o").next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.2).scale(1) 
        self.play(Write(x_label), Write(y_label), Write(o_label), run_time=2, rate_func=smooth)
        #向量数乘
        vector1 = Vector(
            [1, 1, 0],
            color=BLUE,
            tip_length=0.2
        )
        vector1_temp = vector1.copy()
        vector1_label = MathTex(r"(1,1)", color=BLUE) 
        vector1_label_temp = MathTex(r"(1,1)", color=BLUE)
        vector1_label.next_to(vector1.get_end(), UP + RIGHT, buff=0.1)
        vector1_label_temp.next_to(vector1_temp.get_end(), UP + RIGHT, buff=0.1)
        vector1_scale_1 = Vector(
            [2, 2, 0],
            color=BLUE,
            tip_length=0.2
        )
        vector1_scale_label_1 = MathTex(r"(2,2)", color=BLUE) 
        vector1_scale_label_1.next_to(vector1_scale_1.get_end(), UP + RIGHT, buff=0.1)
        vector1_scale = Vector(
            [3, 3, 0],
            color=BLUE,
            tip_length=0.2
        )
        vector1_scale_label = MathTex(r"(3,3)", color=BLUE) 
        vector1_scale_label.next_to(vector1_scale.get_end(), UP + RIGHT, buff=0.1)
        vector1_negitive = Vector(
            [-2, -2, 0],
            color=BLUE,
            tip_length=0.2
        )
        vector1_negitive_label = MathTex(r"(-2,-2)", color=BLUE) 
        vector1_negitive_label.next_to(vector1_negitive.get_end(), DOWN + LEFT, buff=0.1)
        group_vector1 = VGroup(vector1,vector1_label)
        group_vector1_temp = VGroup(vector1_temp,vector1_label_temp)
        group_vector1_scale_1 = VGroup(vector1_scale_1,vector1_scale_label_1)
        group_vector1_scale = VGroup(vector1_scale,vector1_scale_label)
        group_vector1_negitive = VGroup(vector1_negitive,vector1_negitive_label)
        self.play(Create(group_vector1),run_time=1.2,rate_func=smooth)
        self.wait(1)
        self.play(ReplacementTransform(group_vector1,group_vector1_scale_1),run_time=1.2,rate_func=smooth)
        #self.wait(1)
        self.play(ReplacementTransform(group_vector1_scale_1,group_vector1_scale),run_time=1.2,rate_func=smooth)
        #self.wait(1)
        self.play(ReplacementTransform(group_vector1_scale,group_vector1_negitive),run_time=1.2,rate_func=smooth)
        self.play(ReplacementTransform(group_vector1_negitive,group_vector1_temp),run_time=1.2,rate_func=smooth)
        self.play(FadeOut(group_vector1_temp),run_time=1.5)
        #以上完成数乘部分
        #向量相加部分
        vector_a = Vector(
            [3, 1, 0],
            color=BLUE,
            tip_length=0.2
        )
        vector_a_label = MathTex(r"\vec{a} = (3, 1)", color=BLUE)
        vector_a_label.next_to(vector_a.get_end(), DOWN + RIGHT, buff=0.1)
        vector_b = Vector(
            [1, 2, 0],
            color=YELLOW,
            tip_length=0.2
        )
        vector_b_label = MathTex(r"\vec{b} = (1, 2)", color=YELLOW)
        vector_b_label.next_to(vector_b.get_end(), DOWN + RIGHT, buff=0.1)
        vector_c = Vector(
            [4, 3, 0],
            color=GREEN,
            tip_length=0.2
        )
        vector_c_label = MathTex(r"\vec{c} = (4, 3)", color=GREEN)
        vector_c_label.next_to(vector_c.get_end(), UP + LEFT, buff=0.1)
        group_a = VGroup(vector_a,vector_a_label)
        group_b = VGroup(vector_b,vector_b_label)
        group_c = VGroup(vector_c,vector_c_label)
        self.play(Create(group_a),run_time=1.5)
        self.wait()
        self.play(Create(group_b),run_time=1.5)
        self.wait()
        self.play(group_b.animate.shift(RIGHT*3+UP))
        self.wait()
        # self.play(Create(group_c),run_time=1.5)
        # self.wait()
        self.play(FadeOut(vector_a_label),FadeOut(vector_b_label),vector_a.animate.set_opacity(0.5),
                  vector_b.animate.set_opacity(0.5),FadeIn(group_c))
        self.wait()
        self.play(FadeOut(vector_b),FadeOut(vector_a),FadeOut(group_c))
        self.wait()
        #展示左侧合成
        group_b.shift(LEFT*3+DOWN)
        vector_a_label.next_to(vector_a.get_end(), UP + RIGHT, buff=0.1)
        vector_b_label.next_to(vector_b.get_end(), UP + LEFT, buff=0.1)
        vector_c_label.next_to(vector_c.get_end(), DOWN + RIGHT, buff=0.1)
        vector_a.set_opacity(1)
        vector_b.set_opacity(1)
        self.play(Create(group_a),run_time=1.5)
        self.wait()
        self.play(Create(group_b),run_time=1.5)
        self.wait()
        self.play(group_a.animate.shift(RIGHT+2*UP))
        self.wait()
        # self.play(Create(group_c),run_time=1.5)
        # self.wait()
        self.play(FadeOut(vector_a_label),FadeOut(vector_b_label),vector_a.animate.set_opacity(0.5),
                  vector_b.animate.set_opacity(0.5),FadeIn(group_c))
        self.wait()
        self.play(FadeOut(vector_b),FadeOut(vector_a),FadeOut(group_c))
        self.wait()
        # self.play(FadeOut(group_a),FadeOut(group_b),FadeOut(group_c))
        vector_d = vector_b.copy().shift(RIGHT*3+UP)
        vector_e = vector_a.copy().shift(LEFT+2*DOWN)
        self.play(FadeIn(vector_c),FadeIn(vector_a),FadeIn(vector_b)
                 ,FadeIn(vector_e),FadeIn(vector_d),run_time=2 )
        self.wait()
        self.play(FadeOut(vector_c),FadeOut(vector_a),FadeOut(vector_b)
                 ,FadeOut(vector_e),FadeOut(vector_d),run_time=2 )
        self.wait(2)

        self.play(FadeOut(axes),FadeOut(x_label),FadeOut(y_label),FadeOut(o_label),
                  FadeIn(axes_temp),run_time=2,rate_func=smooth)
        self.wait()

