from  manim import *
class scene6(Scene):
    def construct(self):
        axes_4d = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
            "stroke_opacity": 0.3
            },
            axis_config={
            "include_tip": False, 
              # 显示箭头
            "include_ticks":False
            }
        )
        axes_4d_back = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
            "stroke_opacity": 0.3,
            "stroke_color": GREY
            },
            axis_config={
            "include_tip": False,
            "stroke_width": 0,
              # 显示箭头
            "include_ticks":False
            }
        )
        def trans(p):
    # 返回一个新的坐标向量，x 和 y 坐标根据比例进行缩放
            #return np.array([ -2*p[1]+p[0], 3*p[0], p[2]])  # 假设是三维空间（或者如果是二维，只返回前两个值）
        #将底色的
            return np.array([ 3*p[1]+p[0], -2*p[0], p[2]])# x-> x -2y y-> 3x
        self.play(FadeIn(axes_4d_back), run_time=1.5, rate_func=smooth)
        self.wait(1)
        self.play(FadeIn(axes_4d), run_time=1.5, rate_func=smooth)
        vector_a = Arrow(
            axes_4d.c2p(0,0),
            axes_4d.c2p(1,0),
            color=BLUE,
            
            buff=0
        )
        vector_b = Vector(
            axes_4d.c2p(0,1),
            color=YELLOW,
            
        )
        vector_c = Vector(
            axes_4d.c2p(1,1),
            color=GREEN,
            
        )
        vector_a_new = Vector(
            axes_4d.c2p(1,-2),
            color=BLUE,
            
        )
        vector_b_new = Vector(
            axes_4d.c2p(3,0),
            color=YELLOW,
            
        )
        vector_c_new = Vector(
            axes_4d.c2p(4,-2),
            color=GREEN,
            
        )
        i_label = MathTex(r"\vec{i}").next_to(axes_4d.c2p(1, 0), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        j_label = MathTex(r"\vec{j}").next_to(axes_4d.c2p(0, 1), DOWN + LEFT, buff=0.2).scale(1)
          # 设置字体大小为1倍
        i_label_new = MathTex(r"\vec{i'}").next_to(axes_4d.c2p(1, -2), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        j_label_new = MathTex(r"\vec{j'}").next_to(axes_4d.c2p(3, 0), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        def transform(vector, func):
            return vector.animate.apply_function(func)

        self.play(FadeIn(vector_a), FadeIn(vector_b),FadeIn(vector_c),
                  FadeIn(i_label),FadeIn(j_label)
                  ,run_time=2, rate_func=smooth)
        self.wait(1)    
        self.play(axes_4d.animate.apply_function(trans),
                  #vector_a.animate.apply_function(trans).set_tip_length(0.2),
                  #transform(vector_a,trans),
                  ReplacementTransform(vector_a, vector_a_new),
                  ReplacementTransform(vector_b, vector_b_new),
                  ReplacementTransform(vector_c, vector_c_new),    
                  ReplacementTransform(i_label, i_label_new),
                  ReplacementTransform(j_label, j_label_new),
                  #vector_b.animate.apply_function(trans),
                  #vector_c.animate.apply_function(trans),
                  run_time=2, rate_func=smooth)
        self.wait(2)
        x_label = MathTex("x").next_to(axes_4d.c2p(1, 0), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        y_label = MathTex("y").next_to(axes_4d.c2p(0, 1), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        o_label = Tex("o").next_to(axes_4d.c2p(0, 0), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        self.play(FadeIn(x_label),FadeIn(y_label),FadeIn(o_label),
                  run_time=1.5, rate_func=smooth)
        self.wait(1)

        