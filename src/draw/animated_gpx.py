import matplotlib.pyplot as plt
import time
from IPython import display
from xml.dom import minidom
import math 


def drawGPX(master_title, filename, outfilename):
    #READ GPX FILE
    data=open(filename)
    xmldoc = minidom.parse(data)
    track = xmldoc.getElementsByTagName('trkpt')
    elevation=xmldoc.getElementsByTagName('ele')
    datetime=xmldoc.getElementsByTagName('time')
    n_track=len(track)

    #PARSING GPX ELEMENT
    lon_list=[]
    lat_list=[]
    h_list=[]
    time_list=[]
    for s in range(n_track):
        lon,lat=track[s].attributes['lon'].value,track[s].attributes['lat'].value
        elev=elevation[s].firstChild.nodeValue
        lon_list.append(float(lon))
        lat_list.append(float(lat))
        h_list.append(float(elev))
        # PARSING TIME ELEMENT
        dt=datetime[s].firstChild.nodeValue
        time_split=dt.split('T')
        hms_split=time_split[1].split(':')
        time_hour=int(hms_split[0])
        time_minute=int(hms_split[1])
        time_second=int(hms_split[2].split('Z')[0])
        total_second=time_hour*3600+time_minute*60+time_second
        time_list.append(total_second)

    #GEODETIC TO CARTERSIAN FUNCTION
    def geo2cart(lon,lat,h):
        a=6378137 #WGS 84 Major axis
        b=6356752.3142 #WGS 84 Minor axis
        e2=1-(b**2/a**2)
        N=float(a/math.sqrt(1-e2*(math.sin(math.radians(abs(lat)))**2)))
        X=(N+h)*math.cos(math.radians(lat))*math.cos(math.radians(lon))
        Y=(N+h)*math.cos(math.radians(lat))*math.sin(math.radians(lon))
        return X,Y

    #DISTANCE FUNCTION
    def distance(x1,y1,x2,y2):
        d=math.sqrt((x1-x2)**2+(y1-y2)**2)
        return d

    #SPEED FUNCTION
    def speed(x0,y0,x1,y1,t0,t1):
        d=math.sqrt((x0-x1)**2+(y0-y1)**2) *3.6
        delta_t=t1-t0
        s=float(d/delta_t)
        return s


    #POPULATE DISTANCE AND SPEED LIST
    d_list=[0.0]
    speed_list=[0.0]
    l=0
    for k in range(n_track-1):
        if k<(n_track-1):
            l=k+1
        else:
            l=k
        XY0=geo2cart(lon_list[k],lat_list[k],h_list[k])
        XY1=geo2cart(lon_list[l],lat_list[l],h_list[l])
        
        #DISTANCE
        d=distance(XY0[0],XY0[1],XY1[0],XY1[1])
        sum_d=d+d_list[-1]
        d_list.append(sum_d)
        
        #SPEED
        s=speed(XY0[0],XY0[1],XY1[0],XY1[1],time_list[k],time_list[l])
        speed_list.append(s)


    #PLOT TRACK
    f,(track,speed,elevation)=plt.subplots(3,1)
    f.suptitle(master_title, fontsize=14, color="red")
    f.set_figheight(8)
    f.set_figwidth(5)
    plt.subplots_adjust(hspace=0.5)
    track.plot(lon_list,lat_list,'k')
    track.set_ylabel("Latitude")
    track.set_xlabel("Longitude")
    track.set_title("Track Plot")

    #PLOT SPEED
    speed.bar(d_list,speed_list,10,color='w',edgecolor='w')
    speed.set_title("Speed")
    speed.set_xlabel("Distance (m)")
    speed.set_ylabel("Speed (Km/h)")

    #PLOT ELEVATION PROFILE
    base_reg=0
    elevation.plot(d_list,h_list)
    elevation.fill_between(d_list,h_list,base_reg,alpha=0.1)
    elevation.set_title("Elevation Profile")
    elevation.set_xlabel("Distance (m)")
    elevation.set_ylabel("GPS Elevation (m)")
    elevation.grid()


    #ANIMATION/DYNAMIC PLOT
    for i in range(n_track):
        track.plot(lon_list[i],lat_list[i],'yo')
        speed.bar(d_list[i],speed_list[i],30,color='g',edgecolor='g')
        elevation.plot(d_list[i],h_list[i],'ro')
        display.display(plt.gcf())
        display.clear_output(wait=True)
        plt.pause(.2)
    plt.show()
    plt.tight_layout()
    #f.savefig(outfilename, dpi=300)

if __name__ == '__main__':
    master_title = "Electric Scooter + Wheelchair"
    filename = '/Users/lucasmac/Documents/Università/Magistrale/CS-Notes.nosync/Tesi/Tesi/Electric-Scooter-Wheelchair/src/draw/data/2_carrozzina/DarknessBot 09.08.2021 10:34.gpx'
    outfilename = "output/gpx1.png"
    drawGPX(master_title, filename, outfilename)

    master_title = "Electric Scooter Stock Firmware"
    filename = '/Users/lucasmac/Documents/Università/Magistrale/CS-Notes.nosync/Tesi/Tesi/Electric-Scooter-Wheelchair/src/draw/data/only_scooter/DarknessBot 09.08.2021 14:18.gpx'
    outfilename = "output/gpx2.png"
    drawGPX(master_title, filename, outfilename)


