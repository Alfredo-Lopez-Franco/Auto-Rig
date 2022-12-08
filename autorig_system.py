import maya.cmds as cmds

#Global variables
window_Name = "Alfredo_Lopez_AutoRig"
windowTittle = "Alfredo_Lopez_Autorig"
window_w = 202
window_h = 200

fingerJoint = []
fkJoints = []

leftFingersGroups = []
rightFingersGroups = []

leftFingerSystem = "leftFingersSystem_grp"
rightFingerSystem = "rightFingersSystem_grp"

leftFingers = []
rightFingers = []

temp = 0


def create_window():
    """
    Function that creates the window of the auto-rig
    window_name = Alfredo_Lopez_AutoRig
    window_w = 202
    window_h = 200
    """

#Function that checks if the window already exists if it exist it deletes it
    if cmds.window(window_Name, query=True, exists=True):
        cmds.deleteUI(window_Name)
    cmds.window(window_Name)
    cmds.window(
        window_Name,
        edit=True,
        width=window_w,
        height=window_h,
        title=windowTittle,
        minimizeButton=False,
        maximizeButton=False,
        sizeable=False,
    )

#This create the first column of the layout
    cmds.columnLayout("Main_Column", width=window_w, height=window_h)
    custom_UI()

#It creates the window
    cmds.showWindow(window_Name)


def custom_UI():
    """
    Function that creates the custom buttons for different functions
    window_w = 202
    """

#This button calls the blend_joints function
    cmds.button(
        "blendJnts_button",
        label="BlendJnts",
        parent="Main_Column",
        width=window_w,
        height=40,
        command=blend_joints,
    )

#This command create the layout of the interface
    cmds.frameLayout(
        "control_scale_frame",
        label="control scale",
        width=window_w,
        parent="Main_Column",
        collapsable=True,
        backgroundColor=(0.5, 0.0, 0.5),
    )

#This column create a row column for 3 different buttons
    cmds.rowColumnLayout("Controllers", numberOfColumns=3, width=window_w)

#This button calls the different commands
    cmds.button("fkSystem", 
                label="FkSystem", 
                width=window_w / 3, 
                command=FK_system)
    cmds.button("ikSystem", 
                label="IkSystem", 
                width=window_w / 3, 
                command=IK_system)
    cmds.button("switch", 
                label="IKFKSwitch", 
                width=window_w / 3, 
                command=switch)
    cmds.button("fingerSystem", 
                label="FingerSystem", 
                height=30, 
                command=finger_system)

#------------------------ Blend joints ------------------------#
def blend_joints ():
    """
    This function blend the IK joints and the FK joints to the Bind joints
    """

#This creates the blendColor node for the arms
    cmds.createNode('blendColors', name = 'left_shoulder_blndColor')
    cmds.createNode('blendColors', name = 'left_elbow_blndColor')
    cmds.createNode('blendColors', name = 'left_wrist_blndColor')

    cmds.createNode('blendColors', name = 'right_shoulder_blndColor')
    cmds.createNode('blendColors', name = 'right_elbow_blndColor')
    cmds.createNode('blendColors', name = 'right_wrist_blndColor')

#This connects the rotate attributes of the arms to the blend colors
    cmds.connectAttr('left_shoulder_ikJnt.rotate','left_shoulder_blndColor.color1')
    cmds.connectAttr('left_shoulder_fkJnt.rotate','left_shoulder_blndColor.color2')

    cmds.connectAttr('left_elbow_ikJnt.rotate','left_elbow_blndColor.color1')
    cmds.connectAttr('left_elbow_fkJnt.rotate','left_elbow_blndColor.color2')

    cmds.connectAttr('left_wrist_ikJnt.rotate','left_wrist_blndColor.color1')
    cmds.connectAttr('left_wrist_fkJnt.rotate','left_wrist_blndColor.color2')

    cmds.connectAttr('right_shoulder_ikJnt.rotate','right_shoulder_blndColor.color1')
    cmds.connectAttr('right_shoulder_fkJnt.rotate','right_shoulder_blndColor.color2')

    cmds.connectAttr('right_elbow_ikJnt.rotate','right_elbow_blndColor.color1')
    cmds.connectAttr('right_elbow_fkJnt.rotate','right_elbow_blndColor.color2')

    cmds.connectAttr('right_wrist_ikJnt.rotate','right_wrist_blndColor.color1')
    cmds.connectAttr('right_wrist_fkJnt.rotate','right_wrist_blndColor.color2')

#This connects the result of the blendColor nodes to the Bind joints
    cmds.connectAttr('left_shoulder_blndColor.output', 'left_shoulder_jnt.rotate')
    cmds.connectAttr('left_elbow_blndColor.output', 'left_elbow_jnt.rotate')
    cmds.connectAttr('left_wrist_blndColor.output', 'left_wrist_jnt.rotate')

    cmds.connectAttr('right_shoulder_blndColor.output', 'right_shoulder_jnt.rotate')
    cmds.connectAttr('right_elbow_blndColor.output', 'right_elbow_jnt.rotate')
    cmds.connectAttr('right_wrist_blndColor.output', 'right_wrist_jnt.rotate')

#This creates the blendColor node for the legs
    cmds.createNode('blendColors', name = 'left_femur_blndColor')
    cmds.createNode('blendColors', name = 'left_knee_blndColor')
    cmds.createNode('blendColors', name = 'left_ankle_blndColor')
    cmds.createNode('blendColors', name = 'left_tarsais_blndColor')

    cmds.createNode('blendColors', name = 'right_femur_blndColor')
    cmds.createNode('blendColors', name = 'right_knee_blndColor')
    cmds.createNode('blendColors', name = 'right_ankle_blndColor')
    cmds.createNode('blendColors', name = 'right_tarsais_blndColor')

