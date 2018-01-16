import bpy
import math
import random
import BlenderManager

VERSION = 'Default2'

"""
insertAction('idle', 0, action_frame_start=0, action_frame_end=250)
insertAction('77_04', 100, action_frame_start=30, action_frame_end=70, scale=1.5)
"""

#input is an array of dicts {'group_name1':label, 'group_name2':label...}
def baseAnimation(frames, armature):
    sce = bpy.context.scene

    for frame in range(0, len(frames)):
        sce.frame_set(frame)
        #for every bone in the armature
        for pbone in armature.pose.bones:
            pbone.rotation_mode='XYZ'
            #animate a given bone
            if pbone.name == 'Neck1':
                bpy.ops.object.mode_set(mode='POSE')
                pbone.rotation_euler.rotate_axis('X', 
                    math.radians(math.cos(frame/40)/10*random.random()))
                bpy.ops.object.mode_set(mode='OBJECT')
                
            pbone.keyframe_insert(data_path="rotation_euler" ,frame=frame)

def turningHeadAnimation(frames, armature):
    sce = bpy.context.scene
    
    #for every frame 
    for frame, groups in enumerate(frames):
        sce.frame_set(frame)

        if groups['Head'] == 1:
            #for every bone in the armature
            for pbone in armature.pose.bones:
                pbone.rotation_mode='XYZ'
                #animate a given bone
                if pbone.name == 'Neck1':
                    bpy.ops.object.mode_set(mode='POSE')
                    #angle = math.sin(frame/15)*random.random()*1.3
                    angle = 45
                    pbone.rotation_euler.rotate_axis('Y', math.radians(angle))
                    bpy.ops.object.mode_set(mode='OBJECT')
                    
                pbone.keyframe_insert(data_path="rotation_euler" ,frame=frame)
        elif groups['Head'] == 2:
            #for every bone in the armature
            for pbone in armature.pose.bones:
                pbone.rotation_mode='XYZ'
                #animate a given bone
                if pbone.name == 'Neck1':
                    bpy.ops.object.mode_set(mode='POSE')
                    #angle = math.sin(frame/15)*random.random()*1.3
                    angle = -45
                    pbone.rotation_euler.rotate_axis('Y', math.radians(angle))
                    bpy.ops.object.mode_set(mode='OBJECT')
                    
                pbone.keyframe_insert(data_path="rotation_euler" ,frame=frame)

def BaseAction(frames, armature):
    BlenderManager.insertAction('idle', 0, action_frame_end=len(frames))

def ActionAnimation(frames, armature):
    #print(frames)
    intervals = BlenderManager.getLabelIntervals('Head', '1', frames, threshold=2)
    #print(intervals)
    for (start, end) in intervals:
        size = max(end-start, 50)
        BlenderManager.insertAction('scared', start, action_frame_end=size)


#animation passes
ANIMATIONS = [
    #baseAnimation,
    #turningHeadAnimation,
    BaseAction,
    ActionAnimation
]