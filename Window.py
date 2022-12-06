#Hi! This is the first part of my AutoRig system, it works by now with the joints created and the duplicate for IK and FK system

import maya.cmds as cmds

#INTERFACE

window_Name = "AutoRig_AlfredoLopez"
windowTittle = "AutorRig_AlfredoLopez"
window_w = 200
window_h = 200

fingerJoint = []
fkJoints = []

fingerThumbGrp = []
fingerIndexGrp = []
fingerMiddleGrp = []
fingerRingGrp = []
fingerPinkyGrp = []

fingerThumbGrpMod = []
fingerIndexGrpMod = []
fingerMiddleGrpMod = []
fingerRingGrpMod = []
fingerPinkyGrpMod = []

fingerThumbCtrl = []
fingerIndexCtrl = []
fingerMiddleCtrl = []
fingerRingCtrl = []
fingerPinkyCtrl = []

leftFingersGroups = []
rightFingersGroups = []

leftFingerSystem = "leftFingersSystem_grp"
rightFingerSystem = "rightFingersSystem_grp"

leftFingers = []
rightFingers = []

temp = 0


def create_window():
    if cmds.window(window_Name, query = True, exists = True):
        cmds.deleteUI(window_Name)

    cmds.window(window_Name)
    cmds.window(window_Name, edit = True, width = window_w + 2, height = window_h, title = windowTittle, minimizeButton = False, maximizeButton = False, sizeable = False)

    cmds.columnLayout("Main_Column", width = window_w, height = window_h)
    costumUI()

    cmds.showWindow(window_Name)


def costumUI():
    cmds.button("blendJnts_button", label = "BlendJnts", parent = "Main_Column", width = window_w, height = 40, command = blendJoints)

    cmds.frameLayout("control_scale_frame", label = "control scale", width = window_w, parent = "Main_Column", collapsable = True, backgroundColor = (0.5,0.0,0.5))
    cmds.rowColumnLayout("Controllers", numberOfColumns = 3, width = window_w)
    cmds.button ("fkSystem", label = "FkSystem", width = window_w/3, command = FkSystem)
    cmds.button("ikSystem", label = "IkSystem", width = window_w/3, command = IkSystem)
    cmds.button("switch", label = "IKFKSwitch", width = window_w/3, command = Switch)

    cmds.frameLayout("Fingers", label = "color frame", width = window_w, parent = "Main_Column")
    cmds.colorIndexSliderGrp(maxValue = 250)
    cmds.button("fingerSystem", label = "FingerSystem", height = 30, command = fingerSystem)

###################################################### RIG FUNCTIONS #######################################################################################

