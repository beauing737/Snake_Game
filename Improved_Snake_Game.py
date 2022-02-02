###SNAKE GAME 2.0###

from cisc108 import assert_equal
from designer import *
from random import randint

World = {
    'Snake Head': DesignerObject,
    'Snake Direction': str,
    'Snake': [DesignerObject],
    'Recording Placement':[int],
    'Food': [DesignerObject],
    'Food Count':int,
    'Past Movement': [str],
    'Past Turn':[],
    'Snake Speed':int,
    'Background':[DesignerObject],
    'Snake Lenght': int,
    'Text Snake Lenght': DesignerObject,
    'Bounds': [],
    'Big Count':int,
    'Start Count':int,
    'Text 1':DesignerObject,
    'Text Title':DesignerObject,
    'lower title text':DesignerObject
    }

def Snake_head ()-> DesignerObject:
    face_background = circle('black', 28 , get_width()/2-21 , get_height()/4-4)
    Top_head = circle('green', 25 , get_width()/2-18 , get_height()/4)
    Snake_eye_L = circle('red', 8 , get_width()/2+10 , get_height()/4+16)
    Snake_eye_R = circle('red', 8 , get_width()/2-10 , get_height()/4+16)
    Snake_center_face = rectangle('green' , 36 , 36 , get_width()/2-11 , get_height()/4+20)
    bottom_head = circle('green', 18 , get_width()/2-11 , get_height()/4+45)
    Snake_nose_L = circle('black' , 6 , get_width()/2-8 , get_height()/4+58)
    Snake_nose_R = circle('black' , 6 , get_width()/2+8 , get_height()/4+58)
    Snake_pupules_L = line('black', get_width()/2+18 , get_height()/4+17 , get_width()/2+18 , get_height()/4+32 ,thickness=3)
    Snake_pupules_R = line('black', get_width()/2-2 , get_height()/4+17 , get_width()/2-2 , get_height()/4+32 ,thickness=3)
    return group(face_background,Top_head,Snake_center_face,bottom_head,Snake_nose_L,Snake_nose_R,Snake_eye_L,Snake_eye_R,Snake_pupules_L,Snake_pupules_R)

def Snake_body ()-> DesignerObject:
    Snake_link = rectangle('green' , 45 , 45 , get_width()/2-16 , get_height()/4-30 )
    Snake_scale = rectangle('yellow', 15 , 15 , get_width()/2-16 , get_height()/4-30)
    a = rectangle('black', 17 , 17 , get_width()/2-16 , get_height()/4-30)
    Snake_scale_2 = rectangle('yellow', 15 , 15 , get_width()/2+14 , get_height()/4-30)
    b = rectangle('black', 17 , 17 , get_width()/2+12 , get_height()/4-30)
    Snake_scale_3 = rectangle('yellow', 15 , 15 , get_width()/2+14 , get_height()/4)
    c = rectangle('black', 17 , 17 , get_width()/2+12 , get_height()/4-2)
    Snake_scale_4 = rectangle('yellow', 15 , 15 , get_width()/2-16 , get_height()/4)
    d = rectangle('black' , 17 , 17 , get_width()/2-16 , get_height()/4-2)
    Snake_scale_5 = rectangle('yellow', 15 , 15 , get_width()/2-1 , get_height()/4-15)
    e = rectangle('black', 19 , 19 , get_width()/2-3 , get_height()/4-17)
    boarder = rectangle('black', 49 , 45 , get_width()/2-18 , get_height()/4-30)
    return group(boarder,Snake_link,a,b,c,d,e,Snake_scale,Snake_scale_2,Snake_scale_3,Snake_scale_4,Snake_scale_5)

def Background_Screen ()->DesignerObject:
    Snake_center_face = circle('black',600,-200,-200)
    Top_rectangle = rectangle('gray', get_width()-20 , 50 , 10 , 10)
    Bottom_rectangle = rectangle('white',get_width()-20 , get_height()-80,10,70)
    Inside_center = rectangle('black',get_width()-30,get_height()-90,15,75)
    return group(Snake_center_face,Top_rectangle,Bottom_rectangle,Inside_center)

def apple()->DesignerObject:
    side_circle_1 = circle('red',15,200,300)
    side_circle_2 = circle('red',15,215,300)
    below_1 = circle('red',10,207,320)
    below_2 = circle('red',10,219,320)
    rectangle_1 = rectangle('red',20,15,224,310)
    rectangle_1['angle'] = 69
    rectangle_2 = rectangle('red',20,15,200,310)
    rectangle_2['angle'] = 295
    steam = rectangle('brown', 6 , 15 , 216 , 288)
    steam['angle'] = 15
    leaf = rectangle('limegreen', 6 , 9 , 220 , 288)
    leaf['angle'] = 120
    return group(side_circle_1,side_circle_2,below_1,below_2,rectangle_1,rectangle_2,steam,leaf)

def golden_apple()->DesignerObject:
    side_circle_1 = circle('gold',15,570,300)
    side_circle_2 = circle('gold',15,585,300)
    below_1 = circle('gold',10,577,320)
    below_2 = circle('gold',10,589,320)
    rectangle_1 = rectangle('gold',20,15,594,310)
    rectangle_1['angle'] = 69
    rectangle_2 = rectangle('gold',20,15,570,310)
    rectangle_2['angle'] = 300
    steam = rectangle('brown', 6 , 15 ,586 , 288)
    steam['angle'] = 15
    leaf = rectangle('limegreen', 6 , 9 ,590 , 288)
    leaf['angle'] = 120
    return group(side_circle_1,side_circle_2,below_1,below_2,rectangle_1,rectangle_2,steam,leaf)


