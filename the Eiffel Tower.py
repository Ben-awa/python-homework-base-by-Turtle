import turtle
import math as m

# eiffel_tower

# 输入a,y,输出以(0,y)为中心，向左右各延伸a的线
def draw_heng(a,y,t):
    t.setpos(a, y)
    t.down()
    t.setpos(-a, y)
    t.up()
    return 0

# 输入b,x,y,way输出以(x,y)为下顶点，角度为45的斜线
# way==0 向左 way==1 向右
def draw_xie(b,x,y,way,t):
    t.setpos(x, y)
    t.down()
    if way==0:
        t.setpos(x - b * 1 / m.sqrt(2), y + b * 1 / m.sqrt(2))
    else:
        t.setpos(x + b * 1 / m.sqrt(2), y + b * 1 / m.sqrt(2))
    t.up()
    return 0

# 针对向下画的斜线
# way==2 向左 way==3 向右
def draw_xie_down(b,x,y,way,t):
    t.setpos(x, y)
    t.down()
    if way == 3:
        t.setpos(x + b * 1 / m.sqrt(2), y - b * 1 / m.sqrt(2))
    else:
        t.setpos(x - b * 1 / m.sqrt(2), y - b * 1 / m.sqrt(2))
    t.up()
    return 0

# 输入c,y,way，以(0,y)为基准，输出以2c为长的斜线，总体为draw_xie函数的plus版
# way==0 向左 way==1 向右
# 没用上
def draw_xie_plus(c,y,way,t):
    # 上半部分
    draw_xie(c, 0, y, way, t)
    # 下半部分
    t.setpos(0,y)
    t.down()
    if way==0:
        t.setpos(c * 1 / m.sqrt(2), y - c * 1 / m.sqrt(2))
    else:
        t.setpos(-c * 1 / m.sqrt(2), y - c * 1 / m.sqrt(2))
    t.up()
    return 0

# 递归画横线
# 适用于梯形、长方形、三角形
# 输入顶部横线点横坐标x1,x2和底部横线顶点横坐标,x3,x4,输入顶部和底部纵坐标y1,y2,输入想要的数量n，输入画笔t
def draw_heng_more(x1,x2,y1,x3,x4,y2,n,t):
    d1 = abs(x2 - x1)
    d2 = abs(x3 - x4)
    h = abs(y2 - y1)
    blank = n+1 # 间隔n+1个空白

    for i in range(1,blank):
        y_now = min(y1,y2) + i * h / blank
        d_now = max(d1,d2) - abs(d1 -d2)/blank * i
        draw_heng(d_now / 2, y_now, t)
    return 0

# 0.初始化
def Function():
    t = turtle.Turtle()
    t.speed(0)
    turtle.screensize(600, 600, "lightblue")
    screen = turtle.Screen()
    # screen.bgcolor("lightblue")
    screen.title("Tower by Ben_awa")
    t.hideturtle()
    return t

