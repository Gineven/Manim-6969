from  manim import *
class VectorOperationsScene(Scene):
    def construct(self):
        axes =  NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0},
            axis_config={"include_tip": True, "include_ticks": False},
        )
        x_label = axes.get_x_axis_label(Tex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes.get_y_axis_label(Tex("y").scale(1))
        o_label = Tex("o").next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.2).scale(1) 
        self.play(FadeIn(axes),run_time=2)
        self.play(Write(x_label), Write(y_label), Write(o_label), run_time=2, rate_func=smooth)
        group_axes = VGroup(axes,x_label,y_label,o_label)
        self.play(group_axes.animate.shift(LEFT*3))

        
        a = [1,2,-1,1/3,-1,2]
        b = [1,1/2,2,-1,-1/2,-1/3]

        # 创建空列表来存储合成的向量
        c = []
        def add(tuple1,tuple2):
            result = tuple(map(lambda x, y: x + y, tuple1, tuple2))
            return result
        def multiply_tuple(factor, tuple1):
            result = tuple(map(lambda x: x * factor, tuple1))
            return result
        
        # 循环创建并展示向量
        for i in range(len(a)):
            # 从列表a和b中取出向量
            vector_a = Vector(multiply_tuple(a[i],(3,1,0)), color=BLUE).shift(LEFT * 3)  # 将向量a平移
            vector_b = Vector(multiply_tuple(b[i],(1,2,0)), color=YELLOW).shift(LEFT * 3)  # 将向量b平移
            vector_a_label = MathTex(r"\vec{a}", color=BLUE)
            vector_b_label = MathTex(r"\vec{b}", color=YELLOW)
            vector_a_label.next_to(vector_a.get_end(), UP + RIGHT, buff=0.2)
            if i == 2:
                vector_a_label.next_to(vector_a.get_end(), DOWN+LEFT, buff=0.2)
            if i==4:
                vector_a_label.next_to(vector_a.get_end(), DOWN+LEFT, buff=0.2)
            if i == 5:
                vector_b_label.next_to(vector_b.get_end(), DOWN + LEFT, buff=0.2)
            vector_b_label.next_to(vector_b.get_end(), DOWN + RIGHT, buff=0.2)
            # 计算向量c（向量a和向量b的和）
             # 将结果向量加入到c列表

            vector_c = Vector(add(multiply_tuple(a[i],(3,1,0)),multiply_tuple(b[i],(1,2,0))), 
                              color=GREEN).shift(LEFT * 3)
            vector_c_label = MathTex(r"\vec{c}", color=GREEN)
            tuple_c_vector = add(multiply_tuple(a[i],(3,1,0)),multiply_tuple(b[i],(1,2,0)))
            if tuple_c_vector[0]>0 and tuple_c_vector[1]>0: vector_c_label.next_to(vector_c.get_end(), UP + RIGHT, buff=0.2)
            if tuple_c_vector[0]<=0 and tuple_c_vector[1]<0: vector_c_label.next_to(vector_c.get_end(), DOWN + LEFT, buff=0.2)
            if tuple_c_vector[0]<0 and tuple_c_vector[1]>=0: vector_c_label.next_to(vector_c.get_end(), UP + LEFT, buff=0.2)
            # 动画展示向量a, b, 和 c
            self.play(Create(vector_a), Create(vector_b), Write(vector_a_label),Write(vector_b_label))
            self.play(FadeOut(vector_a_label),FadeOut(vector_b_label))
            #self.play(FadeOut(vector_a), FadeOut(vector_b),FadeIn(vector_c),FadeIn(vector_c_label))
            self.play(ReplacementTransform(VGroup(vector_a,vector_b),vector_c),FadeIn(vector_c_label),run_time=1.6)
            self.wait(0.8)
            self.play(FadeOut(vector_c),FadeOut(vector_c_label))
            self.wait(1)

        # 动画结束时展示合成的所有向量
        self.wait(1)
