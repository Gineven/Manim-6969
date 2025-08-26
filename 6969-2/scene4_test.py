from  manim import *
import numpy as np
class VectorOperationsScene(Scene):
    def construct(self):
        axes =  NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0},
            axis_config={"include_tip": True, "include_ticks": False},
        )
        axes_new =  NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={"stroke_opacity": 0.3},
            axis_config={"include_tip": True, "include_ticks": False},
        )
        axes.shift(LEFT*3)
        x_label = axes.get_x_axis_label(MathTex("x").scale(1))  # 设置字体大小为1倍
        y_label = axes.get_y_axis_label(MathTex("y").scale(1))
        o_label = Tex("o").next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.2).scale(1) 
        x_label.shift(LEFT*0.8)
        
        self.add(axes,x_label,y_label,o_label)
        self.wait()
        self.play(axes.animate.shift(RIGHT*3),
                  x_label.animate.shift(RIGHT*3),
                  y_label.animate.shift(RIGHT*3),
                  o_label.animate.shift(RIGHT*3),
                  run_time=2,rate_func=smooth)
        self.wait()
        self.play(FadeOut(axes),FadeIn(axes_new))
        self.wait(2)
#以上部分完成坐标轴的右移动，
#加和和数乘元组的公式：
        def add(tuple1,tuple2):
            result = tuple(map(lambda x, y: x + y, tuple1, tuple2))
            return result
        def multiply_tuple(factor, tuple1):
            result = tuple(map(lambda x: x * factor, tuple1))
            return result
        b = [0,0.5,1,8,-1,-2,-8,0]
        path = VGroup()
        #向量ab
        vector_a = Vector((3,1,0), color=BLUE)
        vector_b = Vector((1,2,0), color=YELLOW)
        vector_c = Vector((4,3,0),color=GREEN)
        vector_a_label = MathTex(r"\vec{a}", color=BLUE)
        vector_b_label = MathTex(r"\vec{b}", color=YELLOW)
        vector_a_label.next_to(vector_a.get_end(), UP + RIGHT, buff=0.2)
        vector_b_label.next_to(vector_b.get_end(), UP + RIGHT, buff=0.2)
        self.play(FadeIn(vector_a), FadeIn(vector_b), run_time=2,rate_func=smooth)
        #self.play(FadeOut(vector_a_label),FadeOut(vector_b_label))
        self.play(vector_b.animate.shift(RIGHT*3+UP))
        self.wait()
        self.play(FadeIn(vector_c),run_time=0.8)
        self.wait()
        for i in range(len(b)):
            vector_b_new = Vector(multiply_tuple(b[i],(1,2,0)), color=YELLOW).shift(RIGHT*3+UP)
            vector_c_new = Vector(add((3,1,0),multiply_tuple(b[i],(1,2,0))),color=GREEN)
            displacement = (vector_b_new.get_end() - (3,1,0))*0.01
            new_line = Line((3,1,0), vector_c_new.get_end()-displacement, color=GREEN)
            new_line.set_stroke(width=6)
            if i == 0: 
                vector_b_temp = vector_b.copy()
                vector_c_temp = vector_c.copy()
                path_temp = path.copy()
                path_temp.set_stroke(width=6)
                path.set_stroke(width=6)
                self.play(ReplacementTransform(vector_b,vector_b_temp),run_time=0.5)
                self.play(ReplacementTransform(vector_c,vector_c_temp),run_time=0.5)
            path = VGroup(path_temp,new_line)    
            
            self.play(ReplacementTransform(vector_b_temp,vector_b_new),
                      ReplacementTransform(vector_c_temp,vector_c_new),
                      ReplacementTransform(path_temp, path),   
                      run_time=1.5)
            vector_b_temp = vector_b_new
            vector_c_temp = vector_c_new
            path_temp = path
            
            self.wait(0.8)
        
        self.play(FadeOut(vector_c_new),run_time=2,rate_func = smooth)
        path_a = Line(
            (-20,-45,0),(20,35,0),color=GREEN
        )
        path_a.set_stroke(width=11.25).set_opacity(0.11)
        self.play(FadeIn(path_a),FadeOut(path),FadeOut(path_temp))
        # factor = [0.5,2,4,1,-2,-4,-1,0]
        factor1 = [round(float(x), 2) for x in np.arange(1, 3.8, 0.05)]
        factor2 = [round(float(x), 2) for x in np.arange(1, -3.8, -0.05)]
        factor = factor1 + factor2 + [1]
        trace = VGroup()
        for i in range(len(factor)):
            vector_a_new = Vector((multiply_tuple(factor[i],(3,1,0))),color=BLUE)
            distance = vector_a_new.get_end() - (3,1,0)
            path_new = path_a.copy().shift(distance)
            path_new.set_stroke(width=11.25).set_opacity(0.11)
            if i == 0: 
                vector_a_temp = vector_a.copy()
                path_new_temp = path_a.copy().set_opacity(0.11)
                path_new_temp.set_stroke(width=11.25)
                
                # self.play(ReplacementTransform(path_a,path_new_temp),run_time=0.5)
                # self.play(ReplacementTransform(vector_a,vector_a_temp),run_time=0.5)
                self.play(
                    FadeOut(path_a),FadeOut(vector_a),FadeIn(path_new_temp),FadeIn(vector_a_temp)
                )
                trace = VGroup(path_new)

                


            else: trace = VGroup(path_new_temp.copy(),path_new)#加了copy
            if i in [0,len(factor1),len(factor)-1]: self.play(
                ReplacementTransform(path_new_temp, trace,rate_func=smooth),  
                ReplacementTransform(vector_a_temp,vector_a_new,rate_func=smooth),
                #FadeIn(trace),FadeOut(path_new_temp),
                run_time=1.5
                
                )




            
             
            else :self.play(
                #ReplacementTransform(path_new_temp, trace,rate_func=linear),  
                ReplacementTransform(vector_a_temp,vector_a_new,rate_func=linear), 
                FadeIn(trace,rate_fun=smooth),path_new_temp.animate.set_opacity(0) , 
                run_time=0.05     
                )
            
            vector_a_temp = vector_a_new
            path_new_temp = trace
                        
       
        

        self.wait(2)
        self.play(FadeOut(trace),run_time=2,rate_func = smooth)
        self.wait(2)
        self.play(FadeOut(axes_new),FadeOut(x_label),FadeOut(y_label),FadeOut(o_label),FadeOut(vector_a_new),
                  run_time=3, rate_func=smooth)
        self.wait(2)

