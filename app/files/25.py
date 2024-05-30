import sys

def contains(segment,point):
    return (min(segment[0][0],segment[1][0])<=point[0]<=max(segment[0][0],segment[1][0]) and
            min(segment[0][1],segment[1][1])<=point[1]<=max(segment[0][1],segment[1][1]));

def length(segment):
    return ((segment[0][0]-segment[1][0])**2+(segment[0][1]-segment[1][1])**2)**0.5;


t=int(sys.stdin.readline());

for _ in range(t):
    points=set([]);
    segments=[];
    lines=[];
    roof=None;
    for i in range(3):
        segment=list(map(int,sys.stdin.readline().split()));
        lines.append([segment[1]-segment[3],segment[2]-segment[0],segment[0]*segment[3]-segment[1]*segment[2]]);
        p1=(segment[0],segment[1]);
        if p1 in points:
            roof=p1;
        else:
            points.add(p1);
        p2=(segment[2],segment[3]);
        if p2 in points:
            roof=p2;
        else:
            points.add(p2);
        segments.append([p1,p2]);

    #first condition
    if len(points)!=5 or roof==None:
        sys.stdout.write('NO\n');
        continue;

    legs=[];
    for i in range(3):
        if roof in segments[i]:
            legs.append(i);

    if len(legs)!=2:
        sys.stdout.write('NO\n');
        continue;

    connector=3-sum(legs);
    conns=[None,None];
    for i in range(2):
        if lines[legs[i]][0]*segments[connector][0][0]+lines[legs[i]][1]*segments[connector][0][1]+lines[legs[i]][2]==0:
            if contains(segments[legs[i]],segments[connector][0]):
                conns[i]=segments[connector][0];
        if lines[legs[i]][0]*segments[connector][1][0]+lines[legs[i]][1]*segments[connector][1][1]+lines[legs[i]][2]==0:
            if contains(segments[legs[i]],segments[connector][1]):
                conns[i]=segments[connector][1];

    if None in conns or conns[0]==conns[1]:
        sys.stdout.write('NO\n');
        continue;

    #second condition
    endp=[];
    for i in range(2):
        if segments[legs[i]][0]==roof:
            endp.append(segments[legs[i]][1]);
        else:
            endp.append(segments[legs[i]][0]);

    if length(endp)<=abs(length(segments[legs[0]])-length(segments[legs[1]])) or length(endp)**2>length(segments[legs[0]])**2+length(segments[legs[1]])**2:
        sys.stdout.write('NO\n');
        continue;

    #third condition
    if (min(length([conns[0],roof]),length([conns[0],endp[0]]))/max(length([conns[0],roof]),length([conns[0],endp[0]]))<0.25 or
        min(length([conns[1],roof]),length([conns[1],endp[1]]))/max(length([conns[1],roof]),length([conns[1],endp[1]]))<0.25):
            sys.stdout.write('NO\n');
            continue;

    sys.stdout.write('YES\n');
    

    

    




        
