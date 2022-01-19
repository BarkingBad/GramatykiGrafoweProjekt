from common import *


def P12(id1, id2, id3):
    global verticies_graph_fragment
    global graph_fragment_list
    id1_middle_vertex = verticies_graph_fragment.get(id1).middle_vertex
    id2_middle_vertex = verticies_graph_fragment.get(id2).middle_vertex
    id3_middle_vertex = verticies_graph_fragment.get(id3).middle_vertex

    if id1_middle_vertex.x < id2_middle_vertex.x == id3_middle_vertex.x:
        P12_vertical_merge_bigger_square_on_left(id1, id2, id3)

    if id1_middle_vertex.x == id3_middle_vertex.x < id2_middle_vertex.x:
        P12_vertical_merge_bigger_square_on_right(id1, id2, id3)

    if id1_middle_vertex.y == id2_middle_vertex.y > id3_middle_vertex.y:
        P12_horizontal_merge_bigger_square_on_bottom(id1, id2, id3)

    if id1_middle_vertex.y > id2_middle_vertex.y == id3_middle_vertex.y:
        P12_horizontal_merge_bigger_square_on_top(id1, id2, id3)


def P12_horizontal_merge_bigger_square_on_bottom(id1, id2, id3):
    global verticies_graph_fragment
    global graph_fragment_list
    graph_fragment_bigger_down = verticies_graph_fragment.get(id3)
    graph_fragment_upper_left = verticies_graph_fragment.get(id1)
    graph_fragment_upper_right = verticies_graph_fragment.get(id2)

    top_left_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_left)
    top_right_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_right)

    bottom_right_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_bigger_down)
    bottom_left_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_bigger_down)

    if top_right_vertex in graph_fragment_bigger_down.vertices:
        y_translation = top_left_vertex.y - bottom_left_vertex.y
        merge_vertices_to_zero_point(top_left_vertex, bottom_left_vertex, graph_fragment_list)
        graph_fragment_modified_list = get_all_connected_graph_fragments_y_sided(graph_fragment_bigger_down)
        to_remove = []
        to_remove_ids = [top_left_vertex.id, top_right_vertex.id, bottom_right_vertex.id]
        to_remove_ids.extend(get_vertices_ids_to_the_bottom(bottom_right_vertex))
    else :
        y_translation = top_right_vertex.y - bottom_right_vertex.y
        merge_vertices_to_zero_point(top_right_vertex, bottom_right_vertex, graph_fragment_list)
        graph_fragment_modified_list = get_all_connected_graph_fragments_y_sided(graph_fragment_bigger_down)
        to_remove = []
        to_remove_ids = [top_left_vertex.id, top_right_vertex.id, bottom_left_vertex.id]
        to_remove_ids.extend(get_vertices_ids_to_the_bottom(bottom_left_vertex))

    vertexes_to_move = graph_fragment_bigger_down.vertices
    for fragment in graph_fragment_modified_list:
        vertexes_to_move += fragment.vertices

    vertexes_to_move = list(dict.fromkeys(vertexes_to_move))

    for v in vertexes_to_move:
        if v.id in to_remove_ids:
            to_remove.append(v)
    for v in to_remove:
        if v in vertexes_to_move:
            vertexes_to_move.remove(v)
    for vertex in vertexes_to_move:
        vertex.y += y_translation