#This connects the rotate attributes of the legs to the blend colors
    cmds.connectAttr('left_femur_ikJnt.rotate','left_femur_blndColor.color1')
    cmds.connectAttr('left_femur_fkJnt.rotate','left_femur_blndColor.color2')

    cmds.connectAttr('left_knee_ikJnt.rotate','left_knee_blndColor.color1')
    cmds.connectAttr('left_knee_fkJnt.rotate','left_knee_blndColor.color2')

    cmds.connectAttr('left_ankle_ikJnt.rotate','left_ankle_blndColor.color1')
    cmds.connectAttr('left_ankle_fkJnt.rotate','left_ankle_blndColor.color2')

    cmds.connectAttr('left_tarsais_ikJnt.rotate','left_tarsais_blndColor.color1')
    cmds.connectAttr('left_tarsais_fkJnt.rotate','left_tarsais_blndColor.color2')

    cmds.connectAttr('right_femur_ikJnt.rotate','right_femur_blndColor.color1')
    cmds.connectAttr('right_femur_fkJnt.rotate','right_femur_blndColor.color2')

    cmds.connectAttr('right_knee_ikJnt.rotate','right_knee_blndColor.color1')
    cmds.connectAttr('right_knee_fkJnt.rotate','right_knee_blndColor.color2')

    cmds.connectAttr('right_ankle_ikJnt.rotate','right_ankle_blndColor.color1')
    cmds.connectAttr('right_ankle_fkJnt.rotate','right_ankle_blndColor.color2')

    cmds.connectAttr('right_tarsais_ikJnt.rotate','right_tarsais_blndColor.color1')
    cmds.connectAttr('right_tarsais_fkJnt.rotate','right_tarsais_blndColor.color2')

#This connects the result of the blendColor nodes to the Bind joints
    cmds.connectAttr('left_femur_blndColor.output', 'left_femur_jnt.rotate')
    cmds.connectAttr('left_knee_blndColor.output', 'left_knee_jnt.rotate')
    cmds.connectAttr('left_ankle_blndColor.output', 'left_ankle_jnt.rotate')
    cmds.connectAttr('left_tarsais_blndColor.output', 'left_tarsais_jnt.rotate')

    cmds.connectAttr('right_femur_blndColor.output', 'right_femur_jnt.rotate')
    cmds.connectAttr('right_knee_blndColor.output', 'right_knee_jnt.rotate')
    cmds.connectAttr('right_ankle_blndColor.output', 'right_ankle_jnt.rotate')
    cmds.connectAttr('right_tarsais_blndColor.output', 'right_tarsais_jnt.rotate')

#------------------------ Finger system ------------------------#
def finger_order(fingerGrp, fingerCtrl, hand):
    """
    This function parent the fingers in a FK system way

    """
    
#This declare empty variables to stack the values for the order
    childGrp = ""
    childCtrl = ""
    fatherCtrl = ""
    fatherGrp = ""
    baby = ""

#For loop to order the fingers from the fingerGrp, in the empty variables
    for i, orig in enumerate(fingerGrp):

        if "03" in fingerGrp[i]:
            baby = fingerGrp[i]

        elif "02" in fingerGrp[i]:
            childGrp = fingerGrp[i]
            childCtrl = fingerCtrl[i]

        elif "01" in fingerGrp[i]:
            fatherCtrl = fingerCtrl[i]
            fatherGrp = fingerGrp[i]

    if "03" in baby:
        cmds.parent(baby, childCtrl)

    cmds.parent(childGrp, fatherCtrl)

    if "left" in fatherGrp:
        cmds.parent(fatherGrp, hand)

    else:
        cmds.parent(fatherGrp, hand)


def control_and_finger_order(finger_side):
    """
    This function create the controllers of the fingers and the hand 
    for the setDrivenKey system
    """
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

#This loop creates the finger controllers
#and depending on the name of the joint 
#it will organize it to different lists
    for i, orig in enumerate(finger_side):
        joint_name = finger_side[i][:-3]
        ctrlName = joint_name + "ctrl"
        ctrl = cmds.circle(name=ctrlName, normal=[1, 0, 0], radius=5, ch=False)
        grpNameMod = ctrlName + "GrpMod"
        cmds.group(name=grpNameMod)
        grpName = ctrlName + "GrpPos"
        grp = cmds.group(name=grpName)
        constraint = cmds.parentConstraint(finger_side[i], grp, mo=False)
        cmds.delete(constraint)
        cmds.parentConstraint(ctrl[0], finger_side[i], mo=True)

        if "thumb" in grpName:
            fingerThumbGrp.append(grpName)
            fingerThumbCtrl.append(ctrlName)

        elif "index" in grpName:
            fingerIndexGrp.append(grpName)
            fingerIndexCtrl.append(ctrlName)

        elif "middle" in grpName:
            fingerMiddleGrp.append(grpName)
            fingerMiddleCtrl.append(ctrlName)

        elif "ring" in grpName:
            fingerRingGrp.append(grpName)
            fingerRingCtrl.append(ctrlName)

        elif "pinky" in grpName:
            fingerPinkyGrp.append(grpName)
            fingerPinkyCtrl.append(ctrlName)

        if "left" in finger_side[i]:
            leftFingersGroups.append(grpNameMod)

        elif "right" in finger_side[i]:
            rightFingersGroups.append(grpNameMod)