# 1. 底层结构
def draw_tower_down(x1 , y1 , x2 , y2 , t):
    # x2 - x1 == 300 ,y1==y2
    # 宽度60
    # 1. 画第一层

    # 左脚
    t.up()
    t.setpos(x1, y1)
    t.down()
    t.setpos(x1 + 60, y1)
    t.up()

    # 右脚
    t.setpos(x2, y2)
    t.down()
    t.setpos(x2 - 60, y2)
    t.up()

    # 脚的内顶点和梯形上端顶点x一致
    h1 = 120


    # 上边围起来
    t.setpos(x1, y1)
    t.down()
    t.setpos(x1 + 60, y1 + h1)
    t.setpos(x2 - 60, y2 + h1)
    t.setpos(x2, y2)
    t.up()

    t.fillcolor("black")
    t.begin_fill()
    # 平行于圆的两条线
    t.setpos(x1 + 50, y1)
    t.down()
    t.setpos(x1 + 50 + 45, y1 + 90)
    t.setpos(x2 - 50 - 45, y2 + 90)
    t.setpos(x2 - 50, y2)
    t.up()
    t.end_fill()

    t.fillcolor("lightblue")
    t.begin_fill()
    # 内圆半径d==90,角度180
    t.setpos(x2 - 60, y2)
    t.down()
    t.seth(90)
    t.circle(90, 180)
    t.up()
    t.end_fill()

    # 中间横线
    t.setpos(x1 + 45, y1 + 90)
    t.down()
    t.setpos(x2 - 45, y2 + 90)
    t.up()

    # 斜面内饰
    # 左
    draw_xie(28, x1 + 35, y1 + 70, 1, t)
    draw_xie(78, x1 + 17, y1 + 35, 1, t)
    draw_xie(128,x1,y1,1,t)
    draw_xie(84, x1 + 20, y1, 1, t)
    draw_xie(35, x1 + 40, y1, 1, t)

    draw_xie(28, x1 + 30, y1, 0, t)
    draw_xie(58, x1 + 60, y1, 0, t)
    draw_xie(48, x1 + 60 + 7, y1 + 35, 0, t)
    draw_xie(51, x1 + 60 + 20, y1 + 55, 0, t)
    draw_xie(22, x1 + 60 + 35, y1 + 75, 0, t)

    # 右
    draw_xie(28, x2 - 35, y2 + 70, 0, t)
    draw_xie(78, x2 - 17, y2 + 35, 0, t)
    draw_xie(128,x2, y2,0,t)
    draw_xie(84, x2 - 20, y2, 0, t)
    draw_xie(35, x2 - 40, y2, 0, t)

    draw_xie(28, x2 - 30, y2, 1, t)
    draw_xie(58, x2 - 60, y2, 1, t)
    draw_xie(48, x2 - 60 - 7, y2 + 35, 1, t)
    draw_xie(51, x2 - 60 - 20, y2 + 55, 1, t)
    draw_xie(22, x2 - 60 - 35, y2 + 75, 1, t)

    # 梯形处的横线
    draw_heng_more(x1 + 45, x2 - 45, y1 + 90, x1 + 60, x2 - 60, y1 + h1, 8, t)

    # 中间层
    t.fillcolor('black')
    t.begin_fill()
    t.setpos(x1 + 55, y1 + h1)
    t.down()
    t.setpos(x2 - 55, y2 + h1)
    t.setpos(x2 - 60, y2 + h1-4)
    t.setpos(x1 + 60, y1 + h1 - 4)
    t.setpos(x1 + 55, y1 + h1)
    t.end_fill()
    t.up()




    # # 2.小梯形 (下面有重复的)
    # t.setpos(x1 + 60, y1)
    # t.down()
    # t.setpos(x1 + 60 + 45, y2 + 90)
    # t.setpos(x2 - 60 - 45, y2 + 90)
    # t.setpos(x2 - 60, y2)
    # t.up()

    # 3. 细节
    # 底座拱门的斜线
    # for x in range(30):
    #     t.setpos(x1 + 2 * x, y1)
    #     t.down()
    #     t.setpos(x1 + 2 * x + 60, y1 + 120)
    #     t.up()
    # for x in range(30):
    #     t.setpos(x2 - 2 * x, y2)
    #     t.down()
    #     t.setpos(x2 - 2 * x - 60, y2 + 120)
    #     t.up()
    # # 底座拱门的横线
    # for high in range(30):
    #     t.setpos(x1 + high*1.5,y1 + high * 3)
    #     t.down()
    #     t.setpos(x1 + 60 + high*1.5,y1 + high * 3)
    #     t.up()

    # 180 ~ 210
    # for i in range(19):
    #     t.setpos(x1+60-i, y1+120-i*2)
    #     t.down()
    #     t.setpos(x2-60+i, y1+120-i*2)
    #     t.up()

