minetest.register_node("objtonodebox:test",{
    description="testing",
    drawtype="nodebox",
    node_box={
        type="fixed",
        fixed={-1,-1,-1,1,1,1}
    },
})