#Here creates the hand controller depending if it is left or right
    hand = ""
    if "left" in finger_side[0]:
        hand = "leftFingersSystem_ctrl"
        cmds.curve(
            name=hand,
            degree=1.0,
            point=[
                (3, 0, -10),
                (5, 0, -8),
                (5, 0, 6),
                (-4, 0, 6),
                (-6, 0, 1),
                (-7, 0, -2),
                (-7, 0, -3),
                (-6, 0, -3),
                (-4, 0, -1),
                (-4, 0, -8),
                (-2, 0, -10),
                (3, 0, -10),
            ],
        )

        cmds.parent(hand, leftFingerSystem, relative=True)
        auto_fingers(leftFingersGroups, hand)

    elif "right" in finger_side[0]:
        hand = "rightFingersSystem_ctrl"
        cmds.curve(
            name=hand,
            degree=1.0,
            point=[
                (3, 0, -10),
                (5, 0, -8),
                (5, 0, 6),
                (-4, 0, 6),
                (-6, 0, 1),
                (-7, 0, -2),
                (-7, 0, -3),
                (-6, 0, -3),
                (-4, 0, -1),
                (-4, 0, -8),
                (-2, 0, -10),
                (3, 0, -10),
            ],
        )

        cmds.parent(hand, rightFingerSystem, relative=True)
        auto_fingers(rightFingersGroups, hand)

#This calls the function finger_order, using the groups, controllers and hand as parameters
    finger_order(fingerThumbGrp, fingerThumbCtrl, hand)
    finger_order(fingerIndexGrp, fingerIndexCtrl, hand)
    finger_order(fingerMiddleGrp, fingerMiddleCtrl, hand)
    finger_order(fingerRingGrp, fingerRingCtrl, hand)
    finger_order(fingerPinkyGrp, fingerPinkyCtrl, hand)

def finger_side(joints):
    """
    This function devide the finger between the joints in left and right side
    """
    for i,orig in enumerate(joints):

        if 'left' in joints[i]:
            leftFingers.append(joints[i])

        else:
            rightFingers.append(joints[i])
    
    control_and_finger_order(leftFingers)
    control_and_finger_order(rightFingers)

def auto_fingers(fingerGroup, hand):
    """
    This function creates a SetDrivenKey
    so the fingers can open the hand, spread it and make a fist
    """

#Creation of the attributes
    cmds.addAttr(
        hand,
        longName="Fist",
        niceName="Fist",
        attribute="float",
        defaultValue=0,
        minimum=0,
        maximum=20,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        hand,
        longName="UpFingers",
        niceName="UpFingers",
        attribute="float",
        defaultValue=0,
        minimum=0,
        maximum=10,
        hidden=False,
        keyable=True,
    )   
    cmds.addAttr(
        hand,
        longName="Spread",
        niceName="Spread",
        attribute="float",
        defaultValue=0,
        minimum=0,
        maximum=10,
        hidden=False,
        keyable=True,
    )

#This loop create the set driven key for every fingerGroup
    for i, orig in enumerate(fingerGroup):
        
        if "thumb" in fingerGroup[i]:
            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateY",
                currentDriver=hand + ".Fist",
                value=90,
                driverValue=20,
            )
            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateY",
                currentDriver=hand + ".Fist",
                value=0,
                driverValue=0,
            )
            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateY",
                currentDriver=hand + ".UpFingers",
                value=-30,
                driverValue=20,
            )
            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateY",
                currentDriver=hand + ".UpFingers",
                value=0,
                driverValue=0,
            )
            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateZ",
                currentDriver=hand + ".Spread",
                value=-30,
                driverValue=20,
            )
            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateZ",
                currentDriver=hand + ".Spread",
                value=0,
                driverValue=0,
            )

        else:
            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateZ",
                currentDriver=hand + ".Fist",
                value=-90,
                driverValue=20,
            )
            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateZ",
                currentDriver=hand + ".Fist",
                value=0,
                driverValue=0,
            )

            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateZ",
                currentDriver=hand + ".UpFingers",
                value=45,
                driverValue=20,
            )
            cmds.setDrivenKeyframe(
                fingerGroup[i] + ".rotateZ",
                currentDriver=hand + ".UpFingers",
                value=0,
                driverValue=0,
            )

            if "middle01" in fingerGroup[i]:
                cmds.setDrivenKeyframe(
                    fingerGroup[i] + ".rotateY",
                    currentDriver=hand + ".Spread",
                    value=-10,
                    driverValue=20,
                )
                cmds.setDrivenKeyframe(
                    fingerGroup[i] + ".rotateY",
                    currentDriver=hand + ".Spread",
                    value=0,
                    driverValue=0,
                )

            elif "ring01" in fingerGroup[i]:
                cmds.setDrivenKeyframe(
                    fingerGroup[i] + ".rotateY",
                    currentDriver=hand + ".Spread",
                    value=20,
                    driverValue=20,
                )
                cmds.setDrivenKeyframe(
                    fingerGroup[i] + ".rotateY",
                    currentDriver=hand + ".Spread",
                    value=0,
                    driverValue=0,
                )

            elif "pinky01" in fingerGroup[i]:
                cmds.setDrivenKeyframe(
                    fingerGroup[i] + ".rotateY",
                    currentDriver=hand + ".Spread",
                    value=30,
                    driverValue=20,
                )
                cmds.setDrivenKeyframe(
                    fingerGroup[i] + ".rotateY",
                    currentDriver=hand + ".Spread",
                    value=0,
                    driverValue=0,
                )

            elif "index01" in fingerGroup[i]:
                cmds.setDrivenKeyframe(
                    fingerGroup[i] + ".rotateY",
                    currentDriver=hand + ".Spread",
                    value=-30,
                    driverValue=20,
                )
                cmds.setDrivenKeyframe(
                    fingerGroup[i] + ".rotateY",
                    currentDriver=hand + ".Spread",
                    value=0,
                    driverValue=0,
                )
    

