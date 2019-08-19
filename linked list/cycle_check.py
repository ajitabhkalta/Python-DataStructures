def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2 != none & marker2.nextnode !=none:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True

    return False 