def P12_vertical_merge_bigger_square_on_right(id1, id2, id3):
    global verticies_graph_fragment
    global graph_fragment_list
    graph_fragment_bigger_right = verticies_graph_fragment.get(id2)
    graph_fragment_upper_left = verticies_graph_fragment.get(id1)
    graph_fragment_lower_left = verticies_graph_fragment.get(id3)

    top_left_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_upper_left)
    bottom_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_lower_left)

    top_right_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_bigger_right)
    bottom_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_bigger_right)

    to_remove = []
    if top_left_vertex in graph_fragment_bigger_right.vertices:
        x_translation = bottom_left_vertex.x - bottom_right_vertex.x
        merge_vertices_to_zero_point(top_left_vertex, top_right_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(bottom_left_vertex, bottom_right_vertex, graph_fragment_list)
        to_remove_ids = [top_left_vertex.id, bottom_left_vertex.id]
        to_remove_ids.extend(get_vertices_ids_to_the_right(top_left_vertex))
    else:
        x_translation = top_left_vertex.x - top_right_vertex.x
        merge_vertices_to_zero_point(top_left_vertex, top_right_vertex, graph_fragment_list)
        merge_vertices_to_zero_point(bottom_left_vertex, bottom_right_vertex, graph_fragment_list)
        to_remove_ids = [top_left_vertex.id, bottom_left_vertex.id]
        to_remove_ids.extend(get_vertices_ids_to_the_right(bottom_left_vertex))

    graph_fragment_modified_list = get_all_connected_graph_fragments_x_sided(graph_fragment_bigger_right)
    vertexes_to_move = graph_fragment_bigger_right.vertices
    for fragment in graph_fragment_modified_list:
        vertexes_to_move += fragment.vertices

    vertexes_to_move = list(dict.fromkeys(vertexes_to_move))

    for v in vertexes_to_move:
        if v.id in to_remove_ids:
            to_remove.append(v)

    for v in to_remove:
        if v in vertexes_to_move:
            vertexes_to_move.remove(v)

    for vertex in vertexes_to_move:
        vertex.x += x_translation


def P12_vertical_merge_bigger_square_on_left(id1, id2, id3):
    global verticies_graph_fragment
    global graph_fragment_list
    graph_fragment_bigger_left = verticies_graph_fragment.get(id1)
    graph_fragment_upper_right = verticies_graph_fragment.get(id2)
    graph_fragment_lower_right = verticies_graph_fragment.get(id3)

    top_left_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_bigger_left)
    bottom_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_bigger_left)

    top_right_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_upper_right)
    middle_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)
    bottom_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_lower_right)

    to_remove = []
    if top_left_vertex in graph_fragment_upper_right.vertices:
        x_translation = bottom_left_vertex.x - bottom_right_vertex.x
        merge_vertices_to_zero_point(bottom_left_vertex, bottom_right_vertex, graph_fragment_list)
        to_remove_ids = [top_left_vertex.id, middle_right_vertex.id, bottom_left_vertex.id]
        to_remove_ids.extend(get_vertices_ids_to_the_right(top_left_vertex))
    else:
        x_translation = top_left_vertex.x - top_right_vertex.x
        merge_vertices_to_zero_point(top_left_vertex, top_right_vertex, graph_fragment_list)
        to_remove_ids = [top_left_vertex.id, middle_right_vertex.id, bottom_left_vertex.id]
        to_remove_ids.extend(get_vertices_ids_to_the_right(bottom_left_vertex))

    incorporate_vertex_to_edge(middle_right_vertex, graph_fragment_bigger_left, top_left_vertex, bottom_left_vertex)

    graph_fragment_modified_list = get_all_connected_graph_fragments_x_sided(graph_fragment_lower_right)
    graph_fragment_modified_list.extend(get_all_connected_graph_fragments_x_sided(graph_fragment_upper_right))

    vertexes_to_move = graph_fragment_upper_right.vertices
    vertexes_to_move += graph_fragment_lower_right.vertices

    for fragment in graph_fragment_modified_list:
        vertexes_to_move += fragment.vertices

    vertexes_to_move = list(dict.fromkeys(vertexes_to_move))

    for v in vertexes_to_move:
        if v.id in to_remove_ids:
            to_remove.append(v)

    for v in to_remove:
        if v in vertexes_to_move:
            vertexes_to_move.remove(v)

    for vertex in vertexes_to_move:
        vertex.x += x_translation