def finger_system():
    """
    This function takes the joints and add them to each finger position
    """

#This select every joint type in the scene
    joint = cmds.ls(type = 'joint')

#This loop devide the joints between the different finger side
#thumb, index, middle, ring and pinky
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

    finger_side(fingerJoint)

#------------------------ FK system ------------------------#
def FK_system():
    """
    This function creates the FK system
    """

    joints = cmds.ls(type="joint")

    for i, orig in enumerate(joints):

        if "_fkJnt" in joints[i] or "clavicle" in joints[i]:
            fkJoints.append(joints[i])

    # Creation of the controllers
    for i, orig in enumerate(fkJoints):

        my_joint = fkJoints[i]

        joint_name = fkJoints[i][:-3]

        ctrl = cmds.circle(
            name=joint_name + "ctrl", normal=[1, 0, 0], radius=5, ch=False
        )

        grp = cmds.group(name=(ctrl[0] + "Grp"))

        constraint = cmds.parentConstraint(fkJoints[i], grp, mo=False)

        cmds.delete(constraint)

        cmds.parentConstraint(ctrl[0], fkJoints[i], mo=True)
        
#Parenting the FK controllers

#Left leg controllers
    cmds.parent('left_tarsais_fkctrlGrp', 'left_ankle_fkctrl')
    cmds.parent('left_ankle_fkctrlGrp', 'left_knee_fkctrl')
    cmds.parent('left_knee_fkctrlGrp', 'left_femur_fkctrl')

#Left arm controllers
    cmds.parent('left_wrist_fkctrlGrp', 'left_elbow_fkctrl')
    cmds.parent('left_elbow_fkctrlGrp', 'left_shoulder_fkctrl')
    cmds.parent('left_shoulder_fkctrlGrp', 'left_clavicle_ctrl')

#Right leg controllers
    cmds.parent('right_tarsais_fkctrlGrp', 'right_ankle_fkctrl')
    cmds.parent('right_ankle_fkctrlGrp', 'right_knee_fkctrl')
    cmds.parent('right_knee_fkctrlGrp', 'right_femur_fkctrl')

#Right arm controllers
    cmds.parent('right_wrist_fkctrlGrp', 'right_elbow_fkctrl')
    cmds.parent('right_elbow_fkctrlGrp', 'right_shoulder_fkctrl')
    cmds.parent('right_shoulder_fkctrlGrp', 'right_clavicle_ctrl')

# ------------------------ IK system ------------------------#
def IK_system():
    """
    This function create the IK system of the rig
    """

    # Left legs
    leftkneePos = cmds.xform(
        "left_knee_ikJnt", query=True, worldSpace=True, translation=True
    )
    leftanklePos = cmds.xform(
        "left_ankle_ikJnt", query=True, worldSpace=True, translation=True
    )
    lefttarsaisPos = cmds.xform(
        "left_tarsais_ikJnt", query=True, worldSpace=True, translation=True
    )
    leftmetaTarsaisPos = cmds.xform(
        "left_metaTarsais_endikJnt", query=True, worldSpace=True, translation=True
    )

    cmds.ikHandle(
        name="left_leg_RP_ikHandle",
        startJoint="left_femur_ikJnt", 
        endEffector="left_ankle_ikJnt"
    )
    cmds.ikHandle(
        name="left_leg_ankleTarsais_SC_ikHandle",
        solver="ikSCsolver",
        startJoint="left_ankle_ikJnt",
        endEffector="left_tarsais_ikJnt",
    )
    cmds.ikHandle(
        name="left_leg_metaTarsais_SC_ikHandle",
        solver="ikSCsolver",
        startJoint="left_tarsais_ikJnt",
        endEffectr="left_metaTarsais_endikJnt",
    )

    cmds.group(name="left_leg_metaTarsais_SC_pivotGrp", empty=True)
    cmds.move(leftmetaTarsaisPos[0], leftmetaTarsaisPos[1], leftmetaTarsaisPos[2])
    cmds.parent("left_leg_metaTarsais_SC_ikHandle", "left_leg_metaTarsais_SC_pivotGrp")

    cmds.group(name="left_kneeIk_ctrlGrp", empty=True)
    cmds.move(leftkneePos[0], leftkneePos[1], leftkneePos[2] + 10)
    cmds.circle(name="left_kneeIk_ctrl", radius=1)
    cmds.parent("left_kneeIk_ctrl", "left_kneeIk_ctrlGrp", relative=True)

    cmds.group(name="left_ankleIk_ctrlGrp", empty=True)
    cmds.move(leftanklePos[0], leftanklePos[1], leftanklePos[2])
    cmds.circle(n="left_ankleIk_ctrl", radius=1)
    cmds.parent("left_ankleIk_ctrl", "left_ankleIk_ctrlGrp", relative=True)

    cmds.group(name="left_footSystem_ctrlGrp", empty=True)
    cmds.move(leftanklePos[0], leftanklePos[1], leftanklePos[2])

    cmds.group(name="left_footToBall_ctrlGrp", empty=True)
    cmds.move(lefttarsaisPos[0], lefttarsaisPos[1], lefttarsaisPos[2])

    cmds.group(name="left_ballToToe_ctrlGrp", empty=True)
    cmds.move(leftmetaTarsaisPos[0], leftmetaTarsaisPos[1], leftmetaTarsaisPos[2])

    cmds.group(name="left_footHeel_ctrlGrp", empty=True)
    cmds.move(leftmetaTarsaisPos[0], leftmetaTarsaisPos[1] - 5, leftmetaTarsaisPos[2] - 25)

    cmds.parentConstraint("left_ankleIk_ctrl", "left_leg_RP_ikHandle")

    cmds.parent("left_ankleIk_ctrlGrp", "left_footToBall_ctrlGrp")
    cmds.parent("left_leg_ankleTarsais_SC_ikHandle", "left_footToBall_ctrlGrp")
    cmds.parent("left_footToBall_ctrlGrp", "left_ballToToe_ctrlGrp")
    cmds.parent("left_leg_metaTarsais_SC_pivotGrp", "left_ballToToe_ctrlGrp")
    cmds.parent("left_ballToToe_ctrlGrp", "left_footHeel _ctrlGrp")
    cmds.parent("left_footHeel _ctrlGrp", "left_footSystem_ctrlGrp")

    cmds.group(name="left_foot_ctrlGrp", empty=True)
    cmds.move(leftanklePos[0], leftanklePos[1], leftanklePos[2])
    cmds.circle(name="left_foot_ctrl", r=2)
    cmds.parent("left_foot_ctrl", "left_foot_ctrlGrp", relative=True)

    cmds.parentConstraint("left_foot_ctrl", "left_footSystem_ctrlGrp")
    cmds.scaleConstraint("left_foot_ctrl", "left_footSystem_ctrlGrp")

