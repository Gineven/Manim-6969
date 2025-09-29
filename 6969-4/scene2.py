# 描述 function

##先出现f(x)=x^2
##公式左侧出现数字2
## 数字2飘入公式并消失， 从公式右侧飘出4

# 描述 transformation
## 上述公式消失，出现""transformation"
## transformation 变成T(v向量)
## 左侧出现二维向量 向公式飞入并消失，公式右侧飞出二维向量

# 文件名: function_to_transform.py

from manim import *

MainSizeScale = 3
class FunctionAndTransformation(Scene):
    def construct(self):
        # e.g. official examples
        # self.eg_fade_anim()

        # --- Part 1: 描述 "function" ---
        self.function_part()

        # --- Part 2: 描述 "transformation" ---
        self.transformation_part()

    # e.g. fade animation
    def eg_fade_anim(self):
        dot = Dot(UP * 2 + LEFT)
        self.add(dot)
        tex = Tex(
            "FadeOut with ", "shift ", r" or target\_position", " and scale"
        ).scale(1)
        animations = [
            FadeOut(tex[0]),
            FadeOut(tex[1], shift=DOWN),
            FadeOut(tex[2], target_position=dot),
            FadeOut(tex[3], scale=0.5),
        ]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))

    def function_part(self):
        # 1. 先出现 f(x)
        func_text = MathTex("f","(x)").scale(MainSizeScale)
        self.play(Write(func_text))
        self.wait(1)

        # 定义f的关系 为 x^2
        f_copy = func_text[0].copy()
        f_process = MathTex("x^2").scale(2).next_to(func_text, UP, buff=1)
        self.play(
            Transform(f_copy, f_process, run_time=2)
        )
        self.wait(1)

        # 2. 公式左侧出现数字 2
        input_num = MathTex("2").scale(MainSizeScale)
        input_num.next_to(func_text, LEFT, buff=2)
        self.play(FadeIn(input_num, shift=UP))
        self.wait(0.5)

        # 3. 数字 2 飞入 f(x) 并逐渐消失
        ## 不清楚 为啥不生效，target
        # self.play(FadeOut(input_num, target=func_text.center))
        self.play(
            FadeOut(input_num, shift=(func_text.get_center() - input_num.get_center()), scale=0.5)
        )

        self.wait(0.5)

        # 4. 从 f(x) 处飞出 4
        result_num = MathTex("4").scale(MainSizeScale)

        # 定义 4 的最终位置
        result_num.next_to(func_text, RIGHT, buff=2)

        # 计算起始位置，即 f(x) 的中心
        start_pos = func_text.get_center()

        # 计算位移向量（从起始位置到最终位置的偏移量）
        # FadeIn 的 shift 参数表示“从哪里来”
        # shift_vector = start_pos - result_num.get_center()
        shift_vector = result_num.get_center() - start_pos

        # 动画：4 从 f(x) 的位置出现，并移动到最终位置
        self.play(FadeIn(result_num, shift=shift_vector, scale=0.2))
        self.wait(2)

        # 保存 f(x) 和 4，以便之后一起消失
        self.function_group = VGroup(func_text, result_num, f_copy)
        self.play(
            FadeOut(self.function_group)
        )
        self.wait(0.5)

    def transformation_part(self):
        # 1. 上述公式消失，出现 "transformation"
        trans_word = Text("Transform").scale(MainSizeScale)
        self.play(
            Write(trans_word)
        )
        self.wait(1)

        # 2. transformation 变成 T(v向量)
        # 同样，将公式分部分，方便引用
        trans_func = MathTex("T", r"(\vec{v})").scale(MainSizeScale)
        self.play(Transform(trans_word, trans_func))
        self.wait(1)

        # 3. 左侧出现二维向量
        input_vect = Matrix([[1], [1]]).next_to(trans_func, LEFT, buff=2).scale(2)
        self.play(FadeIn(input_vect, shift=UP))
        self.wait(0.5)

        # 4. 向量向公式飞入并消失
        v_target = trans_func[1][1] # T(\vec{v}) 中的 \vec{v}
        # self.play(input_vect.animate.move_to(v_target).scale(0.5))
        shift_vector = v_target.get_center() - input_vect.get_center()
        self.play(
            FadeOut(input_vect, shift=shift_vector, scale=0.2),
            run_time=2
        )

        # 5. 公式右侧飞出变换后的二维向量
        # 假设 T 是一个变换矩阵 [[1, 1], [0, 1]] (剪切变换)
        # T * [1, 1] = [2, 1]
        output_vect = Matrix([[2], [1]]).scale(2)
        output_vect.next_to(trans_func, RIGHT, buff=2) # 先放在 T(v) 的位置
        start_pos = trans_func.get_center()
        shift_vector = output_vect.get_center() - start_pos
        self.play(
            FadeIn(output_vect, shift=shift_vector, scale=0.2),
            run_time=2
        )
        # # 动画：输入向量消失，同时 T(v) 整体变换成输出向量
        # self.play(
        #     FadeOut(input_vect),
        #     Transform(trans_word, output_vect) # trans_word 是变换后的 T(v)
        # )
        self.wait(2)

        # 保存 f(x) 和 4，以便之后一起消失
        self.function_group = VGroup(trans_word, output_vect)

        # 清场
        self.play(FadeOut(self.function_group))
        self.wait(1)