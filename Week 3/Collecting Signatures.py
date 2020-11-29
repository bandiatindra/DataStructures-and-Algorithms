import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments = sorted(segments,  key = lambda x: x[1])
    current = segments[0].end
    points.append(current)

    for s in segments:

        if s.start > current:
            current = s.end
            points.append(current)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
       
    points = optimal_points(segments)
    print(len(points))
    print(*points)