#Attribute to create the basic foot movement
    cmds.addAttr(
        "left_foot_ctrl",
        longName="HeelRoll",
        niceName="Heel Roll",
        attribute="float",
        defaultValue=0,
        minimum=0,
        maximum=10,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "left_foot_ctrl",
        longName="ToeRoll",
        niceName="Toe Roll",
        attribute="float",
        defaultValue=0,
        minimum=0,
        maximum=10,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "left_foot_ctrl",
        longName="SwivelToe",
        niceName="Swivel Toe",
        attribute="float",
        defaultValue=0,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "left_foot_ctrl",
        longName="RaiseToe",
        niceName="Raise Toe",
        attribute="float",
        defaultValue=0,
        minimum=-10,
        maximum=10,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "left_foot_ctrl",
        longName="RaiseHeel",
        niceName="Raise Heel",
        attribute="float",
        defaultValue=0,
        minimum=0,
        maximum=20,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "left_foot_ctrl",
        longName="SwivelHeel",
        niceName="Swivel Heel",
        attribute="float",
        defaultValue=0,
        hidden=False,
        keyable=True,
    )

    cmds.setDrivenKeyframe(
        "left_footToBall_ctrlGrp.rotateX",
        currentDriver="left_foot_ctrl.HeelRoll",
        value=60,
        driverValue=10,
    )
    cmds.setDrivenKeyframe(
        "left_footToBall_ctrlGrp.rotateX",
        currentDriver="left_foot_ctrl.HeelRoll",
        value=0,
        driverValue=0,
    )
    cmds.setDrivenKeyframe(
        "left_ballToToe_ctrlGrp.rotateX",
        currentDriver="left_foot_ctrl.ToeRoll",
        value=60,
        driverValue=10,
    )
    cmds.setDrivenKeyframe(
        "left_ballToToe_ctrlGrp.rotateX",
        currentDriver="left_foot_ctrl.ToeRoll",
        value=0,
        driverValue=0,
    )
    cmds.setDrivenKeyframe(
        "left_footHeel_ctrlGrp.rotateX",
        currentDriver="left_foot_ctrl.RaiseHeel",
        value=-60,
        driverValue=20,
    )
    cmds.setDrivenKeyframe(
        "left_footHeel_ctrlGrp.rotateX",
        currentDriver="left_foot_ctrl.RaiseHeel",
        value=0,
        driverValue=0,
    )
    cmds.setDrivenKeyframe(
        "left_leg_metaTarsais_SC_pivotGrp.translateY",
        currentDriver="left_foot_ctrl.RaiseToe",
        value=0,
        driverValue=0,
    )
    cmds.setDrivenKeyframe(
        "left_leg_metaTarsais_SC_pivotGrp.translateY",
        currentDriver="left_foot_ctrl.RaiseToe",
        value=1,
        driverValue=10,
    )
    cmds.setDrivenKeyframe(
        "left_leg_metaTarsais_SC_pivotGrp.translateY",
        currentDriver="left_foot_ctrl.RaiseToe",
        value=-1,
        driverValue=-10,
    )

    cmds.connectAttr("left_foot_ctrl.SwivelHeel", "left_footHeel_ctrlGrp.rotateY")
    cmds.connectAttr("left_foot_ctrl.SwivelToe", "left_ballToToe_ctrlGrp.rotateY")

    cmds.group(name="left_leg_ikSystemGrp", empty=True)
    cmds.parent("left_foot_ctrlGrp", "left_leg_ikSystemGrp", relative=False)
    cmds.parent("left_kneeIk_ctrlGrp", "left_leg_ikSystemGrp", relative=False)

