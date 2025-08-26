from  manim import *
class scene6(Scene):
    def construct(self):
        axes_2d = NumberPlane(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            background_line_style={
            "stroke_opacity": 0
            },
            axis_config={
            "include_tip": True, 
              # 显示箭头
            "include_ticks":False
            }
        ).shift(LEFT * 3)
        x_label = axes_2d.get_x_axis_label(MathTex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes_2d.get_y_axis_label(MathTex("y").scale(1))  # 设置字体大小为1倍
        o_label = Tex("o").next_to(axes_2d.c2p(0, 0), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        
        self.play(FadeIn(axes_2d),FadeIn(x_label),FadeIn(y_label),FadeIn(o_label),
                  run_time=1.5, rate_func=smooth)
        #y=2x+1
        line = Line(
            axes_2d.c2p(-1.5, -2),
            axes_2d.c2p(1, 2),
            color=BLUE
        )
        self.play(FadeIn(line), run_time=2, rate_func=smooth)
        self.wait(2)
        self.play(FadeOut(line), run_time=2, rate_func=smooth)
        self.wait(1)
        self.play(FadeOut(axes_2d),FadeOut(x_label),FadeOut(y_label),FadeOut(o_label),
                  run_time=1.5, rate_func=smooth)
        self.wait(2)