#BlendJoints
def blendJoints (*args):
    pass
    ################################################ ARMS ####################################

    # We create the blendColor Node and add a name
    cmds.createNode('blendColors', name = 'left_shoulder_blndColor')
    cmds.createNode('blendColors', name = 'left_elbow_blndColor')
    cmds.createNode('blendColors', name = 'left_wrist_blndColor')

    cmds.createNode('blendColors', name = 'right_shoulder_blndColor')
    cmds.createNode('blendColors', name = 'right_elbow_blndColor')
    cmds.createNode('blendColors', name = 'right_wrist_blndColor')

    cmds.connectAttr('left_shoulder_ikJnt.rotate','left_shoulder_blndColor.color1')
    cmds.connectAttr('left_shoulder_fkJnt.rotate','left_shoulder_blndColor.color2')

    cmds.connectAttr('left_elbow_ikJnt.rotate','left_elbow_blndColor.color1')
    cmds.connectAttr('left_elbow_fkJnt.rotate','left_elbow_blndColor.color2')

    cmds.connectAttr('left_wrist_ikJnt.rotate','left_wrist_blndColor.color1')
    cmds.connectAttr('left_wrist_fkJnt.rotate','left_wrist_blndColor.color2')

    cmds.connectAttr('left_shoulder_blndColor.output', 'left_shoulder_jnt.rotate')
    cmds.connectAttr('left_elbow_blndColor.output', 'left_elbow_jnt.rotate')
    cmds.connectAttr('left_wrist_blndColor.output', 'left_wrist_jnt.rotate')

    cmds.connectAttr('right_shoulder_ikJnt.rotate','right_shoulder_blndColor.color1')
    cmds.connectAttr('right_shoulder_fkJnt.rotate','right_shoulder_blndColor.color2')

    cmds.connectAttr('right_elbow_ikJnt.rotate','right_elbow_blndColor.color1')
    cmds.connectAttr('right_elbow_fkJnt.rotate','right_elbow_blndColor.color2')

    cmds.connectAttr('right_wrist_ikJnt.rotate','right_wrist_blndColor.color1')
    cmds.connectAttr('right_wrist_fkJnt.rotate','right_wrist_blndColor.color2')

    cmds.connectAttr('right_shoulder_blndColor.output', 'right_shoulder_jnt.rotate')
    cmds.connectAttr('right_elbow_blndColor.output', 'right_elbow_jnt.rotate')
    cmds.connectAttr('right_wrist_blndColor.output', 'right_wrist_jnt.rotate')

    ################################################ LEGS ####################################

    cmds.createNode('blendColors', name = 'left_upperLeg_blndColor')
    cmds.createNode('blendColors', name = 'left_knee_blndColor')
    cmds.createNode('blendColors', name = 'left_ankle_blndColor')
    cmds.createNode('blendColors', name = 'left_tarsais_blndColor')

    cmds.createNode('blendColors', name = 'right_upperLeg_blndColor')
    cmds.createNode('blendColors', name = 'right_knee_blndColor')
    cmds.createNode('blendColors', name = 'right_ankle_blndColor')
    cmds.createNode('blendColors', name = 'right_tarsais_blndColor')

    cmds.connectAttr('left_femur_ikJnt.rotate','left_upperLeg_blndColor.color1')
    cmds.connectAttr('left_femur_fkJnt.rotate','left_upperLeg_blndColor.color2')

    cmds.connectAttr('left_knee_ikJnt.rotate','left_knee_blndColor.color1')
    cmds.connectAttr('left_knee_fkJnt.rotate','left_knee_blndColor.color2')

    cmds.connectAttr('left_ankle_ikJnt.rotate','left_ankle_blndColor.color1')
    cmds.connectAttr('left_ankle_fkJnt.rotate','left_ankle_blndColor.color2')

    cmds.connectAttr('left_tarsais_ikJnt.rotate','left_tarsais_blndColor.color1')
    cmds.connectAttr('left_tarsais_fkJnt.rotate','left_tarsais_blndColor.color2')

    cmds.connectAttr('left_femur_blndColor.output', 'left_upperLeg_jnt.rotate')
    cmds.connectAttr('left_knee_blndColor.output', 'left_knee_jnt.rotate')
    cmds.connectAttr('left_ankle_blndColor.output', 'left_ankle_jnt.rotate')
    cmds.connectAttr('left_tarsais_blndColor.output', 'left_tarsais_jnt.rotate')

    cmds.connectAttr('right_femur_ikJnt.rotate','right_upperLeg_blndColor.color1')
    cmds.connectAttr('right_femur_fkJnt.rotate','right_upperLeg_blndColor.color2')

    cmds.connectAttr('right_knee_ikJnt.rotate','right_knee_blndColor.color1')
    cmds.connectAttr('right_knee_fkJnt.rotate','right_knee_blndColor.color2')

    cmds.connectAttr('right_ankle_ikJnt.rotate','right_ankle_blndColor.color1')
    cmds.connectAttr('right_ankle_fkJnt.rotate','right_ankle_blndColor.color2')

    cmds.connectAttr('right_tarsais_ikJnt.rotate','right_tarsais_blndColor.color1')
    cmds.connectAttr('right_tarsais_fkJnt.rotate','right_tarsais_blndColor.color2')

    cmds.connectAttr('right_femur_blndColor.output', 'right_upperLeg_jnt.rotate')
    cmds.connectAttr('right_knee_blndColor.output', 'right_knee_jnt.rotate')
    cmds.connectAttr('right_ankle_blndColor.output', 'right_ankle_jnt.rotate')
    cmds.connectAttr('right_tarsais_blndColor.output', 'right_tarsais_jnt.rotate')

#Finger System
def fingerOrder(fingerGrp, fingerCtrl, hand):
    pass
    childGrp = ''
    childCtrl = ''
    fatherCtrl = ''
    fatherGrp = ''
    baby = ''
    for i, orig in enumerate(fingerGrp):
        if '03' in fingerGrp[i]:
            baby = fingerGrp[i]
        elif '02' in fingerGrp[i]:
            childGrp = fingerGrp[i]
            childCtrl = fingerCtrl[i]
        elif '01' in fingerGrp[i]:
            fatherCtrl = fingerCtrl[i]
            fatherGrp = fingerGrp[i]

    if '03' in baby:
        cmds.parent(baby, childCtrl)

    cmds.parent(childGrp, fatherCtrl)

    if 'left' in fatherGrp:
        cmds.parent(fatherGrp, hand)
    else:
        cmds.parent(fatherGrp, hand)

############################# Create of the controllers and order of fingers ########################

