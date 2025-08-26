from  manim import *
import numpy as np
class VectorOperationsScene(Scene):
    def construct(self):
        def movelabelpos(tuple1,label1,vec):
            if tuple1[0]==0 and tuple1[1]==0 : label1.next_to(vec.get_end(), UP + RIGHT, buff=0.2)
            elif tuple1[0]>=0 and tuple1[1]>=0 : label1.next_to(vec.get_end(), UP + RIGHT, buff=0.2)
            elif tuple1[0]>=0 and tuple1[1]<=0 : label1.next_to(vec.get_end(), DOWN + RIGHT, buff=0.2)
            elif tuple1[0]<=0 and tuple1[1]<=0 : label1.next_to(vec.get_end(), LEFT + DOWN, buff=0.2)
            else:  label1.next_to(vec.get_end(), LEFT + UP, buff=0.2)




        axes =  NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.3},
            axis_config={"include_tip": True, "include_ticks": False},
        )
        x_label = axes.get_x_axis_label(MathTex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes.get_y_axis_label(MathTex("y").scale(1))
        o_label = Tex("o").next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.2).scale(1) 
        x_label.shift(LEFT*0.8)

        vector_a = Vector((3,1), color=BLUE)
        vector_b = Vector((1,2), color=YELLOW)
        vector_a_label = MathTex(r"\vec{a}", color=BLUE)
        vector_b_label = MathTex(r"\vec{b}", color=YELLOW)
        vector_a_label.next_to(vector_a.get_end(), UP + RIGHT, buff=0.2)
        vector_b_label.next_to(vector_b.get_end(), UP + RIGHT, buff=0.2)

        self.add(axes,x_label,y_label,o_label,vector_a)
        self.wait(3)
        self.play(FadeIn(vector_b),FadeIn(vector_a_label),FadeIn(vector_b_label),rate_func=smooth,run_time=2)


        vec_group_a = [(3,1),(6,3),(2,-3),(-4,-1),(-2,3),(1,1),(2,2),(3,1)]
        vec_group_b = [(1,2),(-2,1),(3,-2),(3,2),(-3,-2),(3,3),(-2,-2),(1,2)]


        for i in range(len(vec_group_a)):
            vec_a = Vector(
                vec_group_a[i],
                color = BLUE
            )    
            vec_b = Vector(
                vec_group_b[i],
                color=YELLOW
            )
            new_a_label = MathTex(r"\vec{a}", color=BLUE).next_to(vec_a.get_end(), UP + RIGHT, buff=0.2)
            new_b_label = MathTex(r"\vec{b}", color=YELLOW).next_to(vec_b.get_end(), UP + RIGHT, buff=0.2)
            movelabelpos(vec_group_a[i],new_a_label,vec_a)
            movelabelpos(vec_group_b[i],new_b_label,vec_b)
            if i == 5:
                new_a_label.next_to(vec_a.get_end(), LEFT, buff=0.6)

            if i == 0:
                vec_a_temp = vector_a.copy()
                vec_b_temp = vector_b.copy()
                label_a_temp = vector_a_label.copy()
                label_b_temp = vector_b_label.copy()
                self.play(ReplacementTransform(vector_a,vec_a_temp),
                          ReplacementTransform(vector_b,vec_b_temp),
                          ReplacementTransform(vector_b_label,label_b_temp),
                          ReplacementTransform(vector_a_label,label_a_temp),
                          run_time=0.8,rate_func=smooth)
                
               
            self.play(ReplacementTransform(vec_a_temp,vec_a),
                          ReplacementTransform(vec_b_temp,vec_b),
                          ReplacementTransform(label_a_temp,new_a_label),
                          ReplacementTransform(label_b_temp,new_b_label),
                          run_time=1.8,rate_func=smooth
                          )
            vec_a_temp = vec_a
            vec_b_temp = vec_b
            label_a_temp = new_a_label
            label_b_temp = new_b_label
            self.wait()
        self.wait(3)
        self.play(FadeOut(axes),FadeOut(x_label),FadeOut(y_label),FadeOut(o_label),
                  FadeOut(vec_a),FadeOut(vec_b),FadeOut(new_a_label),FadeOut(new_b_label))