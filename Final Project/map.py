

#305x305 # 20px padding around sides so in reality 265x265, each line 20px long, 2 lines, so 225 x 225 
#
#

canvas = makeEmptyPicture(305, 305)
show (canvas)



addRectFilled(canvas, 115, 20, 75, 75, gray)#backstage
addText(canvas,120,25, 'Backstage', black)

addLine(canvas, 190, 95, 210, 115, black) ######line Backstage to Staging Area

addRectFilled(canvas, 210, 20, 75, 75, gray)#trailer
addText(canvas,220,25, 'Trailer', black)

addRectFilled(canvas, 20, 115, 75, 75, gray)#spectator seats
addText(canvas,25,120, 'Spectator Seats', black)

addLine(canvas, 95, 152, 115, 152, black) ######line Spectator Seats to Circus Tent

addRectFilled(canvas, 115, 115, 75, 75, gray)#circus Tent
addText(canvas,120,120, 'Circus Tent', black)

addLine(canvas, 153, 115, 153, 95, black) ######line Circus Tent to Backstage
addLine(canvas, 190, 152, 210, 152, black) ######line Circus Tent to Staging Area

addRectFilled(canvas, 210, 115, 75, 75, gray)#staging area
addText(canvas,215,120, 'Staging Area', black)

addLine(canvas, 248, 115, 248, 95, black) ######Staging Area to Trailer

addRectFilled(canvas, 115, 210, 75, 75, gray)#ticket gate
addText(canvas,120, 215, 'ticket Gate', black)

addLine(canvas, 153, 210, 153, 190, black) ######line Ticket Gate to Circus Tent
addLine(canvas, 115, 210, 95, 190, black) ######line Ticket Gate to Spectator Seats


addRectFilled(canvas, 210, 210, 75, 75, gray)#security room
addText(canvas,215,215, 'Security Room', black)

addLine(canvas, 247, 210, 247, 190, black) ######line Security Room to Staging Area

addRect(canvas, 115, 20, 75, 75, red)#Tracker