def Create_World ()-> World:
    return {
    'Background':[Background_Screen()],
    'Snake':[Snake_body()],
    'Snake Head': Snake_head(),
    'Snake Direction': str,
    'Apple': apple(),
    'Golden Apple':golden_apple(),
    'Food Count':0,
    'Past Movement': ['stand by'],
    'Past Turn':[],
    'Recorded Placement':[],
    'Snake Speed':int,
    'Snake Lenght': 3,
    'Text Snake Lenght': DesignerObject,
    'Bounds':[],
    'Speed':Snake_Speed,
    'Big Count':0,
    'Start Count':0,
    'Text 1': text('skyblue' , '' , 20 , get_width() - 275 , 50),
    'Text Title':text('lightgreen' , '' , 45 , 408 , 315),
    'lower title text':text('yellow' , '' , 25 , 410 , 355),
        }


def Snake_Speed(world:World)-> int:
    snake_ = world['Snake Head']
    if snake_['x'] >= get_width()-60 or snake_['x'] <= 60 or snake_['y'] <= 119 or snake_['y'] >= get_height()-61:
        return 1
    else:
        return 5

def movement_collection (world:World , key:str):
    last_turn = world['Past Movement']
    front_turner = World['Snake Direction']
    
    if last_turn:
        if key == 'left':
            if last_turn[-1] != 'right':
                front_turner = 'left'
                world['Past Movement'].append('left')
        if key == 'right':
            if last_turn[-1] != 'left':
                front_turner = 'right'
                world['Past Movement'].append('right')
        if key == 'up':
            if last_turn[-1] != 'down':
                front_turner = 'up'
                world['Past Movement'].append('up')
        if key == 'down':
            if last_turn[-1] != 'up':
                front_turner = 'down'
                world['Past Movement'].append('down')

            
def make_moving (world:World):
    last_turn = world['Past Movement']
    snake_ = world['Snake Head']
    snake_move = world['Snake Direction']
    
    if len(last_turn) > 0:
        if last_turn[-1] == 'left':
            world['Snake Head']['x'] += -Snake_Speed(world)
            world['Snake Head']['angle'] = 270
            world['Recorded Placement'].append(snake_['x'])
        if last_turn[-1] == 'right':
            world['Snake Head']['x'] += Snake_Speed(world)
            world['Snake Head']['angle'] = 90
            world['Recorded Placement'].append(snake_['x'])
        if last_turn[-1] == 'up':
            world['Snake Head']['y'] += -Snake_Speed(world)
            world['Snake Head']['angle'] = 180
            world['Recorded Placement'].append(snake_['y']*-1)
        if last_turn[-1] == 'down':
            world['Snake Head']['y'] += Snake_Speed(world)
            world['Snake Head']['angle'] = 0
            world['Recorded Placement'].append(snake_['y']*-1)
            

'''
def follow_up (world:World):
    count = 0
    for part in world['Snake']:
        count += 1
        print(world['Recorded Placement'])
        if world['Past Movement'] and len(world['Recorded Placement']) > 2:
            if world['Recorded Placement'][-1] > 0:
                part['x'] = world['Recorded Placement'] - (count * -15)
            if world['Recorded Placement'][-1] < 0:
                part['y'] = world['Recorded Placement'] - (count * -15)
'''

def counts(world:World):
    world['Big Count'] += 1
    if len(world['Past Movement']) >= 2:
        world['Start Count'] += 1


def random_apple_proximity(world:World):
    apple_ = world['Apple']
    gold_apple = world['Golden Apple']
    inbounds_x = randint(100,get_width()-100)
    inbounds_y = randint(130,get_height()-100)
    if world['Start Count'] == 1:
        apple_['x'] = inbounds_x
        apple_['y'] = inbounds_y
        gold_apple['x'] = -200
    
    if world['Food Count'] > 0:
        if apple_['x']-15 <= world['Snake Head']['x'] <= apple_['x']+15 or apple_['y']-15 <= world['Snake Head'] <= apple_['y']+15:
            world['Food Count'] += 1
            if world['Food Count'] <= 5:
                apple_['x'] = inbounds_x
                apple_['y'] = inbounds_y


#def apple_count():
                

def text_typing(world:World):    
    world['Text 1']['text'] = 'Big Count: ' + str(world['Big Count']) + '# Start Count: ' + str(world['Start Count']) + ' # Food Count: '+str(world['Food Count'])
    if world['Start Count'] == 0:
        world['Text Title']['text'] = 'Welcome to Snake'
        world['lower title text']['text'] = 'Press Any Arrow To Start'
    else:
        world['Text Title']['text'] = ''
        world['lower title text']['text'] = ''
    
def title_coloring(world:World):
    str_count = str(world['Big Count'])
    if int(str_count[-1]) < 5:
        world['Text Title']['color'] = 'yellow'
        world['lower title text']['color'] = 'lightgreen'
    else:
        world['Text Title']['color'] = 'lightgreen'
        world['lower title text']['color'] = 'yellow'



when('starting', Create_World)
when('typing',movement_collection)
when('updating',make_moving)
#when('updating',follow_up)
when('updating',random_apple_proximity)
when('updating',counts)
when('updating',text_typing)
when('updating',title_coloring)
start()


    