def P12_horizontal_merge_bigger_square_on_top(id1, id2, id3):
    global verticies_graph_fragment
    global graph_fragment_list
    graph_fragment_bigger_top = verticies_graph_fragment.get(id1)
    graph_fragment_lower_left = verticies_graph_fragment.get(id2)
    graph_fragment_lower_right = verticies_graph_fragment.get(id3)

    top_left_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_bigger_top)
    top_right_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_bigger_top)

    bottom_left_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_left)
    bottom_middle_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_lower_left)
    bottom_right_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_lower_right)

    to_remove = []
    if top_left_vertex in graph_fragment_lower_left.vertices:
        y_translation = top_right_vertex.y - bottom_right_vertex.y
        merge_vertices_to_zero_point(top_right_vertex, bottom_right_vertex, graph_fragment_list)
        to_remove_ids = [top_left_vertex.id, bottom_middle_vertex.id, top_right_vertex.id]
        to_remove_ids.extend(get_vertices_ids_to_the_bottom(top_left_vertex))
    else:
        y_translation = top_left_vertex.y - bottom_left_vertex.y
        merge_vertices_to_zero_point(top_left_vertex, bottom_left_vertex, graph_fragment_list)
        to_remove_ids = [top_left_vertex.id, bottom_middle_vertex.id, top_right_vertex.id]
        to_remove_ids.extend(get_vertices_ids_to_the_bottom(top_right_vertex))

    incorporate_vertex_to_edge(bottom_middle_vertex, graph_fragment_bigger_top, top_left_vertex, top_right_vertex)

    graph_fragment_modified_list = get_all_connected_graph_fragments_y_sided(graph_fragment_lower_left)
    graph_fragment_modified_list.extend(get_all_connected_graph_fragments_y_sided(graph_fragment_lower_right))

    vertexes_to_move = graph_fragment_lower_left.vertices
    vertexes_to_move += graph_fragment_lower_right.vertices

    for fragment in graph_fragment_modified_list:
        vertexes_to_move += fragment.vertices

    vertexes_to_move = list(dict.fromkeys(vertexes_to_move))

    for v in vertexes_to_move:
        if v.id in to_remove_ids:
            to_remove.append(v)

    for v in to_remove:
        if v in vertexes_to_move:
            vertexes_to_move.remove(v)
    for vertex in vertexes_to_move:
        vertex.y += y_translation


def incorporate_vertex_to_edge(incorporated_vertex: Vertex, incorporating_graph: GraphFragment,
                               vertex_1_in_incorporating_graph: Vertex, vertex_2_in_incorporating_graph: Vertex):
    incorporated_vertex.x = (vertex_1_in_incorporating_graph.x + vertex_2_in_incorporating_graph.x) / 2
    incorporated_vertex.y = (vertex_1_in_incorporating_graph.y + vertex_2_in_incorporating_graph.y) / 2
    edge_to_delete_1 = (vertex_1_in_incorporating_graph.id, vertex_2_in_incorporating_graph.id)
    edge_to_delete_2 = (vertex_2_in_incorporating_graph.id, vertex_1_in_incorporating_graph.id)

    if edge_to_delete_1 in incorporating_graph.edges:
        incorporating_graph.edges.remove(edge_to_delete_1)
    if edge_to_delete_2 in incorporating_graph.edges:
        incorporating_graph.edges.remove(edge_to_delete_2)

    incorporating_graph.edges.append((incorporated_vertex.id, vertex_1_in_incorporating_graph.id))
    incorporating_graph.edges.append((incorporated_vertex.id, vertex_2_in_incorporating_graph.id))


def merge_vertices_to_zero_point(strong_vertex: Vertex, deleted_vertex: Vertex, graph_fragment_list: List[GraphFragment]):
    for single_graph_fragment in graph_fragment_list:
        if deleted_vertex in single_graph_fragment.vertices:
            middle_vertex = single_graph_fragment.middle_vertex
            merge_vertices_to_zero_point_single_operation(strong_vertex, deleted_vertex,
                                                          verticies_graph_fragment.get(middle_vertex.id))


def merge_vertices_to_zero_point_single_operation(top_vertex: Vertex, bottom_vertex: Vertex,
                                                  lower_graph_fragment: GraphFragment):
    bottom_vertex.y = top_vertex.y
    print(lower_graph_fragment.edges)

    to_remove = []
    to_append = []
    for (a, b) in lower_graph_fragment.edges:
        if a == bottom_vertex.id:
            to_remove.append((bottom_vertex.id, b))
            to_append.append((top_vertex.id, b))
        if b == bottom_vertex.id:
            to_remove.append((a, bottom_vertex.id))
            to_append.append((a, top_vertex.id))
    print(to_remove)

    for t in to_remove:
        lower_graph_fragment.edges.remove(t)
    for t in to_append:
        lower_graph_fragment.edges.append(t)

    print(lower_graph_fragment.edges)

    lower_graph_fragment.vertices.remove(bottom_vertex)
    lower_graph_fragment.vertices.append(top_vertex)
