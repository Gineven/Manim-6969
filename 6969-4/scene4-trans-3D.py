from manim import *
import itertools

class ThreeDLinearTransformationFinal(ThreeDScene):
    
    def get_volumetric_grid(self, axes, color=WHITE, stroke_width=3):
        """一个辅助函数，用于创建真正的三维体网格"""
        grid = VGroup()
        dims = [axes.x_range, axes.y_range, axes.z_range]
        
        ranges = [np.arange(dim[0], dim[1] + dim[2], dim[2]) for dim in dims]
        points = list(itertools.product(*ranges))
        
        # 为了避免绘制超出边界的线，稍微调整一下逻辑
        x_max, y_max, z_max = dims[0][1], dims[1][1], dims[2][1]

        for x, y, z in points:
            if x + 1 <= x_max:
                grid.add(Line(axes.c2p(x, y, z), axes.c2p(x + 1, y, z)))
            if y + 1 <= y_max:
                grid.add(Line(axes.c2p(x, y, z), axes.c2p(x, y + 1, z)))
            if z + 1 <= z_max:
                grid.add(Line(axes.c2p(x, y, z), axes.c2p(x, y, z + 1)))

        grid.set_style(stroke_color=color, stroke_width=stroke_width)
        return grid

    def construct(self):
        target_phi = 65*DEGREES
        target_distance = 4
        
        # 1. 建立三维空间和摄像机
        axes = ThreeDAxes(
            x_range=[-2, 2, 1], y_range=[-2, 2, 1], z_range=[-2, 2, 1],
            x_length=8, y_length=8, z_length=8,
        )
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        self.camera.frame_height = 12

        # 2. 定义变换矩阵
        matrix = np.array([
            [1, 1, 0],
            [0, 1, 0.5],
            [0.5, 0, 1],
        ])

        # 创建初始的白色物体
        original_grid = self.get_volumetric_grid(axes, color=WHITE)
        
        # --- 这是关键的修改点 ---
        # 旧的向量定义方式 (与坐标系缩放不匹配)
        # original_basis_vectors = VGroup(
        #     Vector(RIGHT, color=GREEN), Vector(UP, color=RED), Vector(OUT, color=BLUE)
        # )

        # 新的向量定义方式 (与坐标系单位精确匹配)
        # i_hat = Arrow(ORIGIN, axes.c2p(1, 0, 0), buff=0, color=GREEN, stroke_width=5, tip_length=0.2)
        # j_hat = Arrow(ORIGIN, axes.c2p(0, 1, 0), buff=0, color=RED, stroke_width=5, tip_length=0.2)
        # k_hat = Arrow(ORIGIN, axes.c2p(0, 0, 1), buff=0, color=BLUE, stroke_width=5, tip_length=0.2)

        i_hat = Arrow(ORIGIN, axes.c2p(1, 0, 0), buff=0, color=GREEN, stroke_width=5, max_tip_length_to_length_ratio=0.08)
        j_hat = Arrow(ORIGIN, axes.c2p(0, 1, 0), buff=0, color=RED, stroke_width=5, max_tip_length_to_length_ratio=0.08)
        k_hat = Arrow(ORIGIN, axes.c2p(0, 0, 1), buff=0, color=BLUE, stroke_width=5, max_tip_length_to_length_ratio=0.08)
        original_basis_vectors = VGroup(i_hat, j_hat, k_hat)
        # --- 修改结束 ---

        # 显示坐标轴和白色原始网格/向量
        self.add(axes)
        self.play(Create(original_grid), Create(original_basis_vectors))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(1)

        # 显示变换矩阵
        matrix_mob = Matrix(matrix, h_buff=1.5).scale(0.8)
        matrix_title = Text("Transformation Matrix").next_to(matrix_mob, UP)
        matrix_group = VGroup(matrix_title, matrix_mob)
        # self.add_fixed_in_frame_mobjects(matrix_group.to_corner(UL))
        self.wait(1)

        # 复制一份，变为蓝色，然后执行变换
        transformed_grid = original_grid.copy().set_color(BLUE)
        self.stop_ambient_camera_rotation()
        
        self.add(transformed_grid, original_basis_vectors) # original_basis_vectors 已经在场景中了
        original_grid.set_opacity(0.5)
        self.wait(0.5)

        # 执行核心动画
        self.play(
            FadeOut(original_grid),  # 使用FadeOut而不是Uncreate，效果更平滑
            ApplyMatrix(matrix, transformed_grid),
            ApplyMatrix(matrix, original_basis_vectors),
            run_time=3
        )
        self.wait(2)
        origin_zoom = self.camera.get_zoom()
        self.move_camera(zoom=origin_zoom+1.5, run_time=2),
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(8)
        
        self.stop_ambient_camera_rotation()
        self.wait(2)
        self.move_camera(zoom=origin_zoom, run_time=2)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)