from  manim import *
class scene6(Scene):
    def construct(self):
        axes_2d = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
            "stroke_opacity": 0
            },
            axis_config={
            "include_tip": True, 
              # 显示箭头
            "include_ticks":False
            }
        )
        axes_2d_new = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
            "stroke_opacity": 0.3
            },
            axis_config={
            "include_tip": True, 
              # 显示箭头
            "include_ticks":False
            }
        )

        x_label = axes_2d.get_x_axis_label(MathTex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes_2d.get_y_axis_label(MathTex("y").scale(1))  # 设置字体大小为1倍
        o_label = Tex("o").next_to(axes_2d.c2p(0, 0), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        x_label.shift(LEFT*0.4)
        
        vector_a = Vector(
            (3,1),
            color=BLUE
        )
        

        vector_2a = Vector(
            (6,2),
            color=BLUE
        ).shift(LEFT*3+DOWN*1.6)

        vector_a_1 = Vector(
            (4.5,1.5),
            color=BLUE
        )
        vector_a_2 = Vector(
            (-3,-1),
            color=BLUE
        )
        vector_a_copy = Vector(
            (3,1),
            color=BLUE
        )

         
        vector_b = Vector(
            (1,2),
            color=YELLOW
        )
        vector_b_copy = Vector(
            (1,2),
            color=YELLOW
        )
        

        vector_c = Vector(
            (4,3),
            color=GREEN
        )
        
        axes_2d.shift(LEFT*3+DOWN*1.6)
        #vector_new_label.animate.shift(LEFT*3+DOWN*1.6),
        vector_a.shift(LEFT*3+DOWN*1.6)
        vector_b.shift(LEFT*3+DOWN*1.6)
        vector_c.shift(LEFT*3+DOWN*1.6)
        x_label.shift(LEFT*3+DOWN*1.6)
        y_label.shift(LEFT*3+DOWN*1.6)
        o_label.shift(LEFT*3+DOWN*1.6)
        

        self.play(
            FadeIn(vector_a),FadeIn(axes_2d),FadeIn(x_label),
                  FadeIn(y_label),FadeIn(o_label),run_time=2, rate_func=smooth
        )

        self.wait(2)
        self.play(FadeIn(vector_b),run_time=1.2,rate_func=smooth)
        self.wait(1)
        self.play(vector_b.animate.shift(RIGHT*3+UP),
                  run_time=1.2,rate_func=smooth)
        self.wait(1)

        self.play(vector_a.animate.set_opacity(0.5),
                  vector_b.animate.set_opacity(0.5),
                  FadeIn(vector_c),run_time=2)
        
        self.wait(2)
        self.play(
            FadeOut(vector_b),FadeOut(vector_c),
            vector_a.animate.set_opacity(1)
        )
        self.wait(1)
        self.play(
            ReplacementTransform(vector_a,vector_2a),
            run_time=1.2,rate_func=smooth
        )
        self.wait(1)
        self.play(
            axes_2d.animate.shift(RIGHT*3+UP*1.6),
            x_label.animate.shift(RIGHT*3+UP*1.6),
            y_label.animate.shift(RIGHT*3+UP*1.6),
            o_label.animate.shift(RIGHT*3+UP*1.6),
            vector_2a.animate.shift(RIGHT*3+UP*1.6),
            run_time=2, rate_func=smooth
        )
        self.wait(2)
        self.play(ReplacementTransform(axes_2d,axes_2d_new),)

        self.wait(1)
        self.play(
            ReplacementTransform(vector_2a,vector_a_1),
            run_time=1.2,rate_func=smooth
        )
        self.wait(1)
        self.play(
            ReplacementTransform(vector_a_1,vector_a_2),
            run_time=1.2,rate_func=smooth
        )
        self.wait(1)
        self.play(
            ReplacementTransform(vector_a_2,vector_a_copy),
            run_time=1.2,rate_func=smooth
        )
        self.wait(2)
        self.play(FadeIn(vector_b_copy),run_time=1.2,rate_func=smooth)
        factora = [1,1.5,-0.5,1]
        factorb = [1.5,1.2,1,1]
        for i in range(len(factora)):
            vector_a_new = Vector(
                (factora[i]*3,factora[i]*1),
                color=BLUE
            )
            vector_b_new = Vector(
                (factorb[i]*1,factorb[i]*2),
                color=YELLOW
            )
            vector_c_new = Vector(
                (factora[i]*3+factorb[i]*1,factora[i]*1+factorb[i]*2),
                color=GREEN
            )
            self.play(
                ReplacementTransform(vector_a_copy,vector_a_new),
                ReplacementTransform(vector_b_copy,vector_b_new),
                run_time=1.5, rate_func=smooth
            )
            self.wait(1)
            vector_a_copy = vector_a_new
            vector_b_copy = vector_b_new
            
            if i != 3:
                self.play(
                vector_b_new.animate.shift(factora[i]*3*RIGHT+factora[i]*UP),
                run_time=1.5, rate_func=smooth
            )
                self.play(
                
                vector_a_new.animate.set_opacity(0.5),
                vector_b_new.animate.set_opacity(0.5),
                FadeIn(vector_c_new),
                run_time=1.5, rate_func=smooth
            )
                self.play(
                vector_b_new.animate.shift(factora[i]*3*LEFT+factora[i]*DOWN),
                run_time=1.5, rate_func=smooth
            )
                self.wait(1)
                self.play(
                    FadeOut(vector_c_new),
                    run_time=1.5, rate_func=smooth
            )
            
            
            self.wait(1)
            
            
        self.wait(2)