# 2. 画中下层铁架结构
def draw_tower_middle(x1 , y1 , x2 , y2 , t):
    # 中下层外部框架
    t.setpos(x1 + 10  , y1)
    t.down()
    t.setpos(x1  + 45, y1 + 120)
    t.setpos(x2 - 45, y2 + 120)
    t.setpos(x2 - 10, y2)
    t.up()

    # 内部框架
    t.setpos(x1 + 50, y1)
    t.down()
    t.setpos(x1 + 50 + 30, y1 + 100)
    t.setpos(x2 - 50 - 30, y2 + 100)
    t.setpos(x2 - 50, y2)
    t.up()

    t.setpos(x1 + 45 - 7.5, y1 + 100)
    t.down()
    t.setpos(x2 - 45 + 7.5, y2 + 100)
    t.up()

    # 内部斜线
    # 左
    draw_xie(50, x1 + 25, y1, 1, t)
    draw_xie(20, x1 + 40, y1, 1, t)

    draw_xie(80, x1 + 10, y1, 1, t)
    draw_xie(80, x1 + 16, y1 + 20, 1, t)
    draw_xie(80, x1 + 22, y1 + 40, 1, t)

    draw_xie(57, x1 + 28, y1 + 60, 1, t)
    draw_xie(28, x1 + 34, y1 + 80, 1, t)


    draw_xie(30, x1 + 35, y1, 0, t)

    draw_xie(45, x1 + 50, y1, 0, t)
    draw_xie(45, x1 + 56, y1 + 20, 0, t)
    draw_xie(45, x1 + 62, y1 + 40, 0, t)
    draw_xie(45, x1 + 68, y1 + 60, 0, t)

    draw_xie(30, x1 + 74, y1 + 80, 0, t)

    # 右
    draw_xie(50, x2 - 25, y2, 0, t)
    draw_xie(20, x2 - 40, y2, 0, t)

    draw_xie(80, x2 - 10, y2, 0, t)
    draw_xie(80, x2 - 16, y2 + 20, 0, t)
    draw_xie(80, x2 - 22, y2 + 40, 0, t)

    draw_xie(57, x2 - 28, y2 + 60, 0, t)
    draw_xie(28, x2 - 34, y2 + 80, 0, t)


    draw_xie(30, x2 - 35, y2, 1, t)

    draw_xie(45, x2 - 50, y2, 1, t)
    draw_xie(45, x2 - 56, y2 + 20, 1, t)
    draw_xie(45, x2 - 62, y2 + 40, 1, t)
    draw_xie(45, x2 - 68, y2 + 60, 1, t)

    draw_xie(30, x2 - 74, y2 + 80, 1, t)



    # 梯形处理
    draw_heng_more(x1 + 37.5, x2 - 37.5, y1+100, x1 + 45, x2 - 45, y1 + 120, 5, t)

    # 中间层和涂黑
    t.setpos(x1 + 45 - 3, y1 + 120 + 6)
    t.down()
    t.setpos(x2 - 45 + 3, y2 + 120 + 6)
    t.setpos(x2 - 45, y2 + 120)
    t.setpos(x1 + 45, y1 + 120)
    t.setpos(x1 + 45 - 3, y1 + 120 + 6)
    t.fillcolor('black')
    t.begin_fill()
    t.setpos(x1 + 45 - 4, y1 + 120 + 12)
    t.setpos(x2 - 45 + 4, y2 + 120 + 12)
    t.setpos(x2 - 45 + 3, y2 + 120 + 6)
    t.setpos(x1 + 45 - 3, y1 + 120 + 6)
    t.end_fill()
    t.up()

