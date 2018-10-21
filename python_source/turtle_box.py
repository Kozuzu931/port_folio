def regular_polygon(n):
    import turtle
    kame=turtle.Turtle()
    kame.shape("turtle")
    
    for i in range(0,n):
        kame.forward(100)
        kame.right(360/n)