#Right Legs
    rightkneePos = cmds.xform(
        "right_knee_ikJnt", query=True, worldSpace=True, translation=True
    )
    rightanklePos = cmds.xform(
        "right_ankle_ikJnt", query=True, worldSpace=True, translation=True
    )
    righttarsaisPos = cmds.xform(
        "right_tarsais_ikJnt", query=True, worldSpace=True, translation=True
    )
    rightmetaTarsaisPos = cmds.xform(
        "right_metaTarsais_endikJnt", query=True, worldSpace=True, translation=True
    )

    cmds.ikHandle(
        name="right_leg_RP_ikHandle", 
        startJoint="right_femur_ikJnt", 
        endEffector="right_ankle_ikJnt"
    )
    cmds.ikHandle(
        name="right_leg_ankleTarsais_SC_ikHandle",
        solver="ikSCsolver",
        startJoint="right_ankle_ikJnt",
        endEffector="right_tarsais_ikJnt",
    )
    cmds.ikHandle(
        name="right_leg_metaTarsais_SC_ikHandle",
        sol="ikSCsolver",
        sj="right_tarsais_ikJnt",
        ee="right_metaTarsais_endikJnt",
    )

    cmds.group(name="right_leg_metaTarsais_SC_pivotGrp", empty=True)
    cmds.move(rightmetaTarsaisPos[0], rightmetaTarsaisPos[1], rightmetaTarsaisPos[2])
    cmds.parent(
        "right_leg_metaTarsais_SC_ikHandle", "right_leg_metaTarsais_SC_pivotGrp"
    )

    cmds.group(name="right_kneeIk_ctrlGrp", empty=True)
    cmds.move(rightkneePos[0], rightkneePos[1], rightkneePos[2] + 10)
    cmds.circle(name="right_kneeIk_ctrl", r=1)
    cmds.parent("right_kneeIk_ctrl", "right_kneeIk_ctrlGrp", relative=True)

    cmds.group(name="right_ankleIk_ctrlGrp", empty=True)
    cmds.move(rightanklePos[0], rightanklePos[1], rightanklePos[2])
    cmds.circle(name="right_ankleIk_ctrl", r=1)
    cmds.parent("right_ankleIk_ctrl", "right_ankleIk_ctrlGrp", relative=True)

    cmds.group(name="right_footSystem_ctrlGrp", empty=True)
    cmds.move(rightanklePos[0], rightanklePos[1], rightanklePos[2])

    cmds.group(name="right_footToBall_ctrlGrp", empty=True)
    cmds.move(righttarsaisPos[0], righttarsaisPos[1], righttarsaisPos[2])

    cmds.group(name="right_ballToToe_ctrlGrp", empty=True)
    cmds.move(rightmetaTarsaisPos[0], rightmetaTarsaisPos[1], rightmetaTarsaisPos[2])

    cmds.group(name="right_footHeel_ctrlGrp", empty=True)
    cmds.move(
        rightmetaTarsaisPos[0], rightmetaTarsaisPos[1] - 5, rightmetaTarsaisPos[2] - 25
    )

    cmds.parentConstraint("right_ankleIk_ctrl", "right_leg_RP_ikHandle")

    cmds.parent("right_ankleIk_ctrlGrp", "right_footToBall_ctrlGrp")
    cmds.parent("right_leg_ankleTarsais_SC_ikHandle", "right_footToBall_ctrlGrp")
    cmds.parent("right_footToBall_ctrlGrp", "right_ballToToe_ctrlGrp")
    cmds.parent("right_leg_metaTarsais_SC_pivotGrp", "right_ballToToe_ctrlGrp")
    cmds.parent("right_ballToToe_ctrlGrp", "right_footHeel _ctrlGrp")
    cmds.parent("right_footHeel _ctrlGrp", "right_footSystem_ctrlGrp")

    cmds.group(name="right_foot_ctrlGrp", empty=True)
    cmds.move(rightanklePos[0], rightanklePos[1], rightanklePos[2])
    cmds.circle(name="right_foot_ctrl", r=2)
    cmds.parent("right_foot_ctrl", "right_foot_ctrlGrp", relative=True)

    cmds.parentConstraint("right_foot_ctrl", "right_footSystem_ctrlGrp")
    cmds.scaleConstraint("right_foot_ctrl", "right_footSystem_ctrlGrp")

    cmds.addAttr(
        "right_foot_ctrl",
        longName="HeelRoll",
        niceName="Heel Roll",
        attribute="float",
        defaultValue=0,
        minimum=0,
        maximum=10,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "right_foot_ctrl",
        longName="ToeRoll",
        niceName="Toe Roll",
        attribute="float",
        defaultValue=0,
        minimum=0,
        maximum=10,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "right_foot_ctrl",
        longName="SwivelToe",
        niceName="Swivel Toe",
        attribute="float",
        defaultValue=0,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "right_foot_ctrl",
        longName="RaiseToe",
        niceName="Raise Toe",
        attribute="float",
        defaultValue=0,
        minimum=-10,
        maximum=10,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "right_foot_ctrl",
        longName="RaiseHeel",
        niceName="Raise Heel",
        attribute="float",
        defaultValue=0,
        minimum=0,
        maximum=20,
        hidden=False,
        keyable=True,
    )
    cmds.addAttr(
        "right_foot_ctrl",
        longName="SwivelHeel",
        niceName="Swivel Heel",
        attribute="float",
        defaultValue=0,
        hidden=False,
        keyable=True,
    )

    cmds.setDrivenKeyframe(
        "right_footToBall_ctrlGrp.rotateX",
        currentDriver="right_foot_ctrl.HeelRoll",
        value=60,
        driverValue=10,
    )
    cmds.setDrivenKeyframe(
        "right_footToBall_ctrlGrp.rotateX",
        currentDriver="right_foot_ctrl.HeelRoll",
        value=0,
        driverValue=0,
    )
    cmds.setDrivenKeyframe(
        "right_ballToToe_ctrlGrp.rotateX",
        currentDriver="right_foot_ctrl.ToeRoll",
        value=60,
        driverValue=10,
    )
    cmds.setDrivenKeyframe(
        "right_ballToToe_ctrlGrp.rotateX",
        currentDriver="right_foot_ctrl.ToeRoll",
        value=0,
        driverValue=0,
    )
    cmds.setDrivenKeyframe(
        "right_footHeel_ctrlGrp.rotateX",
        currentDriver="right_foot_ctrl.RaiseHeel",
        value=-60,
        driverValue=20,
    )
    cmds.setDrivenKeyframe(
        "right_footHeel_ctrlGrp.rotateX",
        currentDriver="right_foot_ctrl.RaiseHeel",
        value=0,
        driverValue=0,
    )
    cmds.setDrivenKeyframe(
        "right_leg_metaTarsais_SC_pivotGrp.translateY",
        currentDriver="right_foot_ctrl.RaiseToe",
        value=0,
        driverValue=0,
    )
    cmds.setDrivenKeyframe(
        "right_leg_metaTarsais_SC_pivotGrp.translateY",
        currentDriver="right_foot_ctrl.RaiseToe",
        value=1,
        driverValue=10,
    )
    cmds.setDrivenKeyframe(
        "right_leg_metaTarsais_SC_pivotGrp.translateY",
        currentDriver="right_foot_ctrl.RaiseToe",
        value=-1,
        driverValue=-10,
    )

    cmds.connectAttr("right_foot_ctrl.SwivelHeel", "right_footHeel_ctrlGrp.rotateY")
    cmds.connectAttr("right_foot_ctrl.SwivelToe", "right_ballToToe_ctrlGrp.rotateY")

    cmds.group(name="right_leg_ikSystemGrp", empty=True)
    cmds.parent("right_foot_ctrlGrp", "right_leg_ikSystemGrp", relative=False)
    cmds.parent("right_kneeIk_ctrlGrp", "right_leg_ikSystemGrp", relative=False)