def controlAndFingerOrder(fingerSide):
    for i,orig in enumerate(fingerSide):
        joint_name = fingerSide[i][:-3]
        ctrlName = joint_name + 'ctrl'
        ctrl = cmds.circle(name = ctrlName, normal= [1,0,0], radius = 5, ch = False)
        grpNameMod = ctrlName + 'GrpMod'
        cmds.group(name = grpNameMod)
        grpName = ctrlName + 'GrpPos'
        grp = cmds.group (name= grpName)
        constraint = cmds.parentConstraint(fingerSide[i], grp, mo = False)
        cmds.delete(constraint)
        cmds.parentConstraint(ctrl[0], fingerSide[i], mo= True)
        if 'thumb' in grpName:
            fingerThumbGrp.append(grpName)
            fingerThumbCtrl.append(ctrlName)
            #fingerThumbGrpMod.append(grpNameMod)
        elif 'index' in grpName:
            fingerIndexGrp.append(grpName)
            fingerIndexCtrl.append(ctrlName)
            #fingerIndexGrpMod.append(grpNameMod)
        elif 'middle' in grpName:
            fingerMiddleGrp.append(grpName)
            fingerMiddleCtrl.append(ctrlName)
            #fingerMiddleGrpMod.append(grpNameMod)
        elif 'ring' in grpName:
            fingerRingGrp.append(grpName)
            fingerRingCtrl.append(ctrlName)
            #fingerRingGrpMod.append(grpNameMod)
        elif 'pinky' in grpName:
            fingerPinkyGrp.append(grpName)
            fingerPinkyCtrl.append(ctrlName)
            #fingerPinkyGrpMod.append(grpNameMod)

        if 'left' in fingerSide[i]:
            leftFingersGroups.append(grpNameMod)
        elif 'right' in fingerSide[i]:
            rightFingersGroups.append(grpNameMod)
    
    hand = ''
    if "left" in fingerSide[0]:
        hand = 'leftFingersSystem_ctrl'
        cmds.curve(name = hand, degree = 1.0, point = [(3,0,-10),(5,0,-8),(5,0,6),(-4,0,6),(-6,0,1),(-7,0,-2),(-7,0,-3),(-6,0,-3),(-4,0,-1),(-4,0,-8),(-2,0,-10),(3,0,-10)])
        cmds.parent (hand, leftFingerSystem, relative = True)
        autoFingers(leftFingersGroups, hand)
    elif 'right' in fingerSide[0]:
        hand = 'rightFingersSystem_ctrl' 
        cmds.curve(name = hand, degree = 1.0, point = [(3,0,-10),(5,0,-8),(5,0,6),(-4,0,6),(-6,0,1),(-7,0,-2),(-7,0,-3),(-6,0,-3),(-4,0,-1),(-4,0,-8),(-2,0,-10),(3,0,-10)])
        cmds.parent (hand, rightFingerSystem, relative = True)
        autoFingers(rightFingersGroups, hand)

        
    fingerOrder(fingerThumbGrp, fingerThumbCtrl, hand)
    fingerOrder(fingerIndexGrp, fingerIndexCtrl, hand)
    fingerOrder(fingerMiddleGrp, fingerMiddleCtrl, hand)
    fingerOrder(fingerRingGrp, fingerRingCtrl, hand)
    fingerOrder(fingerPinkyGrp, fingerPinkyCtrl, hand)


################################# Order LEFT AND RIGHT ##################################################
def fingerSide(joints):
    for i,orig in enumerate(joints):
        if 'left' in joints[i]:
            leftFingers.append(joints[i])
        else:
            rightFingers.append(joints[i])
    
    controlAndFingerOrder(leftFingers)
    controlAndFingerOrder(rightFingers)


################################## FINGER SYSTEM-AUTO ##########################################
def autoFingers(fingerGroup, hand):
    cmds.addAttr (hand, longName = 'Fist', niceName = 'Fist', at = 'float', defaultValue = 0, min = 0, max = 20, hidden = False, keyable = True) 
    cmds.addAttr (hand, longName = 'UpFingers', niceName = 'UpFingers', at = 'float', defaultValue = 0, min = 0, max = 10, hidden = False, keyable = True)
    cmds.addAttr (hand, longName = 'Spread', niceName = 'Spread', at = 'float', defaultValue = 0, min = 0, max = 10, hidden = False, keyable = True)
    for i, orig in enumerate (fingerGroup):
        if 'thumb' in fingerGroup[i]:
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Fist', value = 90, driverValue = 20)
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Fist', value = 0, driverValue = 0)
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.UpFingers', value = -30, driverValue = 20)
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.UpFingers', value = 0, driverValue = 0)
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateZ', currentDriver = hand + '.Spread', value = -30, driverValue = 20)
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateZ', currentDriver = hand + '.Spread', value = 0, driverValue = 0)

        else:
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateZ', currentDriver = hand + '.Fist', value = -90, driverValue = 20)
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateZ', currentDriver = hand + '.Fist', value = 0, driverValue = 0)
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateZ', currentDriver = hand + '.UpFingers', value = 45, driverValue = 20)
            cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateZ', currentDriver = hand + '.UpFingers', value = 0, driverValue = 0)
            if 'middle01' in fingerGroup[i]:
                cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Spread', value = -10, driverValue = 20)
                cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Spread', value = 0, driverValue = 0)
            elif 'ring01' in fingerGroup[i]:
                cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Spread', value = 20, driverValue = 20)
                cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Spread', value = 0, driverValue = 0)
            elif 'pinky01' in fingerGroup[i]:
                cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Spread', value = 30, driverValue = 20)
                cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Spread', value = 0, driverValue = 0)
            elif 'index01' in fingerGroup[i]:
                cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Spread', value = -30, driverValue = 20)
                cmds.setDrivenKeyframe(fingerGroup[i] + '.rotateY', currentDriver = hand + '.Spread', value = 0, driverValue = 0)
    
################################### MASTER CODE ##############################

def fingerSystem(*args):
    joint = cmds.ls(type = 'joint')
    for i, orig in enumerate (joint):
        if "thumb" in joint[i] and '_jnt' in joint[i]:
            fingerJoint.append(joint[i])
        if "index" in joint[i] and '_jnt' in joint[i]:
            fingerJoint.append(joint[i])
        if "middle" in joint[i] and '_jnt' in joint[i]:
            fingerJoint.append(joint[i])
        if "ring" in joint[i] and '_jnt' in joint[i]:
            fingerJoint.append(joint[i])
        if "pinky" in joint[i] and '_jnt' in joint[i]:
            fingerJoint.append(joint[i])


    cmds.group(name = leftFingerSystem, empty = True)
    cmds.group(name = rightFingerSystem, empty = True)
    cmds.parentConstraint ('left_wrist_jnt', leftFingerSystem)
    cmds.parentConstraint ('right_wrist_jnt', rightFingerSystem)
    fingerSide(fingerJoint)



