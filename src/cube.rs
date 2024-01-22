use vulkano::{buffer::BufferContents, pipeline::graphics::vertex_input::Vertex};
#[derive(BufferContents, Vertex)]
#[repr(C)]
pub struct Position {
#[format(R32G32B32_SFLOAT)]
    position: [f32; 3],
}
pub const POSITIONS: [Position;8] = [
Position{position:[1.0, -1.0, -1.0]},
Position{position:[1.0, -1.0, 1.0]},
Position{position:[-1.0, -1.0, 1.0]},
Position{position:[-1.0, -1.0, -1.0]},
Position{position:[1.0, 1.0, -0.999999]},
Position{position:[0.999999, 1.0, 1.000001]},
Position{position:[-1.0, 1.0, 1.0]},
Position{position:[-1.0, 1.0, -1.0]},
];
#[derive(BufferContents, Vertex)]
#[repr(C)]
pub struct Normal {
    #[format(R32G32B32_SFLOAT)]
    normal: [f32; 3],
}
pub const NORMALS: [Normal; 6] = [
Normal {normal: [0.0, -1.0, 0.0]},
Normal {normal: [0.0, 1.0, 0.0]},
Normal {normal: [1.0, 0.0, 0.0]},
Normal {normal: [-0.0, 0.0, 1.0]},
Normal {normal: [-1.0, -0.0, -0.0]},
Normal {normal: [0.0, 0.0, -1.0]},
];pub const INDICES: [u16; 108] = [2,1,1,
3,2,1,
4,3,1,
8,1,2,
7,4,2,
6,5,2,
5,6,3,
6,7,3,
2,8,3,
6,8,4,
7,5,4,
3,4,4,
3,9,5,
7,10,5,
8,11,5,
1,12,6,
4,13,6,
8,11,6,
1,4,1,
2,1,1,
4,3,1,
5,14,2,
8,1,2,
6,5,2,
1,12,3,
5,6,3,
2,8,3,
2,12,4,
6,8,4,
3,4,4,
4,13,5,
3,9,5,
8,11,5,
5,6,6,
1,12,6,
8,11,6,];
