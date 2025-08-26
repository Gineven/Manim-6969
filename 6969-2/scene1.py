from  manim import *
class numberline1(Scene):
    def construct(self):
        axis = NumberLine(
            x_range=[-7, 7, 0.5],
            include_ticks=True,
            include_tip=True,
            include_numbers=False
        ).shift(DOWN*2.2)
        
        
        int_ticks = axis.get_tick_marks()
        for i in range(len(int_ticks)):
            if i % 2 == 0 : int_ticks[i].set_length(0.3)
            else: int_ticks[i].set_length(0.15)
        zero_tick = axis.get_tick_marks()[len(axis.get_tick_marks()) // 2]  # 获取刻度为 0 的刻度
        zero_tick.set_color(BLUE) 
        zero_tick.set_length(0.4) 

        axis_a = NumberLine(
            x_range=[-7, 7, 1],
            include_ticks=False,
            include_tip=True,
        ).shift(DOWN*2.2)
        
        axis_temp = NumberLine(
            x_range=[-7, 7, 1],
            include_ticks=False,
            include_tip=True,
        ).shift(DOWN*2.2)
        
        # Make the 0 tick longer
        # zero_tick = axis.get_tick(0)  # default is 0.1
        # zero_tick.set_length(0.3)
        # axis.add(zero_tick)
        #move to DOWM


        self.play(FadeIn(axis_a),run_time=2,rate_func=smooth)
        self.play(ReplacementTransform(axis_a,axis),run_time=1.2)
        
        

        dot = Dot(axis.n2p(2), color=YELLOW)
        self.play(FadeIn(dot), run_time=1.5)

        
        self.play(dot.animate.move_to(axis.n2p(-0.5)), run_time=0.8,rate_func=smooth)
        
        self.play(dot.animate.move_to(axis.n2p(6)), run_time=0.8,rate_func=smooth)
        
        self.play(FadeOut(dot))
        # Set font to Times New Roman for all labels

        #带刻度部分变为不带刻度部分 且向上移动
        # self.play(ReplacementTransform(axis,axis_temp))
        # self.wait(1)
        # self.play(axis_temp.animate.shift(UP*2.2))

        self.play(FadeOut(axis),rate_func=smooth,run_time=2)
        veca = Vector(
            (3,1),
            color = BLUE
        )
        self.play(FadeIn(veca),rate_func=smooth,run_time=2)
        self.wait(2)
        self.play(FadeOut(veca))
        




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
        # 创建二维坐标轴
        axes_2d_temp = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
            "stroke_opacity": 0.3
            },
            axis_config={
            "include_tip": True, 
              # 显示箭头
            "include_ticks":True,
            #
            "include_numbers":True

            }
        )
        axes_2d_a = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
            "stroke_opacity": 0.3
            },
            axis_config={
            "include_tip": True, 
              # 显示箭头
            "include_ticks":False,
            #
            "include_numbers":False

            }
        )
        

        
        
        

        x_label = axes_2d_temp.get_x_axis_label(MathTex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes_2d_temp.get_y_axis_label(MathTex("y").scale(1))  # 设置字体大小为1倍
        o_label = Tex("o").next_to(axes_2d_temp.c2p(0, 0), DOWN + LEFT, buff=0.2).scale(1)  # 设置字体大小为1倍
        self.play(FadeIn(axes_2d_temp),FadeIn(x_label),FadeIn(y_label),FadeIn(o_label),
                  rate_func=smooth,run_time=2)
        self.wait(2)
        #self.play(Write(x_label), Write(y_label), Write(o_label), run_time=2, rate_func=smooth)    
        
        dot1 = Dot(axes_2d_temp.c2p(2,2), color=BLUE)
        dot2 = Dot(axes_2d_temp.c2p(-1,1), color=BLUE)
        self.play(FadeIn(dot1),run_time=1.2)
        self.play(FadeIn(dot2),run_time=1.2)
        vecb = Vector(
            (3,1,0),
            color=BLUE
        ).shift(UP+LEFT)
        vece = Vector(
            (3,1,0),
            color=BLUE
        ).shift(UP+LEFT)
        vecf = Vector(
            (3,1,0),
            color=BLUE
        )
        vecc = vecb.copy().scale(0.7)
        vecd = vecb.copy().scale(1.5)
        vecc1 = vecb.copy().scale(3)
        vecc2 = vecb.copy().scale(0.3)
        self.play(
            ReplacementTransform(VGroup(dot1,dot2),vecb)
        )
        self.wait()
        self.play(
            ReplacementTransform(vecb,vecd)
        )
        self.play(
            ReplacementTransform(vecd,vecc)
        )
        self.play(
            ReplacementTransform(vecc,vece)
        )
        # self.play(
        #     ReplacementTransform(vecc1,vecc2)
        # )
        # self.play(
        #     ReplacementTransform(vecc2,vece)
        # )
        # self.play(vece.animate.shift(DOWN+RIGHT))
        self.play(vece.animate.move_to(axes_2d_temp.c2p(3,1,0)))
        self.play(vece.animate.move_to(axes_2d_temp.c2p(2,-2)))
        self.play(vece.animate.move_to(axes_2d_temp.c2p(-2,-1)))
        self.play(vece.animate.move_to(axes_2d_temp.c2p(1,-1)))
        self.play(vece.animate.move_to(axes_2d_temp.c2p(0,0)))
        self.play(ReplacementTransform(vece,vecf))
        self.play(FadeOut(axes_2d_temp),FadeIn(axes_2d_a),run_time=1.2)


        vector_group = [(6,2),(3,1),(1,2),(-2,3),(-1,-1),(2,-1),(3,1)]
        vector1 = Vector(
            [3, 1, 0],
            color=BLUE,
            #tip_length=0.2
        )  # 起点设置为坐标中心
        
        vector_number_label = MathTex(r"(3,1)", color=BLUE)
        vector_number_label.next_to(vector1.get_end(), UP + RIGHT, buff=0.1)
        self.play(ReplacementTransform(vecf,vector1),Write(vector_number_label),run_time=2)
        for i in range(len(vector_group)):
            vector_new = Vector(vector_group[i],color=BLUE)
            vector_new_label = MathTex(f"{vector_group[i]}", color=BLUE)
            vector_new_label.next_to(vector_new.get_end(), UP + RIGHT, buff=0.1)
            if i == 4: vector_new_label.next_to(vector_new.get_end(), DOWN + LEFT, buff=0.1)
            self.play(ReplacementTransform(vector1,vector_new),
                      ReplacementTransform(vector_number_label,vector_new_label),
                      run_time=1.2)
            self.wait()
            vector1 = vector_new
            vector_number_label = vector_new_label

        self.play(
            FadeOut(axes_2d_a),
            FadeIn(axes_2d),
            #self.play(FadeOut(vector_new_label,run_time=1.2))
            FadeOut(vector_new_label),
            rate_func=smooth,
            run_time=2
        )




        self.play(axes_2d.animate.shift(LEFT*3+DOWN*1.6),
                  #vector_new_label.animate.shift(LEFT*3+DOWN*1.6),
                  vector_new.animate.shift(LEFT*3+DOWN*1.6),
                  x_label.animate.shift(LEFT*3+DOWN*1.6),
                  y_label.animate.shift(LEFT*3+DOWN*1.6),
                  o_label.animate.shift(LEFT*3+DOWN*1.6),
                  )
        self.wait(1)
        #添加标签xy
        

        

        #生成向量
        
        self.play(FadeOut(vector_new),FadeOut(axes_2d),FadeOut(x_label),
                  FadeOut(y_label),FadeOut(o_label),run_time=3)
        self.wait(2)