#FkSystem
def FkSystem(*args):

    joints = cmds.ls(type = 'joint')
    for i,orig in enumerate(joints):
        if '_fkJnt' in joints[i] or 'clavicle' in joints[i]:
            fkJoints.append(joints[i])
    ############################# Create of the controllers ########################

    for i,orig in enumerate(fkJoints):
        my_joint = fkJoints[i]
        joint_name = fkJoints[i][:-3] 
        ctrl = cmds.circle(name = joint_name + 'ctrl', normal= [1,0,0], radius = 5, ch = False)
        grp = cmds.group (name= (ctrl[0] + 'Grp'))
        constraint = cmds.parentConstraint(fkJoints[i], grp, mo = False)
        cmds.delete(constraint)
        cmds.parentConstraint(ctrl[0], fkJoints[i], mo= True)
        
    ################################ Parent of controllers ####################

    cmds.parent('left_tarsais_fkctrlGrp', 'left_ankle_fkctrl')#### LegCTRLS
    cmds.parent('left_ankle_fkctrlGrp', 'left_knee_fkctrl')
    cmds.parent('left_knee_fkctrlGrp', 'left_femur_fkctrl')
    cmds.parent('left_wrist_fkctrlGrp', 'left_elbow_fkctrl')#### ArmCTRLS
    cmds.parent('left_elbow_fkctrlGrp', 'left_shoulder_fkctrl')
    cmds.parent('left_shoulder_fkctrlGrp', 'left_clavicle_ctrl')

    cmds.parent('right_tarsais_fkctrlGrp', 'right_ankle_fkctrl')#### LegCTRLS
    cmds.parent('right_ankle_fkctrlGrp', 'right_knee_fkctrl')
    cmds.parent('right_knee_fkctrlGrp', 'right_femur_fkctrl')
    cmds.parent('right_wrist_fkctrlGrp', 'right_elbow_fkctrl')#### ArmCTRLS
    cmds.parent('right_elbow_fkctrlGrp', 'right_shoulder_fkctrl')
    cmds.parent('right_shoulder_fkctrlGrp', 'right_clavicle_ctrl')