#Left arm
    leftelbowPos = cmds.xform(
        "left_elbow_ikJnt", query=True, worldSpace=True, translation=True
    )
    leftwristPos = cmds.xform(
        "left_wrist_ikJnt", query=True, worldSpace=True, translation=True
    )

    cmds.ikHandle(
        name="left_arm_RP_ikHandle", 
        startJoint="left_shoulder_ikJnt", 
        endEffector="left_wrist_ikJnt"
    )

    cmds.group(name="left_elbowIk_ctrlGrp", empty=True)
    cmds.move(leftelbowPos[0], leftelbowPos[1], leftelbowPos[2] + 10)
    cmds.circle(name="left_elbowIk_ctrl", r=1)
    cmds.parent("left_elbowIk_ctrl", "left_elbowIk_ctrlGrp", relative=True)

    cmds.group(name="left_wristIk_ctrlGrp", empty=True)
    constraint = cmds.parentConstraint("left_wrist_ikJnt", "left_wristIk_ctrlGrp")
    cmds.delete(constraint)
    cmds.circle(name="left_wristIk_ctrl", r=1)
    cmds.parent("left_wristIk_ctrl", "left_wristIk_ctrlGrp", relative=True)

    cmds.parentConstraint("left_wristIk_ctrl", "left_arm_RP_ikHandle")
    cmds.parentConstraint("left_wristIk_ctrl", "left_wrist_ikJnt", skipTranslate=["x", "y", "z"], maintainOffset=True)

    cmds.group(name="left_arm_ikSystemGrp", empty=True)
    cmds.parent("left_wristIk_ctrlGrp", "left_arm_ikSystemGrp", relative=False)
    cmds.parent("left_elbowIk_ctrlGrp", "left_arm_ikSystemGrp", relative=False)

#Right arm
    rightelbowPos = cmds.xform(
        "right_elbow_ikJnt", query=True, worldSpace=True, translation=True
    )
    rightwristPos = cmds.xform(
        "right_wrist_ikJnt", query=True, worldSpace=True, translation=True
    )

    cmds.ikHandle(
        name="right_arm_RP_ikHandle", 
        startJoint="right_shoulder_ikJnt", 
        endEffector="right_wrist_ikJnt"
    )

    cmds.group(name="right_elbowIk_ctrlGrp", empty=True)
    cmds.move(rightelbowPos[0], rightelbowPos[1], rightelbowPos[2] + 10)
    cmds.circle(name="right_elbowIk_ctrl", r=1)
    cmds.parent("right_elbowIk_ctrl", "right_elbowIk_ctrlGrp", relative=True)

    cmds.group(name="right_wristIk_ctrlGrp", empty=True)
    constraint = cmds.parentConstraint("right_wrist_ikJnt", "right_wristIk_ctrlGrp")
    cmds.delete(constraint)
    cmds.circle(name="right_wristIk_ctrl", r=1)
    cmds.parent("right_wristIk_ctrl", "right_wristIk_ctrlGrp", relative=True)

    cmds.parentConstraint("right_wristIk_ctrl", "right_arm_RP_ikHandle")
    cmds.parentConstraint("right_wristIk_ctrl", "right_wrist_ikJnt", skipTranslate=["x", "y", "z"], maintainOffset=True)

    cmds.group(name="right_arm_ikSystemGrp", empty=True)
    cmds.parent("right_wristIk_ctrlGrp", "right_arm_ikSystemGrp", relative=False)
    cmds.parent("right_elbowIk_ctrlGrp", "right_arm_ikSystemGrp", relative=False)


