
def read_obj_file(file_path):
    vertices = []
    normals = []
    tex_coords = []
    faces = []

    with open(file_path, 'r') as obj_file:
        for line in obj_file:
            tokens = line.strip().split()

            if not tokens:
                continue

            prefix = tokens[0]

            if prefix == 'v':
                # Vértices
                vertex = list(map(float, tokens[1:]))
                vertices.append(vertex)
            elif prefix == 'vn':
                # Normales
                normal = list(map(float, tokens[1:]))
                normals.append(normal)
            elif prefix == 'vt':
                # Coordenadas de textura
                tex_coord = list(map(float, tokens[1:]))
                tex_coords.append(tex_coord)
            elif prefix == 'f':
                # Caras
                face = [tuple(map(int, vertex.split('/'))) for vertex in tokens[1:]]
                faces.append(face)

    return vertices, normals, tex_coords, faces

def main():
    file_path = 'cubo.obj'  # Reemplaza esto con la ruta de tu archivo OBJ
    vertices, normals, tex_coords, faces = read_obj_file(file_path)
    f = open("src/cube.rs", "x")

    f.write("use vulkano::{buffer::BufferContents, pipeline::graphics::vertex_input::Vertex};\n#[derive(BufferContents, Vertex)]\n#[repr(C)]\npub struct Position {\n#[format(R32G32B32_SFLOAT)]\n    position: [f32; 3],\n}\npub const POSITIONS: [Position;"+str(len(vertices))+"] = [\n")
    print("Vertices:")
    for vertex in vertices:
        f.write("Position{position:"+str(vertex)+"},\n")
    f.write("];")

    print("\nNormales:")
    f.write("\n#[derive(BufferContents, Vertex)]\n#[repr(C)]\npub struct Normal {\n    #[format(R32G32B32_SFLOAT)]\n    normal: [f32; 3],\n}\npub const NORMALS: [Normal; "+str(len(normals))+"] = [\n")
    for normal in normals:
        f.write("Normal {normal: "+str(normal)+"},\n")
    f.write("];")

    print("\nCoordenadas de Textura:")
    for tex_coord in tex_coords:
        print(tex_coord)
    f.write("pub const INDICES: [u16; "+str(len(faces)*9)+"] = [")
    print("\nCaras:")
    for face in faces:
        print("Cara:")
        for vertex in face:
            f.write(str(vertex[0])+","+str(vertex[1])+","+str(vertex[2])+",\n") 

if __name__ == "__main__":
    main()