#IkSystem
def IkSystem(*args):
############################################# LEFT LEGS ########################################################################################

    leftkneePos = cmds.xform('left_knee_ikJnt', query = True, worldSpace = True, translation = True)
    leftanklePos = cmds.xform('left_ankle_ikJnt', query = True, worldSpace = True, translation = True)
    lefttarsaisPos = cmds.xform('left_tarsais_ikJnt', query = True, worldSpace = True, translation = True)
    leftmetaTarsaisPos = cmds.xform('left_metaTarsais_endikJnt', query = True, worldSpace = True, translation = True)

    cmds.ikHandle(n = 'left_leg_RP_ikHandle', sj = 'left_femur_ikJnt', ee = 'left_ankle_ikJnt')
    cmds.ikHandle(n = 'left_leg_ankleTarsais_SC_ikHandle', sol ='ikSCsolver', sj = 'left_ankle_ikJnt', ee = 'left_tarsais_ikJnt')
    cmds.ikHandle(n = 'left_leg_metaTarsais_SC_ikHandle', sol ='ikSCsolver', sj = 'left_tarsais_ikJnt', ee = 'left_metaTarsais_endikJnt')

    cmds.group (n = 'left_leg_metaTarsais_SC_pivotGrp', empty = True)
    cmds.move(leftmetaTarsaisPos[0], leftmetaTarsaisPos[1], leftmetaTarsaisPos[2])
    cmds.parent('left_leg_metaTarsais_SC_ikHandle', 'left_leg_metaTarsais_SC_pivotGrp')
        
    cmds.group (n = 'left_kneeIk_ctrlGrp', em = True)
    cmds.move(leftkneePos[0], leftkneePos[1], leftkneePos[2] + 10)
    cmds.circle(n = 'left_kneeIk_ctrl', r = 1)
    cmds.parent('left_kneeIk_ctrl', 'left_kneeIk_ctrlGrp', relative = True)

    cmds.group (n = 'left_ankleIk_ctrlGrp', em = True)
    cmds.move(leftanklePos[0], leftanklePos[1], leftanklePos[2])
    cmds.circle(n = 'left_ankleIk_ctrl', r = 1)
    cmds.parent('left_ankleIk_ctrl', 'left_ankleIk_ctrlGrp', relative = True)

    cmds.group (n = 'left_footSystem_ctrlGrp', em = True)
    cmds.move(leftanklePos[0], leftanklePos[1], leftanklePos[2])

    cmds.group (n = 'left_footToBall_ctrlGrp', em = True)
    cmds.move(lefttarsaisPos[0], lefttarsaisPos[1], lefttarsaisPos[2])

    cmds.group (n = 'left_ballToToe_ctrlGrp', em = True)
    cmds.move(leftmetaTarsaisPos[0], leftmetaTarsaisPos[1], leftmetaTarsaisPos[2])

    cmds.group(name = 'left_footHeel_ctrlGrp', em = True)
    cmds.move(leftmetaTarsaisPos[0], leftmetaTarsaisPos[1]-5, leftmetaTarsaisPos[2]-25)

    #cmds.poleVectorConstraint('left_kneeIk_ctrl', 'left_leg_RP_ikHandle')
    cmds.parentConstraint('left_ankleIk_ctrl', 'left_leg_RP_ikHandle')

    cmds.parent('left_ankleIk_ctrlGrp', 'left_footToBall_ctrlGrp')
    cmds.parent('left_leg_ankleTarsais_SC_ikHandle', 'left_footToBall_ctrlGrp')
    cmds.parent('left_footToBall_ctrlGrp', 'left_ballToToe_ctrlGrp')
    cmds.parent('left_leg_metaTarsais_SC_pivotGrp', 'left_ballToToe_ctrlGrp')
    cmds.parent('left_ballToToe_ctrlGrp', 'left_footHeel _ctrlGrp')
    cmds.parent('left_footHeel _ctrlGrp', 'left_footSystem_ctrlGrp')

    cmds.group (n = 'left_foot_ctrlGrp', em = True)
    cmds.move(leftanklePos[0], leftanklePos[1], leftanklePos[2])
    cmds.circle(n = 'left_foot_ctrl', r = 2)
    cmds.parent('left_foot_ctrl', 'left_foot_ctrlGrp', relative = True)

    cmds.parentConstraint('left_foot_ctrl', 'left_footSystem_ctrlGrp')
    cmds.scaleConstraint('left_foot_ctrl', 'left_footSystem_ctrlGrp')

    cmds.addAttr ('left_foot_ctrl', longName = 'HeelRoll', niceName = 'Heel Roll', at = 'float', defaultValue = 0, min = 0, max = 10, hidden = False, keyable = True) 
    cmds.addAttr ('left_foot_ctrl', longName = 'ToeRoll', niceName = 'Toe Roll', at = 'float', defaultValue = 0, min = 0, max = 10, hidden = False, keyable = True)
    cmds.addAttr ('left_foot_ctrl', longName = 'SwivelToe', niceName = 'Swivel Toe', at = 'float', defaultValue = 0, hidden = False, keyable = True)
    cmds.addAttr ('left_foot_ctrl', longName = 'RaiseToe', niceName = 'Raise Toe', at = 'float', defaultValue = 0, min = -10, max = 10, hidden = False, keyable = True)
    cmds.addAttr ('left_foot_ctrl', longName = 'RaiseHeel', niceName = 'Raise Heel', at = 'float', defaultValue = 0, min = 0, max = 20, hidden = False, keyable = True)
    cmds.addAttr ('left_foot_ctrl', longName = 'SwivelHeel', niceName = 'Swivel Heel', at = 'float', defaultValue = 0, hidden = False, keyable = True)

    cmds.setDrivenKeyframe('left_footToBall_ctrlGrp.rotateX', currentDriver = 'left_foot_ctrl.HeelRoll', value = 60, driverValue = 10)
    cmds.setDrivenKeyframe('left_footToBall_ctrlGrp.rotateX', currentDriver = 'left_foot_ctrl.HeelRoll', value = 0, driverValue = 0)
    cmds.setDrivenKeyframe('left_ballToToe_ctrlGrp.rotateX', currentDriver = 'left_foot_ctrl.ToeRoll', value = 60, driverValue = 10)
    cmds.setDrivenKeyframe('left_ballToToe_ctrlGrp.rotateX', currentDriver = 'left_foot_ctrl.ToeRoll', value = 0, driverValue = 0)
    cmds.setDrivenKeyframe('left_footHeel_ctrlGrp.rotateX', currentDriver = 'left_foot_ctrl.RaiseHeel', value = -60, driverValue = 20)
    cmds.setDrivenKeyframe('left_footHeel_ctrlGrp.rotateX', currentDriver = 'left_foot_ctrl.RaiseHeel', value = 0, driverValue = 0)
    cmds.setDrivenKeyframe('left_leg_metaTarsais_SC_pivotGrp.translateY', currentDriver = 'left_foot_ctrl.RaiseToe', value = 0, driverValue = 0)
    cmds.setDrivenKeyframe('left_leg_metaTarsais_SC_pivotGrp.translateY', currentDriver = 'left_foot_ctrl.RaiseToe', value = 1, driverValue = 10)
    cmds.setDrivenKeyframe('left_leg_metaTarsais_SC_pivotGrp.translateY', currentDriver = 'left_foot_ctrl.RaiseToe', value = -1, driverValue = -10)

    cmds.connectAttr('left_foot_ctrl.SwivelHeel', 'left_footHeel_ctrlGrp.rotateY')
    cmds.connectAttr('left_foot_ctrl.SwivelToe', 'left_ballToToe_ctrlGrp.rotateY')

    cmds.group (name = 'left_leg_ikSystemGrp', empty = True)
    cmds.parent('left_foot_ctrlGrp', 'left_leg_ikSystemGrp', relative = False)
    cmds.parent('left_kneeIk_ctrlGrp', 'left_leg_ikSystemGrp', relative = False)


    ############################################################ RIGHT LEGS ################################################################

    rightkneePos = cmds.xform('right_knee_ikJnt', query = True, worldSpace = True, translation = True)
    rightanklePos = cmds.xform('right_ankle_ikJnt', query = True, worldSpace = True, translation = True)
    righttarsaisPos = cmds.xform('right_tarsais_ikJnt', query = True, worldSpace = True, translation = True)
    rightmetaTarsaisPos = cmds.xform('right_metaTarsais_endikJnt', query = True, worldSpace = True, translation = True)

    cmds.ikHandle(n = 'right_leg_RP_ikHandle', sj = 'right_femur_ikJnt', ee = 'right_ankle_ikJnt')
    cmds.ikHandle(n = 'right_leg_ankleTarsais_SC_ikHandle', sol ='ikSCsolver', sj = 'right_ankle_ikJnt', ee = 'right_tarsais_ikJnt')
    cmds.ikHandle(n = 'right_leg_metaTarsais_SC_ikHandle', sol ='ikSCsolver', sj = 'right_tarsais_ikJnt', ee = 'right_metaTarsais_endikJnt')

    cmds.group (n = 'right_leg_metaTarsais_SC_pivotGrp', empty = True)
    cmds.move(rightmetaTarsaisPos[0], rightmetaTarsaisPos[1], rightmetaTarsaisPos[2])
    cmds.parent('right_leg_metaTarsais_SC_ikHandle', 'right_leg_metaTarsais_SC_pivotGrp')
        
    cmds.group (n = 'right_kneeIk_ctrlGrp', em = True)
    cmds.move(rightkneePos[0], rightkneePos[1], rightkneePos[2] + 10)
    cmds.circle(n = 'right_kneeIk_ctrl', r = 1)
    cmds.parent('right_kneeIk_ctrl', 'right_kneeIk_ctrlGrp', relative = True)

    cmds.group (n = 'right_ankleIk_ctrlGrp', em = True)
    cmds.move(rightanklePos[0], rightanklePos[1], rightanklePos[2])
    cmds.circle(n = 'right_ankleIk_ctrl', r = 1)
    cmds.parent('right_ankleIk_ctrl', 'right_ankleIk_ctrlGrp', relative = True)

    cmds.group (n = 'right_footSystem_ctrlGrp', em = True)
    cmds.move(rightanklePos[0], rightanklePos[1], rightanklePos[2])

    cmds.group (n = 'right_footToBall_ctrlGrp', em = True)
    cmds.move(righttarsaisPos[0], righttarsaisPos[1], righttarsaisPos[2])

    cmds.group (n = 'right_ballToToe_ctrlGrp', em = True)
    cmds.move(rightmetaTarsaisPos[0], rightmetaTarsaisPos[1], rightmetaTarsaisPos[2])

    cmds.group(name = 'right_footHeel_ctrlGrp', em = True)
    cmds.move(rightmetaTarsaisPos[0], rightmetaTarsaisPos[1]-5, rightmetaTarsaisPos[2]-25)

    #cmds.poleVectorConstraint('right_kneeIk_ctrl', 'right_leg_RP_ikHandle')
    cmds.parentConstraint('right_ankleIk_ctrl', 'right_leg_RP_ikHandle')

    cmds.parent('right_ankleIk_ctrlGrp', 'right_footToBall_ctrlGrp')
    cmds.parent('right_leg_ankleTarsais_SC_ikHandle', 'right_footToBall_ctrlGrp')
    cmds.parent('right_footToBall_ctrlGrp', 'right_ballToToe_ctrlGrp')
    cmds.parent('right_leg_metaTarsais_SC_pivotGrp', 'right_ballToToe_ctrlGrp')
    cmds.parent('right_ballToToe_ctrlGrp', 'right_footHeel _ctrlGrp')
    cmds.parent('right_footHeel _ctrlGrp', 'right_footSystem_ctrlGrp')

    cmds.group (n = 'right_foot_ctrlGrp', em = True)
    cmds.move(rightanklePos[0], rightanklePos[1], rightanklePos[2])
    cmds.circle(n = 'right_foot_ctrl', r = 2)
    cmds.parent('right_foot_ctrl', 'right_foot_ctrlGrp', relative = True)

    cmds.parentConstraint('right_foot_ctrl', 'right_footSystem_ctrlGrp')
    cmds.scaleConstraint('right_foot_ctrl', 'right_footSystem_ctrlGrp')

    cmds.addAttr ('right_foot_ctrl', longName = 'HeelRoll', niceName = 'Heel Roll', at = 'float', defaultValue = 0, min = 0, max = 10, hidden = False, keyable = True) 
    cmds.addAttr ('right_foot_ctrl', longName = 'ToeRoll', niceName = 'Toe Roll', at = 'float', defaultValue = 0, min = 0, max = 10, hidden = False, keyable = True)
    cmds.addAttr ('right_foot_ctrl', longName = 'SwivelToe', niceName = 'Swivel Toe', at = 'float', defaultValue = 0, hidden = False, keyable = True)
    cmds.addAttr ('right_foot_ctrl', longName = 'RaiseToe', niceName = 'Raise Toe', at = 'float', defaultValue = 0, min = -10, max = 10, hidden = False, keyable = True)
    cmds.addAttr ('right_foot_ctrl', longName = 'RaiseHeel', niceName = 'Raise Heel', at = 'float', defaultValue = 0, min = 0, max = 20, hidden = False, keyable = True)
    cmds.addAttr ('right_foot_ctrl', longName = 'SwivelHeel', niceName = 'Swivel Heel', at = 'float', defaultValue = 0, hidden = False, keyable = True)

    cmds.setDrivenKeyframe('right_footToBall_ctrlGrp.rotateX', currentDriver = 'right_foot_ctrl.HeelRoll', value = 60, driverValue = 10)
    cmds.setDrivenKeyframe('right_footToBall_ctrlGrp.rotateX', currentDriver = 'right_foot_ctrl.HeelRoll', value = 0, driverValue = 0)
    cmds.setDrivenKeyframe('right_ballToToe_ctrlGrp.rotateX', currentDriver = 'right_foot_ctrl.ToeRoll', value = 60, driverValue = 10)
    cmds.setDrivenKeyframe('right_ballToToe_ctrlGrp.rotateX', currentDriver = 'right_foot_ctrl.ToeRoll', value = 0, driverValue = 0)
    cmds.setDrivenKeyframe('right_footHeel_ctrlGrp.rotateX', currentDriver = 'right_foot_ctrl.RaiseHeel', value = -60, driverValue = 20)
    cmds.setDrivenKeyframe('right_footHeel_ctrlGrp.rotateX', currentDriver = 'right_foot_ctrl.RaiseHeel', value = 0, driverValue = 0)
    cmds.setDrivenKeyframe('right_leg_metaTarsais_SC_pivotGrp.translateY', currentDriver = 'right_foot_ctrl.RaiseToe', value = 0, driverValue = 0)
    cmds.setDrivenKeyframe('right_leg_metaTarsais_SC_pivotGrp.translateY', currentDriver = 'right_foot_ctrl.RaiseToe', value = 1, driverValue = 10)
    cmds.setDrivenKeyframe('right_leg_metaTarsais_SC_pivotGrp.translateY', currentDriver = 'right_foot_ctrl.RaiseToe', value = -1, driverValue = -10)

    cmds.connectAttr('right_foot_ctrl.SwivelHeel', 'right_footHeel_ctrlGrp.rotateY')
    cmds.connectAttr('right_foot_ctrl.SwivelToe', 'right_ballToToe_ctrlGrp.rotateY')

    cmds.group (name = 'right_leg_ikSystemGrp', empty = True)
    cmds.parent('right_foot_ctrlGrp',  'right_leg_ikSystemGrp', relative = False)
    cmds.parent('right_kneeIk_ctrlGrp',  'right_leg_ikSystemGrp', relative = False)
    ############################################################ LEFT ARM ##################################################################

    leftelbowPos = cmds.xform('left_elbow_ikJnt', query = True, worldSpace = True, translation = True)
    leftwristPos = cmds.xform('left_wrist_ikJnt', query = True, worldSpace = True, translation = True)

    cmds.ikHandle(n = 'left_arm_RP_ikHandle', sj = 'left_shoulder_ikJnt', ee = 'left_wrist_ikJnt')

    cmds.group (n = 'left_elbowIk_ctrlGrp', em = True)
    cmds.move(leftelbowPos[0], leftelbowPos[1], leftelbowPos[2] + 10)
    cmds.circle(n = 'left_elbowIk_ctrl', r = 1)
    cmds.parent('left_elbowIk_ctrl', 'left_elbowIk_ctrlGrp', relative = True)

    cmds.group (n = 'left_wristIk_ctrlGrp', em = True)
    constraint = cmds.parentConstraint('left_wrist_ikJnt', 'left_wristIk_ctrlGrp')
    cmds.delete(constraint)
    cmds.circle(n = 'left_wristIk_ctrl', r = 1)
    cmds.parent('left_wristIk_ctrl', 'left_wristIk_ctrlGrp', relative = True)

    #cmds.poleVectorConstraint('left_kneeIk_ctrl', 'left_leg_RP_ikHandle')
    cmds.parentConstraint('left_wristIk_ctrl', 'left_arm_RP_ikHandle')
    cmds.parentConstraint('left_wristIk_ctrl', 'left_wrist_ikJnt', skipTranslate = ['x','y','z'], maintainOffset = True)

    cmds.group (name = 'left_arm_ikSystemGrp', empty = True)
    cmds.parent('left_wristIk_ctrlGrp',  'left_arm_ikSystemGrp', relative = False)
    cmds.parent('left_elbowIk_ctrlGrp',  'left_arm_ikSystemGrp', relative = False)

    ############################################################ RIGHT ARM ################################################################

    rightelbowPos = cmds.xform('right_elbow_ikJnt', query = True, worldSpace = True, translation = True)
    rightwristPos = cmds.xform('right_wrist_ikJnt', query = True, worldSpace = True, translation = True)

    cmds.ikHandle(n = 'right_arm_RP_ikHandle', sj = 'right_shoulder_ikJnt', ee = 'right_wrist_ikJnt')

    cmds.group (n = 'right_elbowIk_ctrlGrp', em = True)
    cmds.move(rightelbowPos[0], rightelbowPos[1], rightelbowPos[2] + 10)
    cmds.circle(n = 'right_elbowIk_ctrl', r = 1)
    cmds.parent('right_elbowIk_ctrl', 'right_elbowIk_ctrlGrp', relative = True)

    cmds.group (n = 'right_wristIk_ctrlGrp', em = True)
    constraint = cmds.parentConstraint('right_wrist_ikJnt', 'right_wristIk_ctrlGrp')
    cmds.delete(constraint)
    cmds.circle(n = 'right_wristIk_ctrl', r = 1)
    cmds.parent('right_wristIk_ctrl', 'right_wristIk_ctrlGrp', relative = True)

    #cmds.poleVectorConstraint('right_kneeIk_ctrl', 'right_leg_RP_ikHandle')
    cmds.parentConstraint('right_wristIk_ctrl', 'right_arm_RP_ikHandle')
    cmds.parentConstraint('right_wristIk_ctrl', 'right_wrist_ikJnt', skipTranslate = ['x','y','z'], maintainOffset = True)

    cmds.group (name = 'right_arm_ikSystemGrp', empty = True)
    cmds.parent('right_wristIk_ctrlGrp',  'right_arm_ikSystemGrp', relative = False)
    cmds.parent('right_elbowIk_ctrlGrp',  'right_arm_ikSystemGrp', relative = False)