# ------------------------ Switch method ------------------------#
def switch():
    """
    This function creates the switch system and attatch it to the blend Node
    """

#List of joints to be constrained and the switch controllers
    joints = [
        "left_ankle_ikJnt",
        "left_wrist_ikJnt",
        "right_ankle_ikJnt",
        "right_wrist_ikJnt",
    ]

    switch_controllers = [
        "left_leg_IKFKSwitch01_ctrl",
        "left_arm_IKFKSwitch01_ctrl",
        "right_leg_IKFKSwitch01_ctrl",
        "right_arm_IKFKSwitch01_ctrl",
    ]

#Create the controller and attributes of the switch
    for i, orig in enumerate(joints):
        curve = cmds.curve(
            name=object[i],
            degree=1,
            point=[
                (1, 1, 1),
                (1, -1, 1),
                (1, -1, -1),
                (1, 1, -1),
                (1, 1, 1),
                (-1, 1, 1),
                (-1, -1, 1),
                (-1, -1, -1),
                (-1, 1, -1),
                (-1, 1, 1),
                (-1, -1, 1),
                (1, -1, 1),
                (1, 1, 1),
                (1, 1, -1),
                (-1, 1, -1),
                (-1, -1, -1),
                (1, -1, -1),
            ],
            knot=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        )
        group = cmds.group(name=object[i] + "Grp")
        constraint = cmds.parentConstraint(joints[i], group)
        cmds.delete(constraint)

        cmds.addAttr(
            object[i],
            longName="IK_FK_Switch",
            niceName="IK FK Switch",
            attribute="short",
            defaultValue=0,
            minimum=0,
            maximum=1,
            keyable=True,
        )

    # ARMS
    cmds.connectAttr(
        "left_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "left_shoulder_blndColor.blender"
    )
    cmds.connectAttr(
        "right_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "right_shoulder_blndColor.blender"
    )

    cmds.connectAttr(
        "left_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "left_elbow_blndColor.blender"
    )
    cmds.connectAttr(
        "right_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "right_elbow_blndColor.blender"
    )

    cmds.connectAttr(
        "left_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "left_wrist_blndColor.blender"
    )
    cmds.connectAttr(
        "right_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "right_wrist_blndColor.blender"
    )

    # LEGS
    cmds.connectAttr(
        "left_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "left_femur_blndColor.blender"
    )
    cmds.connectAttr(
        "right_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "right_femur_blndColor.blender"
    )

    cmds.connectAttr(
        "left_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "left_knee_blndColor.blender"
    )
    cmds.connectAttr(
        "right_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "right_knee_blndColor.blender"
    )

    cmds.connectAttr(
        "left_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "left_ankle_blndColor.blender"
    )
    cmds.connectAttr(
        "right_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "right_ankle_blndColor.blender"
    )

    cmds.connectAttr(
        "left_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "left_tarsais_blndColor.blender"
    )
    cmds.connectAttr(
        "right_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "right_tarsais_blndColor.blender"
    )

    cmds.createNode("reverse", name="left_armReverse")
    cmds.createNode("reverse", name="right_armReverse")
    cmds.createNode("reverse", name="left_legReverse")
    cmds.createNode("reverse", name="right_legReverse")

    # Arms
    cmds.connectAttr(
        "left_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "left_arm_ikSystemGrp.visibility"
    )
    cmds.connectAttr(
        "right_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "right_arm_ikSystemGrp.visibility"
    )

    cmds.connectAttr(
        "left_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "left_armReverse.inputX"
    )
    cmds.connectAttr(
        "right_arm_IKFKSwitch01_ctrl.IK_FK_Switch", "right_armReverse.inputX"
    )

    cmds.connectAttr("left_armReverse.outputX", "left_shoulder_fkctrlGrp.visibility")
    cmds.connectAttr("right_armReverse.outputX", "right_shoulder_fkctrlGrp.visibility")

#This part connects the IK_FK_Switch attribute from the swith to the IK FK visibility control groups
    cmds.connectAttr(
        "left_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "left_leg_ikSystemGrp.visibility"
    )
    cmds.connectAttr(
        "right_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "right_leg_ikSystemGrp.visibility"
    )

    cmds.connectAttr(
        "left_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "left_legReverse.inputX"
    )
    cmds.connectAttr(
        "right_leg_IKFKSwitch01_ctrl.IK_FK_Switch", "right_legReverse.inputX"
    )

    cmds.connectAttr("left_legReverse.outputX", "left_femur_fkctrlGrp.visibility")
    cmds.connectAttr("right_legReverse.outputX", "right_femur_fkctrlGrp.visibility")

#Constraint the switches to its corresponding joint
    cmds.parentConstraint(
        "left_wrist_jnt", "left_arm_IKFKSwitch01_ctrlGrp", maintainOffset=True
    )
    cmds.parentConstraint(
        "right_wrist_jnt", "right_arm_IKFKSwitch01_ctrlGrp", maintainOffset=True
    )
    cmds.parentConstraint(
        "left_ankle_jnt", "left_leg_IKFKSwitch01_ctrlGrp", maintainOffset=True
    )
    cmds.parentConstraint(
        "right_ankle_jnt", "right_leg_IKFKSwitch01_ctrlGrp", maintainOffset=True
    )




# ------------------------ Creating the window ------------------------#
create_window()