# 3. 中层往上包括顶层
def draw_tower_up(x1, y1, x2, y2, t):
    # 底下的位置
    x3, y3 = x1 + 7, y1
    x4, y4 = x2 - 7, y2

    # 中上层框架
    t.setpos(x3, y3)
    t.down()
    t.setpos(x3 + 16, y3 + 90)
    t.setpos(x3 + 16 + 16.5, y3 + 200)
    t.setpos(x4 - 16 - 16.5, y4 + 200)
    t.setpos(x4 - 16, y4 + 90)
    t.setpos(x4, y4)
    t.up()

    # 中上层内饰

    # 中间线+三角形
    t.setpos(0, y3 + 200)
    t.down()
    t.setpos(0, y3+50)
    t.setpos(20,y3)
    t.setpos(-20,y3)
    t.setpos(0,y3+50)
    t.up()

    # 三角形内的横线
    draw_heng_more(-20, 20, y3 + 50, 0,0, y3, 8, t)

    # 斜内饰
    draw_xie(25,-20,y3,0,t)
    draw_xie(25, 20, y3, 1, t)
    draw_xie(30, -16, y3 + 10, 0, t)
    draw_xie(30, 16, y3 + 10, 1, t)
    draw_xie(33, -12, y3 + 20, 0, t)
    draw_xie(33, 12, y3 + 20, 1, t)
    draw_xie(36, -8, y3 + 30, 0, t)
    draw_xie(36, 8, y3 + 30, 1, t)
    draw_xie(39, -4, y3 + 40, 0, t)
    draw_xie(39, 4, y3 + 40, 1, t)

    draw_xie(54, x3, y3, 1, t)
    draw_xie(54, x4, y4, 0, t)

    # 以下是y=y3+50往上的斜线
    draw_xie(43, 0, y3 + 50, 0, t)
    draw_xie(43, 0, y3 + 50, 1, t)
    draw_xie_down(60, 0, y3 + 50, 2, t)
    draw_xie_down(60, 0, y3 + 50, 3, t)

    draw_xie(35, 0, y3 + 70, 0, t)
    draw_xie(35, 0, y3 + 70, 1, t)
    draw_xie_down(54, 0, y3 + 70, 2, t)
    draw_xie_down(54, 0, y3 + 70, 3, t)

    draw_xie(32, 0, y3 + 90, 0, t)
    draw_xie(32, 0, y3 + 90, 1, t)
    draw_xie_down(47, 0, y3 + 90, 2, t)
    draw_xie_down(47, 0, y3 + 90, 3, t)

    draw_xie(30, 0, y3 + 110, 0, t)
    draw_xie(30, 0, y3 + 110, 1, t)
    draw_xie_down(39, 0, y3 + 110, 2, t)
    draw_xie_down(39, 0, y3 + 110, 3, t)

    draw_xie(27.5, 0, y3 + 130, 0, t)
    draw_xie(27.5, 0, y3 + 130, 1, t)
    draw_xie_down(32, 0, y3 + 130, 2, t)
    draw_xie_down(32, 0, y3 + 130, 3, t)

    draw_xie(23, 0, y3 + 150, 0, t)
    draw_xie(23, 0, y3 + 150, 1, t)
    draw_xie_down(28, 0, y3 + 150, 2, t)
    draw_xie_down(28, 0, y3 + 150, 3, t)

    draw_xie(19.5, 0, y3 + 170, 0, t)
    draw_xie(19.5, 0, y3 + 170, 1, t)
    draw_xie_down(24, 0, y3 + 170, 2, t)
    draw_xie_down(24, 0, y3 + 170, 3, t)

    # 中间层
    t.setpos(x3 + 16 + 16.5, y3 + 200)
    t.down()
    t.setpos(x3 + 16 + 16.5 - 1, y3 + 206)
    t.setpos(x4 - 16 - 16.5 + 1, y4 + 206)
    t.setpos(x4 - 16 - 16.5, y4 + 200)
    t.up()

    # 中间层上面的圆
    t.goto(x4 - 16 - 16.5 + 1, y4 + 206)
    t.setheading(90)
    t.down()
    # print(x4 - 16 - 16.5 + 1, y4 + 206)
    # print(x3 + 16 + 16.5 - 1, y3 + 206)
    t.circle(10.5,180)
    t.up()

    # 顶端部分
    t.setpos(-1,y4 + 206 + 10.5)
    t.down()
    t.setpos(1,y4 + 206 + 10.5)
    t.setpos(0, y4 + 206 + 10.5 + 50.5)
    t.setpos(-1, y4 + 206 + 10.5)
    t.up()

# 4. 一点点环境
def draw_additional_details(t):
    """添加额外的环境细节"""
    # 添加地面
    t.color("green")
    t.setpos(-200, -250)
    t.down()
    t.setpos(200, -250)
    t.up()

    # 添加云朵
    t.color("white")
    for x, y in [(-100, 100), (120, 80), (-180, 150)]:
        t.setpos(x, y)
        t.down()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.up()
        t.setpos(x + 20, y + 5)
        t.down()
        t.begin_fill()
        t.circle(12)
        t.end_fill()
        t.up()
        t.setpos(x + 35, y - 3)
        t.down()
        t.begin_fill()
        t.circle(10)
        t.end_fill()
        t.up()

# 主函数
def main():
    t = Function()
    draw_tower_down(-150, -250, 150, -250, t)
    draw_tower_middle(-90, -130, 90, -130, t)
    draw_tower_up(-49, 2, 49, 2, t)
    draw_additional_details(t)
    # 用户在屏幕上单击后退出
    turtle.Screen().exitonclick()

if __name__ == "__main__":
    main()
