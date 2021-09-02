import bpy

texture_file1 = "plots/temperature.png"
texture_file2 = "plots/rainfall.png"

globe = bpy.ops.mesh.primitive_uv_sphere_add(segments=180, ring_count=180, radius=2)

mat1 = bpy.data.materials.new(name="globe")
mat1.use_nodes = True

bsdf1 = mat1.node_tree.nodes["Principled BSDF"]
texImage1 = mat1.node_tree.nodes.new('ShaderNodeTexImage')
texImage1.image = bpy.data.images.load(texture_file1)

mat1.node_tree.links.new(bsdf1.inputs['Base Color'], texImage1.outputs['Color'])
mat1.node_tree.links.new(bsdf1.inputs['Base Color'], texImage1.outputs['Color'])

# Create the Displacement node and connect it 
displacement = mat1.node_tree.nodes.new("ShaderNodeDisplacement")
material_output = mat1.node_tree.nodes.get("Material Output")
mat1.node_tree.links.new(displacement.inputs["Height"], texImage1.outputs["Color"])
mat1.node_tree.links.new(material_output.inputs["Displacement"], displacement.outputs["Displacement"])

ob1 = bpy.context.view_layer.objects.active

# Assign it to object
if ob1.data.materials:
    ob1.data.materials[0] = mat1
else:
    ob1.data.materials.append(mat1)
    
###########################################

overlay = bpy.ops.mesh.primitive_uv_sphere_add(segments=180, ring_count=180, radius=2.2)

mat2 = bpy.data.materials.new(name="overlay")
mat2.use_nodes = True

bsdf2 = mat2.node_tree.nodes["Principled BSDF"]
texImage2 = mat2.node_tree.nodes.new('ShaderNodeTexImage')
texImage2.image = bpy.data.images.load(texture_file2)
mat2.node_tree.links.new(bsdf2.inputs['Base Color'], texImage2.outputs['Color'])
mat2.node_tree.links.new(bsdf2.inputs['Alpha'], texImage2.outputs['Alpha'])

ob2 = bpy.context.view_layer.objects.active

# Assign it to object
if ob2.data.materials:
    ob2.data.materials[0] = mat2
else:
    ob2.data.materials.append(mat2)

# enable transparency for eevee
bpy.context.object.active_material.blend_method  = 'BLEND'
bpy.context.object.active_material.shadow_method = 'CLIP'

