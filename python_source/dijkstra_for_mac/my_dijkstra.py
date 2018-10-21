from nodelink import Node,Link

def dijkstra(start,goal):
    for n in Node.get_all_nodes ():
        n.distance=float("inf")
        n.route=None

        start.distance=0
        start.route=[]
        n=start

        distance_finalized={n}
        distance_not_finalized=set()

        while goal not in distance_finalized:

            for e in n.links:
                m=e.opposite(n)
                if m not in distance_finalized:
                    new_m_distance=n.distance+e.lenght
                    if new_m_distance<m.distance:
                        m.distance=new_m_distance
                        m.route=n.route+[e]
                    distance_not_finalized.add(m)

            nearest=None; nearest_distance=float("inf")
            for x in distance_not_finalized:
                if x.distance<nearest_distance:
                   nearest=x
                   nearest_distance=x.distance

            if nearest:
                distance_finalized.add(nearest)
                distance_not_finalized.remove(nearest)
                n=nearest
            else:
                return []
            return goal.route
