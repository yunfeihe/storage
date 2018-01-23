import json, tools, ob, values, stage


def loadLevel(n):
    values.blocks = []    
    n = n - 1
    blocks_info = levels[n]
    for i in range(0,len(blocks_info)):
        if(len(blocks_info)==2 and type(blocks_info[1]) != type([])):
            p = blocks_info
        else:
            p = blocks_info[i]
        b = ob.Block(p)
        values.blocks.append(b)
        tools.log("Blocks:",len(values.blocks))
        
    return 1

def loadLevels():
    data_file = open('levels.data')
    data = data_file.read()
    data_file.close()
    return json.loads(data)
    
def level(order):
    values.blocks = []
    if(order == 'plus' and values.level_now < levels_max ):
        tools.log('values.level_now',values.level_now)
        tools.log(levels_max)
        values.level_now += 1
    if(order == 'minus'and values.level_now > 1):
        values.level_now -= 1
    loadLevel(values.level_now)


    
levels = loadLevels()
levels_max = len(levels)        
