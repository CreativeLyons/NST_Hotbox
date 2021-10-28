#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Bake CornerPin
# COLOR: #4b7224
# TEXTCOLOR: #ffffff
#
#----------------------------------------------------------------------------------------------------------

import nukescripts

ns = nuke.selectedNodes()

nukescripts.clear_selection_recursive()
gradMagics = []
for n in ns:
    if n.Class() == "CornerPin2D":
        n.knob('selected').setValue(True)
    else:
        gradMagics.append(n)

for n in gradMagics:
    n.knob('bakeCornerPin').execute()