#Switch
def Switch(*args):

    #List for joints and object

    joints = ['left_ankle_ikJnt', 'left_wrist_ikJnt', 'right_ankle_ikJnt', 'right_wrist_ikJnt']

    object = ["left_leg_IKFKSwitch01_ctrl", "left_arm_IKFKSwitch01_ctrl", "right_leg_IKFKSwitch01_ctrl","right_arm_IKFKSwitch01_ctrl"]

    ###################################################### Create and Attribute of the Switch ###############################################################
    for i, orig in enumerate(joints):
        curve = cmds.curve(name = object[i], degree = 1, point = [(1,1,1), (1,-1,1), (1 ,-1,-1), (1,1,-1), (1,1,1), (-1,1,1), (-1,-1,1), (-1 ,-1,-1), (-1,1,-1), (-1,1,1), (-1,-1,1), (1,-1,1), (1,1,1), (1,1,-1), (-1,1,-1),(-1,-1,-1), (1,-1,-1)], knot = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])
        group = cmds.group(name = object[i] + "Grp")
        constraint = cmds.parentConstraint(joints[i], group)
        cmds.delete(constraint)
        #if "arm" in object[i]:
            #cmds.move(5, y = True)
        #else:
            #cmds.move(-10, z = True)
        cmds.addAttr(object[i], longName = 'IK_FK_Switch', niceName = 'IK FK Switch', at = 'short', defaultValue = 0, min = 0, max = 1, keyable = True)

    #ARMS

    cmds.connectAttr('left_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_shoulder_blndColor.blender')
    cmds.connectAttr('right_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_shoulder_blndColor.blender')

    cmds.connectAttr('left_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_elbow_blndColor.blender')
    cmds.connectAttr('right_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_elbow_blndColor.blender')

    cmds.connectAttr('left_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_wrist_blndColor.blender')
    cmds.connectAttr('right_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_wrist_blndColor.blender')

    #LEGS

    cmds.connectAttr('left_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_femur_blndColor.blender')
    cmds.connectAttr('right_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_femur_blndColor.blender')

    cmds.connectAttr('left_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_knee_blndColor.blender')
    cmds.connectAttr('right_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_knee_blndColor.blender')

    cmds.connectAttr('left_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_ankle_blndColor.blender')
    cmds.connectAttr('right_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_ankle_blndColor.blender')

    cmds.connectAttr('left_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_tarsais_blndColor.blender')
    cmds.connectAttr('right_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_tarsais_blndColor.blender')


    ###################################################### CONTROLLERS ##############################################

    cmds.createNode('reverse', name = 'left_armReverse')
    cmds.createNode('reverse', name = 'right_armReverse')
    cmds.createNode('reverse', name = 'left_legReverse')
    cmds.createNode('reverse', name = 'right_legReverse')

    #Arms
    cmds.connectAttr('left_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_arm_ikSystemGrp.visibility')
    cmds.connectAttr('right_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_arm_ikSystemGrp.visibility')

    cmds.connectAttr('left_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_armReverse.inputX')
    cmds.connectAttr('right_arm_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_armReverse.inputX')

    cmds.connectAttr('left_armReverse.outputX', 'left_shoulder_fkctrlGrp.visibility')
    cmds.connectAttr('right_armReverse.outputX', 'right_shoulder_fkctrlGrp.visibility')

    #Legs
    cmds.connectAttr('left_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_leg_ikSystemGrp.visibility')
    cmds.connectAttr('right_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_leg_ikSystemGrp.visibility')

    cmds.connectAttr('left_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'left_legReverse.inputX')
    cmds.connectAttr('right_leg_IKFKSwitch01_ctrl.IK_FK_Switch', 'right_legReverse.inputX')

    cmds.connectAttr('left_legReverse.outputX', 'left_femur_fkctrlGrp.visibility')
    cmds.connectAttr('right_legReverse.outputX', 'right_femur_fkctrlGrp.visibility')

    ################################################################### Constraints To the Switches

    cmds.parentConstraint('left_wrist_jnt','left_arm_IKFKSwitch01_ctrlGrp', maintainOffset = True)
    cmds.parentConstraint('right_wrist_jnt','right_arm_IKFKSwitch01_ctrlGrp', maintainOffset = True)
    cmds.parentConstraint('left_ankle_jnt','left_leg_IKFKSwitch01_ctrlGrp', maintainOffset = True)
    cmds.parentConstraint('right_ankle_jnt','right_leg_IKFKSwitch01_ctrlGrp', maintainOffset = True)




############################################################## MAIN ##############################################################################
create_window()
