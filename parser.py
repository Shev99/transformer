from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    file = open(fname, "r")
    lines = file.readlines()
    
    i = 0
    while (i < len(lines)):
        
        if (lines[i] == "line\n"):
            args = lines[i+1].split(" ")
            add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            i+=2
        
        elif(lines[i] == "indent\n"):
            ident(transform)
            i++
        
        elif(lines[i] == "scale\n"):
            args = lines[i+1].split(" ")
            mt = make_scale(int(args[0]), int(args[1]), int(args[2]))
            matrix_mult(mt, transform)
            i+=2

        elif(lines[i] == "move\n"):
            args = lines[i+1].split(" ")
            mt = make_translate(int(args[0]), int(args[1]),int(args[2]))
            matrix_mult(mt, transform)
            i+=2
            
        elif(lines[i] == "rotate\n"):
            args = lines[i+1].split(" ")
            if (rotations[0] == "x"):
                mt = make_rotX(int(args[1]))
            if (rotations[0] == "y"):
                mt = make_rotY(int(args[1]))
            if (rotations[0] == "z"):
                mt = make_rotZ(int(args[1]))
            matrix_mult(mt, transform)
            i+=2

        elif(lines[i] == "apply\n"):
            matrix_mult(transform,points)
            i+=1

        elif(lines[i] == "display\n"):
            for r in range(len(points)):
                for c in range(len(points[r])):
                    points[r][c] = int(points[r][c]) 
            draw_lines(points, screen, color)
            display(screen)
            i+=1
            
        elif(lines[i] == "display\n"):
            save_extension(screen,file_lines[i+1].strip())

        elif(lines[i] == "display\n"):
            break
        
        else:
            raise Exception("Unknown command")


